import random as rnd

def generate_rnd_seq():
    bases_lst = ["A", "C", "T", "G"]
    x = rnd.randint(20, 70)
    random_seq = []
    delimiter = ""

    while len(random_seq) < x:
        random_seq.append(rnd.choice(bases_lst))

    final_seq = delimiter.join(random_seq)
    print("This is your generated DNA sequence: ", final_seq)
    return final_seq

generate_rnd_seq()
# GCACCGCCCCGGCGATTGCCGTAAAGATACGTCGTTTCCGTTTTGAGTTGTTGCTCGCCTA
# CCTCGACGCTTCCGCTAATCGTGAAACAGAGTGTGGCGGTCGTCCGAGG
# AAAATTCGGTGAAAATAACAACTGCGCTACGCGCGGTTAAAC
# AAAATGGTGAGTATGCGTGCACACTCCAGC