import sys

sys.path.append('/usr/lib64/python2.6/site-packages/PIL')

import Image,ImageDraw, ImageFont,ImageFilter
import random

def rndChar():
	return chr(random.randint(65,90))

def rndColor():
	return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

def rndColor2():
	return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

width = 60*4
height = 60

image = Image.new('RGB',(width,height),(255,255,255))

#create font
font = ImageFont.truetype('/usr/share/fonts/dejavu/DejaVuSans.ttf',36)
#create Draw object
draw = ImageDraw.Draw(image)
#fullfill every pix
for x in range(width):
	for y in range(height):
		draw.point((x,y),fill = rndColor())
#output words
for t in range(4):
	draw.text((60*t+10,10),rndChar(),font = font,fill = rndColor2())

#BLUR
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg','jpeg')



