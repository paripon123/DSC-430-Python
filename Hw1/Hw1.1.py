# Paripon Thanthong
# 04/07/2020
# "I have not given or received any unauthorized assistance on this assignment"
# Video Link : https://www.youtube.com/watch?v=r0sK2mxmuZY

## Sudo code on the statement part
# 1. put question in to an array []
# 2. set while condition with counter(when it hit curtain number then stop loop)
# 3. text = input(x[counter])
# 4. if else condition --- If yes, counter +1 mean next index else break.
def grad_logic():
    score = 0
    qa = ["Did student submit single uncompressed file: ",
          "Did student include the Author's name and date: ",
          "Did student include honor statement: ",
          "Did student include unlisted Youtube: "]
    # Counter method for, indexing.
    counter = 0
    while counter != 4:
        ans = input(qa[counter])
        if ans == 'Yes':
            counter += 1
        else:
            print(0)
            return 0
    # Score computation part
    correctness = int(input('Correctness Score 0-3: '))
    elegance = int(input('Elegance Score 0-3: '))
    hygiene = int(input('Hygiene Score 0-2: '))
    discuss = int(input('Discussion Score 0-2: '))

    submission = input("Did student submit assignment on time: ")
    score = correctness + elegance + hygiene + discuss
    if submission == 'Yes':
        print('Score: ',score)
        return score
    else:
        hour = int(input("How many hours late: "))
        score = score - (score * (hour/100))
        print('Score: ',score)
        return score

def main():
    grad_logic()

if __name__ == '__main__':
    main()

