def Palindrome(input1,input2):        
        def ispal(input1):
            sum1=0
            inp=input1
            while(input1>0):
                n=input1%10
                sum1=sum1*10+n
                input1//=10
            if inp==sum1:
                return 2
            else:
                return 1
a=ispal(input1)
return a
pass
