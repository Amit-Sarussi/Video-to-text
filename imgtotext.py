from PIL import Image

def itt(imgPath: str):
    fullStr = ''
    im = Image.open(imgPath)
    size = 55
    resImg = im.resize((size, size))
    resImgPix = resImg.load()
    for x in range(size):
        fullStr = fullStr + "\n"
        for y in range(size):
            if (resImgPix[y,x] > 20):
                fullStr = fullStr + "⬜"
            else:
                fullStr = fullStr + "⬛"
    return fullStr

