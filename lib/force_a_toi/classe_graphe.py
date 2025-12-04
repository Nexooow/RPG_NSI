import networkx as nx
import matplotlib.pyplot as plt
import base64
import numpy as np
import pygame
from io import BytesIO
from matplotlib.offsetbox import OffsetImage,AnnotationBbox
from matplotlib.transforms import offset_copy
from random import randint,choice
from meteor import *
from boom import *
from text_display import *
class Graph:
    def __init__(self,aretes,sommets,orientation):
        self.sommets=sommets
        self.orientation=orientation
        if not self.orientation:
            for i in list(set(aretes)):
                aretes+=[(i[1],i[0],i[2])]
        self.aretes_tuple=list(set(aretes))
        self.aretes={}
        for arete in self.aretes_tuple:
            key,value=arete[0:2]
            if key not in self.aretes:
                self.aretes[key]=[value]
            else:
                self.aretes[key].append(value)
    def voisin(self,nom_sommet):
        return self.aretes[nom_sommet]
    def def_graph(self):
        G=nx.DiGraph() if self.orientation else nx.Graph()
        for arete in self.aretes_tuple:
            a,b,poids=arete
            G.add_edge(a,b,weight=poids)
        G.add_nodes_from(self.sommets)
        return G
    def affichage_graphe(self,b64,pos,formate,nodes_icons):
        img_bytes = base64.b64decode(b64)
        img = plt.imread(BytesIO(img_bytes),format=formate)
        fig, ax = plt.subplots(figsize=(10, 7))
        ax.imshow(img,extent=[0,1000,700,0])
        G=self.def_graph()
        nx.draw(G,pos,node_color ="none", with_labels =True ,node_size = 1000)
        edge_labels=nx.get_edge_attributes(G,"weight")
        edge_color='blue'
        nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels,font_color=edge_color,ax=ax)
        if nodes_icons:
            for node,image in nodes_icons.items():
                if node in pos:
                    img_icon=plt.imread(BytesIO(base64.b64decode(image[0])),format=image[1])
                    img_size=OffsetImage(img_icon,zoom=0.15)
                    x,y=pos[node]
                    off=offset_copy(ax.transData,fig=fig,x=0,y=30,units="points")
                    box=AnnotationBbox(img_size,pos[node],xycoords=off,frameon=False)
                    ax.add_artist(box)
        fig.canvas.draw()
        image = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
        image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        pygame_surface = pygame.surfarray.make_surface(np.transpose(image, (1, 0, 2)))
        plt.close(fig)
        return pygame_surface
    def paths(self,a,b):
        G=self.def_graph()
        chemin=list(nx.shortest_path(G,source=a,target=b,weight='weight'))
        poids=nx.shortest_path_length(G,source=a,target=b,weight='weight')
        return chemin,poids
