import time
import math

x = input("wybierz swoją pierwszą liczbę ")

for i in range(len(x)):
    if x[i] not in "0123456789":
        print("to nie jest liczba")
        quit()

x = int(x)
potegi = 0
potegi = int(potegi)
print("wybierz swoje działanie")
print("1: +")
print("2: -")
print("3: *")
print("4: :")
print("5: √")
print("6: ⁿ")
dzial = input()
dzial = int(dzial)
# ----------------------------------------------------------pierwiastki
if dzial == 5:
    print("twój wynik to", math.sqrt(x))
    quit()
#----------------------------------------------------------potęgi
if dzial == 6:
    print("wybierz do jakiej potęgi chcesz podnieść swoją liczbę")
    y = input()
    y = int(y)
    tmp = x**y
    print("twój wynik to",tmp)
    quit()
    
y = input("wybierz swoją drugą liczbę ")

for i in range(len(y)):
    if y[i] not in "0123456789":
        print("to nie jest liczba")
        quit()

y = int(y)

time.sleep(1)

if dzial == 1:
    print("twój wynik to", x + y)

elif dzial == 2:
    print("twój wynik to", x - y)

elif dzial == 3:
    print("twój wynik to", x * y)

elif dzial == 4:
    if y == 0:
        print("nie można dzielić przez 0")
    else:
        print("twój wynik to", x / y)

else:
    print("błędne działanie")