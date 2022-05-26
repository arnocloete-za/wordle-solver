# Requirement: sudo apt-get install wbritish
# This will add the file: /usr/share/dict/words

# Open the file
file1 = open('/usr/share/dict/words', 'r')
# Read all lines into Lines
Lines = file1.readlines()

# default value
correct = ""

# loop forever until input from user is ! or press Control+c to stop
while correct != "!":
    print("\nLOOP: Enter ! to exit")

    # User input
    correct = input("Enter correct letters, with # between: Example: a##le:\n")
    include_more = input("Enter include letters: Example: tad:\n")
    exclude = input("Enter exclude letters: Example: tdp:\n")

    # don't want to repeat include letters that we already typed in correct
    include = correct.strip('#')
    include = include + include_more

    # Make everything UPPERCASE for comparison purpose
    correct = correct.upper()
    include = include.upper()
    exclude = exclude.upper()

    list_of_words = []    
    count = 0
    # go through lines one by one
    for line in Lines:
        # uppercase line for comparison purpose
        line = line.upper()
        # exclude all words that is not 5 characters. Reason for 6 is they have newlines at end of words
        if len(line) != 6:
            continue
        # exclude the ' character because this is not used in Wordle
        if "'" in line:
            continue

        # Check CORRECT:
        pass_correct = True
        counter = 0
        for i in correct:
            if i == '#':
                counter+=1
                continue
            if i != line[counter]:
                pass_correct = False
                break
            counter+=1
            if counter == 5:
                break
        if not pass_correct:
            continue
        
        # CHECK INCLUDE
        pass_include = False
        for i in include:
            if i in line:
                pass_include = True
        if not pass_include:
            continue

        # CHECK EXCLUDE
        exclude_flag = False
        for i in exclude:
            if i in line:
                exclude_flag = True
        if exclude_flag:
            continue

        # if we reach this point, the word is a valid choice
        list_of_words.append(line)
        count += 1

    for w in list_of_words:
        print(w)
    print("\nAmount of possibilities")
    print(count)



