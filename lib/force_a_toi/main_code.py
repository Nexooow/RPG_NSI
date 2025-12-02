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
class NPC:
    def __init__(self,name,location):
        self.name=name
        self.location=location
def display_frames(image,frame_width,frame_height):
    frames=[]
    sheet_width=image.get_width()
    sheet_height=image.get_height()
    num_frames=sheet_width//frame_width
    for i in range(num_frames):
        frame=image.subsurface((i*frame_width,0,frame_width,frame_height))
        frames.append(frame)
    return frames
graphe=Graph([("Auberge","Mountain",47),("Auberge","Dawn of the world",21),("Dawn of the world","Auberge",21),("Mountain","Ceilidh",36),("Mountain","Auberge",47),("Ceilidh","Mountain",36),("Ceilidh","Auberge",31),("Auberge","Elder Tree",21),("Auberge","Ceilidh",36)],["Auberge","Mountain","Ceilidh","Dawn of the world","Elder Tree"],True)
with open("main_map.txt","r") as f0:
    b64=f0.read()
with open("mountain_map.txt","r") as f1:
    b64_mountain=f1.read()
with open("caelid_map.txt","r") as f2:
    b64_cailidh=f2.read()
with open("radahn_chibi.txt","r") as f3:
    b64_rad=f3.read()
with open("hand_img.txt","r") as f4:
    b64_hand=f4.read()
with open("castle_img.txt",'r') as f5:
    b64_c=f5.read()
with open("oz_img.txt","r") as f6:
    b64_oz=f6.read()
with open("feet_img.txt","r") as f7:
    b64_feet=f7.read()
with open("radahn_fight_zone.txt","r") as f8:
    b64_rad_zone=f8.read()
with open("radahn_pixel.txt","r") as f9:
    b64_radahn=f9.read()
bigfoot=NPC("Casan famhair",(200,400))
giant=NPC("Oz",(500,200))
radahn=NPC("Radahn, Consort of Joy",(766,350))
castle=NPC("Old Castle",(640,570))
finger=NPC("The Toucher",(650,150))
nodes_icons={radahn.name:(b64_rad,'jpeg'),finger.name:(b64_hand,'jpeg'),castle.name:(b64_c,'jpeg'),giant.name:(b64_oz,'webp'),bigfoot.name:(b64_feet,'png')}
graphe_mt=Graph([(bigfoot.name,giant.name,5),(giant.name,bigfoot.name,5)],[bigfoot.name,giant.name],True)
graphe_caelid=Graph([(radahn.name,castle.name,2),(castle.name,finger.name,6),(finger.name, castle.name,5),(castle.name,radahn.name,1)],[castle.name,radahn.name,finger.name],True)
pygame.init()
screen = pygame.display.set_mode((1000, 700))
background = graphe.affichage_graphe(b64,{"Auberge": (200, 400), "Mountain": (600, 120),"Ceilidh": (660, 480),"Dawn of the world": (450, 500),"Elder Tree": (500, 230)},'webp',nodes_icons)
screen.blit(background,(0,0))
running = True
main_img=background
caelid=None
mt=None
fight_zone=None
list_meteor=[]
clock=pygame.time.Clock()
half_radahn=pygame.image.load(BytesIO(base64.b64decode(b64_radahn))).convert_alpha()
radahn_frames=display_frames(half_radahn,1200,1350)
radahn_frame_index=0
explosion_group=pygame.sprite.Group()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.MOUSEBUTTONUP:
            position=event.pos
            if main_img==background and pygame.Rect(500,0,500,350).collidepoint(position):
                mt=graphe_mt.affichage_graphe(b64_mountain,{bigfoot.name:bigfoot.location,giant.name:giant.location},'webp',nodes_icons)
                main_img=mt
            if main_img==background and pygame.Rect(500,400,300,200).collidepoint(position):
                caelid=graphe_caelid.affichage_graphe(b64_cailidh,{radahn.name:radahn.location,castle.name:castle.location,finger.name:finger.location},'webp',nodes_icons)
                main_img=caelid
            if main_img==caelid:
                if pygame.Rect(radahn.location[0]-100,radahn.location[1]-100,200,200).collidepoint(position):
                    fight_zone=pygame.image.load(BytesIO(base64.b64decode(b64_rad_zone))).convert()
                    main_img=fight_zone
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_o:
                main_img=background
    screen.blit(main_img,(0,0))
    if main_img==fight_zone:
        screen.blit(radahn_frames[radahn_frame_index],(0,-120))
        radahn_frame_index=(radahn_frame_index+1)%len(radahn_frames)
        this=randint(1,100)
        if len(list_meteor)<10 and this<=10:
            if this>3:
                list_meteor.append(Meteor((randint(25,910),-25)))
            else:
                border=choice([25,910])
                list_meteor.append(Meteor((border,randint(-25,150))))
        for meteor in list_meteor:
            meteor.deplace()
            meteor.frame_index=(meteor.frame_index+1)%len(meteor.frames)
            if meteor.rect.bottom>=480:
                list_meteor.remove(meteor)
                explosion=Explosion(meteor.rect.center[0],meteor.rect.center[1],meteor.size)
                explosion_group.add(explosion)
            else:
                screen.blit(meteor.frames[meteor.frame_index],meteor.rect)
        text_render_centered_up(screen,"Survive","bold")
    clock.tick(45)
    explosion_group.draw(screen)
    explosion_group.update()

    pygame.display.update()
pygame.quit()
print(graphe.paths("Ceilidh","Elder Tree"))
