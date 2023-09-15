from rich import print

def main():
    dan = 7
    for i in range(1,20):
        print(f'{dan} X {i:02d} = [bold magenta]{dan*i:03}[/bold magenta]')

if __name__=="__main__":
    main()