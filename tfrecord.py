#tfrecord file
import tensorflow as tf
tf.enable_eager_execution()

# to get the path of image and folder

import pathlib
import os

# 1. the path of folder

datadir = pathlib.Path(os.path.join(os.getcwd(), "disease_photos/"))

print(os.getcwd()) # /Users/eunsukkim/Desktop/tutorial1 + disease_photos/
print(datadir)

# 2. the each name of folder

label_names = sorted(item.name for item in datadir.glob("*/") if item.is_dir())
print(label_names)

# 3. each name of folder + number

label_to_index = dict((name, index) for index, name in enumerate(label_names))

print(label_to_index)

# 4. the path of image

all_image_paths = list(datadir.glob("*/*"))
print(all_image_paths)

all_image_paths = [str(path) for path in all_image_paths]
print(all_image_paths)

# 5. each image + number
all_image_labels = [label_to_index[pathlib.Path(path).parent.name] for path in all_image_paths]
print(all_image_labels)

image_ds = tf.data.Dataset.from_tensor_slices(all_image_paths).map(tf.read_file)
print(image_ds)

# save tfdata

tfrec = tf.data.experimental.TFRecordWriter("tfrecord.tfrecord")
tfrec.write(image_ds)




