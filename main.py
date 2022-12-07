import qrcode as qr



def main() :
    
    img = qr.make("https://www.youtube.com/watch?v=bi2NLbLYbic")
    
    img.save("example.png")




if __name__ == "__main__" :
    main()