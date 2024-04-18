from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties, load_prc_file
from direct.task import Task
import math
from direct.actor.Actor import Actor
from math import pi, sin, cos

load_prc_file('config.prc')

class MyApp(ShowBase):

    def __init__(self, _cv_cam):
        ShowBase.__init__(self)

        self.cv_cam = _cv_cam

        self.player1 = self.loader.loadModel("assets/untitled.bam")
        self.player1.reparentTo(self.render)
        self.player1.setScale(1,1,1)
        self.player1.setPos(0, 8, 0)

        self.taskMgr.add(self.task, "update")

    def task(self, task):
        
        return Task.cont



print("A")
#C:\Users\user\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\Scripts\blend2bam "C:\Users\user\Documents\Coding\projects hackathon\SecretPandaProject\FrontEnd\assets\untitled.blend" "C:\Users\user\Documents\Coding\projects hackathon\SecretPandaProject\FrontEnd\assets\untitled.bam" --blender-dir "C:\Program Files\Blender Foundation\Blender 3.6"