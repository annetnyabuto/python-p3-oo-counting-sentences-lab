#!/usr/bin/env python3

class MyString:
  def __init__(self, value = ''):
      self.value = value

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, value):
    if isinstance(value, str):
        self._value = value
    else:
        print("The value must be a string.")
  

  def is_sentence(self):
    return self.value.endswith(".")

  def is_question(self):
    return self.value.endswith("?")

  def is_exclamation(self):
    return self.value.endswith("!")

  def count_sentences(self):
    replaced = self.value.replace('!', '.').replace('?', '.')
    splited = replaced.split('.')
    striped = [sent.strip() for sent in splited if sent.strip()]
    return len(striped)


# Test
string = MyString("This is a string! It has three sentences. Right?")
print(dir(string))
print(string.is_sentence())
print(string.count_sentences())