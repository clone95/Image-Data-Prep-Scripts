from scipy.misc import imread, imsave, imresize
import os, sys, time, argparse

def main(opt):
 
    print("\n---> Removing black & white images ...\n")

    color = 0
    bew = 0
    other = 0
    delete = []
    for root, dirs, files in os.walk(opt.root):
      for file in files:
        print(file)
        path = os.path.join(root, file)
        image = imread(path)

        if len(image.shape) < 3:
            bew += 1
            os.remove(path)
            delete.append(file)

        elif len(image.shape)==3:
            color += 1

        else:
            os.remove(path)
            delete.append(file)
            other += 1
        
        count = color + other + bew
        if count % 100 == 0:
            print("Processed", count, "files.")


    print("Removed", bew, "B&W images and", other, "files of unknown type.", )
    time.sleep(3)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Deletes black and white images')
    parser.add_argument('--root', help = 'Root folder to ', required = True) 
    args = parser.parse_args()
    main(args)

