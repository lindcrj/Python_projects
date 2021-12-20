"""
File: similarity.py
Name:
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    1. input long dna
    2. input short dna
    3. short match long, find the most similar part
    4. print
    """
    long = input('Please give me a DNA sequence to search: ')
    long = long.upper()
    short = input('What DNA sequence would you like to match? ')
    short = short.upper()
    m = match(long, short)
    print('The best match is ' + m)


def match(long, short):
    """
    1. if  long length = 10,
       short length = 5 => need to check 6 times
       short length = 6 => need to check 5 times
       short length = 7 => need to check 4 times
       => no matter what length, the DNA have to match (long-short) + 1 times
    2. cut the long [0:0+short length] -> [1:1+short length] -> ...
    3. Compare who is the most similar these few matches :
       if the alphabet is the same -> add one point
       see who has the highest point
    4. print that DNA　cut out
    """
    ans = ''
    point = 0
    highest = point
    s = len(short)
    o = 0
    while True:
        for i in range(len(long)-len(short)+1):
            point = 0
            ch = long[o:o+s]
            for j in range(len(short)):
                if short[j] == ch[j]:
                    point += 1
            o += 1
            if point > highest:
                highest = point
                ans = ch
        return ans














###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
