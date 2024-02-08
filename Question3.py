# Problem Statement:  
# Write a Python program that generates the Fibonacci sequence up to a specified number of 
# terms, n. The Fibonacci sequence starts with 0 and 1, and each subsequent number in the 
# sequence is the sum of the two preceding numbers (e.g., 0, 1, 1, 2, 3, 5, 8, ...). Prompt the 
# user to enter the number of terms (n) they want in the sequence and then display the 
# Fibonacci sequence up to that number of terms. 

def fibonacci(n):
    fib_arr = [0, 1]
    for i in range(2, n):
        next_number = fib_arr[-1] + fib_arr[-2]
        fib_arr.append(next_number)
    return fib_arr


n = int(input("Enter the number of terms: "))
fib_arr = fibonacci(n)
print("Fibonacci sequence:")
print(fib_arr)