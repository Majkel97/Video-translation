import ffmpeg
from bin import logger

def add_subtitles(input_file, subtitle_file, output_file):
    # Use FFmpeg to add the subtitle track to the video
    logger.print_log("Adding subtitles to a video...")
    input_stream = ffmpeg.input(input_file)
    subtitles = ffmpeg.filter(input_stream.video, "subtitles", subtitle_file)
    output_stream = ffmpeg.output(subtitles, input_stream.audio, output_file, vcodec="h264", acodec="copy", format="mp4")
    try:
        ffmpeg.run(output_stream, capture_stderr=True)
        logger.print_log("Process completed!")
    except ffmpeg.Error as e:
        print(e.stderr.decode())
        logger.print_log("Something goes wront!")