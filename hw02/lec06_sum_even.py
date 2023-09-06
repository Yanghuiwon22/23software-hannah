def get_prime(n,m):
    get_list = [ i for i in range(n, m+1)]
    for j in get_list:
        pass

def main():
    first, last = map(int, input('몇부터 몇까지 고려할까요? ( 띄어쓰기로 구분해주세요. )').split(' '))
    list_prime = [i for i in range(first, last) if get_prime(first, last)]
    print(f'{list_prime}')


if __name__=="__main__":
    main()