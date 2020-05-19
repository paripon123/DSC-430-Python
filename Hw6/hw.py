def median_position(file):
    n=0
    while:
        value =  readline()
        n += 1
    median_position = n/2
    return  median_position
        
def find_min(file):
    min_val = 0
    while:
        value = readline()
        if value < min:
            min_val = value
    return min_val

def find_max(file):
    ...
    return max_val

def cal_mean(min_val,max_val):
    mean_val = (max_val-min_val) / 2 + min_val
    return mean_val

def counter(mean_val,file):
    less_than_mean_counter=0
    larger_than_mean_counter=0
    while:
        value = readline()
        if value < mean_val:
            less_than_mean_counter +=1
        elif value >= mean_val:
            larger_than_mean_counter +=1
        
    return less_than_mean_counter, larger_than_mean_counter



def accumulation(less_than_mean_counter,mean_val,mean_val_position = 0,min_val,max_val): # keep tracking the position of mean_val
    mean_val_position = less_than_mean_counter + mean_val_position +1
    median_position = median_position(file)
    # compare two position to decide which one to go
    if mean_val_position > median_position: #go to the  left side
        max_val = mean_val
        min_val = min_val
    else: #go to the right side
        max_val =  max_val
        min_val= mean_val
    return mean_val_position, min_val,max_val

def main():
    median_position =func
    max_val = func
    min_val =func
    n
    while True:
        
        mean_val =func

        leess_than_mean_counter, larger_than_mean_counter = counter(mean_val,file)
        mean_val_position, min_val,max_val = accumulationi(leess_than_mean_counter,mean_val,0,min_val,max_val)

         if mean_val_p == median_position:
            return mean_val
                                                           
    


    
    
            
        
    
    
