# Paripon Thanthong
# Date : 05/21/2020
# Honor : “I have not given or received any unauthorized assistance on this assignment.”
# Video Link :https://youtu.be/ZBHMldVngPM

# PRNG

class WarAndPeacePseudoRandomNumberGenerator:
    """ Psuedo Random Generator"""

    def __init__(self,seed):
        """Initiate Seed Number"""

        self.seed = seed
        self.lst = []
        self.line_lst = []
        self.index = 0
        with open('war-and-peace.txt','r') as file:
            for line in file.readlines():
                self.line_lst.append(line)
            file.seek(0)
            for lines in file:
                for word in lines.split():
                    if word.isalpha() == True:
                        self.lst.append(word)

    def random(self):
        "Random Number from 0-1"

        self.num = 0
        if (self.seed <= len(self.lst)) and (self.seed <= len(self.line_lst)):
            num_1 = len(self.line_lst[self.seed]) + (len(self.line_lst[self.seed])*100)
            num_2 = len(self.line_lst[num_1]) * 100
        else:
            num_1 = len(self.line_lst) // 32
            num_2 = len(self.line_lst[num_1]) - int((self.seed ** (1//2)))


        trans_num_1 = num_1 * len(self.lst[num_2])
        trans_num_2 = num_2 * len(self.lst[num_1])

        if self.index > len(self.line_lst) // 2 :
            self.index = len(self.line_lst) - self.index
        else:
            self.index += self.seed + self.index


        if abs(self.index) < trans_num_2:
            return abs(self.index)/trans_num_2
        if abs(self.index) > trans_num_2:
            return trans_num_2/abs(self.index)
        if abs(self.index) < trans_num_1:
            return abs(self.index) / trans_num_1
        else:
            return trans_num_1/abs(self.index)

def min_max_mean():
    """Calculate Min,Max Mean from 10000 PRNG numbers"""

    prng = WarAndPeacePseudoRandomNumberGenerator(552)
    num_lst = []
    count = 0
    for i in range (10000):
        count+=1
        num_lst.append(prng.random())
    sort_lst = sorted(num_lst)
    return sort_lst[0],sort_lst[count-1], (sum(sort_lst)/count)


def main():

    min_val,max_val,mean_val = min_max_mean()
    print('PRNG 10000 numbers')
    print('Min Value: {}\nMax Value: {}\nMean Value: {}'.format(min_val,max_val,mean_val))
    # prng = WarAndPeacePseudoRandomNumberGenerator(50000)
    # r = prng.random()
    # #print (r)
    # for i in range(10000):
    #        print(prng.random())



if __name__ == '__main__':
    main()
