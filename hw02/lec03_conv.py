def is_prime(num):
    return num%2==0

def main():
    while True:
        num = int(input('자연수를 입력하세요! '))
        if num > 0:
            if is_prime(num):
                print(f"{num}은/는 소수입니다.")
            else:
                print(f"{num}은/는 소수가 아닙니다.")
            break
        else:
            print('\033[36m' + '자연수가 아닙니다!!!' + '\033[0m')

if __name__ == "__main__":
    main()

