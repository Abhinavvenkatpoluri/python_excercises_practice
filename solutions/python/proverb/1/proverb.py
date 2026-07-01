def proverb(*list_2, qualifier=None):
    list_1 = []

    if not list_2:
        return list_1

    for i in range(len(list_2) - 1):
        line = f"For want of a {list_2[i]} the {list_2[i+1]} was lost."
        list_1.append(line)

    if qualifier:
        list_1.append(f"And all for the want of a {qualifier} {list_2[0]}.")
    else:
        list_1.append(f"And all for the want of a {list_2[0]}.")

    return list_1
    
