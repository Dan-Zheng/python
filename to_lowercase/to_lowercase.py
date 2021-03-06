#!usr/bin/env python

import pyperclip

def main():
    string = raw_input('Enter a string to convert to lowercase: ')
    print '\nLowercase: ' + string.lower() + '\n'

    copy_confirm = raw_input('Copy to clipboard? (y/n)\n').lower()
    if copy_confirm == 'yes' or copy_confirm == 'y':
        pyperclip.copy(string.lower()) # copies the string to clipboard
        print 'Successfully copied to clipboard.'
    else:
        print 'Not copied to clipboard.'

if __name__ == "__main__":
    main()
