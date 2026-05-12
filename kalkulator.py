import time
import math
x = input("wypierz swoją pięrwszą liczbę")
y = input("wypierz swoją drugą liczbę")

print("wybierz swoje działanie")
print("1: +")
print("2: -")
print("3: *")
print("4: :")
dzial = input()
dzial = int(dzial)
print("myślę...")
time.sleep(5)
if dzial == 1:
    print(int(x)+int(y))
if dzial == 2:
    print(int(x)- int(y))