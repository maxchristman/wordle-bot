import numpy as np
import os


all_words = np.loadtxt("word-list.txt", dtype=str)

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

def get_average_score(candidate, word_list=all_words):
    score_sum = 0

    for comparator in word_list:
        score_sum += comparison_score(candidate, comparator)
    
    return score_sum / len(word_list)

def score_words(word_list=all_words):
    scored_words = []
    for word in word_list:
        score = get_average_score(word)
        print(word, "has an average score of", score)
        scored_words.append((word, score))
    
    scored_words.sort(key=lambda x:x[1], reverse=True)
    return scored_words

def show_best_words(word_list=all_words):
    best_words = score_words(word_list)
    os.system("clear")

    i = 0

    while i < 20 and i < len(word_list):
        print("#" + str(i+1) + ":", best_words[i])
        i += 1

# show_best_starting_words()

def narrow_word_list(initial_list, contained_letters, matches, excluded_letters):
    new_list = []
    for word in initial_list:
        split_word = list(word)

        valid = True

        for letter in excluded_letters:
            if letter in split_word:
                valid = False
                break

        for letter in contained_letters:
            if letter not in split_word:
                valid = False 
                break

        for match in matches:
            if word[match[0]] != match[1]:
                valid = False

        if valid:
            new_list.append(word)
    
    return new_list

narrowed_list = narrow_word_list(all_words, [], [(1, 'i'), (2, 'n'), (3, 'c'), (4, 'e')], ['s', 't', 'a', 'r', 'l', 'o'])

show_best_words(narrowed_list)