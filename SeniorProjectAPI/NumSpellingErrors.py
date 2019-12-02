import sys

from textblob import *

text_file_name = sys.argv[1]
path_to_file = "/usr/lib/cgi-bin/textfiles/"+text_file_name
text_file = open(path_to_file, "r")
text = text_file.read()
blob = TextBlob(text)

counter = 0

for word in blob.sentences.words:
    possible_words = word.spellcheck()
    if word != possible_words[0]:
        counter += 1

print(counter)

text_file.close()
