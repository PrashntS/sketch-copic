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
        "insert": (row  * 50, (column) * 30),
        "insert_text": (row * 50, (column) * 30 + 35),
        "size": (50, 25)
    }

    rect = DWG.rect(
        insert = offsets["insert"],
        size   = offsets["size"],
        fill   = COLOR_LIB[ID]
    )

    text = DWG.text(
        ID,
        insert = offsets["insert_text"],
        style  = "font-size: 12px; font-family: P22UndergroundProDemi;",
        fill   = COLOR_LIB[ID]
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
    draw_color("r46", 0, 0)
    draw_color("110", 0, 1)
    draw_color("g82", 10, 10)
    #draw_color("b0000", 1, 0)
    end()

if __name__ == "__main__":
    main()