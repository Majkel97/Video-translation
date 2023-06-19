# Video translation

You can use this project to create English subtitles and videos with English subtitles from a video with Polish transcription.

## Steps

1. Read all video (.mp4) files from the specified folder.
2. Get audio and create .mp3 file.
3. Transcribe the audio using OpenAI API.
4. Translate the transcript from Polish to English using DeepL API.
5. Generate timestamps for each sentence and save as .vtt file.
6. Add subtitles to the video using FFmpeg.

## Installation

1. Download code from this repository and open it in IDE (for example Visual Studio Code).

2. Create a virtual environment and activate it.

```bash
python -m venv /path/to/new/virtual/environment
```

3. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r requirements.txt
```

## Usage

1. Insert your API keys to OpenAI and DeepL at main.py file. You can get them from [OpenAI](https://platform.openai.com/account/api-keys) and [DeepL](https://www.deepl.com/pl/account/summary).

```python
# Replace YOUR_DEEPL_API_KEY with your DeepL API key
deepl_api_key = 'YOUR_DEEPL_API_KEY'

# Replace YOUR_OPENAI_API_KEY with your OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'
```

2. Add video file to /input/ folder and set up proper name at main.py file.

```python
# Replace FILE_NAME with your video name
audio_file = open("input/FILE_NAME.mp4", "rb")
```

3. Run script.

4. Get created transcription.vtt file and / or new video with subtitles from /output/ folder.
