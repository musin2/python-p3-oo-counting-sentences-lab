#!/usr/bin/env python3

class MyString:
  
    def __init__(self, value = "") -> None:
        self.value = value

    @property
    def value(self):
        return self._value
  
    @value.setter
    def value(self, val):
        if not isinstance(val, str):
            print("The value must be a string.")
        else:
            self._value = val

    def is_sentence(self):
        return self.value.endswith('.')
    
    def is_question(self):
        return self.value.endswith("?")
    
    def is_exclamation(self):
        return self.value.endswith("!")
    
    def count_sentences(self):
        # Replace "!" and "?" with "."
        sen = self.value.replace("!",".").replace("?",".")
        # Split the string by "."
        sentences = sen.split(".")
        # Remove empty elements
        sentences = [sentence for sentence in sentences if sentence.strip()]
        return len(sentences)

str1 = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")
str1.count_sentences()