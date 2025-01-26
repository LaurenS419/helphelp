
def process(transcription):
    print(transcription)
    processed = [word.strip(" ,.?!-") for word in transcription.split(" ") if word.strip() != '']
    #processed = transcription.split(" ")

    return processed


if __name__ == "__main__":
    process()