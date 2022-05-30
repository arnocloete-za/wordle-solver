# Requirement: sudo apt-get install wbritish
# This will add the file: /usr/share/dict/words

# Open the file
file1 = open('/usr/share/dict/words', 'r')
# Read all lines into Lines
Lines = file1.readlines()

# default value
correct = ""

# loop forever until input from user is ! or press Control+c to stop
list_of_words = []
first_time = False
 # Open the file
file1 = open('/usr/share/dict/words', 'r')
# Read all lines into Lines
Lines = file1.readlines()
availabe_words = []
list_of_words = []
for line in Lines:
    # uppercase line for comparison purpose
    line = line.upper()
    line = line.strip('\n')
    # exclude all words that is not 5 characters. Reason for 6 is they have newlines at end of words
    if len(line) != 5:
        continue
    # exclude the ' character because this is not used in Wordle
    if "'" in line:
        continue
    if "É" in line:
        continue
    list_of_words.append(line)

while correct != "!":
    availabe_words = list_of_words
    list_of_words = []
    print("\nLOOP: Enter ! to exit")

    word_with_most_vowels = []
    remember_vowels = 0
    word_with_most_consonants = ""
    count_consonants = 0
    for stats in availabe_words:
        this_vowels = 0
        if 'A' in stats:
            this_vowels += 1
        if 'E' in stats:
            this_vowels += 1
        if 'O' in stats:
            this_vowels += 1
        if 'I' in stats:
            this_vowels += 1
        if 'U' in stats:
            this_vowels += 1
        if 'Y' in stats:
            this_vowels += 1
        if this_vowels > remember_vowels:
            word_with_most_vowels.clear()
            word_with_most_vowels.append(stats)
            remember_vowels = this_vowels
        elif this_vowels == remember_vowels:
            word_with_most_vowels.append(stats)
            remember_vowels = this_vowels
    # User input
    print("Amount of possibilities to start with: " + str(len(availabe_words)))
    print("Best choices with most vowels are a list of: " + str(len(word_with_most_vowels)))
    stop = 0
    for disp in word_with_most_vowels:
        stop += 1
        if stop == 20:
            print("....")
            amount = len(word_with_most_vowels) - 20
            print("and " + str(amount) + " more.")
            break
        print(disp)
    correct = input("\nEnter the GREEN correct letters with # between: Example: a##le:\n")


    # don't want to repeat include letters that we already typed in correct
    #include = correct.strip('#')
    #include = include + include_more

    # Make everything UPPERCASE for comparison purpose
    correct = correct.upper()


    #availabe_words = []
    count = 0
    # go through lines one by one
    for line in availabe_words:
        
        # Check CORRECT:
        pass_correct = True
        counter = 0
        for i in correct:
            if counter == 5:
                break
            if i == '#':
                counter+=1
                continue
            if i != line[counter]:
                pass_correct = False
                break
            counter+=1
        if not pass_correct:
            continue
        # if we reach this point, the word is a valid choice
        list_of_words.append(line)
        count += 1

    availabe_words = list_of_words
    list_of_words = []
    print("Amount of possibilities now: " + str(len(availabe_words)))
    include = input("Enter ORANGE include letters with # between: Example: #tad#:\n")
    include = include.upper()

    count = 0

    for line in availabe_words:
         # CHECK INCLUDE
        pass_include = True
        counter = 0
        for i in include:
            if counter == 5:
                break
            if i == '#':
                counter+=1
                continue
            if i not in line:
                # cant be valid word, does not have the orange char in go on
                pass_include = False
                break
            if i == line[counter]:
                # can't be valid word, the orange word in the space character space
                pass_include = False
                break
            counter+=1
        if not pass_include:
            continue
        list_of_words.append(line)
        count += 1

    availabe_words = list_of_words
    list_of_words = []
    print("Amount of possibilities now: " + str(len(availabe_words)))
    exclude = input("Enter exclude letters: Example: tdp:\n")
    exclude = exclude.upper()

    count = 0
    for line in availabe_words:
        # CHECK EXCLUDE
        exclude_flag = False
        for i in exclude:
            if i in line:
                exclude_flag = True
        if exclude_flag:
            continue
        list_of_words.append(line)
        count += 1

    availabe_words = list_of_words
    list_of_words = []
    count += 1

    print("\nPossible words:")
    for w in availabe_words:
        print(w)
    print("\nAmount of possibilities")
    print(len(availabe_words))
    print(count)



