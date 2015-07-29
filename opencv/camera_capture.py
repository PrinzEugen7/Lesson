# -*- coding: utf-8 -*-
import cv2

def main():

    cap = cv2.VideoCapture(0)
    while(1):
        ret, im = cap.read()
        cv2.imshow("Camera Test",im)

        if cv2.waitKey(10) > 0:
            cap.release()
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    main()
