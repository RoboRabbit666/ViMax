<h1 align='center'>🚀 AI-Creator: Fully-Automated Video Editing with LLM Agents</h1>

<div align='center'>
    <a href='https://space.bilibili.com/3546868449544308'><img src="https://img.shields.io/badge/bilibili-00A1D6.svg?logo=bilibili&logoColor=white" /></a>&nbsp;
    <a href=''><img src='https://badges.aleen42.com/src/youtube.svg' /></a>&nbsp;
    <img src="https://badges.pufler.dev/visits/hkuds/ai-creator?style=flat-square&logo=github">&nbsp;
    <img src='https://img.shields.io/github/stars/hkuds/ai-creator?color=green&style=social' />
    <img src='assets/cover_16-9.png' />
</div>

# 🎉 News

- [ ] [2024.04.07] 🎯 Plan to release the technical details of AI-Creator!
- [ ] [2024.04.07] 🎯 Plan to release more implementation code, supporting all the demo video types showcased!
- [ ] [2024.04.07] 🎯 Plan to release more interesting demo videos made by AI-Creator!
- [x] [2024.03.31] 📢 Releasing the implementation code of AI-Creator!
- [x] [2025.03.31] 📢 Releasing the first demo videos! Including Movie Edits, Meme Videos, AI Music Videos, English Talk Show to Chinese Crosstalk Conversion, AI-Generated TV Drama Clips, and Tech News Updates

# Demos
We have made videos of six distinct types using our AI-Creator, including:
<table>
<tr>
<td align="center" width="33%">
<a href="https://www.bilibili.com/video/BV1C9Z6Y3ESo/"><img src="assets/spiderman_cover.png" width="100%"></a>
Movie Edits
</td>
<td align="center" width="33%">
<a href=""><img src="assets/masterma_cover.png" width="100%"></a>
Meme Videos
</td>
<td align="center" width="33%">
<a href=""><img src="assets/airencuoguo_cover.png" width="100%"></a>
Music Videos
</td>
</tr>
<tr>
<td align="center" width="33%">
<a href=""><img src="assets/adapted_crosstalk_cover.png" width="100%"></a>
Verbal Comedy Arts
</td>
<td align="center" width="33%">
<a href="https://www.bilibili.com/video/BV1TmZ6YjEvV/"><img src="assets/joylife_cover.png" width="100%"></a>
TV Drama
</td>
<td align="center" width="33%">
<a href="https://www.bilibili.com/video/BV12mZ6YLEqW/"><img src="assets/openai_news_cover.png" width="100%"></a>
News
</td>
</tr>
</table>

**Note**: All videos are used for research and demonstration purposes only. The audio and visual assets are sourced from the Internet. Please contact us if you believe any content infringes upon your intellectual property rights.

## 1. Movie Edits
Ever dreamed of creating stunning movie edits that captivate your audience? With AI-Creator, you can transform your favorite movie clips into breathtaking montages that tell your unique story, complete with perfectly synchronized music and transitions.

**How AI-Creator Makes Movie Edits**

AI-Creator employs a powerful multimodal encoder that transforms video clips content into high-dimensional vector representations. This system leverages a joint embedding framework that projects both video visual information and textual queries into a unified semantic space, facilitating precise cross-modal retrieval operations during subsequent information access phases. For rhythmic extraction, we employ energy envelopes and spectral characteristics into a unified rhythmic detection framework, facilitating precise identification of perceptually significant time points. In our retrieval and video precision-editing framework, we have designed a dual-stage retrieval workflow. Initially, we employ VLM to comprehend the visual content of source videos, assisting users in transforming conceptual ideas into storyboard textual queries. During the storyboard query generation process, we unify rhythm points and audio information into the LLM, enabling enhanced cross-modal semantic integration and producing high-quality queries that precisely retrieve corresponding video segments. In the second stage, we again leverage VLM to identify and extract, with greater granularity, the segments that best match the query storyboards within the rhythm-constrained boundaries, thereby reducing visual redundancy while enhancing visual coherence and accuracy.

### 1.1 *Spider-Man: Across the Spider-Verse*
<a href='https://www.bilibili.com/video/BV1C9Z6Y3ESo/' target='_blank'><img src='assets/spiderman_cover.png' width=60%/></a>

