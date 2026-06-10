def classify(number):
    if number!=0 and number>0:
       factors=[]
       for item in range(1,number):
           if number%item==0:
              factors.append(item)
       aliquotSum=sum(factors)
       if aliquotSum==number:
          return "perfect"
       if aliquotSum>number:
          return "abundant"
       if aliquotSum<number:
          return "deficient"
    raise ValueError("Classification is only possible for positive integers.")