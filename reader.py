import numpy as np

from file_finder import read_ply_files

def calculate_normal(p1, p2, p3, normalize = False):
    # calculates a normal given 3 points
    # first point is always the point where the normal will be

    v1 = [i - j for i, j in zip(p2, p1)]
    v2 = [i - j for i, j in zip(p3, p1)]

    if normalize:
        v = np.cross(v1, v2)

        return v/np.sum(np.abs(v))

    return np.cross(v1, v2)

def calculate_all_normals(points, faces):
    all_normals = []

    for i, point in enumerate(points):
        shared_faces = []
        for j, face in enumerate(faces):
            if i in face:
                shared_faces.append(face)
        
        if len(shared_faces) == 0:
            continue

        shared_normals = []
        for face in shared_faces:
            shared_normals.append(
                calculate_normal(points[face[0]], points[face[1]], points[face[2]], normalize=True)
            )

        v = np.mean(shared_normals, axis=0)

        all_normals.append(list(v))
            
    return all_normals

def read_model_points():
    file_paths = read_ply_files()

    vertex_list = []
    face_list = []
    num_points = 1
    end_header_check = False
    end_points_check = False

    with open(file_paths[2]) as f:
        count = 1
        for line in f.readlines():
            if line.startswith("element vertex"):
                num_points = int(line.split(" ")[2])
            elif line.startswith("end_header"):
                end_header_check = True
                continue

            if end_header_check:
                vertexes = [float(x) for x in line.split(" ")[0:3]]
                vertex_list.append(vertexes)
                count += 1

            if count > num_points and end_header_check is True:
                end_points_check = True
                end_header_check = False
                continue

            if end_points_check:
                faces = [int(x) for x in line.split(" ")[1:4]]
                face_list.append(faces)

    num_points = len(vertex_list)
    num_faces = len(face_list)

    normal_list = calculate_all_normals(vertex_list, face_list)
    num_normals = len(normal_list)

    return vertex_list, face_list, normal_list, num_normals, num_points, num_faces


if __name__ == "__main__":
    vertex_list, face_list, normal_list, num_normals, num_points, num_faces = read_model_points()

    print(f"Loaded {num_points} points.")
    print(f"Loaded {num_faces} faces.")
    print(f"Loaded {num_normals} normals.")

    print(normal_list[0:5])
