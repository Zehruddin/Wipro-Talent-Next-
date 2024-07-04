def weight_of_hill(input1,input2,input3):
    num=0
    for i in range(input1):
        for j in range(i+1):
            num+=input2
        input2+=input3
    return num
print(weight_of_hill(5,10,2))
