from unittest import TestCase
from trie import Trie


class TestTrieInsert(TestCase):
    def test_insertion(self):
        data1 = {
            'operator': 'A',
            'data': ['1 2']
        }
        data2 = {
            'operator': 'B',
            'data': ['3 4']
        }
        trie = Trie()
        trie.insert(data1, data2)

        self.assertEqual(trie.root.children[1].value, 2)
        self.assertEqual(trie.root.children[3].value, 4)

    def test_no_common_prefix(self):
        data1 = {
            'operator': 'A',
            'data': ['1 0.9']
        }
        data2 = {
            'operator': 'B',
            'data': ['44 0.5']
        }
        trie = Trie()
        trie.insert(data1, data2)
        entries = trie.count_pairs(trie.root)

        self.assertEqual(trie.root.children[1].value, 0.9)
        self.assertEqual(trie.root.children[4].value, '')
        self.assertEqual(trie.root.children[4].children[4].value, 0.5)
        self.assertEqual(entries, 2)

    def test_with_common_prefix(self):
        data1 = {
            'operator': 'A',
            'data': ['1 0.9']
        }
        data2 = {
            'operator': 'B',
            'data': ['11 0.5']
        }
        trie = Trie()
        trie.insert(data1, data2)

        self.assertEqual(trie.root.children[1].value, 0.9)
        self.assertEqual(trie.root.children[1].children[1].value, 0.5)
        self.assertEqual(trie.count_pairs(trie.root), 2)

    def test_different_operators(self):
        data1 = {
            'operator': 'A',
            'data': ['1 0.9', '2 100', '3 5']
        }
        data2 = {
            'operator': 'B',
            'data': ['1 0.9', '2 0']
        }
        trie = Trie()
        trie.insert(data1, data2)
        self.assertListEqual(trie.root.children[1].operator, ['A','B'])
        self.assertListEqual(trie.root.children[2].operator, ['B'])
        self.assertEqual(trie.root.children[1].value, 0.9)
        self.assertEqual(trie.root.children[2].value, 0)
        self.assertEqual(trie.count_pairs(trie.root), 3)

    def test_same_operator(self):
        data1 = {
            'operator': 'A',
            'data': ['1 0.9', '2 3', '3 5', '0 0']
        }
        data2 = {
            'operator': 'A',
            'data': ['1 0.9', '2 5', '5 7']
        }
        trie = Trie()
        trie.insert(data1, data2)
        self.assertEqual(trie.count_pairs(trie.root), 5)
        self.assertListEqual(trie.root.children[1].operator, ['A'])

    def test_invalid_key(self):
        data1 = {
            'operator': 'A',
            'data': ['']
        }
        data2 = {
            'operator': 'B',
            'data': ['1 1']
        }
        trie = Trie()
        trie.insert(data1, data2)
        self.assertEqual(trie.root.children[1].value, 1)

    def test_alpha_in_data(self):
        data1 = {
            'operator': 'A',
            'data': ['a 2']
        }
        data2 = {
            'operator': 'B',
            'data': ['1 a']
        }
        trie = Trie()
        trie.insert(data1, data2)
        self.assertEqual(trie.count_pairs(trie.root), 0)