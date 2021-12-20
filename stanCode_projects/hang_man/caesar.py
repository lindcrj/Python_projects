"""
File: caesar.py
Name:
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = int(input('Secret number: '))
s = input('What\'s the ciphered string?')
s = s.upper()


def main():
    """
    1. Apply the secret number to wrap around the string => generate a new ALPHABET
    2. decipher the input to the new ALPHABET, record the index
    3. match the recorded index with the original ALPHABET => print
    """
    new_alphabet = new(ALPHABET)
    password = decipher(new_alphabet)
    print(password)


def new(string):
    """
    1. count from the back to the front and intercept
    2. paste on a " "
    3. take the rest of the original ALPHABET
    4. paste behind STEP2
    """
    ans = ''
    for i in range(26-n, 26, 1):
        ans += string[i]
    for j in range(0, 26-n, 1):
        ans += string[j]
    return ans


def decipher(string):
    """
    1. Record the index of the matched letter
    2. Go back to correspond to the original ALPHABET
    3. print
    """
    ans = ''
    for i in s:  # W L L H A
        j = string.find(i)  # 0 15 15 11 4
        for ch in range(len(ALPHABET)):
            if j == ch:
                ans += ALPHABET[ch]
        if j == -1:
            ans += i
    return ans














#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
