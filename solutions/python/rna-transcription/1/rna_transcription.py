def to_rna(dna_strand):
    dict_1={'G':'C','C':'G','T':'A','A':'U'}
    result=""
    for item in dna_strand:
        if item in dict_1:
           result+=dict_1[item]
        else: result+=item
    return result