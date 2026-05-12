import time
import math

x = input("wybierz swoją pierwszą liczbę ")
    
for i in range(len(x)):
    if x[i] not in "0123456789":
        print("to nie jest liczba")
        quit()
    else:
        x = int(x)
print("wybierz swoje działanie")
print("1: +")
print("2: -")
print("3: *")
print("4: :")
print("5: √")
dzial = input()
dzial = int(dzial)

if dzial == 5:
    print(math.sqrt(x))
    exit()

y = input("wybierz swoją drugą liczbę ")

for i in range(len(y)):
    if y[i] not in "0123456789":
        print("to nie jest liczba")
        quit()
    else:
        y = int(y)

time.sleep(1)

if dzial == 1:
    print("twój wynik to", int(x) + int(y))

if dzial == 2:
    print("twój wynik to", int(x) - int(y))

if dzial == 3:
    print("twój wynik to", int(x) * int(y))

if dzial == 4:
    print("twój wynik to", int(x) / int(y))

if dzial > 5:
    print("błędne działanie")