**Key Features:**
- Perfect sync between visuals and background music rhythm (eg. 13s, 22s, 25s)
- Expert capture of high-energy scenes (<1 min) from the full movie (>2 hours)
- Maintain visual continuity and reduce redundant clips
- Accurately align the storyboard description of the user prompt (eg. 1st, 2nd sections)

Through intelligent analysis of xx hours of film footage, AI-Creator automatically identifies **rhythm cues**, **high-energy action scenes**, and **character highlights** to achieve precise editing.

**Prompt**:
```
Begin with Gwen with blonde hair sitting at a dining table in front of a window, followed by her playing drums with pop textures and notes in the background. Include action scenes featuring Miguel O'Hara in his dark blue suit with red accents, sharp red claws and black/red eye lenses, Spider-Gwen in her white and pink suit with hood and ballet shoes, Miles Morales with curly hair and red spider logo on his chest, and The Spot in his black suit covered in white spots using portal powers. Focus on the chase scene in the blue sky with trains, and emphasize quality motion such as web-swinging, fighting, and colorful special effects throughout the sequence.
```

### 1.2 *Interstella*

<a href='https://www.bilibili.com/video/BV1yQZ6YkEkw/' target='_blank'><img src='assets/interstella_cover_love.png' width=45%/></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<a href='https://www.bilibili.com/video/BV1koZ6YuEeL/' target='_blank'><img src='assets/interstella_cover.png' width=45%/></a>

**Key Features:**
- For the same input video, edit different styles by adapting your prompts

We showcase two distinct edits of *Interstella* created using AI-Creator. The first version focuses on the theme "love transcending space and time," while the second emphasizes humanity's courage in space exploration. Both edits demonstrate how different prompts can shape the narrative and emotional impact of the same source material.

**Prompt**:
```
Version 1:
Love can transcend tiem and space.
```
```
Version 2:
Celebrate humanity's courage in space exploration. Include scenes featuring spaceships, wormholes, black holes, space station docking maneuvers, ocean planets, and glacial worlds. Show astronauts in their distinctive white spacesuits as they venture into the unknown, highlighting mankind's relentless drive to explore the cosmos.
```

### 1.3 *Nezha*
<a href='https://www.bilibili.com/video/BV1NQZ6YCEPH/' target='_blank'><img src='assets/nezha_cover.png' width=60%/></a>

**Key Features:**
- Capturing scences of conflicts and battals

**Prompt:**
```
Capture more scenes of conflicts and battles between Nezha and Shen Gongbao (black-robed), Dragon Prince Ao Bing (blue-robed).
```

### 1.4 *Titanic*
<a href='https://www.bilibili.com/video/BV12mZ6YLEXJ/' target='_blank'><img src='assets/titanic_cover.png' width=60%/></a>

**Key Features:**
- Understanding of romantic scenes

**Prompt:**
```
A romantic and sweet love story about Jack and Rose meeting on the Titanic. It cannot include the part where the ship is in distress, nor the night scene. In the first section, Rose, wearing a purple hat and a white shirt, walks out of a white car with a purple umbrella, looking thoughtfully.
```

## 2. Meme Videos
Want to create engaging and hilarious meme videos? AI-Creator helps you craft memorable content by intelligently combining video clips, text, and effects into shareable content that could go viral.

**How AI-Creator Makes Meme Videos**
- Users just need to provide the video path and your requirements.
- Automatically preprocesses audio (voice separation, loudness normalization, resampling, transcription) with corresponding agents
- Automatically segments the audio and performs segment-level copywriting adaptation via the Writer Agent
- Uses the Infer Agent for zero-shot inference on audio segments
- Aligns and merges audio-visual content automatically with the Combiner Agent

### 2.1 Master Ma as AI Researcher
<table>
<tr>
<td align="center" width="50%">
<a href='https://www.bilibili.com/video/BV1AV411S7yc/?spm_id_from=333.337.search-card.all.click&vd_source=13182b3a133b27042e1f14577e85d60f' target='_blank'><img src='assets/masterma_cover.png' width=100%/></a>
Master Ma as AI Researcher
</td>
<td align="center" width="50%">
<a href='https://www.bilibili.com/video/BV1584y1N7cR/' target='_blank'><img src='assets/masterma_original_cover.png' width=100%/></a>
Original Video of Master Ma
</td>
</tr>
</table>

