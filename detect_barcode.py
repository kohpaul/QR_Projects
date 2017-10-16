# import the necessary packages
from imutils.video import VideoStream
import imutils
import simple_barcode_detection
import argparse
import time
import cv2


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help = "path to the (optional) video file")
ap.add_argument("-pc", "--picamera", type=int, default=-1,
        help="whether or not the Raspberry Pi camera should be used")

args = vars(ap.parse_args())

## if the video path was not supplied, grab the reference to the
## camera
#if not args.get("video", False):
#	camera = cv2.VideoCapture(0)

## otherwise, load the video
#else:
#	camera = cv2.VideoCapture(args["video"])

# initialize the video stream and allow the cammera sensor to warmup
camera = VideoStream(usePiCamera=args["picamera"] > 0).start()
time.sleep(2.0)


# keep looping over the frames
while True:
	# grab the current frame
#	(grabbed, frame, hierarchy) = camera.read()
	frame = camera.read()
	frame = imutils.resize(frame, width=400)

#	# check to see if we have reached the end of the
#	# video
#	if not grabbed:
#		break

	# detect the barcode in the image
	box = simple_barcode_detection.detect(frame)

	# if a barcode was found, draw a bounding box on the frame
	cv2.drawContours(frame, [box], -1, (0, 255, 0), 2)

	# show the frame and record if the user presses a key
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break

# cleanup the camera and close any open windows
# camera.release()
camera.stop()
cv2.destroyAllWindows()
