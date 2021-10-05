import numpy as np
import pandas as pd
from glob import glob
from PIL import Image

# Load in all images
files = glob('./results/gen_faces/*.jpg')
images = [Image.open(file) for file in files]
n = len(images)

# get subject name
print("Enter name: ")
subject_name = str(input())

# get scoring of all images 10 times
df = pd.DataFrame()
indicies = np.arange(len(images))
for i in range(10):
    # Go through all the images in random order
    np.random.shuffle(indicies)
    for idx in indicies:
        # display image
        images[idx].show()

        # get image name
        name = files[idx].split('\\')[-1].split('.jpg')[0]

        # get score from subject
        print("Enter score (1-5): ")
        score = int(input())

        # add to dataframe
        df.loc[i, name] = score

df.to_csv(f'./results/scoring_{subject_name}.csv', index=True)