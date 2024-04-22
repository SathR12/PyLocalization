import cv2 as cv
import numpy as np
import math
import pupil_apriltags
import pose2d
import constants
import odometry
from pupil_apriltags import Detector
from constants import Constants
from pose2d import Pose2d
from odometry import Field

#DirectShow framework developed by Microsoft for managing media streams on Windows platforms.
camera = cv.VideoCapture(Constants.CameraConstants.SOURCE, cv.CAP_DSHOW) 
camera.set(cv.CAP_PROP_FRAME_WIDTH, Constants.CameraConstants.WIDTH)
camera.set(cv.CAP_PROP_FRAME_HEIGHT, Constants.CameraConstants.HEIGHT)

#check if supports manual camera exposure control
assert cv.CAP_PROP_EXPOSURE > 0

#initialize apriltag detector
detector = Detector(families = Constants.AprilTagConstants.FAMILY)

#pose initialization 
pose = Pose2d(0, 0, 0)

#set field
field = Field()
field.setFieldImage(Constants.FieldConfig.FIELD_IMG)

if not camera.isOpened():
    #throw error msg and terminate program 
    print("camera is unable to be opened")
    exit()

def detectTags(frame, grayscale):
    detected = detector.detect(
        img = grayscale,
        estimate_tag_pose = True,
        camera_params = ([
            Constants.CameraConstants.FX,     
            Constants.CameraConstants.FY,
            Constants.CameraConstants.CX,
            Constants.CameraConstants.CY
        ]),
        tag_size = Constants.AprilTagConstants.APRILTAG_SIZE
    )
    
    for result in detected:
        #coordinates of tl and br
        A, B, C, D = result.corners
        A = (int(A[0]), int(A[1]))
        B = (int(B[0]), int(B[1]))
        C = (int(C[0]), int(C[1]))
        D = (int(D[0]), int(D[1]))
        
        cv.line(frame, A, B, (0, 255, 0), 2)
        cv.line(frame, B, C, (0, 255, 0), 2)
        cv.line(frame, C, D, (0, 255, 0), 2)
        cv.line(frame, D, A, (0, 255, 0), 2)
            
        #extract pose data
        #print(result.pose_R)
        pose.updateX(result.pose_t[0][0])
        pose.updateY(result.pose_t[2][0])
        pose.updateRotation(result.pose_R[2][0]) #TO DO: radians only
        #print(pose.__str__())
     
        if (result.tag_id in Constants.AprilTagMapConstants.LOCATION.keys()):
            world_pose = pose.getWorldCoordinates(Constants.AprilTagMapConstants.LOCATION[result.tag_id])
            field.setRobotPose(world_pose.getX(), world_pose.getY(), math.degrees(world_pose.getRotation()))
            #print("world", world_pose.__str__())
            
   
while True:
    #ret boolean whether there is a frame return 
    ret, frame = camera.read()
    grayscale = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    if not ret:
        print("frame was not received")
        break
    
    key = cv.waitKey(1) #waits for key press and stores ASCII value 
    if key == ord("q"):
        break
    
    detectTags(frame, grayscale)
    cv.imshow("Frame", frame)

#free up system resources
camera.release() 
cv.destroyAllWindows()
field.showField()
        
    