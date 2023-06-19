import datetime
from bin import logger

def generate_timestamps(translated_text):
    # Split the translated text into sentences
    logger.print_log("Spliting text to sentences...")
    sentences = translated_text.split(". ")

    # Generate timestamps for each sentence
    logger.print_log("Generating timestamps for each sentence...")
    timestamps = []
    start_time = datetime.time.min
    for i, sentence in enumerate(sentences):
        duration = len(sentence) / 10
        end_time = (datetime.datetime.combine(datetime.date.today(), start_time) + datetime.timedelta(seconds=duration)).time()
        timestamps.append((start_time, end_time, sentence))
        start_time = end_time
    logger.print_log("Timestamps created!")
    return timestamps

def write_vtt_file(timestamps, VTT_NAME):
    # Write the VTT file
    logger.print_log("Creating VTT file...")
    with open(VTT_NAME, "w") as f:
        f.write("WEBVTT\n\n")
        for i, timestamp in enumerate(timestamps):
            start_time, end_time, sentence = timestamp
            f.write("{} --> {}\n{}\n\n".format(
                start_time.strftime('%H:%M:%S.%f')[:-3],
                end_time.strftime('%H:%M:%S.%f')[:-3],
                sentence)
            )
    logger.print_log("File created!")