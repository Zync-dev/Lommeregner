import os, time

start = True

if start == True:
    num1input = float(input("Hvad er dit første nummer?\nSkriv her: "))
    tegninput = input("Hvilket tegn vil du regne med?\nSkriv her: ")
    num2input = float(input("Hvad er dit andet nummer?\nSkriv her: "))

    if tegninput == "+":
        print("Svaret er:\n" + str(num1input+num2input))
    elif tegninput == "-":
        print("Svaret er:\n" + str(num1input-num2input))
    elif tegninput == "*":
        print("Svaret er:\n" + str(num1input*num2input))
    elif tegninput == "/":
        print("Svaret er:\n" + str(num1input/num2input))
    elif tegninput == "**":
        print("Svaret er:\n" + str(num1input**num2input))

startagain = input("Tryk enter for et nyt regnestykke")

if startagain == "":
    startagain == True