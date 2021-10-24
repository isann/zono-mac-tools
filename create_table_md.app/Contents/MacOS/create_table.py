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
        if row == "":
            break
        columns = row.split("\t")
        if i == 0:
            for column in columns:
                out += "|" + column
            out += "|\n"
            for column in columns:
                out += "|----"
            out += "|\n"
        else:
            for column in columns:
                out += "|" + column
            out += "|\n"
    set_data(out)




if __name__ in '__main__':
    main()
