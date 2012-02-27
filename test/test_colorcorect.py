# -*- coding: utf-8 -*-
import sys
import Image
from colorcorrect.algorithm import stretch, grey_world, retinex, max_white, retinex_adjust, standard_deviation_weighted_grey_world,standard_deviation_and_luminance_weighted_gray_world
from colorcorrect.util import from_pil, to_pil

if __name__=="__main__":
    img = Image.open(sys.argv[1])
    img.show()
    to_pil(stretch(from_pil(img))).show()
    to_pil(grey_world(from_pil(img))).show()
    to_pil(retinex(from_pil(img))).show()
    to_pil(max_white(from_pil(img))).show()
    to_pil(retinex_adjust(retinex(from_pil(img)))).show()
    to_pil(standard_deviation_weighted_grey_world(from_pil(img),50,50)).show()
    to_pil(standard_deviation_and_luminance_weighted_gray_world(from_pil(img),16,16)).show()