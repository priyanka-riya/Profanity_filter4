import re

# Load bad words from file
with open('data/bad_words.txt', 'r') as file:
    bad_words = [word.strip().lower() for word in file.readlines()]

# Regex to replace bad words with *
def censor_text(text):
    pattern = re.compile(r'\b(' + '|'.join(re.escape(word) for word in bad_words) + r')\b', re.IGNORECASE)
    return pattern.sub(lambda m: '*' * len(m.group()), text)
