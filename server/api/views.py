from django.http import StreamingHttpResponse, HttpResponseServerError, HttpResponse
import cv2

# Global variable to hold camera instance
camera = None


def generate_frames():
    global camera
    while True:
        if camera is not None:
            success, frame = camera.read()
            if not success:
                break
            else:
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def video_feed(request):
    return StreamingHttpResponse(generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame')


def start_camera(request):
    global camera
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not camera.isOpened():
        return HttpResponseServerError("Failed to open camera.")
    return HttpResponse("Camera started.")


def stop_camera(request):
    global camera
    if camera is not None:
        camera.release()
        camera = None
    return HttpResponse("Camera stopped.")
