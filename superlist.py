class SuperList(list):
    def save(self, filename):
        with open(filename, 'w') as out:
            for i in self:
                out.write(f"{i}\n")

    @classmethod
    def load(cls, filename):
        res = SuperList()
        with open(filename, 'r') as inp:
            for s in inp:
                if '.' in s:
                    res.append(float(s))
                else:
                    res.append(int(s))
        return res


sl = SuperList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
sl.save("superlist.txt")
s2 = SuperList.load("superlist.txt")
print(s2)
