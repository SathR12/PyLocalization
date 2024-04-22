#field gui
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.transforms as transforms
import numpy as np
import constants
from constants import Constants

class Field:
    def __init__(self):
        plt.figure().set_size_inches(15, 8)
        ax = plt.gca()
        ax.axis("off")


    def setFieldImage(self, path):
        img = mpimg.imread(path)
        #does not resize image automatically
        plt.imshow(
            img,
            extent = [
                Constants.FieldConfig.XMIN,
                Constants.FieldConfig.XMAX,
                Constants.FieldConfig.YMIN,
                Constants.FieldConfig.YMAX
            ],
            aspect = "auto"
        )
    

    def setRobotPose(self, x, y, rotation):
        #clear past point
        #plt.cla()
        #self.setFieldImage(Constants.FieldConfig.FIELD_IMG)
        #defining the rotational origin
        robot_point = plt.plot(
                 x,
                 y,
                 marker = (3, 0, Constants.FieldConfig.INITIAL_HEADING + rotation),
                 markersize = 25,
                 linestyle = "None",
                 color = "lime"
        )[0]
                    
        
        plt.draw()
        plt.pause(0.01)
        robot_point.remove()
        

    def showField(self):
        plt.show()

#plt.plot(2, 2, "o")