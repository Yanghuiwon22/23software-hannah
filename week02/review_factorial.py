def fac(num):
    if num == 1:
        return 1
    return num * fac(num-1)
#재귀 함수 사용
#예전엔 효용이 있었으나 지금은 아니다.


def main():
    num = int(input('(음수가 아닌 정수를 입력하세요.) \n팩토리얼로 계산할 값을 입력하세요! : '))

    if num > 0:
        print(f'{num}!은 값은' '\033[36m' + f'{fac(num)}' + '\033[0m' + '입니다.')
    else:
        print('음수가 아닌 정수를 입력하세요!!!')


if __name__=="__main__":
    main()