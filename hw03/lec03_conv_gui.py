import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()

def simple_gui_input(text):
    return simpledialog.askstring(title="GUI창",
                                    prompt=text)

def is_prime(num):
    count = 0
    for i in range(1,num+1):
        if num%i == 0:
            count += 1
    return count == 2

def main():
    while True:
        num = int(simple_gui_input('자연수를 입력하세요! '))
        if num > 0:
            if is_prime(num):
                print(f"{num}은/는 \033[36m소수\033[0m입니다.")
            else:
                print(f"{num}은/는 \033[36m소수가 아닙니다.")
            break
        else:
            print('\033[36m' + '자연수가 아닙니다!!!' + '\033[0m')

if __name__ == "__main__":
    main()

