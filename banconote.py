
money=input("Importo ---> ")
money=int(money)

ven=0
di=0
ci=0
un=0

while(money > 19):
      ven+=1
      money-=20

if(money > 9):
   di=1
   money-=10

if(money > 4):
   ci=1
   money-=5

while(money > 0):
      un+=1
      money-=1


print("$20 = ", ven)
print("$10 = ", di)
print("$5 = ", ci)
print("$1 = ", un)