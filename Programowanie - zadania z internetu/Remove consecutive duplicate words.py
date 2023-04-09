def remove_consecutive_duplicates(s):
    arr = []
    word = ""
    for i in range(0, len(s)):
        if s[i] == " ":
            word = ""
            for j in range(0, i):
                word += s[j]
            arr.append(word)
            word = ""
        

    return arr

print(remove_consecutive_duplicates("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"))
