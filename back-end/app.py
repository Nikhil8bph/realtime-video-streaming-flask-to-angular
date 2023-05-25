import cv2
import base64
from flask import Flask, Response
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app,cors_allowed_origins="*")

# Function to capture and stream video frames
def stream_frames():
    camera = cv2.VideoCapture(0)  # Adjust the camera index as needed

    while True:
        success, frame = camera.read()

        if not success:
            break

        # Encode the frame as a JPEG image
        _, encoded_image = cv2.imencode('.jpg', frame)

        # Convert the encoded image to base64
        base64_image = base64.b64encode(encoded_image.tobytes()).decode('utf-8')

        # Send the base64-encoded image to the client
        socketio.emit('video_stream', base64_image)

    camera.release()

@app.route('/')
def index():
    return 'Flask Backend'

@socketio.on('connect')
def on_connect():
    # Start streaming frames when a client connects
    socketio.start_background_task(stream_frames)

if __name__ == '__main__':
    socketio.run(app)
