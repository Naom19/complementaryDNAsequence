
#we define the main function and logic
def main():     
    sequence = input_sequence() #ask the user for the DNA sequence (ACGT) 

    complementary_seq= get_complementary(sequence) #write a function that finds the complement for each base
        
    print(f"original sequence: {sequence}") #prints the original sequence for reference to the user

    print(f"your complementary sequence is: {complementary_seq}") #prints the complementary DNA sequence!
     

    
def input_sequence():
    return input(" Enter your DNA sequence: ").upper() #makes sure that all the bases are upper letters

def get_complementary(sequence):
    #we create a dictionary that maps each DNA base with its complementary base 
    complement = {"A":"T", "C":"G", "G":"C", "T":"A"} 

    #We need that for each base in the input sequence, looks for its complementary base in the dictionary 'complement'
    #the join method bonds/concatenates "" all the complementary bases in a single string
    return "".join(complement[base] for base in sequence) 
    #complement is the dictionary & [base] is the key value

if __name__ == "__main__":
    main()
