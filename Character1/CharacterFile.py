from imports1 import *
import imports1
import CharacterFile
import CollisionEntries
class Character1():
    def __init__(self,collisiontraverse):
        self.modelpath="models/jack.obj"
        self.eventsaccept=DirectObject.DirectObject()
        self.model=loader.loadModel(self.modelpath)
        self.model.reparentTo(render)
        self.collisionNodePath=CollisionEntries.CollisionNodePath()
        self.collisionNodePath=[self.collisionNodePath.collisionNodePath,self.collisionNodePath.node]
###############################################        

        
        self.collisionShape=CollisionBox(*self.model.getTightBounds())

        self.collisionNodePath[1].addSolid(self.collisionShape)
        print(self.collisionNodePath[1])
        collisiontraverse.collisiontraversing.addCollider(self.collisionNodePath[0],collisiontraverse.collisionlist)
        self.collisionNodePath[0].reparentTo(self.model)
###############################################     


        
        self.eventsaccept.accept("a",self.moveleft,extraArgs=[1])
        self.eventsaccept.accept("d",self.moveright,extraArgs=[1])
        self.eventsaccept.accept("w",self.moveforward,extraArgs=[1])
        self.eventsaccept.accept("s",self.moveback,extraArgs=[1])
        self.eventsaccept.accept("space",self.jump,extraArgs=[3])
        taskMgr.doMethodLater(0.1,self.jumptime,"Jumptime",appendTask=True)
        
###############################################
###############################################
###############################################
###############################################

    ###############################
    ###############################
    def jumptime(self,task):
        try:
            distance=(self.model.getZ()-imports1.floor1.getZ())
            if distance>=0:
                self.model.setZ(self.model.getZ()-0.1)
            if distance<0:
                self.model.setZ(self.model.getZ()+0.1)
            print(dposition)
        except:
            pass
        return task.again
    
    ###############################
    ###############################

    def jump(self,movementspeed):
        self.relativePos(self.model,(0,0,1),movementspeed)

    ###############################
    ###############################    
    def moveleft(self,movementspeed):
        self.relativePos(self.model,(-1,0,0),movementspeed)

    ###############################
    ###############################
    def moveright(self,movementspeed):
        self.relativePos(self.model,(1,0,0),movementspeed)

    ###############################
    ###############################
    def moveback(self,movementspeed):
        self.relativePos(self.model,(0,-1,0),movementspeed)

    ###############################
    ###############################
    def moveforward(self,movementspeed):
        self.relativePos(self.model,(0,1,0),movementspeed)

    ###############################
    ###############################
    def relativePos(self,model,movedirection,relativemovement):
        model.setPos(model,movedirection[0]*relativemovement,movedirection[1]*relativemovement,movedirection[2]*relativemovement)
        
    ###############################
    ###############################
