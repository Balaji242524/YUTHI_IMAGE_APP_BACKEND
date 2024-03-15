from deepface import DeepFace

def get_facedetect():
    dfs = DeepFace.find(
        img_path="",
        model_name="DeepFace",
        distance_metric="cosine",
        enforce_detection=False,
        db_path="./db",
    )
    return dfs

print(dfs)