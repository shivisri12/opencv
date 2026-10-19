# Shape Detection Using OpenCV

## Overview
This project detects and identifies basic geometric shapes in an image using Python and OpenCV. It uses image processing techniques, contour detection, and polygon approximation to classify shapes such as triangles, squares, rectangles, pentagons, hexagons, and circles.

## Features
- Loads an input image for shape detection.
- Converts the image to grayscale.
- Applies binary thresholding to separate shapes from the background.
- Detects contours and filters them based on area.
- Identifies shapes based on the number of polygon vertices.
- Draws contours and labels detected shapes.
- Saves the processed image as `output1.png`.
- Provides a menu to view project details or run the shape detection program.

## Technologies Used
- **Python** — programming language
- **OpenCV (cv2)** — image processing and contour detection
- **NumPy** — used internally by OpenCV for image data handling

## Project Structure

```text
Shape-Detection/
├── shape_detection.py
├── shapedetection.txt
├── input1.png
├── output1.png
└── README.md
```

*Note: `output1.png` is generated when the program runs successfully.*

## How It Works
1. The program displays a main menu.
2. Select **1** to display project details from `shapedetection.txt`.
3. Select **2** to run shape detection on `input1.png`.
4. The image is converted to grayscale and thresholded.
5. Contours are detected and small contours with an area of 500 pixels or less are ignored.
6. Polygon approximation is used to estimate the number of vertices.
7. Shapes are classified based on their vertices and, for quadrilaterals, their aspect ratio.
8. The detected shapes are outlined and labeled, and the result is saved as `output1.png`.

## Shape Classification
| Number of vertices | Detected shape |
|---|---|
| 3 | Triangle |
| 4 | Square or Rectangle |
| 5 | Pentagon |
| 6 | Hexagon |
| Other | Circle (default classification) |

## Installation

Make sure Python is installed, then install OpenCV:

```bash
pip install opencv-python
```

## How to Run

1. Clone or download this repository.
2. Place your test image in the project folder and name it `input1.png`.
3. Ensure `shapedetection.txt` exists if you want to use the project-details menu option.
4. Run the Python script:

```bash
python shape_detection.py
```

5. Enter `2` to run the shape detector.
6. View the detected shapes in the display window and check the generated `output1.png` file.

## Output
The program displays the thresholded image and the processed image with detected shapes labeled. The processed result is saved as `output1.png`.

## Future Improvements
- Improve detection for rotated or irregular shapes.
- Handle different lighting conditions and background colors.
- Add support for webcam-based real-time shape detection.
- Improve circle detection using dedicated circle-detection techniques.

## Author
Shivi Srivastava
