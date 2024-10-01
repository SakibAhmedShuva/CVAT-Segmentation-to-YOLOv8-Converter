import json
import os

# Load COCO annotations
coco_file = '/mnt/data/instances_default.json'  # Update with the correct path to your COCO JSON file
output_dir = './yolov8_annotations/'  # Directory to save YOLOv8 formatted annotations

os.makedirs(output_dir, exist_ok=True)

# Helper function to normalize coordinates
def normalize_bbox(bbox, img_width, img_height):
    return [coord / img_width if i % 2 == 0 else coord / img_height for i, coord in enumerate(bbox)]

# Parse the COCO file
with open(coco_file, 'r') as f:
    coco_data = json.load(f)

# Extract categories and their IDs
categories = {cat['id']: cat['name'] for cat in coco_data['categories']}

# Create YOLOv8 annotation for each image
for annotation in coco_data['annotations']:
    image_id = annotation['image_id']
    img_info = next(img for img in coco_data['images'] if img['id'] == image_id)
    img_width = img_info['width']
    img_height = img_info['height']
    img_filename = img_info['file_name']

    # Prepare YOLOv8 output
    output_filename = os.path.splitext(img_filename)[0] + '.txt'
    output_filepath = os.path.join(output_dir, output_filename)

    with open(output_filepath, 'a') as out_file:
        category_id = annotation['category_id']
        segmentation = annotation['segmentation'][0]  # Assuming this is a polygon segmentation

        # Normalize segmentation coordinates
        normalized_segmentation = normalize_bbox(segmentation, img_width, img_height)
        
        # Write to the YOLOv8 formatted file
        out_file.write(f"{category_id} " + " ".join(map(str, normalized_segmentation)) + "\n")

print(f"YOLOv8 annotations saved in {output_dir}")
