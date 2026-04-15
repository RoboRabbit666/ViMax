import asyncio
from pipelines.idea2video_pipeline import Idea2VideoPipeline


# SET YOUR OWN IDEA, USER REQUIREMENT, AND STYLE HERE
idea = \
    """
A lone warrior in a tattered black cloak walks through a ruined cyberpunk city at dusk.
Neon signs flicker in the smog. He stops and draws a glowing ancient sword,
facing a mysterious hooded stranger who emerges from the shadows.
"""
user_requirement = \
    """
No more than 1 scene. Each scene no more than 3 shots.
Dark fantasy cyberpunk style with cinematic camera work.
"""
style = "3D Anime, cinematic"


async def main():
    pipeline = Idea2VideoPipeline.init_from_config(
        config_path="configs/idea2video.yaml")
    await pipeline(idea=idea, user_requirement=user_requirement, style=style)

if __name__ == "__main__":
    asyncio.run(main())
