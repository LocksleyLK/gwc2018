from PIL import Image

def load_img(filename):
    im = Image.open(filename)
    return im

def show_img(im):
    im.show()

def save_img(im, filename):
    im.save(filename)



def obamicon(im):
    #1 save colors for filter
    darkBlue = (0, 51, 76)
    red = (217, 26, 33)
    lightBlue = (112, 150, 158)
    yellow = (252, 227, 166)

    #get list of pixels in picture and save it
    pixelList = []
    oldPixelList = im.getdata()

    for pixel in oldPixelList:
        intensity = pixel[0] + pixel[1] + pixel[2]
        if(intensity < 182):
            pixelList.append(darkBlue)
        elif(intensity < 364):
            pixelList.append(red)
        elif(intensity < 546):
            pixelList.append(lightBlue)
        else:
            pixelList.append(yellow)
    #makes new image
    im.putdata(pixelList)

    return im

def sepia(im):
    darkSepia = (255, 255, 148)
    medDarkSepia = (255, 255, 89)
    medLightSepia = (166, 120, 43)
    inBetween = (106, 64, 0)
    lightSepia = (31, 12, 0)

    sepiaPixelList = []
    oldSepiaPixelList = im.getdata()

    for pixel in oldSepiaPixelList:
        sepia_intensity = pixel[0] + pixel[1] + pixel[2]
        if(sepia_intensity < 61):
            sepiaPixelList.append(lightSepia)
        elif(sepia_intensity < 221):
            sepiaPixelList.append(inBetween)
        elif(sepia_intensity < 400):
            sepiaPixelList.append(medLightSepia)
        elif(sepia_intensity < 546):
            sepiaPixelList.append(medDarkSepia)
        else:
            sepiaPixelList.append(darkSepia)
    #makes new image
    im.putdata(sepiaPixelList)

    return im
