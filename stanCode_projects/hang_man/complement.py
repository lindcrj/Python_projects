"""
File: complement.py
Name:
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    1. input a DNA string
    2. make sure all DNA alphabets will be upper
    3. turn A <=> T & C <=> G
    4. print the new DNA
    """
    dna = input('Please give me a DNA　strand and I\'ll find the complement: ')
    dna = dna.upper()
    new_dna = build_complement(dna)
    print('The complement of ' + dna + ' is ' + new_dna)


def build_complement(dna):
    """
    turn A <=> T & C <=> G
    """
    ans = ""
    for base in dna:
        if base == 'A':
            ans += 'T'
        if base == 'T':
            ans += 'A'
        if base == 'G':
            ans += 'C'
        if base == 'C':
            ans += 'G'
    return ans






###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
