from PIL import Image
import os, time, argparse


def main(opt):

	img_dir = opt.root
	dim = int(opt.min_size)
	too_small = 0
	processed = 0
	new_size = int(opt.resize)
	resized = 0
	removed = 0

	for root, dirs, files in os.walk(img_dir):
		for file in files:
			file_path = os.path.join(root, file)
			processed += 1

			try:
				im = Image.open(file_path)
				width, height = im.size

				if width < dim and height < dim:
					too_small += 1				
					im.close()
					os.remove(file_path)
				else:
					resized += 1
					im = im.resize((new_size, new_size))
					im.save(file_path)
					im.close()
				
				if processed % 100 == 0:
					print("Processed: ", processed)
			
			except:
				os.remove(file_path)
				removed += 1


	print("Images too small:", too_small)
	print("Images resized:", resized)
	print("Images corrupted and removed:", removed)
	time.sleep(180)


	
				

				
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Resizes all images')
    parser.add_argument('--root', help = 'Images folder', required = False) 
    parser.add_argument('--min_size', help = 'Minimum size allowed', required = False) 
    parser.add_argument('--resize', help = 'Squared final dimensions', required = False) 
    args = parser.parse_args()
    main(args)