**Key Features:**
- Intelligent understanding and transformation of meme concepts
- Precise audio synthesis and precise scene matching

**Prompt:**
```
Create a humorous narrative about two PhD students seeking advice from Master Ma. For the two PhD students, one of them is known for high citation counts and the other for numerous publications. Transform martial arts terms into AI research terminology while keeping phrase lengths similar (length difference should be less than two Chinese characters). The story highlights their academic rivalry and ends with Master Ma advising against "窝里斗" (internal competition). Keep signature phrases like "大意了没有闪" (wasn't cautious enough) and "四两拨千斤" (achieving great results with minimal effort) while avoiding mentions of real institutions. The word combinations should be logical and appropriate for an academic context.
```

### 2.2 Xiao-Ming-Jian-Mo(小明剑魔) Meme
<table>
<tr>
<td align="center" width="50%">
<a href='https://www.bilibili.com/video/BV1AV411S7yc/?spm_id_from=333.337.search-card.all.click&vd_source=13182b3a133b27042e1f14577e85d60f' target='_blank'><img src='assets/xiaomingjianmo1_cover.png' width=100%/></a>
Video 1: Mixue's Response
</td>
<td align="center" width="50%">
<a href='https://www.bilibili.com/video/BV1AV411S7yc/?spm_id_from=333.337.search-card.all.click&vd_source=13182b3a133b27042e1f14577e85d60f' target='_blank'><img src='assets/xiaomingjianmo_findyourproblem_meme.png' width=100%/></a>
Video 2: Find Your Own Problems
</td>
</tr>
<tr>
<td align="center" width="50%">
<a href='https://www.bilibili.com/video/BV1AV411S7yc/?spm_id_from=333.337.search-card.all.click&vd_source=13182b3a133b27042e1f14577e85d60f' target='_blank'><img src='assets/xiaomingjianmo_mvp_cover.png' width=100%/></a>
Video 3: MVP
</td>
<td align="center" width="50%">
<a href='https://www.bilibili.com/video/BV1ZYQzY5E1x' target='_blank'><img src='assets/xiaomingjianmo_original_cover.png' width=100%/></a>
Video 4: Original 小明剑魔 Video
</td>
</tr>
</table>

The 小明剑魔 meme has gained massive popularity recently through his insightful yet comedic streaming commentary. Many content creators have successfully adapted his distinctive speech pattern into creative videos. We've used AI-Creator to generate three videos of this viral meme format, each capturing the unique style and energy of the original while adding new creative elements.

**Prompts:**
```
Video 1:
Background: Mixue Ice Cream is a national chain brand focusing on ice cream and tea beverages. On March 15th (Consumer Rights Day), they were reported to be using overnight lemons. However, compared to other exposures, using overnight lemons isn't considered a particularly serious violation and is somewhat understandable.

- Speaker: Snow King (Mixue's representative)
- Purpose: Emphasize that the **overnight lemon** situation isn't too serious, highlighting Mixue's good reputation
- Must preserve the phrases "Look in my eyes tell me why why baby why", "回答我"
- Must end with the word "说话"
- If the original text contains awkward phrasing, such as redundant words or confused semantics, don't imitate that style or sentence structure
- Ensure natural and fluent sentences
```
```
Video 2:
Based on the following scenario, create an angry rebuttal from Zhuge Liang (me):
- Speaker: Zhuge Liang (me)
- Start with "**北伐失败怎么不找找自己问题**" (Why don't you look at your own problems for the failure of the Northern Expedition), followed by "...找自己问题" pattern sentences that **all** reference anime events
- Anime examples must mention specific characters
- Only the **last** "...找自己问题" should return to the Northern Expedition scenario
- Use colloquial language and diverse anime references
```
```
Video 3:
Based on the following scenario, create an angry rebuttal from Zhuge Liang (me):
- Speaker: Zhuge Liang (me)
- Zhuge Liang (me) is challenged about why a certain Three Kingdoms character has a higher rating than him and launches a fierce rebuttal
- Must include: "三点零、十三点零、躺赢狗"
- Do not start with "零杠几"
- Later rating comparisons should show stark differences (can be exaggerated)
- Use colloquial language, align with historical facts, and only replace specific content
```

