from PIL import Image
import pyzbar.pyzbar as pyzbar
import time


path = "C:/Users/Proteam/Desktop/test/generate-barcode8l.png"  # /QR_Code.png /generate-barcode.png /frame2.png


def main():
    img = Image.open(path)
    stime = time.time()
    qr = pyzbar.decode(img)
    endtime = time.time()
    
    print("Hi %s - %s, delay %s.The decoded QR code is: %s" % (stime, endtime, endtime - stime, qr))


if __name__ == "__main__":
    main()
