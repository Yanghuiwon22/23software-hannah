def m2ha():
    m = float(input('? m^2 =>: '))
    print(f'{m}ha는 \033[36m{m/10000}m^2\033[0m입니다.')
    print('++++++++++++++++++++++++++++++++++++++++++++')
def ha2m():
    hac = float(input('몇 ha를 알고싶으세요? : '))
    print(f'{hac}ha는 \033[36m{hac*10000}m^2\033[0m입니다.')
    print('++++++++++++++++++++++++++++++++++++++++++++')

def main():
    print(f'\033[31m1ha는 10000m^2입니다.\033[0m')
    ha2m()
    m2ha()


if __name__ == "__main__":
    main()
