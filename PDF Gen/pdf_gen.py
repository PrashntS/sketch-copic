#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import svgwrite
from svgwrite import px, px, mm

COLOR_LIB = {}
DWG = None

def draw_color(ID, column, row):
    global DWG
    offsets = {
        "insert": (row  * 55, column * 45),
        "insert_text": (row * 55, (column + 1) * 45 - 10),
        "size": (50, 25)
    }

    rect = DWG.rect(
        insert = offsets["insert"],
        size   = offsets["size"],
        fill   = "#" + COLOR_LIB[ID]
    )

    text = DWG.text(
        ID,
        insert = offsets["insert_text"],
        style  = "font-size: 12px; font-family: P22UndergroundProDemi; line-height: 12px",
        fill   = "#" + COLOR_LIB[ID]
    )

    DWG.add(text)
    DWG.add(rect)

def init ():
    global COLOR_LIB, DWG
    DWG = svgwrite.Drawing(filename = "out.svg")
    if os.path.exists("copic-library.json"):
        with open("copic-library.json", "r") as f:
            COLOR_LIB = json.loads(f.read())
        return None
    raise Exception("Copic Color Library doesn't exists.")

def end ():
    global DWG
    DWG.save()

def main():
    init()
    row = 0
    column = 0
    prev_char = None
    for i in sorted(COLOR_LIB):
        if prev_char is None:
            prev_char = i[0]
        if prev_char is not i[0]:
            row = 0
            column += 2
            prev_char = i[0]
        if row == 15:
            row = 0
            column += 1
        draw_color(i, row, column)
        row += 1

    end()

if __name__ == "__main__":
    main()