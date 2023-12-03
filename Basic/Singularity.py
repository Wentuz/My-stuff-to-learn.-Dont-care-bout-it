''' Unoptimal, more readable
def real_numbers(n):
    count = 0
    
    for number in range(1, n, 2):
        if number % 3 != 0 and number % 5 != 0:
            count += 1

    return count
'''

# -= excludes numbers, += includes numbers
def real_numbers(n):
    count = n

    count -= n // 2
    count -= n // 3
    count -= n // 5
    count += n // 6
    count += n // 10
    count += n // 15
    count -= n // 30
    
    return count



print(real_numbers(5))
print(real_numbers(10))
print(real_numbers(20))  # Example usage
