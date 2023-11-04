#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
if __name__ == '__main__':
    school = {'1a': 25, '1b': 27, '2b': 30, '6a': 24, '7v': 28,}
    school['1a'] = 30
    school['3c'] = 26
    del school['2b']
    total_students = sum(school.values())
    print(school)
    print(f"Общее количество учащихся в школе: {total_students}")

