def user_input():
    filename = 'StemAndLeaf' + input("Which file you want to read?[1,2,3]: ") + '.txt'
    # print(filename)
    return filename


def read_file(file_name):
    file = open(file_name, 'r')
    line_list = file.readlines()
    file.close()

    # Put number in a list and sort it with sorted()
    num_list = []
    for i in range(0, len(line_list)):
        x = int(line_list[i].strip())
        num_list.append(x)
    return sorted(num_list)


def convert_datatype(num_list):
    str_list = []
    for i in num_list:
        str_list.append(str(i))
    return str_list

def stem_leaf_plot(plot_list):
    stem = ''
    leaf = ''
    for value in plot_list:
        get_stem = value[:-1] # Get Stem : Stem will be first digit to the one before last.
        get_leaf = value[-1] # Get leaf : Leaf will be only last digit/Character.
        if stem != get_stem :
            print(stem + '|' + leaf)
            stem = get_stem
            leaf = ''
        leaf = leaf + ' ' + get_leaf
    print(stem + '|' + leaf)

def main():

    file_name = user_input()  # There is 3 file3 , which we will get the file name out of this by let the user decide
    num_list = read_file(file_name)  # Read output for desire file and sort it
    # print(num_list)
    plot_list = convert_datatype(num_list)
    stem_leaf_plot(plot_list) # Plot function

    # Ans = user_continue()  # Ask user if they want to continue to plot another file
    #if Ans != 'Yes':  # if Ans say yes , it will run again.
    #   var = False


if __name__ == '__main__':
    main()