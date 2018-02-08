# -*- coding: utf-8 -*-

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    bad_symbles = (',', '.', ' ', ':', '!', '?')
    for symble in bad_symbles:
        text = text.replace(symble, '')
    clear_text = text.lower()
    return clear_text == reverse(clear_text)

something = input('Введите текст: ')

if (is_palindrome(something)):
    print('Это палиндром')
else:
    print('Это не палиндром')

