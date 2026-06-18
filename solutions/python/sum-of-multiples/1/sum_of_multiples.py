def sum_of_multiples(limit, multiples):
    result=set()
    for i in multiples:
        if i!=0:
           for j in range(0,limit):
              if j%i==0:
                 result.add(j)
        else: result.add(i)
    return sum(result)
