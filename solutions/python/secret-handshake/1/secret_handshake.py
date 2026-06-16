def commands(binary_str):
    list_1=[]
    if len(binary_str)==5:
       if binary_str[-1]=="1":
          list_1.append("wink")
       if binary_str[-2]=="1":
           list_1.append("double blink")
       if binary_str[-3]=="1":
           list_1.append("close your eyes")
       if binary_str[-4]=="1":
           list_1.append("jump")
       if binary_str[-5]=="1":
           list_1.reverse()
    return list_1
