import cv2
import numpy as np
import os

input_path = r"E:\data\vasc"
output_path = r"E:\out\vasc"

os.makedirs(output_path, exist_ok=True)

image_files = [f for f in os.listdir(input_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

drawing = False
mask = None
prev_pt = None

def draw_circle(event, x, y, flags, param):
    global drawing, mask, prev_pt
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        prev_pt = (x, y)
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing and prev_pt is not None:
            cv2.line(mask, prev_pt, (x, y), (255, 255, 255), 5)
            prev_pt = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        prev_pt = None

for file_name in image_files:
    image_path = os.path.join(input_path, file_name)
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"error: {file_name}")
        continue

    mask = np.zeros_like(image)

    cv2.namedWindow("Draw Mask")
    cv2.setMouseCallback("Draw Mask", draw_circle)

    while True:
        display_image = cv2.addWeighted(image, 0.7, mask, 0.3, 0)
        cv2.imshow("Draw Mask", display_image)
        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            break

    cv2.destroyAllWindows()

    gray_mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    _, binary_mask = cv2.threshold(gray_mask, 1, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(binary_mask, contours, -1, 255, thickness=cv2.FILLED)

    mask_path = os.path.join(output_path, f"mask_{file_name}")
    cv2.imwrite(mask_path, binary_mask)

print("done")










