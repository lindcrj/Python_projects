FILE = 'dictionary.txt'

names = {}


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
    print(dictxt)


def read_dictionary(filename):
    global names
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line[0] not in names:
                names[line[0]] = []
                names[line[0]].append(line)
            else:
                names[line[0]].append(line)
    return names








if __name__ == '__main__':
    main()