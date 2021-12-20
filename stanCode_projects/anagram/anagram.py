"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


names = []
ana = 0
ana_lst = []
prefix_ind = []



def main():
    global ana, ana_lst
    """
    TODO:
    """
    # start = time.time()
    ####################
    #                  #
    #       TODO:      #
    #                  #
    ####################
    # end = time.time()
    print("Welcome to stanCode '"'Anagram Generator'"'(or -1 to quit)")
    dictxt = read_dictionary(FILE)
    while True:
        print('----------------------------------')
        s = input('Find anagrams for: ')
        if s == EXIT:
            break
        else:
            print("Searching...")
            start = time.time()
            find_anagrams(s, [], [])
            end = time.time()
            print(ana, "anagrams: ", ana_lst)
            ana = 0
            ana_lst = []
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary(filename):
    global names
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            names.append(line)
    return names


def find_anagrams(s, new_lst, index_lst):
    """
    :param s:
    :return:
    """
    global ana, ana_lst,prefix_ind
    s_lst = list(str(s))
    if len(index_lst) == len(s_lst):
        new_lst = []
        for ind in index_lst:
            new_lst.append(s_lst[ind])
        s = "".join(new_lst)
        if s in names:
            if s not in ana_lst:
                ana += 1
                ana_lst.append(s)
                print("Found: ", s)
                print("Searching...")
    else:
        for i in range(len(s_lst)):
            if i in index_lst:
                pass
            else:
                index_lst.append(i)
                if len(index_lst) == 2:
                    for ind in index_lst:
                        prefix_ind.append(s_lst[ind])
                    sub_s = "".join(prefix_ind)
                    if has_prefix(sub_s) is False:
                        pass
                find_anagrams(s, new_lst, index_lst)
                index_lst.pop()
    return s, ana, ana_lst


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    for name in names:
        if str(name).startswith(sub_s):
            return True
    return False




if __name__ == '__main__':
    main()
