def main():
    with open('input.txt') as file:
        data = file.read().strip().split('\n')
        n = int(data[0])
        symbols = data[1]
        number = int(data[2])
        cleaned_sumbols = ''
        for symbol in symbols:
            if symbol != ' ':
                cleaned_sumbols += symbol
        output = str(int(cleaned_sumbols)+number)
        for symbol in output:
            print(symbol, end=' ')



if __name__ == '__main__':
    main()
