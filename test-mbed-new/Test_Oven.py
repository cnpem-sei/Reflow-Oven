from datetime import datetime 
from serial import Serial
from matplotlib.animation import FuncAnimation
from itertools import count
from matplotlib.axis import YAxis 
from tkinter.filedialog import askdirectory
from MBTempCoef import MBed as mb
from tkinter import *
from AniButon import AniButon
import time
import matplotlib.pyplot as plt 
import random
import numpy as np
import csv

def update(x):
    while (x==1):
        value = ''
        time.sleep(time_sec)   
        column2_temp.append(MbedTemp())
        
        print (column2_temp)

        column1_time.append(time.time() - start_time)
        
        
        ax.plot(column1_time[1:], column2_temp[1:], label = 'temp ')
        
        if (not (column1_time[-1] == "time") and float(column1_time[-1]) >= read_duration):
            ax.clear()
            name = path + file_name+'.csv'
            save_csv_file(column1_time, column2_temp)
            plot_graph(column1_time, column2_temp, name) 
            end()

def save_csv_file(column1_time, column2_temp):
    name = path + file_name+'.csv'
    with open(name , 'w') as f: 
        a = ''
        for index in range(len(column1_time)):
            a += f"{column1_time[index]},{(str(column2_temp[index]) )}\n"
        f.write(a)
        f.close()

def plot_graph(column1_time, column2_temp, name):
    fig, ax = plt.subplots(1, 1, figsize=(20, 10))
    ax.locator_params(axis='y', tight=True, nbins=15)
    ax.locator_params(axis='x', tight=True, nbins=20)
    ax.set_yscale("log")
    ax.plot(column1_time[1:], column2_temp[1:], label = 'temp')
    plt.legend()
    plt.xlabel('Time [s]')
    plt.ylabel('Temperature [°C]')
    plt.grid()
    plt.savefig(name+'.jpg')
    plt.close()
    #end()

def end ():
    print('Acsition save as sucefull')
    exit()

def MbedTemp():
    print("estou aqui")
    connection.write("1".encode('utf-8'))
    value = connection.read(6).decode('utf8')
    return (float(value))

if __name__ == '__main__':
    connection = Serial("COM4", 9600, write_timeout=0.2, timeout=0.2)
        
    print('Step 1 - Starting...')

    print('Step 2 - Insert ports that will be measured and duration test.')
    total_ports = []
    read_duration = int(input('Duration time test:'))
    column1_time = []
    column2_temp = []
    value = ''
    
    print('Setep 3 - Insert folder location and name file')
    path = (askdirectory(title='Select Folder')+'/')
    file_name = input('Insert file name:')
    name = path + file_name+'.csv'
    Tk().destroy
 
    time_sec = 1
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    start_time = time.time() 
    update (1)