# Offline-Image-Segmentation-Tool
This is a Python script that allows you to perform offline image segmentation. The user can manually draw masks on images, and the script automatically saves the selected areas as binary masks.

# Features:
Fully offline processing
Manually draw masks on images
Supports common image formats (JPG, PNG, JPEG)
Automatically saves drawn masks
Easy to use and fast

# Usage:
In the mask.py file, set the paths for the input images and the output directory where the masks will be saved.
Execute the script using the following command:
python mask.py

# Drawing Instructions:
Left-click and drag the mouse to draw a mask on the image.
Make sure to draw a closed boundary around the object you want to segment. The closed contour helps the tool to detect the area accurately.
You can draw multiple strokes until the boundary is complete.

# Save and Move to Next Image:
Once you've drawn the closed boundary, press the ESC key.
The script will automatically process the mask and save it as a binary image in the output directory.
It will then load the next image for segmentation.

# Output:
All the saved masks will be stored in the output folder with filenames prefixed by mask_.
Each mask highlights the segmented area in white (255) on a black (0) background.
