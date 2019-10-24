from PIL import Image
import os, sys, time, argparse


def main(opt):

    print("\n---> Converting to .jpg ...\n")

    img_dir = opt.root
    seen = 0
    processed = 0

    for root, dirs, files in os.walk(img_dir):
      for file in files:
        seen += 1
        old_path = os.path.join(root, file)
        #abs_path = os.path.abspath(file)
        filename = os.path.splitext(file)[0]
        extension = os.path.splitext(file)[1]
        
        if extension.lower() == ".jpg" or extension.lower() == ".jpeg" :
            pass
        elif extension.lower() == ".png" :
            res = filename + ".jpg"
            im = Image.open(old_path)
            im = im.convert('RGB')
            path = os.path.join(root, res)
            im.save(path, quality=95)
            im.close()
            os.remove(old_path)   
            processed += 1
        else: 
            im.close()
            os.remove(old_path)   
        
        if seen % 500 == 0:
            print("Seen images:", seen)


    
    print("Processed from other formats to .jpg", processed, "out of", seen)
    time.sleep(3)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Convert to .jpg')
    parser.add_argument('--root', help = 'Image folder to convert  --> .jpg', required = True) 
    args = parser.parse_args()
    main(args)



