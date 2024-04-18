from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties, load_prc_file, LVecBase3f,LVector3f, DirectionalLight, look_at, Quat
from direct.task import Task
import math
from direct.actor.Actor import Actor
from math import atan2, pi

from client import Client

load_prc_file('Config.prc')
up_vector = LVecBase3f(0, 0, 1)

class App(ShowBase):

    def __init__(self, _cv_cam, client):
        ShowBase.__init__(self)

        self.cv_cam = _cv_cam
        self.client = client

        light = DirectionalLight('light')
        light.setColor((0.6, 0.65, 0.8, 0.3))
        dlnp = render.attachNewNode(light)
        render.setLight(dlnp)

        self.player1_parts = {
            #"right fist": Actor("assets/box.bam"),
            #"left fist": Actor("assets/box.bam"),
            "right shoulder": Actor("assets/player/R_upperarm.bam"),
            "left shoulder": Actor("assets/player/L_upperarm.bam"),
            "right elbow": Actor("assets/player/R_forearm.bam"),
            "left elbow": Actor("assets/player/L_forearm.bam"),
            "chest": Actor("assets/player/chest.bam"),
            "head": Actor("assets/player/head.bam")
        }
        self.rig_connections = { # start: end, for angle calculations
            "right shoulder":"right elbow",
            "left shoulder": "left elbow",
            "right elbow": "right fist",
            "left elbow": "left fist",
        }
        
        
        self.taskMgr.add(self.task, "update")
        #self.taskMgr.add(self.test, "spin")

        for key, part in self.player1_parts.items():
            part.reparentTo(self.render)
            if (key == "head"):
                part.setScale(0.42, 0.42, 0.42)
            elif (key == "chest"):
                part.setScale(0.32, 0.32, 0.32)
            else:
                part.setScale(0.35, 0.35, 0.35)

    def task(self, task):
        self.camera.setPos(0.5, -4, -0.5)
        cam_coords = self.cv_cam.update()
        enemy_coords = {}
        while self.client.unread():
            msg = self.client.read().split(" ")
            if msg[0] == "coords":
                enemy_coords[msg[1]] = (float(msg[2]), float(msg[3]), float(msg[4]))
            # enemy_coords body_part x y z      for enemy body
        
        for nxt in cam_coords:
            position = nxt
            x = str(cam_coords[nxt][0])
            y = str(cam_coords[nxt][1])
            z = str(cam_coords[nxt][2])

            self.client.send(" ".join(["coord", position, x, y, z]))
        #TODO: render other body given their coords
        self.update_parts(enemy_coords, task.time)
        return Task.cont

    def update_parts(self, coords, time):
        for key, value in coords.items():
            if (key in self.player1_parts.keys()):
                self.player1_parts[key].setPos(value[0], value[2], -value[1])

                if (key in self.rig_connections):
                    end = coords[self.rig_connections[key]]
                    diff = LVecBase3f(value[0] - end[0], value[1] - end[1], value[2] - end[2])
                    self.set_hpr(diff, self.player1_parts[key])
    def test(self, task):
        angleDegrees = task.time * 6.0
        self.player1_parts["left elbow"].setHpr(0, angleDegrees, 0)
                                                    #     forward back  l/r
        return Task.cont

    def set_hpr(self, vector, node):
        
        #v0 = LVecBase3f(-v.y, v.x, 0)
        #u0 = v0.cross(v)
        left_right = atan2(vector.y, vector.x)
        forward_backwards = atan2(vector.z, vector.y)
        idk = atan2(vector.z, vector.x)
        #x = atan(vector.z /vector.y)
        node.setHpr(90-left_right*180/pi, 90 -forward_backwards*180/pi , 0)
        #node.setHpr(LVecBase3f(0, left_right*180/pi, 0))
                    #  l/r, f/b, roll
    #def get_hpr(self, vector):
        #quat = Quat()
        #look_at(quat, vector, LVector3f.up())
        #return quat.get_hpr()




#C:\Users\user\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\Scripts\blend2bam "C:\Users\user\Documents\Coding\projects hackathon\SecretPandaProject\FrontEnd\assets\untitled.blend" "C:\Users\user\Documents\Coding\projects hackathon\SecretPandaProject\FrontEnd\assets\untitled.bam" --blender-dir "C:\Program Files\Blender Foundation\Blender 3.6"