## 3. AI Music Videos
Ready to create music videos realizing your creative ideas? AI-Creator helps you write lyrics, select singers you specify, and generate matching visuals to bring your musical vision to life. The system can coordinate lyrics, visuals, and music to create engaging amateur music videos.

**How AI-Creator Makes Music Videos**
- Users just need to provide the music MIDI file, original lyrics, BGM file (optional), target voice file, and requirements. 
- Automatically performs loudness normalization and annotates the MIDI file using the Annotator Agent.
- Automatically calibrates and adapts lyrics at the word level via the Analyzer Agent.
- Automatically divides long rest intervals to reduce melodic errors and enables song covers.


<a href='https://www.bilibili.com/video/BV1AV411S7yc/?spm_id_from=333.337.search-card.all.click&vd_source=13182b3a133b27042e1f14577e85d60f' target='_blank'><img src='assets/airencuoguo_cover.png' width=60%/></a>

**Key Features:**
- Automated lyric generation based on themes
- Intelligent matching of visuals and lyrics

**Prompts:**
```
The song is performed by Patrick Star, focusing on the theme of ​**"the struggles of manuscript submission and dealing with overly critical reviewers"**, following the original lyrics' sentence structure while replacing specific content. It incorporates elements of reviewer nitpicking (e.g., questioning innovation, demanding redundant experiments) and expresses frustration with lines like "If only I could swap reviewers, this academic fate is too cruel" to highlight the emotional toll of peer review.
```


## 4. Cross-Culture Verbal Comedy Arts
Interested in bridging cultural gaps through comedy? Transform popular English talk show segments into authentic Chinese crosstalk performances, and vice versa. Complete with cultural adaptations and localized humor that resonates with audiences of different culture backgrounds.

**How AI-Creator Makes Talk Show Transitions**
- Users just need to provide the target cross-talk (comedy dialogue) audio file.
- Automatically adapts the script based on the provided target audio file.
- Automatically selects the appropriate vocal tone for voice cloning according to the emotional context of the script.

**Key Features:**
- Cultural context adaptation and localization of humor
- Performance style transformation while preserving core comedic elements
- Voice generation

### 4.1 English Stand-up Comedy to Chinese Crosstalk
<table>
<tr>
<td align="center" width="50%">
<a href=""><img src="assets/adapted_crosstalk_cover.png" width="100%"></a>
Chinese Crosstalk Adaptation
</td>
<td align="center" width="50%">
<a href="https://www.bilibili.com/video/BV1u1421t78T"><img src="assets/standup_original_cover.png" width="100%"></a>
Original Stand-up Comedy Segment
</td>
</tr>
</table>

### 4.2 Chinese Crosstalk to English Stand-up Comedy
<table>
<tr>
<td align="center" width="50%">
<a href=""><img src="assets/adapted_standupcomedy_cover.png" width="100%"></a>
Stand-up Comedy Adaptation
</td>
<td align="center" width="50%">
<a href="https://www.bilibili.com/audio/au4765690/"><img src="assets/crosstalk_original_cover.png" width="100%"></a>
Original Chinese Crosstalk Segment
</td>
</tr>
</table>

## 5. Novel-to-Screen Adaptation
Want to bring your favorite novels to life? AI-Creator transforms written narratives into compelling video adaptations, complete with AI-generated scenes, characters, and dialogues - all without the need for actual filming or actors. Experience your beloved stories in a whole new medium.

**How AI-Creator Makes Novel-to-Screen Adaption**

[lingxuan write here]

**Key Features:**
- Transforming novel narratives into visual storytelling by adapting descriptive text into cinematic scenes
- Automated scene matching that pairs textual descriptions with appropriate visual elements, ensuring narrative coherence

<a href="https://www.bilibili.com/video/BV1TmZ6YjEvV/"><img src="assets/joylife_cover.png" width="60%"></a>

We used AI-Creator to generate a video adaptation of the opening chapters from *Joy of Life*. Our agents analyzed the novel's text and automatically created a compelling video sequence by intelligently selecting and arranging relevant scenes from the TV series.

