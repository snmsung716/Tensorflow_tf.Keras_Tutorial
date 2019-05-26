# pickle file

# npy file
import pickle
# to get the path of image and folder

import pathlib
import os
import cv2
# 1. the path of folder

datadir = "/disease_photos"
datadir = os.path.join(os.getcwd() + datadir)
print(datadir)

categories = ["arm", "foot", "hand"]
training_data=[]
for categories_revised in categories:
	label_names = os.path.join(datadir, categories_revised)
	print(label_names)

	# each nmae of folder + number
	label_to_index = categories.index(categories_revised)
	print(label_to_index)

	for image in os.listdir(label_names):
		print(image)

		image_array = cv2.imread(os.path.join(label_names, image), cv2.IMREAD_COLOR)
		print(image_array)
		training_data.append([image_array, label_to_index])
print(len(training_data))

# save pickle file

pickle_out = open("pickle.pickle", "wb")
pickle.dump(training_data, pickle_out)
pickle_out.close()

