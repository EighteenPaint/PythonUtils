import cv2
import time
import dlib
from threading import Timer

srcHash = ''
def has_face(frame,):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    rects = detector(gray, 1)
    if(len(rects) > 0) :
        return True
    return False
def capture(frame, time):
    if(has_face(frame)):
        print u'face detector successfull save image'
        if(is_not_duplicate(frame)):
            res = cv2.resize(frame, (480, 480), interpolation=cv2.INTER_AREA)
            cv2.imwrite(str(time) + '.jpg', res)
def face_dector_test(filename):
    image = cv2.imread("test.jpg")
    print image
    has_face(image)
def is_not_duplicate(target):
    target_hash = dHash(target)
    global srcHash
    if srcHash is '':
         srcHash = target_hash
         return True
    else:
        if(cmpHash(srcHash,target_hash) > 5):
            srcHash = target_hash;
            return True
    return False

def aHash(img):
    img = cv2.resize(img, (8, 8), interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    s = 0
    hash_str = ''
    for i in range(8):
        for j in range(8):
            s = s + gray[i, j]
    avg = s / 64
    for i in range(8):
        for j in range(8):
            if gray[i, j] > avg:
                hash_str = hash_str + '1'
            else:
                hash_str = hash_str + '0'
    return hash_str


def dHash(img):
    img = cv2.resize(img, (9, 8), interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hash_str = ''
    for i in range(8):
        for j in range(8):
            if gray[i, j] > gray[i, j + 1]:
                hash_str = hash_str + '1'
            else:
                hash_str = hash_str + '0'
    return hash_str


def cmpHash(hash1, hash2):
    n = 0
    if len(hash1) != len(hash2):
        return -1
    for i in range(len(hash1)):
        if hash1[i] != hash2[i]:
            n = n + 1
    return n
if __name__ == '__main__':
    rtsp = "rtsp://192.168.31.8:554/0000000000200000000000000530003:0000000000140000000000000500003:192.168.31.8:420000/MainStream"
    cap = cv2.VideoCapture(rtsp)
    ret = cap.read()
    while ret:
        frame = cap.read()
        # frame is a tuple,so use frame[1]
        Timer(0.04, capture(frame[1], time.time()))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    cap.release()
    # src = cv2.imread("1538038685.69.jpg")
    # target = cv2.imread("test.jpg")
    # is_not_duplicate(src,target)

