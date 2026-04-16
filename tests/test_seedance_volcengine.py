"""Smoke tests for the direct Volcengine Ark SeedDance 2.0 API.

Test 1 — t2v:   text-only, no reference images. Verifies basic connectivity.
Test 2 — ff2v:  single first_frame image. Verifies that the `first_frame` role
                is supported by SeedDance 2.0 (critical for ViMax pipeline).

Run:
    python tests/test_seedance_volcengine.py

The API key must be set via the VOLCENGINE_API_KEY environment variable.
A demo first-frame image is expected at:
    demo/ViMax_output/vimax_outputs/idea2video/scene_0/shots/0/first_frame.png
"""

import asyncio
import logging
import os
import sys

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _REPO_ROOT)

from tools.video_generator_doubao_seedance_volcengine_api import VideoGeneratorDoubaoSeedanceVolcengineAPI

_DEMO_FIRST_FRAME = os.path.join(
    _REPO_ROOT,
    "demo/ViMax_output/vimax_outputs/idea2video/scene_0/shots/0/first_frame.png",
)


async def test_t2v(generator: VideoGeneratorDoubaoSeedanceVolcengineAPI):
    print("\n=== Test 1: t2v (text-only) ===")
    output = await generator.generate_single_video(
        prompt="A calm ocean wave on a sunny day.",
        reference_image_paths=[],
        aspect_ratio="16:9",
        duration=5,
    )
    print(f"PASS. Video URL: {output.data}")


async def test_ff2v(generator: VideoGeneratorDoubaoSeedanceVolcengineAPI):
    print("\n=== Test 2: ff2v (first_frame role) ===")
    if not os.path.exists(_DEMO_FIRST_FRAME):
        print(f"SKIP. Demo image not found at: {_DEMO_FIRST_FRAME}")
        return
    output = await generator.generate_single_video(
        prompt="A lone warrior walks slowly down a ruined cyberpunk street at dusk.",
        reference_image_paths=[_DEMO_FIRST_FRAME],   # first_frame role
        aspect_ratio="16:9",
        duration=5,
    )
    print(f"PASS. Video URL: {output.data}")


async def run():
    api_key = os.environ.get("VOLCENGINE_API_KEY")
    if not api_key:
        print("ERROR: set VOLCENGINE_API_KEY before running this test.")
        sys.exit(1)

    generator = VideoGeneratorDoubaoSeedanceVolcengineAPI(api_key=api_key)

    await test_t2v(generator)
    await test_ff2v(generator)


if __name__ == "__main__":
    asyncio.run(run())
