from deepface import DeepFace

analysis = DeepFace.analyze(img_path='face_sample.jpg', actions=["age", "gender", "emotion", "race"])
print(analysis)