  # QR_Code detector
  Detects QR COde using Raspbian Pi model 3 B, PiCamera NOIR v2 
  with openCV 3.3 in real-time (streaming).

  HW : 
  * Raspberry Pi 3 model b 
  * piCamera NOIR v2 
  * x4 zoom cellphone lens ( for detecting ~3m range) * not necessary
       
  SW & Library used: 
  * pyhton v3.5
  * numpy
  * PIL
  * imutil (Thanks to https://www.pyimagesearch.com/ by Adrian Rosebrock)
  * OpenCV v3.3.0
  * zbarlight
                     
  # To Run
  ~$ python3 detect_barcode2.py -pc 1   (for piCamera)
  ~$ python3 detect_barcode2.py         (for webcam)
  
  # To change Resolution and frame rate
  ~$ sudo nano /usr/local/lib/python3.5/dist-packages/imutils/video/videostream.py
  
  #720p60(1280, 720)  1080p30(1920, 1200) 640x480p90
  
  from .webcamvideostream import WebcamVideoStream
  class VideoStream:
        def __init__(self, src=0, usePiCamera=False, resolution=(640,480),
                framerate=90):

  # TODO
  * Optimize for faster FPS
  * Detect smaller QR code from 3m away
  * Apply deep learning for distorted, folded QR codes
