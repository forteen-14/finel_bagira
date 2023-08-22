import math
import turtle
import time
from datetime import date

def one():
    ##########################################
    # question 1 part 1
    user_num = float(input("Enter a number: "))
    print(int(user_num))

    # question 1 part 2
    user_num = float(input("Enter a number: "))
    root = math.sqrt(user_num)
    print(root)

    # question 1 part 3
    first_user_num = int(input("Enter a number: "))
    second_user_num = int(input("Enter a number: "))
    print(first_user_num ^ second_user_num)

    # question 1 part 4
    user_num = int(input("Enter a number: "))
    print("e" ^ user_num)

    # question 1 part 5
    x = float(input("Enter a number: "))
    part1 = 3*(math.tan(x))
    part2 =(math.cos(x))*(math.cos(x))
    print(part1 - part2)


def two():
    ##########################################
    # question 2 part 2 part 1
    #draw a squre
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)

    turtle.clear()
    # question 2 part 2 part 2
    #draw a circle fill blue
    turtle.color("blue")
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()

    # question 2 part 2 part 3
    turtle.goto(100,80)
    # question 2 part 2 part 4
    turtle.setx(45)
    # question 2 part 2 part 5
    turtle.clear()
    turtle.color("red")
    turtle.bgcolor("red")
    # question 2 part 2 part 7
    turtle.color("green")
    turtle.pensize(4)
    turtle.right(90)
    turtle.forward(200)


def three():
    books = 18
    notebooks = 23
    pens = 9
    user_books = int(input("Enter number of books: "))
    user_notebooks = int(input("Enter number of notebooks: "))
    user_pens = int(input("Enter number of pens: "))
    books = books - user_books
    notebooks = notebooks - user_notebooks
    pens = pens - user_pens
    print("Pens left: ", pens)
    print("Notebooks left: ", notebooks)
    print("Books left: ", books)
    print("date of purchase:", date.today())
# question 3 part 2
    books += 4
    notebooks += 2
    pens += 5
    user_books = int(input("Enter number of books: "))
    user_notebooks = int(input("Enter number of notebooks: "))
    user_pens = int(input("Enter number of pens: "))
    user_purchase_date = input("Enter date of purchase: ")

    user_books = int(input("Enter number of books: "))
    user_notebooks = int(input("Enter number of notebooks: "))
    user_pens = int(input("Enter number of pens: "))
    second_user_purchase_date = input("Enter date of purchase: ")

    #compare dates and print the earlier date
    if user_purchase_date < second_user_purchase_date:
        print("First purchase date is earlier")
    else:
        print("Second purchase date is earlier")



def main():
    # question 2 part 2 part 6
    #turtle.title("turtle practice session")
    #two()
    #time.sleep(5)
    three()


if __name__ == "__main__":
    main()


