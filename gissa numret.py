import random
ai = random.randint(1,4)
print("gissa på ett av valen från menyn")

meny = 0 

while meny != 5:
    print("tryck på 1 för att gissa på hjärter ♥")
    print("tryck på 2 för att gissa på spader ♠ ")
    print("tryck på 3 för att gissa på klöver ♣ ")
    print("tryck på 4 för att gissa på ruter ♦ ")
    print("tryck på 5 för att avsluta")
    try:
        meny = int(input("välj en siffra för att fortsätta "))
    except:
        print("du måste gissa på en siffra ifrån menyn")


