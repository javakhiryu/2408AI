import cv2
import matplotlib.pyplot as plt
# Load image, grayscale, and adaptive threshold

image = cv2.imread('live.png')
image = cv2.resize(image,(370,370))
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
1


i = image[123:150,124:154]
cv2.imshow("myimage",i)
plt.imshow(i)
cv2.imwrite("./data/8.png",i)
cv2.waitKey()
plt.show()
#import cv2
#import matplotlib.pyplot as plt
#import os
#
## Define input and output directories
#input_dir = "./raw_data"
#output_dir = "./data"
#
## Ensure the output directory exists
#os.makedirs(output_dir, exist_ok=True)
#
## List of raw file names
#file_names = ['raw_live.png'] #'raw_2048.png', 'raw_4.png', 'raw_8.png', 'raw_16.png', 'raw_32.png', 'raw_64.png', 'raw_128.png', 'raw_256.png', 'raw_512.png', 'raw_1024.png', 'raw_end.png', 'raw_lostConnection.png'
#
## Process each file
#for file_name in file_names:
#    # Construct full file path
#    input_path = os.path.join(input_dir, file_name)
#    
#    # Read image
#    image = cv2.imread(input_path)
#    
#    # Convert to grayscale
#    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#    
#    # Construct output file name without 'raw_'
#    output_file_name = file_name.replace('raw_', '')
#    output_path = os.path.join(output_dir, output_file_name)
#    
#    # Save the processed image
#    cv2.imwrite(output_path, gray_image)
#    
#    # Display the image using matplotlib
#    plt.imshow(gray_image, cmap='gray')
#    plt.title(f'Processed {output_file_name}')
#    plt.show()
#
#    # Optionally, if you want to display the image using OpenCV
#    cv2.imshow("Processed Image", gray_image)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()
