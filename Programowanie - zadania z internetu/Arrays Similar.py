def arrays_similar(seq1, seq2):

    length = min(len(seq1), len(seq2))
    term = 0
    
    for i in range(0, length):
        if seq1[i] == seq2[i]:
            term += 1

    if term == max(len(seq1), len(seq2)):
        return True
    else:
        for i in range(0, length):
            if seq1[i] == 
        seq1.sort()
        seq2.sort()
        if seq1 == seq2:
            return True
        else:
            return False
    

arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 1, 2, 4, 3]
arr3 = [1, 2, 3, 4]
arr4 = [1, 2, 3, "4"]

print(arrays_similar(arr3, arr4))
            
            
