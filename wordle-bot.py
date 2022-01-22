import numpy as np
import os


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

def score_starting_words():
    scored_words = []
    for word in words:
        score = get_average_score(word)
        print(word, "has an average score of", score)
        scored_words.append((word, score))
    
    scored_words.sort(key=lambda x:x[1], reverse=True)
    return scored_words


def show_best_starting_words():
    best_words = score_starting_words()
    os.system("clear")

    for i in range(20):
        print("#" + str(i+1) + ":", best_words[i])

show_best_starting_words()