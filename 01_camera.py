import cv2

cameraCapture = cv2.VideoCapture()
# 帧率
fps = 30
# 宽度
width = cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)
# 高度
height = cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)
size = (int(width),int(height))

# videoWriter 第一个参数是文件路径名，第二参数是视频编码，I420
# 对应的是H.263，第三个参数是帧率，第四个参数是每帧的宽高
videoWriter = cv2.VideoWriter('./test_data/camera_output.avi',
    cv2.VideoWriter_fourcc('I','4','2','0'),fps,size)

success,frame = cameraCapture.read()
numFramesRemaining = 10 * fps -1
while success and numFramesRemaining > 0:
    videoWriter.write(frame)
    success,frame = cameraCapture.read()
    numFramesRemaining -=1
cameraCapture.release()