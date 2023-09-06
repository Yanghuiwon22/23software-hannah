def f2c(temp_f):
    pass


def main():
    temp_f = 80
    # 두 줄
    temp_c = f2c(temp_f)
    print(f"{temp_f}F => {temp_c}℃")

    # 한 줄
    print(f"{temp_f}F => {f2c(temp_f)}℃")


if __name__ == "__main__":
    main()
