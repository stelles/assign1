from re import *
from collections import *

# Tokenizer class

class Tokenizer:
    
    
    def __init__(self, raw_text):
        self.raw_text = raw_text
        self.clean_tokens = self.tokenize(raw_text)
        self.sentences = self.sentence_parse(self.clean_tokens)

    def clean_word(self, word):
            
        clean_words = []

        while word and not word[0].isalpha() and not word[0].isdigit():
            clean_words.append(word[0])
            word = word[1:]
        while word and not word[len(word)-1].isalpha() and not word[len(word)-1].isdigit():
            # if word[len(word)-1] != '\n':
            clean_words.append(word[len(word)-1])
            word = word[:len(word)-1]
        clean_words.append(word.lower())
        return clean_words

    def tokenize(self, raw_text):

        tokens = []
            
        clean_tokens = []   
        raw_text = raw_text.replace('\n', ' ')
        raw_tokens = raw_text.split(' ')
        for word in raw_tokens:
            if not word.isalpha() or not word.isdigit():
                clean_tokens.extend(self.clean_word(word))
            else:
                clean_tokens.append(word.lower())   
        return clean_tokens     
                    
    def sentence_parse(self, clean_tokens):
        
        clean_sent = []
        sentence = ""

        for word in clean_tokens:
            if sentence == "":
                sentence += word
            elif word.isalpha() or word.isdigit():
                sentence += " " + word
            else:
                sentence += word
            if word == '.':
                clean_sent.append(sentence)
                sentence = ""

        return clean_sent


    def analysis(self):
        number_tokens = []
        letter_tokens = []
        combo_tokens = []

        freq_table = []

        for word in self.clean_tokens:
            if word.isdigit():
                number_tokens.append(word)
            if word.isalpha():
                letter_tokens.append(word)
            if match("[A-Za-z]*", word) and match("[0-9]*", word):
                combo_tokens.append(word)
            if word.isalpha() or len(word) > 1:
                freq_table.append(word)
        
        self.freq_table = Counter(freq_table)
        self.number_tokens = set(number_tokens)
        self.letter_tokens = set(letter_tokens)
        self.combo_tokens = set(combo_tokens)

        print "%%%%%%%%% Top 100 words : Frequency %%%%%%%%%%%%"

        for w in self.freq_table.most_common(100):
            print w[0] + " : ",
            print w[1]

        freq_table_nocounter = [w for w in freq_table if w not in self.stopword_list]

        print "%%%%%% Top 100 non-stopwords : Frequency %%%%%%%"

        for w in Counter(freq_table_nocounter).most_common(100):
            print w[0] + " : ",
            print w[1]


        print "%%%%%%%% Top 100 word pairs : Frequency %%%%%%%%%"

        freq_table_pairs = []
        for i in range(len(freq_table)-1):
            if freq_table[i] not in self.stopword_list and freq_table[i+1] not in self.stopword_list:
                freq_table_pairs.append(freq_table[i] + " " + freq_table[i+1])

        for p in Counter(freq_table_pairs).most_common(100):
            print p[0] + " : ",
            print p[1]



        print "Frequency of single words : ",
        print float(len([x for x in self.freq_table.most_common() if x[1] == 1]))/len(self.freq_table)


        print "Distinct Number count : %d" % len(self.number_tokens)
        print "Distinct Word count : %d" % len(self.letter_tokens)
        print "Distinct Combo count : %d" % len(self.combo_tokens)


    def add_stop_tokens(self, stopword_list):
        self.stopword_list = stopword_list


if __name__ == "__main__":
    
    f = open("nc.txt", "r")

    raw = f.read()

    f.close()

    f = open("stopwords.txt", 'r')

    stop_list = f.read()
    f.close()

    my_tokens = Tokenizer(raw)
    my_tokens.add_stop_tokens(stop_list.replace('\r', "").split('\n'))


    my_tokens.analysis()
