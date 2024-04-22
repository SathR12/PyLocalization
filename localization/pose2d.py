class Pose2d:
    def __init__(self, x, y, rotation):
        self.x = x
        self.y = y
        self.rotation = rotation
    
    #TO DO: fix this 
    def relativeTo(self, pose):
        relativeX = self.x - pose.getX()
        relativeY = self.y - pose.getY()
        return Pose2d(relativeX, relativeY, self.rotation)

    def getWorldCoordinates(self, tag_pose):
        return Pose2d(self.x + tag_pose.getX(), self.y + tag_pose.getY(), self.rotation)
        
    def updateX(self, x):
        self.x = x
    
    def updateY(self, y):
        self.y = y
    
    def updateRotation(self, rotation):
        self.rotation = rotation
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getRotation(self):
        return self.rotation
    
    def __str__(self):
        return ("x:", self.x, "y:", self.y, "rotation:", self.rotation)
       
    