import base64
import os.path
import codecs


def sendImage(ImageName):
    image = open(ImageName, 'rb') #open binary file in read mode
    image_read = image.read()
    #image_64_encode = base64.encodestring(image_read)
    return image_read


def storeImage(image_64_encode,ImageName):
    #image_64_decode = codecs.decode(image_64_encode+"==".encode(), encoding='base64')
    #image_64_decode = base64.decodestring(image_64_encode)

    #counter+=1
    save_path = 'D:/ServerTrial/images'
    completename = os.path.join(save_path, ImageName)

    image_result = open(completename, 'wb') # create a writable image and write the decoding result
    image_result.write(image_64_encode)
    return completename
