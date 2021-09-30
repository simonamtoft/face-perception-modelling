import numpy as np
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
indicies = np.arange(n)
scores = np.zeros((10, n))
for i in range(10):
    # Go through all the images in random order
    np.random.shuffle(indicies)
    for idx in indicies:
        # display image
        images[idx].show()

        # get score from subject
        print("Enter score (1-5): ")
        scores[i, idx] = int(input())

# store the results
np.savetxt(f'./results/scoring_{subject_name}.txt', scores, delimiter=',')