import math
import pose2d
from pose2d import Pose2d

#constants class
class Constants:
    class CameraConstants:
        SOURCE = 0
        WIDTH = 640
        HEIGHT = 480
        EXPOSURE = -6
        FX = 548.83474762
        FY = 550.99717907
        CX = 296.87065692
        CY = 275.41895032
        
    class AprilTagConstants:
        FAMILY = "tag36h11"
        TAG_IDS = [i for i in range(1, 15)]
        APRILTAG_SIZE = .5 #has to be in meters
        
    class AprilTagMapConstants:
        LOCATION = {
            1: Pose2d(14.06, 0.52, 0),
            2: Pose2d(4, 5, 0)
        }
        
    class FieldConfig:
        XMIN = 0
        XMAX = 16
        YMIN = 0
        YMAX = 8
        INITIAL_HEADING = 270
        FIELD_IMG = r"C:\Users\laks\Desktop\localization\config\2024-field.png"
        
