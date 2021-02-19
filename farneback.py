import cv2
import numpy as np
# the video feed is reed in as
# a VideoCapture object
cap = cv2.VideoCapture("Cars On The Road.mp4")
# first frame in entire video sequence
ret, first_frame = cap.read()
# converts frame to grayscale
# because detecting edges with less computationally expensive
prev_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
# Creates an image filled with zero
# intensities with the same dimensions
# as  the frame (first_frame)
mask = np.zeros_like(first_frame)
# Get the Default resolutions
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter('output2.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
while (cap.isOpened()):
    ret, frame = cap.read()
    # Opens a new window and displays the input frame
    cv2.imshow("input", frame)
    # converts each frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Calculates dense optical flow by farneback method
    flow = cv2.calcOpticalFlowFarneback(prev_gray, gray,
                                        None,
                                        0.5, 3, 15, 3, 5, 1.2, 0)
    # Computes the magnitude and angle of the 2D vectors
    magnitude, angle = cv2.cartToPolar(flow[..., 0], flow[..., 1])
    # Sets image hue according to the optical flow direction
    mask[..., 0] = angle * 180 / np.pi / 2
    # Sets image value according to the optical flow
    # magnitude (normalized)
    mask[..., 2] = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)

    # Converts HSV to RGB (BGR) color representation
    rgb = cv2.cvtColor(mask, cv2.COLOR_HSV2BGR)
    # Opens a new window and displays the output frame
    cv2.imshow("dense optical flow", rgb)
    # write the  frame
    out.write(rgb)
    # Updates previous frame
    prev_gray = gray

    # Frames are read by intervals of 1 millisecond.
    # The programs breaks out of the while loop when the
    # user presses the 'q' key
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
# The following frees up resources and
# closes all windows
cap.release()
out.release()
cv2.destroyAllWindows()