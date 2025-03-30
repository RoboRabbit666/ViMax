import os
from pydub import AudioSegment

from environment.agents.base import BaseAgent


class MadSVCMixer(BaseAgent):
    def __init__(self):
        super().__init__()

    def process_message(self, message):
        bgm_path = message.content.get("bgm")
        output_dir = message.content.get('output_dir')
        potential_vocals = [f for f in os.listdir(output_dir) if
                            f.endswith(('.wav', '.mp3'))]
        if not potential_vocals:
            return {"status": "error", "message": "No vocal file specified and no audio files found in parent directory"}
        vocal_path = os.path.join(output_dir, potential_vocals[0])
        print(f"Using vocal file: {vocal_path}")

        output_filename = f"mixed_{os.path.basename(vocal_path)}"
        output_path = os.path.join(output_dir, output_filename)

        bgm_volume = -1

        try:
            print("Loading audio files for mixing...")
            bgm_audio = AudioSegment.from_file(bgm_path)
            vocal_audio = AudioSegment.from_file(vocal_path)

            bgm_audio = bgm_audio + bgm_volume
            print(f"Adjusted BGM volume by {bgm_volume} dB")

            print("Mixing audio...")
            if len(bgm_audio) < len(vocal_audio):
                repeated_bgm = bgm_audio
                while len(repeated_bgm) < len(vocal_audio):
                    repeated_bgm += bgm_audio
                repeated_bgm = repeated_bgm[:len(vocal_audio)]
                mixed_audio = vocal_audio.overlay(repeated_bgm)
            else:
                mixed_audio = bgm_audio.overlay(vocal_audio)

            print(f"Exporting mixed audio to {output_path}...")
            output_format = output_path.split(".")[-1] if "." in output_path else "wav"
            mixed_audio.export(output_path, format=output_format)

            return {
                "status": "success",
                "message": f"Mixed audio saved to {output_path}",
                "output_path": output_path
            }

        except Exception as e:
            import traceback
            traceback.print_exc()
            return {"status": "error", "message": f"Error mixing audio: {str(e)}"}