**Prompt:**
```
编写通顺的解说文案，字数达到1500。
```

## 6. Tech News Updates
Want to create engaging tech news videos? AI-Creator helps transform complex technical updates into visually appealing content with dynamic graphics and clear explanations that keep viewers informed and engaged.

**How AI-Creator Makes News Videos**

[Lingxuan write this part]

**Key Features:**
- Automated news content summarization
- Dynamic visuals selection and composition
- Clear audio narration synthesis

### 6.1 Tech News: OpenAI's GPT-4o Image Generation Release
<table>
<tr>
<td align="center" width="50%">
<a href="https://www.bilibili.com/video/BV12mZ6YLEqW/"><img src="assets/openai_news_cover.png" width="100%"></a>
Tech News made by AI-Creator
</td>
<td align="center" width="50%">
<a href="https://www.youtube.com/watch?v=2f3K43FHRKo"><img src="assets/tech_news_original_cover.png" width="100%"></a>
Original Tech Report
</td>
</tr>
</table>

**Prompt:**
```
Short tech news, colloquial expression within 250 words, check the accuracy of key terms, e.g. the GPT model name should be 4o instead of 4.0
```

### 6.2 Dune Movie Cast Updates
<table>
<tr>
<td align="center" width="50%">
<a href="https://www.bilibili.com/video/BV1m1Z6Y2Erb/"><img src="assets/dune_news_cover.png" width="100%"></a>
News About <i>Dune</i>
</td>
<td align="center" width="50%">
<a href="https://www.youtube.com/watch?v=AVQRnDFZ1Qs"><img src="assets/dune_original_cover.png" width="100%"></a>
Original Interview with <i>Dune</i> Cast
</td>
</tr>
</table>

**Prompt:**
```
[Add prompt example here]
```

# Acknowledgements

We would like to express our deepest gratitude to the numerous individuals and organizations that have made AI-Creator possible. This project stands on the shoulders of giants, benefiting from the collective wisdom of the open-source community and the groundbreaking work of AI researchers worldwide.

First and foremost, we are indebted to the open-source community and AI service providers whose tools and technologies form the foundation of our work:

- [CosyVoice](https://github.com/FunAudioLLM/CosyVoice)
- [Fish Speech](https://github.com/fishaudio/fish-speech)
- [Seed-VC](https://github.com/Plachtaa/seed-vc)
- [DiffSinger](https://github.com/MoonInTheRiver/DiffSinger)
Lingxuan: VideoRAG, LightRAG, nano-graphrag, ImageBind, CosyVoice, whisper-large-v3 turbo, MiniCPM-V-2_6-int4, Librosa, moviepy, FFmpeg

Our work has been significantly enriched by the creative contributions of content creators across various platforms:
- The talented creators behind the original video content we used for testing and demonstration
- The comedy artists whose work inspired our cross-cultural adaptations
- The filmmakers and production teams behind the movies and TV shows featured in our demos
- The content creators who have shared their knowledge and insights about video editing techniques

All content used in our demonstrations is for research purposes only. We deeply respect the intellectual property rights of all content creators and welcome any concerns or feedback regarding content usage.

<!-- # Framework of AI-Creator

[First a framework plot]
Then a short explanation on the framework, without specific technical details. -->

# Usage
## Clone and install
```
git clone https://github.com/HKUDS/AI-Creator.git

conda create --name aicreator python=3.10

conda activate cosyvoice

pip install -r requirements.txt
```

## Model download
```
# CosyVoice Model Download
cd tools/CosyVoice
mkdir -p pretrained_models
git clone https://www.modelscope.cn/iic/CosyVoice2-0.5B.git pretrained_models/CosyVoice2-0.5B
```
```
# Fish Speech Model Download
cd tools/fish-speech
huggingface-cli download fishaudio/fish-speech-1.5 --local-dir checkpoints/fish-speech-1.5
# 对于中国大陆用户，可使用 mirror 下载。
HF_ENDPOINT=https://hf-mirror.com huggingface-cli download fishaudio/fish-speech-1.5 --local-dir checkpoints/fish-speech-1.5
```
```
# Seed-VC Model Download
Initial activation of the song cover functionality triggers an automatic model download.
```

