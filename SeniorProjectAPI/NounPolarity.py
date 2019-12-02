import sys

from textblob import *

text_file_name = sys.argv[1]
path_to_file = "/usr/lib/cgi-bin/textfiles/"+text_file_name
text_file = open(path_to_file, "r")
text = text_file.read()
blob = TextBlob(text)

