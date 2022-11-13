from PIL import Image
from functools import wraps
from time import perf_counter
import sys

allPaternsSymb = [' ','⠠','⠄','⠤','⠐','⠰','⠔','⠴','⠂','⠢','⠆','⠦','⠒','⠲','⠖','⠶','⠈','⠨','⠌','⠬','⠘','⠸','⠜','⠼','⠊','⠪','⠎','⠮','⠚','⠺','⠞','⠾','⠁','⠡','⠅','⠥','⠑','⠱','⠕','⠵','⠃','⠣','⠇','⠧','⠓','⠳','⠗','⠷','⠉','⠩','⠍','⠭','⠙','⠹','⠝','⠽','⠋','⠫','⠏','⠯','⠛','⠻','⠟','⠿']


def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args,**kwargs)
        return cache[key]
    return wrapper

@memoize
def itt(imgPath: str):
    
    fullStr = ''
    im = Image.open(imgPath)
    width, height = im.size
    imlo = im.load()
    for y in range(height//3):
        fullStr += '\n'
        for x in range(width//2):
            bi = 0
            if ((imlo[x*2,(y*3)][0]) > 100):
                bi += 32
            if ((imlo[(x*2)+1,(y*3)][0]) > 100):
                bi += 16
            if ((imlo[x*2,(y*3)+1][0]) > 100):
                bi += 8
            if ((imlo[(x*2)+1,(y*3)+1][0]) > 100):
                bi += 4
            if ((imlo[x*2,(y*3)+2][0]) > 100):
                bi += 2
            if ((imlo[(x*2)+1,(y*3)+2][0]) > 100):
                bi += 1
            fullStr += allPaternsSymb[bi]
    return fullStr
            
# if __name__ == '__main__':
#     x = ['g']
#     start = perf_counter()
#     for i in range(20000):
#         x.append(itt('test.jpg'))
#     end = perf_counter()

#     print(x)
#     print(f'Time: {end-start} sec')