#!/usr/bin/env python3

def dna_complement(dna_sequence):

    ''' Returns the complement of a DNA sequence.

    Input:
    dna_sequence: string
        Case insensitive string containing the characters A, T, G, C

    Output:
    dna_complement: string
        Capitalized string of characters, DNA complement of input string '''
    
    # Create an empty list for the complement elements
    complement = []
    
    # Create a list of valid bases to check input
    valid_dna_bases = ['a','A','t','T','g','G','c','C']
    
    # Create a dictionary to determine base complements
    dict_complement = {'a':'T','A':'T','t':'A','T':'A','g':'C','G':'C','c':'G','C':'G'}
    
    for elem in dna_sequence:
        # Test if element of input is a valid DNA base
        if valid_dna_bases.count(elem)==0:
            return(None)
        # Find that base's complement
        else:
            complement.append(dict_complement[elem])
            
    return(''.join(complement))

    
# Demo the function

# Set the two example input DNA sequences
example1_dna_sequence = 'atGCCCtga'
example2_dna_sequence = 'atGC4CCtqga'

# Example 1 - function should return DNA complement
print(example1_dna_sequence)
example1_complement = dna_complement(example1_dna_sequence)
print(example1_complement)

#Example 2 - function should return None
print(example2_dna_sequence)
example2_complement = dna_complement(example2_dna_sequence)
print(example2_complement)
