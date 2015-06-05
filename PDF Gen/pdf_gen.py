#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import svgwrite
from svgwrite import px, px, mm

COLOR_LIB = {}

def draw():
    dwg = svgwrite.Drawing(filename = "out.svg")

    hlines = dwg.add(dwg.g(id='hlines', stroke='#b3e3f1'))

    dwg.add(dwg.rect(insert = (0*px, 0*px), size = (50*px, 20*px), fill = '#b3e3f1'))

    dwg.add(dwg.text("Reported Crimes in Sweden",
                                       insert = (410, 50),
                                       fill = "rgb(255,255,0)",
                                       style = "font-size:49px; font-family:P22UndergroundProDemi"))

    """
    for y in range(20):
        hlines.add(dwg.line(start=(20*px, (20+y)*px), end=(18*px, (2+y)*px)))

    vlines = dwg.add(dwg.g(id='vline', stroke='blue'))
    for x in range(17):
        vlines.add(dwg.line(start=((2+x)*px, 2*px), end=((2+x)*px, 21*px)))

    #shapes = dwg.add(dwg.g(id='shapes', fill='red'))

        # set presentation attributes at object creation as SVG-Attributes
    shapes.add(dwg.circle(center=(15*px, 8*px), r='2.5px', stroke='blue',
                          stroke_width=3))

    # override the 'fill' attribute of the parent group 'shapes'
    shapes.add(dwg.rect(insert=(5*px, 5*px), size=(45*mm, 45*mm),
                        fill='blue', stroke='red', stroke_width=3))

    # or set presentation attributes by helper functions of the Presentation-Mixin
    ellipse = shapes.add(dwg.ellipse(center=(10*px, 15*px), r=('5px', '10mm')))
    ellipse.fill('green', opacity=0.5).stroke('black', width=5).dasharray([20, 20])"""
    dwg.save()
    pass

def init_color_lib ():
    global COLOR_LIB
    if os.path.exists("copic-library.json"):
        with open("copic-library.json", "r") as f:
            COLOR_LIB = json.loads(f.read())
        return None
    raise Exception("Copic Color Library doesn't exists.")

def main():
    draw()
    pass

if __name__ == "__main__":
    main()