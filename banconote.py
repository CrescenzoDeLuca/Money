
money = input("Importo ---> ")
money = int(money)

ven = money//20
money = money%20

di = money//10
money = money%10

ci = money//5
money = money%5

un = money
un = int(un)

print("$20 = ", ven)
print("$10 = ", di)
print("$5 = ", ci)
print("$1 = ", un)