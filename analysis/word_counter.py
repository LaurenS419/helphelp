
countable_words = ['like', 'um', 'uhm', 'so']

def count(transcription):
    counts = {}

    for word in transcription:
        if word in countable_words:
            counts[word] = counts.get(word, 0) + 1


    return counts

def total_count(transcription):
    return len(transcription)


if __name__ == "__main__":
    count()