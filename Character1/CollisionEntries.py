from imports1 import *
class CollisionHandling():
    def __init__(self):
        self.collisiontraversing=CollisionTraverser()
        self.collisionlist=CollisionHandlerQueue()
        taskMgr.doMethodLater(0.01,self.traverseloop,"TraverseLooping",appendTask=True)

    ###############################
    ###############################
    def traverseloop(self,task):
       self.collisiontraversing.traverse(render)
       try:
         for each in self.collisionlist.entries:
             fromnodepath=each.getFromNodePath()
             fromnodepath.getParent().setPos(fromnodepath.getParent(),each.getSurfacePoint(render)-each.getInteriorPoint(render))
             
       except Exception as exception:
             print(exception)
       
       return task.again

      ###############################
      ###############################
      
class CollisionNodePath():
    def __init__(self):
        self.node=CollisionNode("CollisionNode")
        self.collisionNodePath=render.attachNewNode(self.node)
        
    ###############################
    ###############################
