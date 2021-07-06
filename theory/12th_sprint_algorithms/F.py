"""
Palindrome
"""
from string import ascii_letters, digits

def main():
    with open('input.txt') as file:
        data = file.read().strip()
        cleaned_data = ''
        for simbol in data:
            if simbol in ascii_letters + digits:
                cleaned_data += simbol.lower()
        for i in range(int(len(cleaned_data)/2+1)):
            if cleaned_data[i] != cleaned_data[-i-1]:
                return False
        return True

if __name__ == '__main__':
    print(main())
