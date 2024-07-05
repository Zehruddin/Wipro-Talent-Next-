def Weight_of_String(input1,input2):
        ab=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        no=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
        dic=dict(zip(ab,no))
        vow="aeiou"
        weight=0
        
        for i in input1.lower():
            if i.isalpha():
                if input2==0:
                    if i not in vow:
                        weight+=dic[i]
                else:
                    weight+=dic[i]
        return weight
res=Weight_of_String("Hello World!",0)
return res
