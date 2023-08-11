from unittest import TestCase
from trie import Trie


class TestTrieSearch(TestCase):
    def setUp(self):
        data1 = {
            'operator': 'A',
            'data': [
                '1 0.9',
                '268 5.1',
                '46 0.17',
                '4620 0.0',
                '468 0.15',
                '4631 0.15',
                '4673 0.9',
                '46732 1.1'
            ]
        }
        data2 = {
            'operator': 'B',
            'data': [
                '1 0.92',
                '44 0.5',
                '46 0.2',
                '467 1.0',
                '48 1.2'
            ]
        }
        self.trie = Trie()
        self.trie.insert(data1, data2)

    def test_found_longest_key(self):
        search_string = '+46-73-212345'
        result = self.trie.search(search_string)
        self.assertEqual(result['key'], '46732')
        self.assertEqual(result['value'], 1.1)
        self.assertEqual(result['operator'], ['A'])

    def test_key_not_found(self):
        search_string = '+63-123-4567'
        result = self.trie.search(search_string)
        self.assertIsNone(result, msg=f'Expected no result, got {result}')

    def test_empty_key(self):
        search_string = ''
        result = self.trie.search(search_string)
        self.assertIsNone(result, msg=f'Expected no result, got {result}')

    def test_invalid_key_alpha(self):
        search_string = '48c'
        result = self.trie.search(search_string)
        self.assertIsNone(result, msg=f'Expected no result, got {result}')