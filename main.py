from trie import Trie

def main():
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
    trie = Trie()
    trie.insert(data1, data2)

    result = trie.search('+46-73-212345')
    print(result)


if __name__ == '__main__':
    main()
