# CVAT Segmentation to YOLOv8 Converter

A Python script that converts CVAT polygons / segmentation data / annotations in COCO JSON format to YOLOv8 compatible format for object detection and segmentation tasks.

## Features

- Converts COCO JSON format to YOLOv8 annotation format
- Handles polygon segmentation data
- Normalizes coordinates according to YOLOv8 requirements
- Preserves category IDs and mappings
- Processes multiple images and annotations

## Prerequisites

- Python 3.6 or higher
- Access to CVAT-exported annotations in COCO JSON format

## Installation

Clone this repository:

```bash
git clone https://github.com/SakibAhmedShuva/cvat-yolov8-converter.git
cd cvat-yolov8-converter
```

## Usage

1. Update the `coco_file` path in the script to point to your COCO JSON file:

```python
coco_file = '/path/to/your/instances_default.json'
```

2. Run the script:

```bash
python cvat_to_yolov8.py
```

The script will:
- Create a directory named `yolov8_annotations` (if it doesn't exist)
- Process each annotation in the COCO JSON file
- Generate corresponding YOLOv8 format text files for each image

## Output Format

For each image in the COCO dataset, the script creates a text file with the same name as the image (but with .txt extension) containing the annotations in YOLOv8 format:

```
<category_id> <x1> <y1> <x2> <y2> ... <xn> <yn>
```

Where:
- `category_id` is the class ID
- `x1, y1, x2, y2, ..., xn, yn` are normalized polygon coordinates

## Example

Input (COCO format):
```json
{
  "images": [{"id": 1, "width": 800, "height": 600, "file_name": "image1.jpg"}],
  "annotations": [
    {
      "image_id": 1,
      "category_id": 0,
      "segmentation": [[100, 100, 200, 100, 200, 200, 100, 200]]
    }
  ]
}
```

Output (YOLOv8 format in image1.txt):
```
0 0.125 0.166667 0.25 0.166667 0.25 0.333333 0.125 0.333333
```

## Limitations

- Currently only supports polygon segmentation
- Assumes one segmentation per annotation
- Does not handle complex, nested polygons

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Your Name - [@yourusername](https://twitter.com/yourusername)

Project Link: [https://github.com/SakibAhmedShuva/CVAT-Segmentation-to-YOLOv8-Converter](https://github.com/SakibAhmedShuva/CVAT-Segmentation-to-YOLOv8-Converter)
