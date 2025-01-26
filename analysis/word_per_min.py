from mutagen.mp3 import MP3

def get_wpm(word_count, filepath):

    audio = MP3(filepath)
    mins = float(audio.info.length) / 60.0

    return float(word_count) / audio.info.length