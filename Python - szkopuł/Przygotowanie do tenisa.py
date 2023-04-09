odp = input("Podaj ciąg: ")
wyrazA = 0
wyrazB = 0
t = []
for i in range(0, len(odp) - 1):
    if odp[i] == "A":
        wyrazA += 1
    elif odp[i] == "B":
        wyrazB += 1

if wyrazA > wyrazB:
    print("A")
elif wyrazA < wyrazB:
    print("B")
else:
    print("Po równo")
