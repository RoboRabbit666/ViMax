from openai import OpenAI
import os
from environment.agents.base import BaseAgent
from environment.config.config import config
import soundfile as sf
import json


class CrossTalkTranslator(BaseAgent):
    def __init__(self):
        super().__init__()
        self.client = OpenAI(api_key=config['llm']['api_key'])
        self.client.base_url = config['llm']['base_url']

    def process_message(self, message=None):
        json_path = 'dataset/cross_talk/ct.json'
        chunks = []
        current_time = 0.0
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for idx, item in enumerate(data):
            wav_path = os.path.join("dataset/cross_talk/exp", f"{idx}.wav")
            try:
                data, samplerate = sf.read(wav_path)
                duration = len(data) / samplerate
                end_time = current_time + duration

                # 在content开头添加[role]
                content = f"[{item['role']}] {item['text']}"  # 假设role字段存在

                chunks.append({
                    "id": idx + 1,
                    "timestamp": round(end_time, 3),
                    "content": content  # 使用添加了role的content
                })

                current_time = end_time

            except Exception as e:
                print(f"无法读取 {wav_path}: {str(e)}")
                continue

        result = {
            "sentence_data": {
                "count": len(chunks),
                "chunks": chunks
            }
        }

        with open('dataset/cross_talk/timestamps.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)

        return 0