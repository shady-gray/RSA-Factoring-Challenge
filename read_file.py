#!/usr/bin/python3
def convert_to_int(rope):
    new_list = []
    for item in rope:
        new_list.append(int(item))
    return new_list


def read_file(file=''):
    with open(file) as fp:
        numbers = [line.rstrip() for line in fp]
    return convert_to_int(numbers)
