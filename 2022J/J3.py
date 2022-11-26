first = input()

start = 0
for i in range(len(first)):
    try:
        if first[i] != "+" or first[i] != "-":
            pass
        if first[i] == "+":
            print(first[start:i], "tighten", first[i+1])
            start = i+2
        if first[i] == "-":
            print(first[start:i], "loosen", first[i+1])
            start = i+2
    except:
        continue

#15 pts