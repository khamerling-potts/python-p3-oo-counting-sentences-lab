#!/usr/bin/env python3


class MyString:
    def __init__(self, value=""):
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
        return self._value.endswith(".")

    def is_exclamation(self):
        return self._value.endswith("!")

    def is_question(self):
        return self._value.endswith("?")

    def count_sentences(self):
        split_value = self.value.split(" ")
        count = 0

        for word in split_value:
            print(word)
            if word.endswith(".") or word.endswith("?") or word.endswith("!"):
                count += 1

        return count


complex_string = MyString(
    "This, well, is a sentence. This is too!! And so is this, I think? Woo..."
)
complex_string.count_sentences()
