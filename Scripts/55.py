class Text:
  def __init__(self, text):
    self.text = text

  def charcount1(self):
    return len(self.text)

  def lettercount(self):
    letters = [char for char in self.text if char.isalpha()]
    return len(letters)

  def spacecount(self):
    spaces = [char for char in self.text if char.isspace()]
    return len(spaces)

  def charcount2(self):
    chars = [char for char in self.text if not char.isspace()]
    return len(chars)

  def wordarray(self):
    words = self.text.split()
    return words

  def sentencearray(self):
    sentences = self.text.split('.')
    return sentences

text = Text("Вставить текст")
charcount1 = text.charcount1()
print(charcount1)
lettercount = text.lettercount()
print(lettercount)
spacecount = text.spacecount()
print(spacecount)
charcount2 = text.charcount2()
print(charcount2)
wordarray = text.wordarray()
print(wordarray)
sentencearray = text.sentencearray()
print(sentencearray)