import time
import math
x = input("wypierz swoją pięrwszą liczbę ")
y = input("wypierz swoją drugą liczbę ")

print("wybierz swoje działanie")
print("1: +")
print("2: -")
print("3: *")
print("4: :")
dzial = input()
dzial = int(dzial)
time.sleep(1)

if dzial == 1:
    print("twój wynik to",int(x)+int(y))
if dzial == 2:
    print("twój wynik to",int(x)- int(y))
if dzial == 3:
    print("twój wynik to",int(x)*int(y))
if dzial == 4:
    print("twój wynik to",int(x)/int(y))
if dzial > 4:
    print("błędne działanie")
