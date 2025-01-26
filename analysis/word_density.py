
# STOP_WORDS = ["the", "i", "me", "you", "are", ""] #necessary?


def find_dense(transcription):

    indices = []  
    window_size = 10

    start = 0
    stop = min(start + window_size, len(transcription)) 

    while start < len(transcription):
        tracker = {}  

        for j in range(start, stop):
            word = transcription[j].lower()
            tracker[word] = tracker.get(word, 0) + 1

            if tracker[word] == 2: 
                for i in range(start, stop):
                    if transcription[i].lower() == word and i not in indices:
                        indices.append(i)

        
        start += window_size
        stop = min(start + window_size, len(transcription)) 

    return indices


if __name__ == "__main__":

    trans = [
    "According", "to", "all", "known", "laws", "of", "aviation", # 6
    "there", "is", "no", "way", "a", "bee", "should", "be", "able", "to", "fly", # 17
    "Its", "wings", "are", "too", "small", "to", "get", "its", "fat", "little", "body", "off", "the", "ground", #31
    "The", "bee", "of", "course", "flies", "anyway", "because", "bees", "don't", "care", "what", "humans", "think", "is", "impossible", #46
    "Yellow", "black", "Yellow", "black", "Yellow", "black", "Yellow", "black", #54
    "Ooh", "black", "and", "yellow", #58
    "Let's", "shake", "it", "up", "a", "little" #64
    ]

    indices = find_dense(trans)

    print(indices)

    for element in indices:
        print(trans[element])

    #return indices

