import cv2  
import mediapipe as mp
import pyautogui

hand_detector =mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_w, screen_h = pyautogui.size()
pyautogui.FAILSAFE = False
index_y=0
mid_y=0


cap= cv2.VideoCapture(0)
while cap.isOpened():
    _, frame = cap.read()
    frame= cv2.flip(frame,1)
    frame_h, frame_w , frame_d =frame.shape
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmarks in enumerate(landmarks):
                x= int(landmarks.x * frame_w)
                y= int(landmarks.y * frame_h)



                
                if id == 8:
                    cv2.circle(img= frame,center = (x,y) , radius = 10 , color=(0,255,255))
                    index_x = (screen_w/frame_w )* x
                    index_y = (screen_h/ frame_h )* y
                    pyautogui.moveTo(index_x,index_y)


                if id == 5:
                    cv2.circle(img= frame,center = (x,y) , radius = 10 , color=(0,150,255))
                    mid_x = (screen_w/frame_w) * x
                    mid_y = (screen_h/ frame_h )* y
                    
                    
                if id == 4:
                    cv2.circle(img= frame,center = (x,y) , radius = 10 , color=(0,150,255))

                    thumb_x = (screen_w/frame_w) * x
                    thumb_y = (screen_h/ frame_h) * y
                    
                    if (mid_y - thumb_y)>=0 and (mid_y - thumb_y)<=10:
                        
                        pyautogui.leftClick()
                        

    cv2.imshow ('Virtual Mouse',frame)
    if cv2.waitKey(10) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

