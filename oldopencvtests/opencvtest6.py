import numpy as np
import cv2



if __name__ == "__main__":
    # find the webcam
    
    capture = cv2.VideoCapture(0)

    w=int(capture.get(cv2.CV_CAP_PROP_FRAME_WIDTH ))
    h=int(capture.get(cv2.CV_CAP_PROP_FRAME_HEIGHT ))
    # video recorder
    fourcc = cv2.cv.CV_FOURCC(*'XVID')  # cv2.VideoWriter_fourcc() does not exist
    video_writer = cv2.VideoWriter("output.avi", fourcc, 25, (w, h))
    # video recorder
    #fourcc = cv2.cv.CV_FOURCC(*'XVID')  # cv2.VideoWriter_fourcc() does not exist
    #video_writer = cv2.VideoWriter("output.avi", fourcc, 20, (680, 480))

    # record video
    while (capture.isOpened()):
        ret, frame = capture.read()
        if ret:
            video_writer.write(frame)
            cv2.imshow('Video Stream', frame)

        else:
            break

    capture.release()
    video_writer.release()
    cv2.destroyAllWindows()