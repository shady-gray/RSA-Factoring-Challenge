#!/usr/bin/python3
import time


def find_factors(number):
    mulList = []
    for div in range(2, 1 + int(number ** 0.5)):
        if (number % div) == 0:
            mulList.append(div)
            quotient = number // div
            if quotient != div and div * quotient == number:
                mulList.append(quotient)
            break
        else:
            continue
    return mulList


def check_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, 1 + int(number ** 0.5), 2):
        if number % i == 0:
            return False
    return True


def get_prime(number):
    primeList = []
    for div in range(2, 1 + int(number ** 0.5)):
        if (number % div) == 0:
            if div % 2 == 0 and div != 2:
                continue
            else:
                if check_prime(div):
                    quotient = number // div
                    if check_prime(quotient):
                        primeList.append(div)
                        primeList.append(quotient)
                    else:
                        continue
                else:
                    continue
            break
        else:
            continue
    return primeList
