from file_finder import read_ply_files

def read_model_points():
    file_paths = read_ply_files()

    vertex_list = []
    face_list = []
    num_points = 1
    end_header_check = False
    end_points_check = False

    with open(file_paths[1]) as f:
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

    # TODO actually calculate normals
    normal_list = [[1.0, 1.0, 1.0] for x in vertex_list]
    num_normals = len(normal_list)

    return vertex_list, face_list, normal_list, num_normals, num_points, num_faces


if __name__ == "__main__":
    vertex_list, face_list, normal_list, num_normals, num_points, num_faces = read_model_points()

    print(f"Loaded {num_points} points.")
    print(f"Loaded {num_faces} faces.")
    print(f"Loaded {num_normals} normals.")