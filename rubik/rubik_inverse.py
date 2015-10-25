#!usr/bin/env python
# -*- coding: utf-8 -*-

import re
import pyperclip

def format_string(string):
    result = ''
    if string.endswith(' '):
        string = string[:-1]

    string = string.replace('’', '\'') # change UTF-8 quotation mark to ASCII quotation
    # string = "".join(s.split()) # remove all whitespace from string
    string = string.replace(' ', '') # remove all spaces from string

    if re.search('[^UDFBLRMESXYZudfblrmesxyz2\']', string): # fail accepted characters
        return False
    else:
        i = 0
        move_list = []
        while i < len(string):
            if re.search('[UDFBLRMESXYZudfblrmesxyz]', string[i]):
                if i < len(string) - 1 and re.search('[2\']', string[i+1]): # if complex move (2')
                    move_list.append(string[i:i+2])
                    i += 2
                else:
                    move_list.append(string[i])
                    i += 1
            else:
                return False

        move_list.reverse() # same as move_list[::-1]

        for move in move_list:
            if re.search('[XYZ]', move): # convert [XYZ] to [xyz]
                move = move.lower()
            elif re.search('[mes]', move): # convert [mes] to [MES]
                move = move.upper()
            result = result + invert_move(move) + ' ' # append move to result

    result = result[0:-1]
    print 'Inverse: ' + result
    if len(move_list) >= 15:
        print 'That\'s a long sequence of moves. Don\'t mess up!'
    copy_confirm = raw_input('Copy to clipboard? (Y/n)\n').lower()
    if copy_confirm == 'yes' or copy_confirm == 'y' or copy_confirm == '':
        pyperclip.copy(result) # copies the string to clipboard
        print 'Successfully copied to clipboard.'
    else:
        print 'Not copied to clipboard.'
    return result

def invert_move(move):
    if '\'' in move:
        move = move[:-1]
    elif '2' not in move:
        move = move + '\''
    return move

def main():
    print 'This script returns the inverse of an Rubik\'s cube algorithm. Currently works for 2x2 to 5x5.'
    while True:
        string = raw_input('Enter an algorithm as a string of moves: \n')

        if format_string(string):
            break
        else:
            print 'Invalid move input, try again. (Accepted chars: UDFBLRMESudfblrxyz2\')\n' #UDFBLRudfblrXYZxyz

if __name__ == "__main__":
    main()
