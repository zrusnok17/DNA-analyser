# function allowing the user to input the DNA sequence:

def input_sequence():
    global final_seq
    final_seq = str(input("Hello, please input your DNA sequence: "))
    final_seq = final_seq.upper()
    seq_set = set(final_seq)
    correct_bases = {"A", "T", "C", "G"}
    rna_bases = {"A", "U", "C", "G"}
    if seq_set.issubset(correct_bases):
        print("Your sequence is alright, you can proceed.")
    elif seq_set.issubset(rna_bases):
        print("You input an RNA sequence, try again.")
        input_sequence()
    else:
        print("Your sequence is not valid, try again")
        input_sequence()
    return final_seq

input_sequence()

def show_menu():
    print("-" * 50)
    print("""Choose your next action:
        1. calculate sequence length
        2. transcribe DNA sequence to primary mRNA
        3. calculate GC-content
        4. generate complementary strand and ds-DNA
        5. find starting codon
        6. exit""")
    global choice
    try:
        choice = int(input("Please input your choice: "))
        return choice
    except ValueError:
        print("I didn't understand that. Please input a valid number")
        print("-" * 50)

def choose_again():
    again = str(input("Do you want to perform another action? (y/n) "))
    if again == "y" or "Y":
        handle_choices()
    elif again == "n" or "N":
        print("Okay, goodbye.")
        exit()
    else:
        print("Sorry, I didn't understand that, please write 'y' for yes or 'n' for no")

def handle_choices():
    while True:
        choice = show_menu()

        # 1. calculate sequence length
        if choice == 1:
            print(f"Your sequence is {len(final_seq)} nucleotides long")

        # 2. transcribe DNA sequence to primary mRNA
        elif choice == 2:
            print("Your original sequence: ", final_seq)
            mrna_seq = final_seq.replace("T", "U")
            print("Primary mRNA transcript: ", mrna_seq)

        # 3. calculate GC-content
        elif choice == 3:
            g = "G"
            c = "C"
            if g and c in final_seq:
                g_amt = final_seq.count(g)
                c_amt = final_seq.count(c)
                GC_content = (g_amt + c_amt) / len(final_seq) * 100
                print(f"GC-content: {round(GC_content, 2)} %")
            else:
                print("Your sequence doesn't contain any guanins (G) or cytosins (C)")

        # 4. generate complementary strand and ds-DNA
        elif choice == 4:
            compl_seq = final_seq.replace("A", "t").replace("T", "a").replace("G", "c").replace("C", "g")
            compl_seq = compl_seq.upper()
            print("Complementary strand: ", compl_seq)
            print("Both strands of DNA would look like this: ")
            print(final_seq)
            print(compl_seq)

        # 5: find starting codon
        elif choice == 5:
            start_codon = "ATG"
            if start_codon in final_seq:
                start_lower = final_seq.replace("ATG", "atg")
                print("Starting codon is shown in lower-case: ", start_lower)
            else:
                print("Your sequence doesn't contain any starting codons")

        # exit
        elif choice == 6:
            print("You chose exit, goodbye.")
            break

        else:
            print("Your input is not valid, try again.")
            print("-"*50)
            handle_choices()

handle_choices()