## Program : Validation Module
## Developer : Trevor Murphy
## Date : start(23/02/2017)
## Description : Validation module.

import string
import fp

# Validates strings. Does not allow any punctuation or numbers. Loop checks text string
# for digits or special characters, if it finds any sets text back to '' and breaks the
# for loop, when text is valid, returns text capitalized. No params.
def only_txt(maxl, name):
    digits = string.digits
    specChars = string.punctuation
    text = ''
    print(len(text))
    while len(text) < 1 or len(text) > maxl:
        text = input('Enter ' + name + ': ')
        for i in text:
            if i in specChars:
                text = ''
                print('No special characters allowed.')
                break
            elif i in digits:
                text = ''
                print('No digits allowed.')
                break
        if len(text) > maxl:
            print('Maximum length is', maxl)
    return text


# Validates yes or no questions,
# returns first letter of input, lowercase
def yes_no(question):
    print(question +'?')
    fp.s_txt()
    yesno = ''
    while yesno not in ('y','n','yes','no'):
        print('Please enter yes or no. (y or n)')
        yesno = input().lower()
    return yesno[:1]


# Validates input as integer by using infinite loop
# to teset for value errors until there is no value error
def input_int():
    while True:
        try:
            number = int(input('Please enter a number.\n'))
        except ValueError:
            continue
        else:
            return number

# Takes a question and 2 options, prints the question,
# prints the options, and only allows that input
def dual_option(question, one, two, o = 'fl', t = 'fl'):
    if o == 'fl':
        o = one[:1].lower()
    if t == 'fl':
        t = two[:1].lower()
    print(question +'?')
    decision = ''
    while decision not in (o, t):
        print('Please enter', one, 'or', two + '.', '(', o, 'or', t, ')')
        decision = input()[:1].lower()
    return decision[:1]

# Allows int input within a range of 1 to amnt
def num_choices(amnt):
    while True:
        print('(Between 1 and', amnt, ')')
        choice = input_int()
        if choice >= 1 and choice <= amnt:
            break
    return choice

# Validates proper input based on contents of list/tuple(tuple pref)
# Only first character is capital, formats lists properly
def in_choices(choices, prompt = 'Please choose '):
    x = str
    clen = 0
##    longc = 0
    for c in choices:
##        if c > longc:
##            longc = c
        clen += len(c) + 4
    while x not in choices:
        print(prompt + str(choices))
        fp.s_txt(1 + len(prompt) + clen)
        x = input()
        x = x.lower().capitalize()
        #print(x)
        fp.s_txt(len(x) + 2)
        print()
    return x
        
def main():
    pass
main()
