def findfrequency(string):
    freq = {}
    print(f"The length of string is: {len(string)}")
    for i in string:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

print(findfrequency("AAAACCCGGT"))