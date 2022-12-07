import qrcode as qr
from PIL import Image



def main() :
    
    towards = "https://www.youtube.com/watch?v=bi2NLbLYbic"

    code = qr.QRCode(version=1, error_correction=qr.ERROR_CORRECT_H, box_size=10, border=4)
    code.add_data(towards)
    code.make(fit=True)
    
    img = code.make_image()
    img.save("example.png")


if __name__ == "__main__" :
    main()