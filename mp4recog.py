from deepface import DeepFace
import cv2
def checkFrame(path):
	face_analysis = DeepFace.analyze(img_path=path, actions=['emotion'])
	return(face_analysis[0]['emotion'])

# Function to extract frames
def FrameCapture():

	# Path to video file
	vidObj = cv2.VideoCapture("\\FileSaving\\test.mp4")
	totalFrames = vidObj.get(cv2.CAP_PROP_FRAME_COUNT)

	randomFrameNumber=random.randint(0, totalFrames)
	vidObj.set(cv2.CAP_PROP_POS_FRAMES,randomFrameNumber)
	success, image = vidObj.read()
	if success:
    		cv2.imwrite("\\FileSaving\\random_frame.jpg", image)
	
	return(checkFrame("\\FileSaving\\random_frame.jpg"))
