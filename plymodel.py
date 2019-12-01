# model data structure

class PlyModel():
    def __init__(self, vertex_list, face_list, normal_list):
        self.vertex_list = vertex_list
        self.face_list = face_list
        self.normal_list = normal_list

    @property
    def flattened_face_list(self):
        return [item for sublist in self.face_list for item in sublist]
    
    @property
    def flattened_face_num(self):
        return len(self.flattened_face_list)

    @property
    def vertex_num(self):
        return len(self.vertex_list)

    @property
    def normal_num(self):
        return len(self.normal_list)

    @property
    def face_num(self):
        return len(self.face_list)