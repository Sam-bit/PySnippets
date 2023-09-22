import uuid
from django.contrib.auth.models import User
import face_recognition

NUM_FACES = 9

def get_face_id(image_path):
    image = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(image)
    if len(face_locations) > 1 or len(face_locations) < 1:
        return False

    for user in User.objects.filter(profile__enable_facial_recognition=True):
        known_image = face_recognition.load_image_file(user.profile.face.path)
        unknown_image = image
        user_encoding = face_recognition.face_encodings(known_image)[0]
        user_encodings = list()
        user_encodings.append(user_encoding)
        user_faces = Face.objects.filter(user=user).order_by('-timestamp')
        for face in user_faces:
            if open(face.image.path,"rb").read() == open(image_path,"rb").read():
                return False
        if user_faces.count() > NUM_FACES:
            user_faces = user_faces[:NUM_FACES]
        for face in user_faces:
            image = face_recognition.load_image_file(face.image.path)
            image_encoding = face_recognition.face_encodings(image)[0]
            user_encodings.append(image_encoding)
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
        results = face_recognition.compare_faces(user_encodings, unknown_encoding)
        if results[0]:
            return user.profile.uuid
    return str(uuid.uuid4())