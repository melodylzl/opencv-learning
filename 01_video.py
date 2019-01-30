import cv2

videoCapture = cv2.VideoCapture('./test_data/1.avi')
# 帧率
fps = videoCapture.get(cv2.CAP_PROP_FPS)
# 视频的宽度
width = videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)
# 视频的高度
height = videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)
size = (int(width),int(height))

# videoWriter 第一个参数是文件路径名，第二参数是视频编码,第三个参数是帧率，第四个参数是每帧的宽高
# cv2.VideoWriter_fourcc('I', '4'，'2', '0'):该选项是一个未压缩的 YUV 颜色编码， 是4: 2:0色度子采样。这种编码有很好的兼容性，但会产生较大文件，文件扩展名为.avi
# cv2.VideoWriter_fourcc('P', 'I'，'M', '1'):该选项是 MPEG-1 编码类型，文件扩展名为.avi
# cv2.VideoWriter_fourcc('X', 'V'，'I', 'D'):该选项是 MPEG-4 编码类型，如果希望得到的视频大小为平均值，推荐使用此选项，文件扩展名为.avi
# cv2.VideoWriter_fourcc('T', 'H'，'E', 'O'):该选项是 Ogg Vorbis,文件扩展名应为.ogv。
# cv2.VideoWritcr_fourcc('F', 'L'，'V', '1'):该选项是一个 Flash 视频，文件扩展名应为.flv。
videoWriter = cv2.VideoWriter('./test_data/1_output.avi',
    cv2.VideoWriter_fourcc('I','4','2','0'),fps,size)

success,frame = videoCapture.read()
while success:
    videoWriter.write(frame)
    success,frame = videoCapture.read()