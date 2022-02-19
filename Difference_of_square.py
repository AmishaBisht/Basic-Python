
import math
def square_of_sum(number):
    sum =0

    if number!= 0:
       for i in range(1, number+1): 
           sum += i
           
    return sum*sum
        


def squaresum(n) :
  
    # Iterate i from 1 
    # and n finding 
    # square of i and
    # add to sum.
    sm = 0
    for i in range(1, n+1) :
        sm = sm + (i * i)
      
    return sm

def difference_of_squares(number):
    difference=square_of_sum(number)-squaresum(number)
    return difference
  
# Driven Program

# print( "square is:", square_of_sum(100))
# print(squaresum(100))
print(difference_of_squares(100))
