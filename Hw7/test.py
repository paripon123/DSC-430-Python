class WarAndPeacePseudoRandomNumberGenerator:

    def __init__(self,seed):
        """Initiate Seed Number"""

        self.seed = seed
        self.index_lst = []
        self.index_lst_dec = []
        self.index = 0
        file = open('war-and-peace.txt')
        text = file.read()
        words = text.split()

        for i in range(len(words)):
            self.index_lst.append(i)
            self.index_lst_dec.append(i / len(words))

    def random(self):
        if self.index > len(self.index_lst) //2:
            self.index = len(self.index_lst) - self.index
        else:
            self.index += self.seed + self.index
        return self.index_lst_dec[self.index]

def main():
    prng = WarAndPeacePseudoRandomNumberGenerator(1000)
    r = prng.random()
    for i in range(0,9999):
        print(prng.random())

if __name__ == '__main__':
    main()
