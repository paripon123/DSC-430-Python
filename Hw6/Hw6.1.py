# Paripon Thanthong
# Date : 05/15/2020
# Honor : “I have not given or received any unauthorized assistance on this assignment.”
# Video Link : https://youtu.be/rKR13PZY8T4
import statistics
def read_file():
    """Read File and prepare the data"""

    open_file = open('avocado.csv','r')
    infile = open_file.readlines()
    store_txt = []
    for line in infile:
        strip_line = line.strip()
        store_txt.append(strip_line)
    open_file.close()
    return store_txt


def find_index(col_name):
    """ Find index of column name"""

    first_col = read_file()[0]
    for index in range(len(first_col.split(','))):
        if first_col.split(',')[index] == col_name:
            return index

def store_value(col_name):
    """Store value by column name in a list"""

    index_n = find_index(col_name)
    data = read_file()[1:]
    store = []
    for line in data:
        store.append(float(line.split(',')[index_n]))
    return store

def readAndComputeMean_SM(col_name):
    """Find Mean with Statistics Modole"""

    value = store_value(col_name)
    return statistics.mean(value)

def readAndComputeSD_SM(col_name):
    """Find Standard Deviation with Statistics Modole"""

    value = store_value(col_name)
    return statistics.stdev(value)

def readAndComputeMedian_SM(col_name):
    """Find Median with Statistics Modole"""

    value = store_value(col_name)
    return statistics.median(value)

    # for i in range(len(new[0].split(','))):
    #     # print(i,new[0].split(',')[i])
    #     if new[0].split(',')[i] == 'Total Volume':
    #         print(i)

def readAndComputeMean_HG(col_name):
    """Find Mean with manually computational"""

    value = store_value(col_name)
    mean = sum(value) / len(value)
    return mean

def readAndComputeSD_HG(col_name):
    """Find Standard Deviation with manually computational"""

    value = store_value(col_name)
    mean = sum(value) / len(value)
    subtract = []
    for i in value:
        subtract.append((i-mean)**2)
    #print(sum(subtract))
    sd = (sum(subtract)/len(value)) ** (1/2)
    return sd

def readAndComputeMedian_HG(col_name):
    """Find Median with manually computational"""

    value = sorted(store_value(col_name))
    if len(value) % 2 != 0:
        median = value[(len(value)//2)]
    else:
        median = (value[(len(value)//2) -1] + value[(len(value)//2)])/2
    return median

def index_col_MML(col_name):
    """Locate the index of column by column name for Memory Less method"""

    col_index = 0
    with open('avocado.csv') as file:
        for col in file.readline().split(','):
            if col != col_name:
                col_index += 1
            else:
                col_index += 0
                return col_index

def readAndComputeMean_MML(col_name):
    """"Find Mean with Memory Less method"""

    with open('avocado.csv') as file:
        col_index = index_col_MML(col_name)
        sum_value = 0
        length_val = 0

        for line in file.readlines()[1:]:
            length_val += 1
            sum_value += float(line.split(',')[col_index])
        return sum_value/length_val

def readAndComputeSD_MML(col_name):
    """Find Standard Deviation with Memory Less Method"""

    with open('avocado.csv','r') as file:
        col_index = index_col_MML(col_name)
        sum_value = 0
        length_val = 0

        for line in file.readlines()[1:]:
            length_val += 1
            sum_value += float(line.split(',')[col_index])
        mean = sum_value / length_val

        file.seek(0)

        subtract_mean = 0
        for sline in file.readlines()[1:]:
            subtract_mean += ((float(sline.split(',')[col_index]) - mean) ** 2)
        sd = (subtract_mean/length_val) ** (1/2)
        return sd

def median_position():
    """Locate median position for Memory Less"""

    with open('avocado.csv','r') as file :
        loc = 0
        count = 0
        header = file.readline()
        while True:
            value = file.readline()
            count += 1
            if value == '':
                count = count -1
                if count %2 ==0:
                    loc = count/2
                    return loc,count
                else:
                    loc = count//2 +1
                    return int(loc),int(count)


def find_min_max(col_name):
    """Find Min and Max value for Memory Less"""

    col_index = index_col_MML(col_name)
    with open('avocado.csv','r') as file:
        header = file.readline()
        min_val = float(file.readline().split(',')[col_index])
        max_val = min_val
        for i in file.readlines():
            val = float(i.split(',')[col_index])
            if val < min_val:
                min_val = val
            elif val > max_val:
                max_val = val
        return min_val, max_val

def find_midrange(min_val,max_val):
    """This Function find the mean value from min and max value, also known as Midrange"""

    mean_val = ((max_val - min_val)/2) + min_val
    return mean_val

def counter(col_name,mean_val):
    """Identify the how many value below and above the given mean value at time"""

    col_index = index_col_MML(col_name)
    with open('avocado.csv','r') as file:
        count_less_than_M = 0
        count_larger_than_M = 0
        header = file.readline()
        for i in file.readlines():
            val = float(i.split(',')[col_index])
            if val < mean_val:
                count_less_than_M += 1
            elif val >= mean_val:
                count_larger_than_M += 1
        return count_less_than_M, count_larger_than_M

def track_mean_position(count_less_than_M,mean_val,mean_val_position,min_val,max_val):
    """Updating the of current mean value, min value and max value"""

    mean_val_position = count_less_than_M + mean_val_position + 1
    median_location,num = median_position()

    if mean_val_position > median_location :
        min_val = min_val
        max_val = mean_val
    else:
        min_val = mean_val
        max_val = max_val
    return mean_val_position,min_val,max_val


def readAndComputeMedian_MML(col_name):
    """Loop function the do the computation and match the median position and mean position"""

    median_loc,num_line = median_position()
    min_val, max_val = find_min_max(col_name)
    while True:
        mean_val = find_midrange(min_val, max_val)
        below_mean_count, above_or_equal_mean_count = counter(col_name, mean_val)
        mean_val_p, min_val, max_val = track_mean_position(below_mean_count, mean_val, 0, min_val, max_val)
        if mean_val_p == median_loc:
            return mean_val

def main():

    print('The mean value from statistics module :',readAndComputeMean_SM('Total Volume'))
    print('The mean value from manually coputational: ', readAndComputeMean_HG('Total Volume'))
    print('The mean value from Memory Less method: ', readAndComputeMean_MML('Total Volume'),'\n')

    print('The standard deviation value from statistics module : ',readAndComputeSD_SM('Total Volume'))
    print('The standard deviation value from manually coputational: ', readAndComputeSD_HG('Total Volume'))
    print('The standard deviation value with Memory Less method: ', readAndComputeSD_MML('Total Volume'),'\n')

    print('The median value from statistics module is: ',readAndComputeMedian_SM('Total Volume'))
    print('The mean value from manually coputational: ', readAndComputeMedian_HG('Total Volume'))
    print('The approximate median value from Memory Less method: ', readAndComputeMedian_MML('Total Volume'))

if __name__ == '__main__':
    main()
