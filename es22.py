#Hamming

def distance(strand_a, strand_b):
    hamming = 0
    if(len(strand_a) != len(strand_b)):
        raise ValueError("Strands must be of equal length.")
        
    for k in range(len(strand_a)):
        if(strand_a[k] != strand_b[k]):
            hamming = hamming + 1

    return hamming
