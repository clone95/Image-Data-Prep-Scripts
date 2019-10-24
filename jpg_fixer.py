import os, time, argparse
from PIL import Image


def verify_image(img_file):
     # test image
   try:
      v_image = Image.open(img_file)
      v_image.verify()
      return True;

   except OSError:
      return False;


def main(opt):

   print("\n---> Validating images... \n")

   img_dir = opt.root
   files_count = 0
   corrupted = 0
   to_delete = []
   
   for root, dirs, files in os.walk(img_dir):
      for file in files:

         if file.endswith(".jpg"):
               currentFile = os.path.join(root, file)

               if verify_image(currentFile):
                  if files_count % 500 == 0:
                     print("processed", files_count, "files")
                  files_count += 1

               else:
                  files_count += 1
                  corrupted += 1
                  os.remove(currentFile)
                  print("corrupted file") 
   
   print("\nDeleted", corrupted, "corrupted files out of", files_count)
   time.sleep(3)

        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Description')
    parser.add_argument('--root', help = 'Folder to fix', required = False) 
    args = parser.parse_args()
    main(args)
