import openai
import os
from bin import translate
from bin import generate_vtt
from bin import add_subtitles
from bin import logger
from moviepy.editor import *

# Replace YOUR_DEEPL_API_KEY with your DeepL API key
deepl_api_key = "YOUR_DEEPL_API_KEY"

# Replace YOUR_OPENAI_API_KEY with your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

# Specify the folder path
folder_path = "input"

# List all files in the folder
file_names = os.listdir(folder_path)

# Loop over the files and print their names
for file_name in file_names:
    os.path.splitext(file_name)[0]
    logger.print_log("------------------------------")
    logger.print_log("###   Starting process for file " + file_name)
    logger.print_log("------------------------------")
    file_name_without_suffinx = os.path.splitext(file_name)[0]
    VIDEO_PATH = "input/" + file_name
    AUDIO_PATH = "input/" + file_name_without_suffinx + ".mp3"
    VTT_NAME = "output/" + file_name_without_suffinx + "transcription.vtt"

    # Load the video file
    video = VideoFileClip(VIDEO_PATH)

    # Extract the audio from the video
    audio = video.audio

    # Write the audio to a file
    audio.write_audiofile(AUDIO_PATH)

    # Close the video and audio files
    video.close()
    audio.close()

    # Replace FILE_NAME with your video name
    audio_file = open(AUDIO_PATH, "rb")

    # Transcribe the audio using OpenAI API
    logger.print_log("Starting transcript generation...")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    logger.print_log("Transcript generated!")

    # Translate the transcript from Polish to English using DeepL API
    translated_text = translate.translate_text_deepl(
        transcript["text"], "PL", "EN", deepl_api_key
    )

    # Generate timestamps for each sentence
    timestamps = generate_vtt.generate_timestamps(translated_text)

    # Write the VTT file
    generate_vtt.write_vtt_file(timestamps, VTT_NAME)

    # Set the path to the output video file
    output_file = "output/" + file_name_without_suffinx + "_with_EN_subtitles.mp4"

    # Add subtitles to the video using FFmpeg
    add_subtitles.add_subtitles(VIDEO_PATH, VTT_NAME, output_file)
