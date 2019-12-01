from file_finder import read_ply_files
from plymodel import PlyModel

def read_model_points():
    file_paths = read_ply_files()

    vertex_list = []
    normal_list = []
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
                normals = [float(x) for x in line.split(" ")[3:] if x != "\n"]
                vertex_list.append(vertexes)
                normal_list.append(normals)
                count += 1

            if count > num_points and end_header_check is True:
                end_points_check = True
                end_header_check = False
                continue

            if end_points_check:
                faces = [int(x) for x in line.split(" ")[1:4]]
                face_list.append(faces)
    
    return vertex_list, face_list, normal_list


if __name__ == "__main__":
    model = PlyModel(*read_model_points())

    print(model.face_list[0:5])
    print(model.vertex_list[0:5])
    print(model.normal_list[0:5])
