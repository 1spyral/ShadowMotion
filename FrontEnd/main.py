from app import App 
from camera import Camera
from client import Client

cv_cam = Camera()
#cv_cam.update()
client = Client()
app = App(cv_cam, client)

app.run()
