import logging
from typing import List, Literal, Optional
import asyncio
import aiohttp
from interfaces.video_output import VideoOutput
from utils.image import image_path_to_b64

# Direct Volcengine Ark API — does not route through any third-party proxy.
# API key format: UUID (e.g. xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx)
# model: Ark endpoint ID (e.g. ep-20260416124751-x4tfn) created in the Ark console.
#
# SeedDance 2.0 API differences vs 1.0 lite:
#   - ratio / duration / watermark are top-level JSON fields, NOT embedded in the prompt text
#   - first_frame / last_frame roles are preserved for ViMax first-last-frame control
#   - generate_audio is a new optional top-level field

_BASE_URL = "https://ark.cn-beijing.volces.com/api/v3/contents/generations/tasks"


class VideoGeneratorDoubaoSeedanceVolcengineAPI:
    def __init__(
        self,
        api_key: str,
        # All three modes point to the same 2.0 endpoint by default.
        # Override if separate endpoints are created per mode.
        t2v_model: str = "ep-20260416124751-x4tfn",
        ff2v_model: str = "ep-20260416124751-x4tfn",
        flf2v_model: str = "ep-20260416124751-x4tfn",
    ):
        self.api_key = api_key
        self.t2v_model = t2v_model
        self.ff2v_model = ff2v_model
        self.flf2v_model = flf2v_model

    async def create_video_generation_task(
        self,
        prompt: str,
        reference_image_paths: List[str],
        aspect_ratio: str = "16:9",
        duration: Literal[5, 10] = 5,
        generate_audio: bool = False,
    ) -> str:
        """Create a video generation task and return the task ID."""
        if len(reference_image_paths) == 0:
            model = self.t2v_model
        elif len(reference_image_paths) == 1:
            model = self.ff2v_model
        elif len(reference_image_paths) == 2:
            model = self.flf2v_model
        else:
            raise ValueError("reference_image_paths must contain 0, 1, or 2 images.")

        logging.info(f"Calling {model} via Volcengine Ark API to generate video...")

        content = [{"type": "text", "text": prompt}]
        if len(reference_image_paths) >= 1:
            content.append(
                {
                    "type": "image_url",
                    "image_url": {"url": image_path_to_b64(reference_image_paths[0])},
                    "role": "first_frame",
                }
            )
        if len(reference_image_paths) >= 2:
            content.append(
                {
                    "type": "image_url",
                    "image_url": {"url": image_path_to_b64(reference_image_paths[1])},
                    "role": "last_frame",
                }
            )

        # SeedDance 2.0: ratio / duration / watermark are top-level fields
        payload = {
            "model": model,
            "content": content,
            "ratio": aspect_ratio,
            "duration": duration,
            "watermark": False,
            "generate_audio": generate_audio,
        }
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        response_json = {}
        while True:
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(_BASE_URL, headers=headers, json=payload) as response:
                        response_json = await response.json()
                        logging.info(f"Response: {response_json}")
                        task_id = response_json["id"]
            except Exception as e:
                logging.error(f"Error creating video generation task: {e}. Raw response: {response_json}. Retrying in 1 second...")
                await asyncio.sleep(1)
                continue
            break

        logging.info(f"Task created. Task ID: {task_id}")
        return task_id

    async def query_video_generation_task(self, task_id: str) -> str:
        """Poll the task until completion and return the video URL."""
        url = f"{_BASE_URL}/{task_id}"
        headers = {"Authorization": f"Bearer {self.api_key}"}

        while True:
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url, headers=headers) as response:
                        response_json = await response.json()
            except Exception as e:
                logging.error(f"Error querying task {task_id}: {e}. Retrying in 1 second...")
                await asyncio.sleep(1)
                continue

            status = response_json.get("status")
            if status == "succeeded":
                video_url = response_json["content"]["video_url"]
                logging.info(f"Video generation succeeded. URL: {video_url}")
                return video_url
            elif status == "failed":
                logging.error(f"Video generation failed. Response: {response_json}")
                raise ValueError(f"Video generation failed: {response_json}")
            else:
                logging.info(f"Status: {status}. Checking again in 2 seconds...")
                await asyncio.sleep(2)

    async def generate_single_video(
        self,
        prompt: str,
        reference_image_paths: List[str],
        aspect_ratio: str = "16:9",
        duration: Literal[5, 10] = 5,
        generate_audio: bool = False,
        # resolution and fps are not supported in SeedDance 2.0 API
        **kwargs,
    ) -> VideoOutput:
        task_id = await self.create_video_generation_task(
            prompt, reference_image_paths, aspect_ratio, duration, generate_audio
        )
        video_url = await self.query_video_generation_task(task_id)
        return VideoOutput(fmt="url", ext="mp4", data=video_url)
