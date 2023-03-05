from deepface import DeepFace
import cv2
def checkFrame(path):
    face_analysis = DeepFace.analyze(img_path=path, actions=['emotion'])
    return(face_analysis[0]['emotion'])

def checkFrames(mp4):
    vidcap = cv2.VideoCapture('\\FileSaving\\test.mp4')
    success, image = vidcap.read()
    count = 0
    success = True
    while success:
        success, image = vidcap.read()
        cv2.imwrite("\\Frames\\frame"+ str(count), image)  # save frame as JPEG file
        if cv2.waitKey(10) == 27:  # exit if Escape is hit
            break
        count += 1

    average = {'angry': 0, 'disgust': 0, 'fear': 0, 'happy': 0, 'sad': 0, 'suprise' : 0, 'neutral' : 0}
    for i in range(count-1):
        temp = checkFrame("\\Frames\\frame" + str(i))
        for key in temp.keys():
            average[key] += temp[key]

    r = {"neg" : (average['disgust']+average['angry']+average['fear'])/count, 'neu' : (average['suprise']+average['neutral'])/2, 'pos' : (average["happy"]/count)}
    return r

