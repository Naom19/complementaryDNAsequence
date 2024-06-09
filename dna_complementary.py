
#we define the main function and logic
def main():     
    """ sequence = input_sequence() #ask the user for the DNA sequence (ACGT) 

    complementary_seq= get_complementary(sequence) #write a function that finds the complement for each base
    

    """
    
def input_sequence():
    return input(" Enter your DNA sequence: ").upper() #makes sure that all the bases are upper letters

def get_complementary(sequence):
    complement = {"A":"T", "C":"G", "G":"C", "T":"A"}
