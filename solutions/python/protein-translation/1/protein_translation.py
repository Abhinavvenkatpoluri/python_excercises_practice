def proteins(strand):
    dict_1 = {
        "AUG": "Methionine",

        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",

        "UUA": "Leucine",
        "UUG": "Leucine",

        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",

        "UAU": "Tyrosine",
        "UAC": "Tyrosine",

        "UGU": "Cysteine",
        "UGC": "Cysteine",

        "UGG": "Tryptophan",

        "UAA": "STOP",
        "UAG": "STOP",
        "UGA": "STOP"
    }
    str=""
    result=[]
    count=0
    for i in "".join(strand):
        str+=i
        count+=1
        if count%3==0:
           if dict_1[str]!="STOP":
              result.append(dict_1[str])
           else: return result
           str=""
    return result
