import time
from itertools import product
from spellchecker import SpellChecker

spell = SpellChecker()

def is_valid_word(word):
    """
    Checks if a word is spelled correctly.
    """
    return word in spell

def generate_unique_combinations(word_chunks, max_length=4):
    """
    Generates all unique combinations of word chunks without repetition.
    """
    all_combinations = set()
    used_combinations = set()  # Keep track of used combinations

    # Convert word chunks to lowercase
    word_chunks_lower = [chunk.lower() for chunk in word_chunks]

    # Generate combinations up to the specified maximum length
    for r in range(1, min(len(word_chunks_lower), max_length) + 1):
        for combo in product(word_chunks_lower, repeat=r):
            candidate = ''.join(combo)
            if is_valid_word(candidate) and combo not in used_combinations:
                all_combinations.add(candidate)
                used_combinations.add(combo)  # Mark the combination as used

    return all_combinations

if __name__ == "__main__":
    start_time = time.time()

    word_chunks = ['ics', 'clo', 'acr', 'pan', 'to', 'oni', 'wn', 'at', 'ob', 'is', 'st', 'hly', 'as', 'gm', 'mim', 'ters', 'usi', 'ill', 'rin', 'ing']

    # Generate valid words with a maximum length of 4 (no repetition)
    unique_valid_words_set = generate_unique_combinations(word_chunks, max_length=4)

    # Print valid words
    for word in unique_valid_words_set:
        print(f"Valid word (unique): {word}")

    print(f"Total unique valid words: {len(unique_valid_words_set)}")
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")