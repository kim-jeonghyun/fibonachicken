def do_fibo(num):
    if num<=1:
        return num
    else:
        return do_fibo(num-1) + do_fibo(num-2)

if __name__=='__main__':
    user_num = int(input('Type any positive integer: '))
    result = do_fibo(user_num)
    print(result)
