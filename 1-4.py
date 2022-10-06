from collections import Counter
import re
from string import punctuation
import os.path

class Text:
    __slots__ = ["name", "filtered", "popular_list"]

    def __init__(self, name):
        if not os.path.isfile(name):
            raise ValueError("File doesnt exist!")
        self.ame = name
        # Open text file for reading.

    def searcher(self, inp):
        occurrences = 0
        with open(self.name) as f:
            for lines in f:
                occurrences += lines.lower().count(inp)
            return f'Number of occurrences of {inp} is {occurrences}'

    def count_word(self):
        words = 0
        with open(self.name) as f:
            for lines in f:
                words += len(lines.split())
        return words

    def count_line(self):
        sentences = 0
        with open(self.name) as f:
            for lines in f:
                if not lines.endswith('.' or '!' or '?'):
                    sentences -= 1
                sentences += len(re.split(r"[.!?]+", lines))
        return sentences

    def most_common(self):
        with open(self.name) as f:
            text = f.read()
            count = Counter(text.translate(punctuation).lower().split())
            print(count)
        return [item for item in count.most_common(10)]

    def __str__(self):
        return f'Number of words: {self.count_word()} Number of sentences: {self.count_line()}\n' \
               f'Most popular words: {self.most_common()}'

def main():
    obj = Text('test.txt')
    print(obj)
    print(obj.searcher('b'))


if __name__ == '__main__':
    main()