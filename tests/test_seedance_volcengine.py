"""Minimal smoke test for the direct Volcengine Ark SeedDance API.

Sends a single text-to-video task (no reference images) with a short
prompt and low-cost settings, then polls until the task completes or
fails.  Run with:

    python -m pytest tests/test_seedance_volcengine.py -s

Or directly:

    python tests/test_seedance_volcengine.py

The API key must be set via the VOLCENGINE_API_KEY environment variable.
"""

import asyncio
import logging
import os
import sys

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.video_generator_doubao_seedance_volcengine_api import VideoGeneratorDoubaoSeedanceVolcengineAPI


async def run():
    api_key = os.environ.get("VOLCENGINE_API_KEY")
    if not api_key:
        print("ERROR: set VOLCENGINE_API_KEY before running this test.")
        sys.exit(1)

    generator = VideoGeneratorDoubaoSeedanceVolcengineAPI(api_key=api_key)

    print("Creating t2v task (text-only, 5 s, 16:9)...")
    output = await generator.generate_single_video(
        prompt="A calm ocean wave on a sunny day.",
        reference_image_paths=[],
        aspect_ratio="16:9",
        duration=5,
    )

    print(f"SUCCESS. Video URL: {output.data}")


if __name__ == "__main__":
    asyncio.run(run())
