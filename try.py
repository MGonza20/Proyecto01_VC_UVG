


# Importando librerias necesarias
import cv2 as cv
import numpy as np

from matplotlib import pyplot as plt
from skimage.morphology import skeletonize
from skimage.measure import approximate_polygon

from Node import Node


image_path = 'images/1_gt.pgm'
imagen_color = cv.imread(image_path)
imagen_gris = cv.cvtColor(imagen_color, cv.COLOR_BGR2GRAY)
_, binary_image = cv.threshold(imagen_gris, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)


skeleton = skeletonize(binary_image)


def get_node(graph_list, x, y):
    node = [node for node in graph_list if node.x == x and node.y == y]
    return node[0] if len(node) > 0 else Node(x, y)


all_nodes_list = []

graph_nodes = []
for i in range(1, skeleton.shape[0] - 1):
    for j in range(1, skeleton.shape[1] - 1):
        if skeleton[i, j]: 
            all_nodes_list.append((i, j))

            new_node = Node(i, j)
            if i - 1 >= 0 and skeleton[i - 1, j]: new_node.parent = get_node(graph_nodes, i - 1, j) # Norte
            if i - 1 >= 0 and j - 1 >= 0 and skeleton[i-1, j-1]: new_node.parent = get_node(graph_nodes, i-1, j-1) # Nor Oeste
            if i - 1 >= 0 and j + 1 < skeleton.shape[1] and skeleton[i-1, j+1]: new_node.parent = get_node(graph_nodes, i-1, j+1) # Nor Este

            if i + 1 < skeleton.shape[0] and skeleton[i + 1, j]: new_node.child = get_node(graph_nodes, i + 1, j) # Sur
            if i + 1 < skeleton.shape[0] and j - 1 >= 0 and skeleton[i+1, j-1]: new_node.child = get_node(graph_nodes, i+1, j-1) # Sur Oeste
            if i + 1 < skeleton.shape[0] and j + 1 < skeleton.shape[1] and skeleton[i+1, j+1]: new_node.child = get_node(graph_nodes, i+1, j+1) # Sur Este
            
            if j - 1 >= 0 and skeleton[i, j - 1]: new_node.neighbor = get_node(graph_nodes, i, j - 1) # Oeste
            if j + 1 < skeleton.shape[1] and skeleton[i, j + 1]: new_node.neighbor = get_node(graph_nodes, i, j + 1) # Este

            graph_nodes.append(new_node)

all_nodes_list = np.array(all_nodes_list)




extreme_nodes_list = []
for i in range(1, skeleton.shape[0] - 1):
    for j in range(1, skeleton.shape[1] - 1):
        if skeleton[i, j]:
            rows, columns = np.ogrid[i-1:i+2, j-1:j+2]
            if np.sum(skeleton[rows, columns]) == 2:
                extreme_nodes_list.append((i, j))



tolerance = 5
ap = approximate_polygon(all_nodes_list, tolerance)


bifurcation_nodes_list = []
trifurcation_nodes_list = []

for i in range(1, skeleton.shape[0] - 1):
		for j in range(1, skeleton.shape[1] - 1):
				if skeleton[i, j]:
						# Check if is not already in either list
						right = skeleton[i, j+1] and (i, j+1) not in bifurcation_nodes_list and (i, j+1) not in trifurcation_nodes_list
						left = skeleton[i, j-1] and (i, j-1) not in bifurcation_nodes_list and (i, j-1) not in trifurcation_nodes_list
						up = skeleton[i-1, j] and (i-1, j) not in bifurcation_nodes_list and (i-1, j) not in trifurcation_nodes_list
						down = skeleton[i+1, j] and (i+1, j) not in bifurcation_nodes_list and (i+1, j) not in trifurcation_nodes_list
						upper_left = skeleton[i-1, j-1] and (i-1, j-1) not in bifurcation_nodes_list and (i-1, j-1) not in trifurcation_nodes_list
						upper_right = skeleton[i-1, j+1] and (i-1, j+1) not in bifurcation_nodes_list and (i-1, j+1) not in trifurcation_nodes_list
						lower_left = skeleton[i+1, j-1] and (i+1, j-1) not in bifurcation_nodes_list and (i+1, j-1) not in trifurcation_nodes_list
						lower_right = skeleton[i+1, j+1] and (i+1, j+1) not in bifurcation_nodes_list and (i+1, j+1) not in trifurcation_nodes_list
						neighbors = [right, left, up, down, upper_left, upper_right, lower_left, lower_right]
						neighbors_sum = np.sum(neighbors)
						# Trifurcation has higher priority
						if neighbors_sum == 4:
								trifurcation_nodes_list.append((i, j))
						elif neighbors_sum == 3:
								bifurcation_nodes_list.append((i, j))
						


def generate_abstract_graph(graph_nodes, extreme_nodes_list, bifurcation_nodes_list, trifurcation_nodes_list, ap):
    edges = []
