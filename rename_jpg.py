
import os

count = 0
label = 0
root = '../data/DEV'

for folder in os.listdir(root):
    for image in os.listdir(root + folder):
        old_name = root + folder + '/' + image
        os.rename(old_name, root + folder + '/' + str(count) + "_" + str(label) + ".jpg")
        
        if count % 100 == 0:
                print('Done:   ....    ', count)
        count += 1 
    label += 1
            
