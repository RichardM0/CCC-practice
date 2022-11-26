
starNum = 0
in1 = int(input())
for i in range(in1): 
    in2 = int(input())
    in3 = int(input())
    star = in2*5 - in3*3

    if star > 40:
        starNum+=1

if starNum == in1:
    print(str(in1) + "+")
else:
    print(in1)