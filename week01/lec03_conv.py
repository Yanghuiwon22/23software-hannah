

def temperature():
    temp_c = int(input('섭씨를 입력하세요'))
    temp_f = int(input('화씨를 입력하세요'))

    print(f'{temp_c}℃ - > {(temp_c*32)+32}Ｆ')
    print(f'{temp_f}Ｆ - > {(temp_f-32)/1.8}℃')


def main():
    temperature()

if __name__=='__main__':
    main()