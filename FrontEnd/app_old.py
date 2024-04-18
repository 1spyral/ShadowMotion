from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties, load_prc_file, LVecBase3f, DirectionalLight
from direct.task import Task
import math
from direct.actor.Actor import Actor
from math import pi, sin, cos

load_prc_file('Config.prc')

@DeprecationWarning
class App(ShowBase):

    def __init__(self, _cv_cam):
        ShowBase.__init__(self)

        self.cv_cam = _cv_cam

        light = DirectionalLight('light')
        light.setColor((0.6, 0.65, 0.8, 0.3))
        dlnp = render.attachNewNode(light)
        render.setLight(dlnp)

        self.player1 = Actor("assets/player.bam")
        self.player1.reparentTo(self.render)
        self.player1.setScale(1,1,1)
        #self.player1.setPos(0, 8, 0)

        self.player1_nodes = {
            "cb":self.player1.controlJoint(None, "modelRoot", "body"),
              "rs":self.player1.controlJoint(None, "modelRoot", "right shoulder"),
                "ru":self.player1.controlJoint(None, "modelRoot", "right upperarm"),
                  "rf":self.player1.controlJoint(None, "modelRoot", "right forearm"),
              "ls":self.player1.controlJoint(None, "modelRoot", "left shoulder") ,
                "lu":self.player1.controlJoint(None, "modelRoot", "left upperarm") ,
                  "lf":self.player1.controlJoint(None, "modelRoot", "left forearm"),
              "ch":self.player1.controlJoint(None, "modelRoot", "head"),
        }
        self.rig_joint_nodes = { # start, end
            "rf":("right elbow", "right fist"),
            "lf": ("left elbow", "left fist"),
            "ru": ("right shoulder", "right elbow"),
            "lu": ("left shoulder", "left elbow"),
            "ch": ("head start", "head end")
        }
        self.rig_joint_parents = {
            "rf": ("right elbow", self.player1_nodes["ru"]),
            "lf": ("left elbow", self.player1_nodes["lu"]),
            "ru": ("chest", self.player1_nodes["cb"]),
            "lu": ("chest", self.player1_nodes["cb"]),
            "ch": ("chest", self.player1_nodes["cb"]),
        }

        print(self.player1.listJoints())
        
        
        self.taskMgr.add(self.task, "update")


        self.boxes = {
            "right fist": Actor("assets/box.bam"),
            "left fist": Actor("assets/box.bam"),
            "right shoulder": Actor("assets/box.bam"),
            "left shoulder": Actor("assets/box.bam"),
            "right elbow": Actor("assets/box.bam"),
            "left elbow": Actor("assets/box.bam"),
            "chest": Actor("assets/box.bam")
        }
        for box in self.boxes.values():
            box.reparentTo(self.render)
            box.setScale(0.08, 0.08, 0.08)

    def task(self, task):

        cam_coords = self.cv_cam.update()

        self.update_boxes(cam_coords)
        for rig_part in self.rig_joint_nodes.keys():
            parts = self.rig_joint_nodes[rig_part]
            if ((parts[0] in cam_coords.keys() and parts[1] in cam_coords.keys())):
                self.update_part(cam_coords, rig_part)
        
        return Task.cont

    def update_part(self, coords, part):
        
        prev = coords[self.rig_joint_parents[part][0]]
        start = coords[self.rig_joint_nodes[part][0]]
        end  =  coords[self.rig_joint_nodes[part][1]]
        #diff = LVecBase3f(end[0] - start[0], end[2] - start[2], -(end[1] - start[1]))
        pos = LVecBase3f(prev[0] - start[0], prev[1] - start[1], (prev[2] -start[2]))
        #scale = LVecBase3f(diff.length(), diff.length(), diff.length())

        #self.player1_nodes[part].setHpr(diff)
        self.player1_nodes[part].setPos(pos)
        #self.player1_nodes[part].setPosHpr(pos, diff)
        #self.player1_nodes[part].setPosHprScale(pos, diff, scale)
    def update_boxes(self, coords):
        for key, value in coords.items():
            self.boxes[key].setPos(value[0], value[2], -value[1])




#C:\Users\user\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\Scripts\blend2bam "C:\Users\user\Documents\Coding\projects hackathon\SecretPandaProject\FrontEnd\assets\untitled.blend" "C:\Users\user\Documents\Coding\projects hackathon\SecretPandaProject\FrontEnd\assets\untitled.bam" --blender-dir "C:\Program Files\Blender Foundation\Blender 3.6"