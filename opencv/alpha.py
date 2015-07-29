# -*- coding: utf-8 -*-
import cv2

def main():
    im = cv2.imread("test.png",cv2.IMREAD_UNCHANGED)
    cv2.imshow("show", im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
