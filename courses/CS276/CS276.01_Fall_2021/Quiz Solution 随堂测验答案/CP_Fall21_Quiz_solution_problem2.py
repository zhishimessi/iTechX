import math
import os
import sys

import numpy as np

def rotate(angle):
    res = np.array([ [math.cos(angle), 0, math.sin(-angle)],[0,1,0],[ math.sin(-angle),0, math.cos(angle)]])
    return res

def rodrigues_rotation_matrix(axis, theta):
    axis = np.asarray(axis)
    theta = np.asarray(theta)
    axis = axis/math.sqrt(np.dot(axis, axis))
    a = math.cos(theta/2.0)
    b, c, d = -axis*math.sin(theta/2.0)
    aa, bb, cc, dd = a*a, b*b, c*c, d*d
    bc, ad, ac, ab, bd, cd = b*c, a*d, a*c, a*b, b*d, c*d
    return np.array([[aa+bb-cc-dd, 2*(bc+ad), 2*(bd-ac)],
                     [2*(bc-ad), aa+cc-bb-dd, 2*(cd+ab)],
                     [2*(bd+ac), 2*(cd-ab), aa+dd-bb-cc]])



sTs = []
for i in range(0,360,3):


    angle = 3.1415926*2*(360 - i) / 360.0
    

    pos = s_pos - center
    pos = rodrigues_rotation_matrix(up,-angle).dot(pos) 
    
    pos = pos + center
    
    #print('pos:',pos)
    
    lookat = center - pos
    lookat = lookat/np.linalg.norm(lookat)
    
    xaxis = np.cross(lookat, up)
    xaxis = xaxis / np.linalg.norm(xaxis)
    
    yaxis = -np.cross(xaxis,lookat)
    yaxis = yaxis/np.linalg.norm(yaxis)
    
    nR = np.array([xaxis,yaxis,lookat, pos]).T
    nR = np.concatenate([nR,np.array([[0,0,0,1]])])
