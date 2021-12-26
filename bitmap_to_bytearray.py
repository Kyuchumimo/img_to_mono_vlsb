#Multidimensional bitmap to bytearray (horizontal addressing) Python script, suitable for Nokia 5110 PCD8544 84x48 LCD and SSD1306 128x64 OLED displays. 
#Script by Kyuchumimo. Available to the entire Open Source community
#!/usr/bin/env python3
# usage: python3 thisfile.py infile.png/jpeg/jpg/bmp

from PIL import Image
import sys

im = Image.open(sys.argv[1])  # Can be many different formats. Must be a 1-bit b/w 84x48 image

pix = im.load()
print(im.size)  # Get the width and hight of the image for iterating over

a = ""

for i in range(0,(im.size[1]-1)//8+1):
    for j in range(0,im.size[0]):
        for k in range(7, -1, -1):
            try:
                if pix[j,k+(8*i)] == (255, 255, 255):
                    a = a + "0"
                elif pix[j,k+(8*i)] == (0, 0, 0):
                    a = a + "1"
                else:
                    print("invalid color request: {} at {} pos".format(pix[j,k+(8*i)], [j,k+(8*i)]))
                    sys.exit()
            except IndexError:
                a = a + "0"

print("bytearray(b'",end='')
for i in range(0,(im.size[0]*(((im.size[1]-1)//8+1)*8))//8):
    print("\\",end='')
    print("x",end='')
    print(f'{int(a[0+(8*i):8+(8*i)], 2):02x}',end="")
print("')",end='')
