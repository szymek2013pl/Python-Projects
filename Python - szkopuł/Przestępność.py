odp = int(input())
if odp % 100 == 0 and odp % 400 != 0 or odp % 4 != 0:
    print("NIE")
else:
    print("TAK")
