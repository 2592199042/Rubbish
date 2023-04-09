import os
import random
import shutil

# Define paths to image and label directories
image_dir = "D:\bishe\rubbishdata\images\train"
label_dir = "D:\bishe\rubbishdata\images\train"

# Define path to output directory
output_dir = "D:/garbage_classification"

# Define train, validation, and test set ratios
train_ratio = 0.8
val_ratio = 0.1
test_ratio = 0.1

# Define the number of categories
num_categories = 44

# Create directories for train, validation, and test sets
for category in range(1, num_categories+1):
    os.makedirs(os.path.join(output_dir, "train", str(category)), exist_ok=True)
    os.makedirs(os.path.join(output_dir, "val", str(category)), exist_ok=True)
    os.makedirs(os.path.join(output_dir, "test", str(category)), exist_ok=True)

# Loop through each label file and split images into train, validation, and test sets
for label_file in os.listdir(label_dir):
    with open(os.path.join(label_dir, label_file), "r") as f:
        lines = f.readlines()
        for line in lines:
            # Extract the category information from the label file
            category = line.strip().split()[0]

            # Calculate a random number to determine which set to put the image in
            rand_num = random.random()

            # Copy image and label files to train directory
            if rand_num < train_ratio:
                shutil.copy(os.path.join(image_dir, label_file.replace(".txt", ".jpg")), os.path.join(output_dir, "train", category, label_file.replace(".txt", ".jpg")))
                shutil.copy(os.path.join(label_dir, label_file), os.path.join(output_dir, "train", category, label_file))

            # Copy image and label files to validation directory
            elif rand_num < train_ratio + val_ratio:
                shutil.copy(os.path.join(image_dir, label_file.replace(".txt", ".jpg")), os.path.join(output_dir, "val", category, label_file.replace(".txt", ".jpg")))
                shutil.copy(os.path.join(label_dir, label_file), os.path.join(output_dir, "val", category, label_file))

            # Copy image and label files to test directory
            else:
                shutil.copy(os.path.join(image_dir, label_file.replace(".txt", ".jpg")), os.path.join(output_dir, "test", category, label_file.replace(".txt", ".jpg")))
                shutil.copy(os.path.join(label_dir, label_file), os.path.join(output_dir, "test", category, label_file))