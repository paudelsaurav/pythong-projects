#Advanced Example to calculate the time elapsed during the calculation

import time
def timeit(func):
    def timeit_inner(number):
        start_time=time.time()
        result=func(number)
        end_time=time.time()
        total_time = end_time - start_time 
        # f-format 
        print(f'Function {func.__name__} with parameter { number } Took {total_time:.4f} seconds') 
        return result
    return timeit_inner 
@timeit  
#timeit function takes calculate_something function as parameter 
def calculate_something(num): 
    total = sum((x for x in range(0, num**2))) 
    return total 
print(calculate_something(100))


#make a function to obtain fibonacci series
