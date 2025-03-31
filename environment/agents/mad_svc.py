import os
import yaml
from environment.communication.message import Message
from environment.roles.loudness_normalizer import LoudnessNormalizer
from environment.roles.mad_svc.mad_svc_analyzer import MadSVCAnalyzer
from environment.roles.mad_svc.mad_svc_annotator import MadSVCAnnotator
from environment.roles.mad_svc.mad_svc_coverist import MadSVCCoverist
from environment.roles.mad_svc.mad_svc_mixer import MadSVCMixer
from environment.roles.mad_svc.mad_svc_spliter import MadSVCSpliter
from environment.roles.mad_svc.mad_svc_subtitle import MadSVCSubtitle
from environment.roles.mad_svc.mad_svc_translator import MadSVCTranslator


class MadSVCAgent:
    def __init__(self, config):
        self.midi = config["mad_svc"]["midi"]
        self.lyrics = config["mad_svc"]["lyrics"]
        self.target = config["mad_svc"]["target"]
        self.reqs = config["mad_svc"]["reqs"]
        self.bgm = config["mad_svc"]["bgm"]

        self.normalizer = LoudnessNormalizer()
        self.mixer = MadSVCMixer()
        self.annotator = MadSVCAnnotator()
        self.analyzer = MadSVCAnalyzer()
        self.spliter = MadSVCSpliter()
        self.cover = MadSVCCoverist()
        self.translator = MadSVCTranslator()
        self.subtitle = MadSVCSubtitle()

    def orchestrator(self):
        pre_msg = Message(content={"audio_dir": os.path.dirname(self.target)})
        loudness_result = self.normalizer.process_message(pre_msg)
        annotator_msg = Message(content={"midi": self.midi, "lyrics": self.lyrics})
        annotator_result = self.annotator.process_message(annotator_msg)

        analyzer_msg = Message(content={"annotator_result": annotator_result.content, "reqs": self.reqs})
        analyzer_result = self.analyzer.process_message(analyzer_msg)

        with open('dataset/mad_svc/script.txt', 'r', encoding='utf-8') as f:
            script = f.read()
        analyzer_result = Message(content={"lyrics": script})
        spliter_msg = Message(content={"annotator_result": annotator_result, "analyzer_result": analyzer_result})
        spliter_result = self.spliter.process_message(spliter_msg)

        name = os.path.basename(self.midi)
        pure_name = os.path.splitext(name)[0]
        trans_msg = Message(content={"name": pure_name})
        trans_result = self.translator.process_message(trans_msg)

        new_name = annotator_result.content.get('name') + '_cover'
        cover_msg = Message(content={"source": f"dataset/mad_svc/cover/有何不可_cover.wav", "target": self.target})
        cover_msg = Message(content={"source": f"dataset/mad_svc/cover/{new_name}.wav", "target": self.target})
        cover_result = self.cover.process_message(cover_msg)
        cover_result = Message(content={'output_dir': 'dataset/mad_svc/final'})

        if self.bgm is not None:
            pre_msg = Message(content={"audio_dir": cover_result.content.get('output_dir')})
            loudness_result = self.normalizer.process_message(pre_msg)

            mixer_message = Message(content={"bgm": self.bgm, "output_dir": cover_result.content.get('output_dir')})
            mixer_result = self.mixer.process_message(mixer_message)
            print(mixer_result)


        # subtitle_msg = Message(content={
        #     "annotation_path": 'dataset/mad_svc/lyrics_annotation/有何不可_cover.json',
        #     "video_path": 'dataset/mad_svc/final/有何不可.mp4',
        #     "output_path": 'dataset/mad_svc/final/有何不可_subtitle.mp4'})
        # subtitle_result = self.subtitle.process_message(subtitle_msg)

        return {
            "status": "success"
            }

def gen_mad_svc():
    print("Welcome to the Mad Generator SVC")
    with open('environment/config/mad_svc.yml', 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    agent = MadSVCAgent(config)
    return agent.orchestrator()
