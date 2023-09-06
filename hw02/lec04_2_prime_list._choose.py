def is_prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    return count == 2

def main():
    first, last = map(int,input(f'빈칸에 원하는 수를 입력하세요 => \033[36m[]\033[0m부터 \033[36m[]\033[0m까지 중 소수를 구하자!(띄어쓰기로 구분) ').split(' '))
    list_prime = [x for x in range(first, last+1) if is_prime(x)]
    print(f"1-100까지 중 소수는 \033[36m{(list_prime)}\033[0m입니다.")
    print(f"1-100까지 중 소수의 갯수는 \033[36m{len(list_prime)}\033[0m입니다.")


if __name__ == "__main__":
    main()
