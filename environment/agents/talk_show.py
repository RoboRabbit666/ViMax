import os
import yaml
from environment.communication.message import Message
from environment.roles.loudness_normalizer import LoudnessNormalizer
from environment.roles.resampler import Resampler
from environment.roles.separator import Separator
from environment.roles.talk_show.talk_show_adapter import TalkShowAdapter
from environment.roles.talk_show.talk_show_subtitle import TalkShowSubtitle
from environment.roles.talk_show.talk_show_synth import TalkShowSynth
from environment.roles.talk_show.talk_show_translator import TalkShowTranslator
from environment.roles.transcriber import Transcriber


class TalkShowAgent:
    def __init__(self, config):
        self.reqs = config["talk_show"]["reqs"]
        self.audio_path = config["talk_show"]["audio_path"]
        self.target = config["talk_show"]["target"]

        self.seperator = Separator()
        self.normalizer = LoudnessNormalizer()
        self.resampler = Resampler()
        self.transcriber = Transcriber()
        self.adapter = TalkShowAdapter()
        self.synth = TalkShowSynth()
        self.translator = TalkShowTranslator()
        self.subtitle = TalkShowSubtitle()
    def orchestrator(self):
        pre_msg = Message(content={"audio_dir": os.path.dirname(self.audio_path)})
        separator_msg = self.seperator.process_message(pre_msg)

        normalizer_result = self.normalizer.process_message(pre_msg)
        resampler_result = self.resampler.process_message(pre_msg)
        transcriber_result = self.transcriber.process_message(pre_msg)
        
        target_msg = Message(content={"audio_dir": self.target})
        transcriber_target_result = self.transcriber.process_message(target_msg)
        
        lab_path = os.path.splitext(self.audio_path)[0] + '.lab'
        adapter_msg = Message(content={"reqs": self.reqs, "lab_path": lab_path})
        adapter_result = self.adapter.process_message(adapter_msg)

        synth_msg = Message(content={"script": adapter_result.content.get('script'), "target": self.target})
        synth_result = self.synth.process_message(synth_msg)
        
        # json_path = "dataset/talk_show/ts.json"
        # audio_dir = "dataset/talk_show/guodegang/exp"
        # video_path = "dataset/talk_show/guodegang/final/final.mp4"
        # output_path = "dataset/talk_show/guodegang/final/final_subtitle.mp4"
        # subtitle_msg = Message(content={"video_path": video_path, "output_path": output_path, "audio_dir": audio_dir, "json_path": js})
        # subtitle_result = self.subtitle.process_message(subtitle_msg)

        translator_msg = Message(content={"target": self.target})
        translator_result = self.translator.process_message(translator_msg)

def gen_talk_show():
    print("Welcome to the Talk Show Generator")
    with open('environment/config/talk_show.yml', 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    print(config)
    agent = TalkShowAgent(config)
    return agent.orchestrator()
