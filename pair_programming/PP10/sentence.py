
#!/usr/bin/env python3
# Pair programming 10
# group member: Victoria DiTomasso, Yingchen Liu, Yuxi Liu

import reprlib

class Sentence:
    def __init__(self, text):
        self.words = text.split()
        self.text = text

    def __iter__(self):
        for word in self.words:
            yield word

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

### testing ###

# test_sent = Sentence('This is a sentence')
# for word in test_sent:
#     print(word)
