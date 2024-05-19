def fibo(n):
    if n==0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return [0,1]
    else:
        fib_Seq = fibo(n-1)
        fib_Seq.append(fib_Seq[-1]+fib_Seq[-2])
        return fib_Seq
    
n = int(input("Enter the number of terms: "))   
print(fibo(n))