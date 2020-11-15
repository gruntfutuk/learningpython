from collections import Counter


def get_text(filename):
....with open(filename) as f:
........return f.read()


def simple(text):
....text = text.lower()
....punctuation = """!()-[]{};:'"\,<>./?@#$%^&*_~"""
....for character in text:
........if character in punctuation:
............text = text.replace(character, "")
....return text


def using_counter(words):
....return Counter(words)


def using_count(words):
....frequency = {}
....search_words = set(words)
....for word in search_words:
........frequency[word] = text.count(word)
....return frequency


text = get_text("alice_in_wonderland.txt")
words = simple(text).split()
countering = using_counter(words)
counting = using_count(words)

words_found = set(list(countering.keys()) + list(counting.keys()))
for word in words_found:
....print(f"{word:15} {countering.get(word, 'xxx'):3}  {counting.get(word, 'xxx'):3}")
