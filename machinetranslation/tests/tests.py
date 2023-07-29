"""
Module: tests.py

This module contains test cases for machine translation functions.
"""

from . import english_to_french, french_to_english

# Test for the translation of the word 'Hello' and 'Bonjour'
ENGLISH_WORD = 'Hello'
french_translation = english_to_french(ENGLISH_WORD)
print(f"Translation of '{ENGLISH_WORD}' to French: {french_translation}")

# Test for the translation of the word 'Bonjour' and 'Hello'
FRENCH_WORD = 'Bonjour'
english_translation = french_to_english(FRENCH_WORD)
print(f"Translation of '{FRENCH_WORD}' to English: {english_translation}")
