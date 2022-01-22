class Solution:
    def sortSentence(self, s: str) -> str:
        return ' '.join(x[0] for x in sorted([(x[:-1], x[-1]) for x in s.split()], key=lambda x: x[1]))
