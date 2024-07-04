def OddorEvenSum_of_Digits(input1,input2):
        def Sum(input1,input2):
            sum1=0
            while input1>0:
                n=input1%10
                if input2=="odd":
                    if n%2!=0:
                        sum1+=n
                else:
                    if n%2==0:
                        sum1+=n
                input1//=10
            return sum1
        res_sum=Sum(input1,input2)
        return res_sum
        pass
