import argparse
from encrypt import encrypt
from decrypt import decrypt
import os

secretInfo = "i am sanya "

inputImgPath = os.path.join(os.path.curdir, "image.jpg")
outputImgPath = os.path.join(os.path.curdir, "newimage.png")

parser = argparse.ArgumentParser(description='Hide info in image.')
parser.add_argument('-d', '--decrypt', action="store_true",)
parser.add_argument('-e', '--encrypt', action="store_true",)
parser.add_argument('-i', '--imgPath', default=inputImgPath )


args = parser.parse_args()
if args.decrypt:
    res = decrypt(args.imgPath)
    print("Раcшифрована информация с файла",  res, "в", args.imgPath)
elif args.encrypt:
    encrypt(args.imgPath, secretInfo, outputImgPath)
    print("Зашифрована информация", secretInfo, "в", outputImgPath)
else:
    print("Пу")
