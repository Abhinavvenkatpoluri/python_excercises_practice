def decode(string):
    if not string:
        return ""
    result=""
    count=0
    num=""
    for i,j in enumerate(string):
        if j.isdigit():
           num+=j
        else:
           if not num:
              result+=j
           else: result+=int(num)*j
           num=""
    return result
              
def encode(string):
    if not string:
        return ""
    result = ""
    count = 0
    letter = string[0]
    for i, j in enumerate(string):
        if j == letter:
            count += 1
        else:
            if count>1:
               result += str(count) + letter
            else:
               result +=letter
            letter = j
            count = 1
    if count>1: result += str(count) + letter
    else: result +=letter
    
    return result
        
            
            
        
