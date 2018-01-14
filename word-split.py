line = input('Enter a phrase: Hell')
words = [word for word in line.split()]
for counter, word in enumerate(words):
  print(word,':',counter)