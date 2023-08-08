from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def convertToImg(outtext):
    img = Image.new('RGB', (751, 970), color = 'white')
    img.save('blank.png')
    # Open an Image
    img = Image.open('blank.png')
    
    # Call draw Method to add 2D graphics in an image
    I1 = ImageDraw.Draw(img)
    
    textx=outtext
    mfont = ImageFont.truetype("handwriting.ttf",40)

    # print(string)
    newstr=textx.replace('\n'," ")
    # print(newstr)
    size = 35
    modstr=""
    list1 = newstr.split()
    # print(list1)
    count = 0
    lines=1
    for i in list1:
        if count+len(i)>size:
            count=0
            modstr+="\n"+i
            lines+=1
        else:
            count+=len(i)
            modstr=modstr+" "+i
    # Add Text to an image
    I1.text((40,35), modstr,font=mfont, fill=(0, 0, 0))
    
    # Display edited image
    # img.show()
    
    # Save the edited image
    img.save("output.png")