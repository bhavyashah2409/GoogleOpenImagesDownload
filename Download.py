import fiftyone as f

IMAGES = 1000
CLASSES = ["Boat"]
FOLDER = 'data'
dataset = f.zoo.load_zoo_dataset("open-images-v7", split="all", label_types=["detections"], classes=CLASSES, max_samples=IMAGES, dataset_dir=FOLDER)
print(dataset)
