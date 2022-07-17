#Multidimensional bitmap to bytearray (horizontal addressing) Python script, suitable for Nokia 5110 PCD8544 84x48 LCD and SSD1306 128x64 OLED displays. 
#Script by Kyuchumimo. Available to the Open Source community
#!/usr/bin/env python3
# usage: python3 thisfile.py infile.png/jpeg/jpg/bmp

from PIL import Image
import os, sys

im = Image.open(sys.argv[1])  # Can be many different formats.
im = im.crop((0,0,min(im.size[0], 84), min(im.size[1], 48))).convert("1").convert("RGB")

data = bytearray((im.size[0]*(((im.size[1]-1)//8+1)*8))//8)
for i in range((im.size[1]-1)//8+1):
    for j in range(im.size[0]):
        for k in range(7, -1, -1):
            try:
                if im.getpixel((j,k+(8*i))) == (0, 0, 0):
                    data[j+(i*im.size[0])] |= 1 << k
            except IndexError:
                pass

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

print(data)

if os.name == 'nt':
    os.system('pause')
else:
    os.system("""
bash -c "read -n 1 -s -r -p 'Press any key to continue . . . \n'"
""")
sys.exit()
