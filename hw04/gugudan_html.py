from rich import print

def main():
    dan = 7
    
    filename = "index.html"
    
    with open(filename, 'w', encoding='utf-8') as f:
        
        f.write('<html>\n')
        f.write('<body>\n')
        f.write(f'<h2>{dan}단</h2>\n')
        f.write('<div>\n')
        for i in range(1,10):
            f.write(f'{dan} X {i:2d} = {dan*i:02d}<br>\n')
        f.write('</div>\n')
        f.write('</body>\n')
        f.write('</html>\n')

if __name__=="__main__":
    main()