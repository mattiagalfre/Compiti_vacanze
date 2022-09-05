#Anagrams

def find_anagrams(word, candidates):
    anagrams = []
    wordL = word.lower()
    for candidate in candidates:
        candL = candidate.lower()
        if(candL != wordL and sorted(wordL) == sorted(candL)):
            anagrams.append(candidate)
    return anagrams
