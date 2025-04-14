import os
import yaml
from transformers.tools.evaluate_agent import translator

from environment.communication.message import Message
from environment.roles.cross_talk.cross_talk_adapter import CrossTalkAdapter
from environment.roles.cross_talk.cross_talk_subtitle import CrossTalkSubtitle
from environment.roles.cross_talk.cross_talk_synth import CrossTalkSynth
from environment.roles.cross_talk.cross_talk_translator import CrossTalkTranslator
from environment.roles.loudness_normalizer import LoudnessNormalizer
from environment.roles.resampler import Resampler
from environment.roles.separator import Separator

from environment.roles.transcriber import Transcriber


class CrossTalkAgent:
    def __init__(self, config):
        self.reqs = config["cross_talk"]["reqs"]
        self.audio_path = config["cross_talk"]["audio_path"]
        self.dou_gen = config["cross_talk"]["dou_gen"]
        self.peng_gen = config["cross_talk"]["peng_gen"]

        self.seperator = Separator()
        self.normalizer = LoudnessNormalizer()
        self.resampler = Resampler()
        self.transcriber = Transcriber()
        self.adapter = CrossTalkAdapter()
        self.synth = CrossTalkSynth()
        self.subtitle = CrossTalkSubtitle()
        self.translator = CrossTalkTranslator()

    def orchestrator(self):
        pre_msg = Message(content={"audio_dir": os.path.dirname(self.audio_path)})
        dou_gen_msg = Message(content={"audio_dir": self.dou_gen})
        peng_gen_msg = Message(content={"audio_dir": self.peng_gen})

        separator_result = self.seperator.process_message(pre_msg)
        normalizer_result = self.normalizer.process_message(pre_msg)
        resampler_result = self.resampler.process_message(pre_msg)
        transcriber_result = self.transcriber.process_message(pre_msg)
        transcriber_dou_gen_res = self.transcriber.process_message(dou_gen_msg)
        transcriber_peng_gen_res = self.transcriber.process_message(peng_gen_msg)

        lab_path = os.path.splitext(self.audio_path)[0] + '.lab'
        adapter_msg = Message(content={"reqs": self.reqs, "lab_path": lab_path, "dou_gen": self.dou_gen, "peng_gen": self.peng_gen})
        adapter_result = self.adapter.process_message(adapter_msg)

        synth_msg = Message(content={"script": adapter_result.content.get('script'), "dou_gen": self.dou_gen, "peng_gen": self.peng_gen})
        synth_result = self.synth.process_message(synth_msg)

        # video_path = synth_result.content.get("video_path")
        # output_path = synth_result.content.get("output_path")
        # video_path = "dataset/cross_talk/final/final.mp4"
        # output_path = "dataset/cross_talk/final/final_subtitle.mp4"
        # json_path = "dataset/cross_talk/ct.json"
        # audio_dir = "dataset/cross_talk/exp"
        # subtitle_msg = Message(content={"video_path": video_path, "output_path": output_path, "audio_dir": audio_dir, "json_path": json_path})
        # subtitle_result = self.subtitle.process_message(subtitle_msg)

        translator_result = self.translator.process_message()


def gen_cross_talk():
    print("Welcome to the Cross Talk Generator")
    with open('environment/config/cross_talk.yml', 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    print(config)
    agent = CrossTalkAgent(config)
    return agent.orchestrator()
