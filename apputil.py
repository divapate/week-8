from collections import defaultdict
import numpy as np
import random


class MarkovText(object):

    def __init__(self, corpus):
        self.corpus = corpus
        self.tokens = corpus.split()
        self.term_dict = None

    def get_term_dict(self):
        term_dict = defaultdict(list)

        # Build transition dictionary
        for i in range(len(self.tokens) - 1):
            current_word = self.tokens[i]
            next_word = self.tokens[i + 1]
            term_dict[current_word].append(next_word)

        # Convert back to normal dict
        self.term_dict = dict(term_dict)

        return self.term_dict


    def generate(self, seed_term=None, term_count=15):

        # Make sure dictionary exists
        if self.term_dict is None:
            raise ValueError("You must call get_term_dict() first.")

        # Choose starting word
        if seed_term:
            if seed_term not in self.term_dict:
                raise ValueError("Seed term not found in corpus.")
            current_word = seed_term
        else:
            current_word = random.choice(list(self.term_dict.keys()))

        output = [current_word]

        for _ in range(term_count - 1):

            next_words = self.term_dict.get(current_word)

            # If word has no followers (end of corpus case)
            if not next_words:
                current_word = random.choice(list(self.term_dict.keys()))
            else:
                current_word = np.random.choice(next_words)

            output.append(current_word)

        return " ".join(output)

corpus = "Astrid is very kind, is she not?"
text_gen = MarkovText(corpus)

text_gen.get_term_dict()
print(text_gen.term_dict)

print(text_gen.generate())
print(text_gen.generate(seed_term="is", term_count=10))
