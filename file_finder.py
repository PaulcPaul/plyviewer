import os

def read_ply_files():
    model_path = "bunny\\reconstruction"

    model_files = []

    for f in os.listdir(model_path):
        if f.endswith("ply"):
            model_files.append(os.path.join(model_path, f))

    return model_files

if __name__ == "__main__":
    for i in read_ply_files():
        print(i)