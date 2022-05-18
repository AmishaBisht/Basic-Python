def cal_squ(number):
    result= []
    for i in number:
        result.append(number*number)
    return result

def cal_cube(numbers):
    result = []
    for i in numbers:
        result.append(numbers*numbers*numbers)
    return result

array = range(1,25)
 cal_squ(array)
 cal_cube(array)