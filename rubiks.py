import pyray as pr
import numpy as np

class Cube:
    def __init__(self, size, center, face_color):
        self.size = size
        self.center = center
        self.face_color = face_color
        self.orientation = np.eye(3)


        # Initialize empty lists for models to update face colors
        self.model = None
        self.gen_meshe(size)
        # Create and position the meshes
        self.create_model()
    
    def gen_meshe(self, scale: tuple):
        # Create the central cube mesh
        self.mesh = pr.gen_mesh_cube(*scale)

    def create_model(self):
        self.model = pr.load_model_from_mesh(self.mesh)
        self.model.transform = pr.matrix_translate(self.center[0], self.center[1], self.center[2])


class Rubik:
    def __init__(self) -> None:
        self.cubes = []
        self.generate_rubik(2)
    
    def generate_rubik(self, size):
        colors = [pr.WHITE, pr.BLUE, pr.ORANGE, pr.RED, pr.YELLOW, pr.GREEN]
        offset = size - 0.7
        size_z = size * 0.9, size * 0.9, size * 0.1
        size_x = size * 0.9, size * 0.1, size * 0.9
        size_y = size * 0.1, size * 0.9, size * 0.9


        for x in range(3):
            for y in range(3):
                for z in range(3):
                    face_colors = [
                        pr.BLACK if z != 2 else colors[0],  # Front
                        pr.BLACK if z != 0 else colors[1],  # Back
                        pr.BLACK if x != 2 else colors[2],  # Right
                        pr.BLACK if x != 0 else colors[3],  # Left
                        pr.BLACK if y != 2 else colors[4],  # Top
                        pr.BLACK if y != 0 else colors[5]   # Bottom
                    ]
                    # Center
                    center_position = np.array([(x - 1) * offset,
                                                (y - 1) * offset,
                                                (z - 1) * offset])
                    
                    center = Cube((size, size, size),
                                  center_position,
                                  pr.BLACK)
                    
                    # front face
                    front_position = np.array([center_position[0],
                                               center_position[1],
                                               center_position[2] + size/2])
                    
                    front = Cube(size_z, front_position, face_colors[0])

                    # back face
                    back_position = np.array([center_position[0],
                                               center_position[1],
                                               center_position[2] -size/2])
                    
                    back = Cube(size_z, back_position, face_colors[1])

                    # right face
                    right_position = np.array([center_position[0] + size/2,
                                               center_position[1],
                                               center_position[2]])
                    
                    right = Cube(size_y, right_position, face_colors[2])

                    # left face
                    left_position = np.array([center_position[0] - size/2,
                                               center_position[1],
                                               center_position[2]])
                    
                    left = Cube(size_y, left_position, face_colors[3])

                    # top face
                    top_position = np.array([center_position[0],
                                               center_position[1] + size/2,
                                               center_position[2]])
                    
                    top = Cube(size_x, top_position, face_colors[4])

                    # bottom face
                    bottom_position = np.array([center_position[0],
                                               center_position[1] - size/2,
                                               center_position[2]])
                    
                    bottom = Cube(size_x, bottom_position, face_colors[5])

                    self.cubes.append([center, front, back, right, left, top, bottom])

        return self.cubes
    