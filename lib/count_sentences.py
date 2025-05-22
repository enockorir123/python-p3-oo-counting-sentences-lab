#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=''):
        self._value = ''
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        # Split on sentence-ending punctuation marks: ., !, ?
        # Use regex to split on one or more of these punctuation marks
        parts = re.split(r'[.!?]+', self._value)
        # Filter out empty strings after split
        sentences = [part.strip() for part in parts if part.strip()]
        return len(sentences)