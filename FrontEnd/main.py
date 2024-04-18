from app import App 
from camera import Camera

cv_cam = Camera()
while True:
    cv_cam.update()
#app = App(cv_cam)
#app.run()