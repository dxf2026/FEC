from deepface import DeepFace
import cv2
def checkFrame(path):
    face_analysis = DeepFace.analyze(img_path=path, actions=['emotion'])
    return(face_analysis[0]['emotion'])

# Program To Read video
# and Extract Frames

import cv2

# Function to extract frames
def FrameCapture():

	# Path to video file
	vidObj = cv2.VideoCapture("\\FileSaving\\test.mp4")

	# Used as counter variable
	count = 0

	# checks whether frames were extracted
	success = 1
    average = {'angry': 0, 'disgust': 0, 'fear': 0, 'happy': 0, 'sad': 0, 'suprise' : 0, 'neutral' : 0}
	while success:

		# vidObj object calls read
		# function extract frames
		success, image = vidObj.read()

		# Saves the frames with frame-count
		cv2.imwrite("\\FileSaving\\frame.jpg", image)

        temp = checkFrame("\\Frames\\frame.jpg")
        for key in temp.keys():
            average[key] += temp[key]

    r = {"neg" : (average['disgust']+average['angry']+average['fear'])/count, 'neu' : (average['suprise']+average['neutral'])/2, 'pos' : (average["happy"]/count)}
    return r
