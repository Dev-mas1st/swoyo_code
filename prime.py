def prime_numbers(low, high):
    
    #checking arguments
    left = isinstance(low, int) and low > 0
    right = isinstance(high, int) and high > 0
    if not (left and right): return []
    
    #swaping values if the lower end is bigger than the higher end.
    #this avoids the need to sort the values as they will already be sorted.
    #this is also good for avoiding uneeded operations, which affects the efficiency of the code
    #and increses its time complixity
    if low > high:
        temp = low
        low = high
        high = temp
    
    primes = []
    for i in range(low,high +1):
        if i > 1:
            for k in range(2,i):
                if (i%k) == 0:
                    break
            else:
                primes.append(i)
    return primes
