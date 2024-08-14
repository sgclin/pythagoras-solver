# pythagoras solver
from os import system
from random import randint

triples = [[3,4,5], [5,12,13], [7,24,25], [8,15,17], [9,40,41],
               [11,60,61], [12,35,37], [13,84,85], [15,112,113], 
               [16,63,65]]

score = 0

# main menu
def main_menu():
    system("cls")
    print("1. Get Hypotenuse")
    print("2. Get Short Side")
    print("3. Quick Test")
    print("4. Exit")

    choice = int(input(">> "))

    match choice:
        case 1:
            system("cls")
            a = int(input("Short side A: "))
            b = int(input("Short side B: "))
            print(f"Hypotenuse: {get_hyp(a,b)}")          
        case 2:
            system("cls")
            c = int(input("Hypotenuse: "))
            b = int(input("Known short side: "))
            print(f"Unknown short side: {get_short(c,b)}")
        case 3:
            system("cls")
            send_questions()
        case 4:
            exit(0)
        case _:
            system("cls")
            main_menu()

def get_hyp(a:int, b:int):
    # a^2 + b^2 = c^2

    c = (a**2 + b**2) ** 0.5

    return int(c)

def get_short(c:int, b:int):
    # a^2 = c^2 - b^2

    a = (c**2 - b**2) ** 0.5

    return int(a)

def gen_question():
    global score
    selected_triple = triples[randint(0,len(triples)-1)]

    # loading values from selected pythagorean triple
    a = selected_triple[0]
    b = selected_triple[1]
    c = selected_triple[2]

    # preventing questions asked multiple times
    triples.remove(selected_triple)

    qtype = randint(1,2)

    if qtype == 1:
        print(f"Short side A: {a}\nShort side B: {b}")
        answer = int(input("Hypotenuse: "))

        if answer == c:
            score += 1
    else:
        print(f"Hypotenuse: {c}\nKnown short side: {b}")
        # could make it switch between A and B but this works
        answer = int(input("Unknown short side: "))
      
        if answer == a:
            score += 1

def send_questions():
    for i in range(1,11):
        print(f"Question {i}:")
        gen_question()
        print()
    print(f"Total score: {score} / {i}")

if __name__ == "__main__":
    main_menu()
