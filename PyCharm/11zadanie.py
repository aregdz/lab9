#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
if __name__ == '__main__':
    m = {1: "A", 2: "B", 3: "C", 4: "D"}
    dict_items = {v: k for k, v in m.items()}
    print(dict_items)
