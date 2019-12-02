import sys

from textblob import *

text_file_name = sys.argv[1]
path_to_file = "/usr/lib/cgi-bin/textfiles/" + text_file_name
text_file = open(path_to_file, "r")
text = text_file.read()
blob = TextBlob(text)

blobTest = TextBlob("Welcome to the [Company] website. My company believes that good financial decisions don't have to be "
                "confusing. I can provide simple, proven techniques that can help you make the most of your money and "
                "help achieve more of your financial goals. This site will not only introduce you to my company "
                "philosophy and services, but it will also offer a wealth of educational materials, articles, "
                "newsletters, calculators, and other tools -- all designed to keep you up-to-date on financial "
                "issues, strategies, and trends. This educational material is updated frequently, as is our calendar "
                "of events, which lists upcoming financial workshops that you may want to attend. If you have any "
                "questions or want to schedule a complimentary meeting to discuss your specific questions, "
                "you can e-mail me at (e-mail address) or call (phone number). company philosophy or the company "
                "philosophy")

words = {}
for np in blobTest.noun_phrases:
    num_occurrences = words.get(np, 0)
    update_word = {np: num_occurrences + 1}
    words.update(update_word)

top_five = sorted(words)[:5]

print(top_five)

# text_file.close()
