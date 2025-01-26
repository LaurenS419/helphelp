## NOT USED

countable_words = ['like', 'um', 'uhm', 'so']

def count(transcription):
    counts = {}

    for word in transcription:
        if word.lower() in countable_words:
            counts[word.lower()] = counts.get(word.lower(), 0) + 1


    return counts

def total_count(transcription):
    return len(transcription)


if __name__ == "__main__":
    count()