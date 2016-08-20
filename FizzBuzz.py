# -*- coding: utf-8 -*-

print("FIZZBUZZ!")

stevilka = int(raw_input("Izberi število med 1 in 100: ")) + 1

while True:
    if stevilka > 101 or stevilka < 2:
        stevilka = int(raw_input("Prosim vnesite število med 1 in 100: ")) + 1
    else:
        for x in range(1, stevilka):
            if x % 3 == 0 and x % 5 == 0:
                print("fizzbuzz")
            elif x % 3 == 0:
                print("fizz")
            elif x % 5 == 0:
                print("buzz")
            else:
                print(x)
        break