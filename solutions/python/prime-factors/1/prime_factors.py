def factors(value):
  
    result = []
    val = value
    while val % 2 == 0:
        result.append(2)
        val //= 2

    i = 3
    while i <= val ** 0.5:
        while val % i == 0:
            result.append(i)
            val //= i
        i += 2
    if val > 1:
        result.append(val)

    return result
    
    
    
