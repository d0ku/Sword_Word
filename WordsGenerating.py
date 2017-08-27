import random

class Random_Word_Generator:

    dictionary = {}
    dictionary_length = 0

    def __init__(self):
        pass


    def load_dictionary(self,location="dictionaries/English/Ascii_letters.txt"):
        with open(location, "r") as english_dictionary:
            words = []
            file_length = 0
            for x in english_dictionary:
                file_length += 1
                words.append(x)

        indexes = [x for x in range(0, file_length)]

        self.dictionary = dict(zip(indexes, words))
        self.dictionary_length = file_length

    def load_english_dictionary(self):
        with open("dictionaries/words_alpha.txt", "r") as english_dictionary:
            words = []
            file_length = 0
            for x in english_dictionary:
                file_length += 1
                words.append(x)

        indexes = [x for x in range(0, file_length)]

        self.dictionary = dict(zip(indexes, words))
        self.dictionary_length = file_length

    def set_box(self, box):
        self.box = box

    def random_english_word(self, max_length=50):

        word_number = random.randint(0, self.dictionary_length)
        corresponding_word = self.dictionary[word_number]
        while len(corresponding_word) > max_length:
            word_number = random.randint(0, self.dictionary_length - 2)
            corresponding_word = self.dictionary[word_number]

        word_object_to_return = Word(corresponding_word, self.box)
        return word_object_to_return


class Word:
    word = ""
    length = 0
    begin_point = 0
    end_point = 0
    height = 0

    def __init__(self, word, box):
        self.box = box
        temp = ""
        for x in word:
            if x != "\n":
                temp += x
        self.word = temp
        self.length = len(word)
        self.height = random.randint(0, len(self.box.matrix[0]) - 1)
        self.end_point = 0
        self.begin_point = self.end_point - self.length