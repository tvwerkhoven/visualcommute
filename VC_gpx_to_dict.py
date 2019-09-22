#%% initialization

import numpy as np
import matplotlib.pyplot as plt

work_dir='C:\\Ruben\\code\\visualcommute'

import os
import glob

os.chdir(work_dir)

plt.close('all');

import xml.etree.ElementTree as ET
import datetime

#%% functions

def conv_dict_to_arr(my_dict):
    N_points=len(my_dict.keys())
    out_arr=np.zeros([N_points,2])
    for i_point in range(N_points):
        out_arr[i_point,:]=my_dict[i_point][1:3]
    return out_arr

#%% get all gpx data

gpx_data_list=glob.glob('data/*.gpx');

N_files=len(gpx_data_list)
print('%d gpx files found' % N_files)

#%% load first gpx file

i_file=0

tree = ET.parse(gpx_data_list[i_file])
root = tree.getroot()

#%% process all data to dict

my_dict={}

for i_seg,t_seg in enumerate(root):
    my_dict[i_seg]={}
    if len(t_seg)==4: # check if we have a track segment
        for i_point,t_point in enumerate(t_seg[3]):
            t_lat=t_point.attrib['lat']
            t_lon=t_point.attrib['lon']
            # point syntax: [0,1,2,3]=[elevation,time,hdop,vdop]
            my_dict[i_seg][i_point]=[datetime.datetime.strptime(t_point[1].text, '%Y-%m-%dT%H:%M:%S.%fZ'),float(t_lat),float(t_lon),float(t_point[0].text)]

#%% plotting all GPS points for different segments

plt.figure()
for i_seg in range(10):
    plot_arr=conv_dict_to_arr(my_dict[i_seg])
    plt.subplot(2,5,i_seg+1)
    plt.plot(plot_arr[:,0],plot_arr[:,1],'.')
    plt.xlabel('latitude (deg)');
    plt.ylabel('longitude (deg)');
    plt.title('segment %d' % i_seg);
    
