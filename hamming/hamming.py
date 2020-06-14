def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("DNA strands must have the same length")

    hamming_distance = 0
    i = 0
    while(i < len(strand_a)):
        if strand_a[i] != strand_b[i]:
            hamming_distance += 1
        i += 1

    return hamming_distance
