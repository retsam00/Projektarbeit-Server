import base64
import hashlib

def string_to_image(imgstring):
    imgdata = base64.b64decode(imgstring)
    imgname = hashlib.md5(imgdata).hexdigest() + '.jpg'
    print(imgname)
    filename = 'images/' + imgname
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()
    return filename