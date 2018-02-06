# -*- coding: utf-8 -*-
def total(inital=5, *numbers, plus=10, **keywords):
    count = inital
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    count += plus
    return count




print(total(10, 1, 2, 3, vegetables=50, fruits=100, plus=100))