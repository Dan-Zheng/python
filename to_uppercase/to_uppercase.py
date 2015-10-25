#!usr/bin/env python

import pyperclip

def main():
    string = raw_input('Enter a string to convert to uppercase: ')
    print '\nUppercase: ' + string.upper() + '\n'

    copy_confirm = raw_input('Copy to clipboard? (y/n)\n').lower()
    if copy_confirm == 'yes' or copy_confirm == 'y':
        pyperclip.copy(string.upper()) # copies the string to clipboard
        print 'Successfully copied to clipboard.'
    else:
        print 'Not copied to clipboard.'

if __name__ == "__main__":
    main()
