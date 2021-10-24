# -*- coding: utf-8 -*-
__author__ = 'zono'

import subprocess


def get_data():
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    return p.communicate()[0]


def set_data(data):
    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    p.communicate(data)


def main():
    clip = get_data()
    line = clip.split("\n")
    out = ""
    for i in range(0, len(line)):
        row = line[i]
        if i == 0:
            out += "> " + row
        elif row == "":
            out += "\n>"
        else:
            out += "\n> " + row
    set_data(out)




if __name__ in '__main__':
    main()
