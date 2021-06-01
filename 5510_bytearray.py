#84x48 bitmap to bytearray, suitable for Nokia 5510 LCD display horizontal addressing.
#Script by Kyuchumimo. Available to the entire Open Source community
#!/usr/bin/env python3
# usage: python3 thisfile.py infile.png/jpeg/jpg/bmp

from PIL import Image
import sys

im = Image.open(sys.argv[1])  # Can be many different formats. Must be a 1-bit b/w 84x48 image

pix = im.load()
print(im.size)  # Get the width and hight of the image for iterating over

if im.size != (84, 48):
    print("Must be a 84x48 image!")
    sys.exit()

a = ""

for i in range(0,6):
    for j in range(0,im.size[0]):
        for k in range(7,-1,-1):
            if pix[j,k+(8*i)] == (255,255,255):
                a = a + "0"
            if pix[j,k+(8*i)] == (0,0,0):
                a = a + "1"

print("b'",end='')
for i in range(0,504):
    print("\\",end='')
    print("x",end='')
    print(f'{int(a[0+(8*i):8+(8*i)], 2):02x}',end="")
print("'",end='')
