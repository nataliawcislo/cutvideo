import cv2

cap = cv2.VideoCapture("video1.mp4")
success,image = cap.read()
fps = cap.get(cv2.CAP_PROP_FPS)      # OpenCV2 version 2 used "CV_CAP_PROP_FPS" liczba ramek na sek
print(fps)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) ## dlugosc filmu
print(frame_count)
duration = frame_count/fps
print(duration)
input = 3
count = 0
print(round(duration))

while success:
    if cv2.waitKey(round(duration)):
        count += 1
        cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
        success,image = cap.read()
        print('Read a new frame%d: ', success)


# print('fps = ' + str(fps))
# print('number of frames = ' + str(frame_count))
# print('duration (S) = ' + str(duration))
# minutes = int(duration/60)
# seconds = duration%60
# print('duration (M:S) = ' + str(minutes) + ':' + str(seconds))

cap.release()
