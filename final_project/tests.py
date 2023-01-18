import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishtToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench("Hello"), "Bonjour") # test when Hello is given is as input the output is Bonjour.
        self.assertEqual(englishToFrench(" "), " ") # test when a single blank character is given is as input the output is a blank.
        self.assertEqual(englishToFrench(""), "***No text was input***") # test when a single blank character is given is as input the output is a blank.
        self.assertEqual(englishToFrench("123"), "123") # test when numerals are given is as input the output is the same numerals.
        

class TestFrenchToEnglish(unittest.TestCase): 
    def test2(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")  # test when Bonjour is given as input the output is Hello. 

        
unittest.main()