from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties, load_prc_file, LVecBase3f
from direct.task import Task
import math
from direct.actor.Actor import Actor
from math import pi, sin, cos

load_prc_file('Config.prc')

class App(ShowBase):

    def __init__(self, _cv_cam):
        ShowBase.__init__(self)

        self.cv_cam = _cv_cam

        self.player1 = Actor("assets/untitled.bam")
        self.player1.reparentTo(self.render)
        self.player1.setScale(1,1,1)
        self.player1.setPos(0, 8, 0)

        self.player1_nodes = {
            "rf":self.player1.controlJoint(None, "modelRoot", "right forearm"),
            "lf":self.player1.controlJoint(None, "modelRoot", "forearm"), # i forgot a left
            "ru":self.player1.controlJoint(None, "modelRoot", "right upperarm"),
            "lu":self.player1.controlJoint(None, "modelRoot", "left upperarm") ,
            "ch":self.player1.controlJoint(None, "modelRoot", "head"),
            "cb":self.player1.controlJoint(None, "modelRoot", "body"),
        }
        self.rig_joint_nodes = { # start, end
            "rf":("right elbow", "right fist"),
            "lf": ("left elbow", "left fist"),
            "ru": ("right shoulder", "right elbow"),
            "lu": ("left shoulder", "left elbow"),
            "ch": ("head start", "head end")
        }

        print(self.player1.listJoints())
        
        
        self.taskMgr.add(self.task, "update")

    def task(self, task):
        #print("A")

        cam_coords = self.cv_cam.update()

        for rig_part in self.rig_joint_nodes.keys():
            update_part(cam_coords, rig_part)
        
        return Task.cont

    def updatePart(self, coords, part):
        start = coords[self.rig_joint_nodes[part][0]]
        end  =  coords[self.rig_joint_nodes[part][1]]
        diff = LVecBase3f(end[0] - start[0], end[1] - start[1], end[2] - start[2])
        pos = LVecBase3f(start[0], start[1], start[2])
        scale = LVecBase3f()



#C:\Users\user\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\Scripts\blend2bam "C:\Users\user\Documents\Coding\projects hackathon\SecretPandaProject\FrontEnd\assets\untitled.blend" "C:\Users\user\Documents\Coding\projects hackathon\SecretPandaProject\FrontEnd\assets\untitled.bam" --blender-dir "C:\Program Files\Blender Foundation\Blender 3.6"