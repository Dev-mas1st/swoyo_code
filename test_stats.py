import unittest
from stats import text_stat


class Test(unittest.TestCase):
    def test_text_stat(self):
        self.assertEqual(text_stat("lorem.txt"),{'a': (28, 25), 'b': (5, 5), 'c': (10, 9), 'd': (16, 15), 'e': (59, 45), 'f': (6, 6), 'g': (11, 11), 'h': (14, 14), 'i': (32, 27), 'k': (7, 7), 'l': (17, 15), 'm': (18, 16), 'n': (38, 30), 'o': (25, 23), 'p': (18, 17), 'r': (24, 23), 's': (39, 33), 't': (43, 36), 'u': (17, 17), 'v': (5, 4), 'w': (6, 6), 'x': (2, 2), 'y': (13, 13), 'A': (1, 1), 'I': (6, 6), 'L': (5, 5), 'M': (1, 1), 'P': (1, 1), 'word_amount': 91, 'paragraph_amount': 4, 'bilingual_word_amount': 61})
        self.assertEqual(text_stat("lorem"), {'error': "[Errno 2] No such file or directory: 'lorem'"})
        self.assertEqual(text_stat("test.docx"), {'error': "'utf-8' codec can't decode byte 0xd2 in position 16: invalid continuation byte"})
        self.assertEqual(text_stat(1), {'error': 'Cannot open console output buffer for reading'})
