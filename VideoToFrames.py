import cv2,time
vidcap = cv2.VideoCapture("D:\SmartVideoRecorder\DEFAULT_20220408_151729.mp4")
success,image = vidcap.read()
count = 0
secs_gap =1
start_from_secs= 0
vidcap.set(cv2.CAP_PROP_POS_MSEC, start_from_secs * 1000)
while success:
  cv2.imwrite("E:\\PySnippets\\New folder\\frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  time.sleep(secs_gap)
  count += 1