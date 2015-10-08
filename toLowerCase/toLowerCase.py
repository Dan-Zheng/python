#!usr/bin/env python

import pyperclip

def main():
    string = str(raw_input('Enter a string to convert to lowercase: '))
    print('\nLowercase: ' + string.lower() + '\n')

    copyConfirm = raw_input('Copy to clipboard? (y/n)\n').lower()
    if copyConfirm == 'yes' or copyConfirm == 'y':
        pyperclip.copy(string) # copies the string to clipboard
        print('Successfully copied to clipboard.')
    else:
        print('Not copied to clipboard.')


if __name__ == "__main__":
    main()
