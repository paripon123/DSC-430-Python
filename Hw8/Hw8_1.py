# Paripon Thanthong
# Date : 05/26/2020
# Honor : “I have not given or received any unauthorized assistance on this assignment.”
# Video Link : https://youtu.be/dX40kOUIoJo

# Plot Generator

import random


class SimplePlotGenerator:
    """Clss Simple Plot Generator"""

    def __init__(self):
        """Contructor : set the value"""

        # self.name = [name for name in open('plot_names.txt').read().split('\n') if name != '']
        # self.adjectives = [adj for adj in open('plot_adjectives.txt').read().split('\n') if adj != '']
        # self.professions = [prof.strip() for prof in open('plot_profesions.txt').read().split('\n') if prof != '']
        # self.verbs = [verb for verb in open('plot_verbs.txt').read().split('\n') if verb != '']
        # self.adjectives_e = [adj_e for adj_e in open('plot_adjectives_evil.txt').read().split('\n') if adj_e != '']
        # self.villian_job = [villian_job for villian_job in open('plot_villian_job.txt').read().split('\n') if villian_job != '']
        # self.villains = [villian for villian in open('plot_villains.txt').read().split('\n') if villian != '']
        self.phrase = 'Something happens'

    def generate(self):
        """Generate Plot(return a plot)"""
        return self.phrase


class RandomPlotGenerator(SimplePlotGenerator):
    """Random Plot Generator"""

    def __init__(self):
        """Constructor : store each files to variables"""
        self.name = [name for name in open('plot_names.txt').read().split('\n') if name != '']
        self.adjectives = [adj for adj in open('plot_adjectives.txt').read().split('\n') if adj != '']
        self.professions = [prof.strip() for prof in open('plot_profesions.txt').read().split('\n') if prof != '']
        self.verbs = [verb for verb in open('plot_verbs.txt').read().split('\n') if verb != '']
        self.adjectives_e = [adj_e for adj_e in open('plot_adjectives_evil.txt').read().split('\n') if adj_e != '']
        self.villian_job = [villian_job for villian_job in open('plot_villian_job.txt').read().split('\n') if villian_job != '']
        self.villains = [villian for villian in open('plot_villains.txt').read().split('\n') if villian != '']

    def generate(self):
        """Plot a sentence with random value"""

        self.phrase = random.choice(self.name) + ', a ' + random.choice(self.adjectives) + ' ' + random.choice(
            self.professions) + ', must ' + random.choice(self.verbs) + ' the ' + random.choice(
            self.adjectives_e) + ' ' + random.choice(self.villian_job) + ', ' + random.choice(self.villains) + '.'
        return self.phrase


class InteractivePlotGenerator(SimplePlotGenerator):
    """Class User interactive plot"""

    def __init__(self):
        """Constructor : store each files to variables"""

        self.name = [name for name in open('plot_names.txt').read().split('\n') if name != '']
        self.adjectives = [adj for adj in open('plot_adjectives.txt').read().split('\n') if adj != '']
        self.professions = [prof.strip() for prof in open('plot_profesions.txt').read().split('\n') if prof != '']
        self.verbs = [verb for verb in open('plot_verbs.txt').read().split('\n') if verb != '']
        self.adjectives_e = [adj_e for adj_e in open('plot_adjectives_evil.txt').read().split('\n') if adj_e != '']
        self.villian_job = [villian_job for villian_job in open('plot_villian_job.txt').read().split('\n') if villian_job != '']
        self.villains = [villian for villian in open('plot_villains.txt').read().split('\n') if villian != '']

        print('\n You will be asked to type the the word or phrase from a given list exactly as is.\n')
        print('There will be 7 total of word or name that you will need to fill in order to form a plot.\n')


    def screen_input(self, random_5):
        """Pre-Screen User input only for the given choices """

        while True:
            try:
                print('This is list of 5 random selection.')
                print(random_5,'\n')
                user_int = input('Select word or phrase from a given choice above: ')
                if user_int not in random_5:
                    print('This is not a given choice, try again!')
                else:
                    return user_int
            except:
                print('Wrong input!')

    def generate(self):
        """Show choice of word for user and Ask used to input only the 5 given choices"""

        name_5 = random.sample(self.name, 5)
        self.pick_name = self.screen_input(name_5)

        adj_5 = random.sample(self.adjectives, 5)
        self.pick_adj = self.screen_input(adj_5)

        prof_5 = random.sample(self.professions, 5)
        self.pick_prof = self.screen_input(prof_5)

        verb_5 = random.sample(self.verbs, 5)
        self.pick_verb = self.screen_input(verb_5)

        adj_e_5 = random.sample(self.adjectives_e, 5)
        self.pick_adj_e = self.screen_input(adj_e_5)

        villian_job_5 = random.sample(self.villian_job, 5)
        self.pick_villian_job = self.screen_input(villian_job_5)

        villian_5 = random.sample(self.villains, 5)
        self.pick_villian = self.screen_input(villian_5)

        self.phrase = self.pick_name + ', a ' + self.pick_adj + ' ' + self.pick_prof + ', must ' + self.pick_verb + ' the ' + self.pick_adj_e + ' ' + self.pick_villian_job + ', ' + self.pick_villian + '.'

        return self.phrase

def intro():
    """Introduction"""

    print("""Welcome to Plot Generator!!! """)


def main():

    intro()
    # pq = SimplePlotGenerator()
    # pq = RandomPlotGenerator()
    pq = InteractivePlotGenerator()
    print(pq.generate())
    # print(pq.choice())


if __name__ == '__main__':
    main()
