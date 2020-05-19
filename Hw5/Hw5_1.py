# Paripon Thanthong
# Date :05/08/2020
# Honor : “I have not given or received any unauthorized assistance on this assignment.”
# Video Link : https://youtu.be/lsZgC4kwBHQ

### SixSidedDie
## roll() -- random number from 1-6
## getFaceValue() --
## __repr__()
# TenSideDie
# TwentySideDie

### Class Cup:
# roll(), getSum(), __repr__()
import random


class SixSidedDie:
    """Roll Six Sides Die"""

    number = 6

    def roll(self):
        self.num = random.randint(1, self.number)

    def getFaceValue(self):
        return self.num

    def __repr__(self):
        return 'SixSidedDie({})'.format(self.num)


class TenSideDie(SixSidedDie):
    """Roll Ten Sides Die"""
    number = 10

    def __repr__(self):
        return 'TenSidedDie({})'.format(self.num)


class TwentySideDie(SixSidedDie):
    """Roll Twenty Sides Die"""
    number = 20

    def __repr__(self):
        return 'TwentySidedDie({})'.format(self.num)


class Cup:
    """Class Cup that take multiple dice and Show to total value"""

    def __init__(self, six=1, ten=1, twenty=1):  # Set Default = 1 dice for each side.
        """Constructor of the Class"""

        self.sixdie = SixSidedDie()
        self.tendie = TenSideDie()
        self.twentydie = TwentySideDie()
        self.six = six
        self.ten = ten
        self.twenty = twenty

    def roll(self):
        """Roll all the dice in the Cup
        Note : Get random value from all the dice"""

        self.die_list = []
        self.total = 0
        for i in range(self.six):
            self.sixdie.roll()
            self.die_list.append(self.sixdie)  # Call __repr__ from it's own function.
            self.total += self.sixdie.getFaceValue()

        for i in range(self.ten):
            self.tendie.roll()
            self.die_list.append(self.tendie)
            self.total += self.tendie.getFaceValue()

        for i in range(self.twenty):
            self.twentydie.roll()
            self.die_list.append(self.twentydie)
            self.total += self.twentydie.getFaceValue()

    def getSum(self):
        """Get The total Value from all of the dice"""
        return self.total

    def __repr__(self):
        self.tup = ''
        for i in self.die_list:
            self.tup = self.tup + str(i) + ','
        return 'Cup({})'.format(self.tup[:-1])


def main():
    """ Test the Class"""

    # six = SixSidedDie()
    # six.roll()
    # print(six.getFaceValue())
    # print(six)
    # TenSideDie()
    # TwentySideDie()
    #
    cup = Cup(1,2,2)  # Cup with 1 six 2 ten and 2 twenty
    cup.roll()
    print(cup)
    print(cup.getSum())


if __name__ == '__main__':
    main()
