# import required classes

from PIL import Image, ImageDraw, ImageFont

# create Image object with the input image




# create font object with the font file and specify
# desired size
def numbr(n):
    s='0'*(4-len(str(n)))+str(n)
    return(s)
font = ImageFont.truetype('Roboto-Bold.ttf', size=45)

# starting position of the message
for i in range(1,1600,4):
    image = Image.open('b.jpeg')
    draw = ImageDraw.Draw(image)
    #print(numbr(i),i+2)
    (x, y) = (1631, 2397)
    message = numbr(i)
    color = 'rgb(0, 0, 0)' # black color
    draw.text((x, y), message, fill=color, font=font)
    (x, y) = (3373, 2397)
    message = numbr(i+2)
    color = 'rgb(0, 0, 0)' # black color

    draw.text((x, y), message, fill=color, font=font)

    # save the edited image

    image.save(str(numbr(i))+'.PNG')
        
'''
(x, y) = (1631, 2397)
message = "777!"
color = 'rgb(0, 0, 0)' # black color
draw.text((x, y), message, fill=color, font=font)
(x, y) = (3373, 2397)
message = "777!"
color = 'rgb(0, 0, 0)' # black color

draw.text((x, y), message, fill=color, font=font)

# save the edited image

image.save('greeting_card.png')

'''
