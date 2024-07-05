def Second_word_Upper(input1):
            str1=input1.split(" ")
            if len(str1)==1:
                return "LESS"
            else:
                return str1[1].upper()
input1=input("Enter a string:")
res=Second_word_Upper(input1)
return res
