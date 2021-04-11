#功能：对视频文件进行剪切。
#剪切指定长度的视频，选择要裁剪的视频，选择开始时间点和停止时间点即可。
#将处理后的视频保存为output.avi文件
import cv2   #OpenCV
import tkinter.filedialog #Python文件对话框
import numpy
# CONFIG
INTERVAL = 2.5
filename = 'video/vid.avi'

cap = cv2.VideoCapture(filename)  #打开视频文件
frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)  #获得视频文件的帧数
fps = cap.get(cv2.CAP_PROP_FPS)  #获得视频文件的帧率
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  #获得视频文件的帧宽
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  #获得视频文件的帧高
video_length = frames/fps  #计算视频长度/s

# TODO: 将每个视频切分成INTERVALs每秒的短视频，命名为：vid($i)_clip($j)
# 其中，i为视频的索引，j为每个视频中短视频的索引

for idx, start in enumerate(numpy.arange(0.0, video_length, INTERVAL)):
    stop = start + INTERVAL
    #创建保存视频文件类对象
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output/output_' + str(idx) +'.avi',fourcc, fps, (int(width),int(height)))

    #设置帧读取的开始位置
    cap.set( cv2.CAP_PROP_POS_FRAMES,start*fps)
    pos = cap.get(cv2.CAP_PROP_POS_FRAMES)#获得帧位置
    while( pos <= stop*fps ):
        ret,frame = cap.read()#捕获一帧图像
        out.write(frame)#保存帧
        pos = cap.get(cv2.CAP_PROP_POS_FRAMES)

cap.release()
out.release()
