in1 = input()
tempString = ""
for i in range(len(in1)):
    if in1[i].isnumeric():
        try:
            if in1[i-1] == "+":
                print(tempString + " tighten " + in1[i])
                tempString = ""
                i+=1
                continue
        except:
            pass
    if in1[i].isnumeric():
        try:
            if in1[i-1] == "-":
                print(tempString + " loosen " + in1[i])
                tempString = ""
                continue
        except:
            pass
        tempString = ""

    if in1[i] == "+" or in1[i] == "-":
        continue
    tempString += in1[i]
  

