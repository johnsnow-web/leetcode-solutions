class SegmentTree:
    def __init__(self, s):
        self.n = len(s)
        size = 4 * self.n

        self.left = [''] * size
        self.right = [''] * size
        self.pref = [0] * size
        self.suff = [0] * size
        self.best = [0] * size

        self.build(1, 0, self.n - 1, s)

    def build(self, node, l, r, s):
        if l == r:
            self.left[node] = self.right[node] = s[l]
            self.pref[node] = self.suff[node] = self.best[node] = 1
            return

        mid = (l + r) // 2
        self.build(node * 2, l, mid, s)
        self.build(node * 2 + 1, mid + 1, r, s)

        self.pull(node, l, r)

    def pull(self, node, l, r):
        L = node * 2
        R = node * 2 + 1

        self.left[node] = self.left[L]
        self.right[node] = self.right[R]

        self.pref[node] = self.pref[L]
        self.suff[node] = self.suff[R]
        self.best[node] = max(self.best[L], self.best[R])

        mid = (l + r) // 2

        if self.right[L] == self.left[R]:
            # Combine suffix of left + prefix of right
            combined = self.suff[L] + self.pref[R]
            self.best[node] = max(self.best[node], combined)

            # Entire left segment has the same character
            if self.pref[L] == mid - l + 1:
                self.pref[node] = self.pref[L] + self.pref[R]

            # Entire right segment has the same character
            if self.suff[R] == r - mid:
                self.suff[node] = self.suff[R] + self.suff[L]

    def update(self, node, l, r, idx, ch):
        if l == r:
            self.left[node] = self.right[node] = ch
            return

        mid = (l + r) // 2

        if idx <= mid:
            self.update(node * 2, l, mid, idx, ch)
        else:
            self.update(node * 2 + 1, mid + 1, r, idx, ch)

        self.pull(node, l, r)

    def change(self, idx, ch):
        self.update(1, 0, self.n - 1, idx, ch)

    def answer(self):
        return self.best[1]


class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        tree = SegmentTree(s)
        ans = []

        for ch, idx in zip(queryCharacters, queryIndices):
            tree.change(idx, ch)
            ans.append(tree.answer())

        return ans