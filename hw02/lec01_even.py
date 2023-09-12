def main():
    try:
        num = int(input("숫자를 입력하세요 : "))
        if num % 2 == 0:
            if num%10 in [2,4,5,9]:
                print(f"{num}는 \033[36m짝수\033[0m입니다.")
            else:
                print(f"{num}은 \033[36m짝수\033[0m입니다.")

        else:
            if num%10 in [2,4,5,9]:
                print(f"{num}는 \033[36m홀수\033[0m입니다.")
            else:
                print(f"{num}은 \033[36m홀수\033[0m입니다.")
    except ValueError:
        print('정수를 입력해야 합니다.')

if __name__ == "__main__":
    main()
