# Importa as bibliotecas necessárias.
import cv2
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--foreground', required=False, type=str, help='Path of the foreground video', default='data/webcam.mp4')
parser.add_argument('-b', '--background', required=False, type=str, help='Path of the background video', default='data/praia.mp4')

args = vars(parser.parse_args())

# Loads both videos
cap_foreground = cv2.VideoCapture(args['foreground'])
cap_background = cv2.VideoCapture(args['background'])

# Collects metadata for saving the videos
# Foreground metadata
fps = cap_foreground.get(cv2.CAP_PROP_FPS)
fg_height = int(cap_foreground.get(cv2.CAP_PROP_FRAME_HEIGHT))
fg_width = int(cap_foreground.get(cv2.CAP_PROP_FRAME_WIDTH))

# Background metadata
bg_height = int(cap_background.get(cv2.CAP_PROP_FRAME_HEIGHT))
bg_width = int(cap_background.get(cv2.CAP_PROP_FRAME_WIDTH))

assert fg_height == bg_height, "The videos must have the same height"
assert fg_width == bg_width, 'The videos must have the same width'

# Defines the codec
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
foreground_output = cv2.VideoWriter('foreground_output.mp4', fourcc, fps, (fg_width, fg_height))
result_output = cv2.VideoWriter('final_output.mp4', fourcc, fps, (fg_width, fg_height))

while True:
    # Reads one frame from each video
    ret_foreground, frame_foreground = cap_foreground.read()
    ret_background, frame_background = cap_background.read()

    # Ends the loop if any of the videos end
    if not ret_foreground or not ret_background:
        break

    # Defines the green channel ranges to create the mask. We need this because the videos
    # do not have pure green values
    lower_green = np.array([0, 110, 0], dtype=np.uint8)
    upper_green = np.array([135, 255, 135], dtype=np.uint8)

    # Creates the mask for green elements
    '''cv2.inRange function is used to create a binary mask where pixels within a specified 
    range are set to white (255) and pixels outside the range are set to black (0).'''
    mask = cv2.inRange(frame_foreground, lower_green, upper_green)

    # Use the mask to collect the background image that correspond to the greenscreen 
    # in the foreground video
    background = cv2.bitwise_and(frame_background, frame_background, mask=mask)

    # Invert the mask to obtain the pixes outside the green range
    mask_inv = np.invert(mask)

    # Uses the inverted mask to remove the green background
    foreground = cv2.bitwise_and(frame_foreground, frame_foreground, mask=mask_inv)

    result = cv2.addWeighted(background, 1, foreground, 1, 0)

    # Save foreground video
    foreground_output.write(foreground)

    # Save final/result video
    result_output.write(result)

    cv2.imshow("Result", result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap_foreground.release()
cap_background.release()

foreground_output.release()
result_output.release()

cv2.destroyAllWindows()