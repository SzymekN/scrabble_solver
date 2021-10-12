import itertools
import csv
import sys

def count_points(word):
    # count points for given word
    points = 0
    for letter in list(word):
        if letter == 'q' or letter == 'z':
            points += 10
        elif letter == 'j' or letter == 'x':
            points += 8
        elif letter == 'k':
            points += 5
        elif letter == 'f' or letter == 'h' or letter == 'v' or letter == 'w' or letter == 'y':
            points += 4
        elif letter == 'b' or letter == 'c' or letter == 'm' or letter == 'p':
            points += 3
        elif letter == 'd' or letter == 'g':
            points += 2
        else:
            points += 1
    return points

def variations(letters, words):
    # generate all variations of all lengths in given list
    solutions = []
    for i in range(2,len(letters)+1):
        test = ["".join(item) for item in itertools.permutations(letters, i)]
        test = set(test)
        for w in test:
            if w in words:
                solutions.append([w,count_points(w)])

    print(f"All available solutions: {len(solutions)}")
    return solutions

    
maxInt = sys.maxsize

# set field size as big as possible, dividing by 10 on overflow errors
while True:
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)


# create set containing every word in English
words = set()
with open('words.csv', encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            words.add(row[0].lower())
            line_count += 1

# game control on/off
game_on = 'y'
while game_on == 'y':

    # input letters
    letters = list(input("Enter letters: ").replace(" ",""))
    print(f"Entered letters: {' '.join(letters)}")

    # generate solutions and sort 
    possibilities = variations(letters, words)
    possibilities.sort(key= lambda x: x[1], reverse= True)

    best = min(len(possibilities),10)
    print(f"Best {best} solutions")

    # print possible solutions
    counter = 0
    for pos in possibilities:
        choice = 'y'
        print(f'{pos[0]} - {pos[1]}pt.')
        counter += 1
        if counter % 10 == 0:
            choice = input("Show next 10 solutions? (y/n): ")
        if choice == 'n':
            break

    game_on = input("Continue game? (y/n): ")
