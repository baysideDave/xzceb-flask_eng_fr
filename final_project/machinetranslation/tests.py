import unittest
from translator import englishToFrench, frenchToEnglish

class TestEnglishtToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench("Hello"), "Bonjour") # test when Hello is given is as input the output is Bonjour.
        self.assertEqual(englishToFrench(" "), " ") # test when a single blank character is given is as input the output is a blank.
        self.assertEqual(englishToFrench(""), "***Error: No text was input***") # test when a single blank character is given is as input the output is a blank.
        self.assertEqual(englishToFrench("123"), "123") # test when numerals are given is as input the output is the same numerals.
        self.assertEqual(englishToFrench("this is strange"), "Ceci est étrange") # test when numerals are given is as input the output is the same numerals.
        #self.assertEqual(englishToFrench("flat"), "Plate")# simple phrase 

class TestFrenchToEnglish(unittest.TestCase): 
    def test2(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")  # test when Bonjour is given as input the output is Hello. 
        self.assertEqual(frenchToEnglish(" "), " ") # test when a single blank character is given is as input the output is a blank.
        self.assertEqual(frenchToEnglish(""), "***Error: No text was input***") # test when a single blank character is given is as input the output is a blank.
        self.assertEqual(frenchToEnglish("cela est étrange"), "This is strange") # translation of french poetry
        self.assertEqual(frenchToEnglish("123"), "123") # test when numerals are given is as input the output is the same numerals.
        #self.assertEqual(frenchToEnglish("plate"), "Flat") # simple phrase
unittest.main()
