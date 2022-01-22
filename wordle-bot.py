import numpy as np

words = np.loadtxt("word-list.txt", dtype=str)

word_length = 5

def comparison_score(candidate, comparator, full_match_value=2, partial_match_value=1):
    split_candidate, split_comparator = list(candidate), list(comparator)

    word_score = 0


    counted_letters = []

    for i in range(word_length):
        if split_candidate[i] == split_comparator[i]:
            word_score += full_match_value
            counted_letters.append(split_candidate[i])
        elif split_candidate[i] in counted_letters:
            continue
        elif split_candidate[i] in split_comparator:
            word_score += partial_match_value
            counted_letters.append(split_candidate[i])

    return word_score

def get_average_score(candidate):
    score_sum = 0

    for comparator in words:
        score_sum += comparison_score(candidate, comparator)
    
    return score_sum / len(words)

def get_best_starting_word():
    best_word = words[0]
    best_score = 0

    for word in words:
        print("Calculating score for", word)
        new_score = get_average_score(word)
        print("Got score of", new_score)
        if new_score >= best_score:
            best_word = word
            best_score = new_score

    print("Final result:")
    print(best_word, "won with a score of", best_score)

get_best_starting_word()