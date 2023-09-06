def main():
    a = int(input("숫자를 입력하세요."))
    if a % 2 == 0:
        print(f"{a}은/는 \033[36m짝수\033[0m입니다.")
    else:
        print(f"{a}은/는 \033[36m홀수\033[0m입니다.")


if __name__ == "__main__":
    main()
