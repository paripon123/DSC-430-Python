# Paripon Thanthong
# Date : 05/26/2020
# Honor : “I have not given or received any unauthorized assistance on this assignment.”
# Video Link :https://youtu.be/HPfKH3Jr_BM

# Plot Viewer

from Hw8_1 import *


class PlotViewer:
    """Plot Viewer to view multiple generator"""

    def registerPlotGenerator(self, generator):
        """Register generator class"""

        self.generate_sub = generator

    def generate(self):
        """Pass generate method from other Class"""

        return self.generate_sub.generate()

def main():
    """Main function that try out on multiple Plot generator Classes"""

    pv = PlotViewer()
    pv.registerPlotGenerator(InteractivePlotGenerator())
    print(pv.generate())

if __name__ == '__main__':
    main()

