from imports1 import *
import imports1
import CharacterFile
from CollisionEntries import *
window=ShowBase()
collisiontraverse=CollisionHandling()
character1=CharacterFile.Character1(collisiontraverse)
imports1.floor1=loader.loadModel("models/Floor.egg")
imports1.floor1.reparentTo(render)
imports1.floor1.setCollideMask(BitMask32.allOn())
window.run()
