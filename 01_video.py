import cv2

videoCapture = cv2.VideoCapture('./test_data/1.avi')
# 帧率
fps = videoCapture.get(cv2.CAP_PROP_FPS)
# 视频的宽度
width = videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)
# 视频的高度
height = videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)
size = (int(width),int(height))

# videoWriter 第一个参数是文件路径名，第二参数是视频编码，I420
# 对应的是H.263，第三个参数是帧率，第四个参数是每帧的宽高
videoWriter = cv2.VideoWriter('./test_data/1_output.avi',
    cv2.VideoWriter_fourcc('I','4','2','0'),fps,size)

success,frame = videoCapture.read()
while success:
    videoWriter.write(frame)
    success,frame = videoCapture.read()