frutas = ["banana", "pera","uva"]
for fruta in frutas:
    print(fruta)

for c in "banana":
        print(c)

frutas.append("manga")
frutas.append("morango")

for f in frutas:
    print(f)
    if f == "manga":
        continue

for n in range(8):
    print(n)

for n in range(4,8):
    print(n)

for n in range(10,51,5):
    print(n)


for b in range(11):
    print("número:", b)
else:
    print("Acabou o laço")

time1 = [["Maria Rita" ,"Raphael"], "Hadson", "Rogério",["Flávio","Camyle"]]
time2 = ["Eduardo","Urick","Karlos","Lucas","Igor"]

for t1 in time1:
    if type(t1) == list:
        for tt1 in t1:
            print(tt1)
    else:
        print(t1)
    for t2 in time2:
        print(t2)

for x in time1:
    if type(x) == list:
        for y in x:
            print(x)
        else:
            print(x)

