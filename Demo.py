#!/usr/bin/env python
# coding: utf-8

# In[6]:


import plotly.plotly as py
from plotly.graph_objs import *
import plotly.dashboard_objs as dashboard
import IPython.display
from IPython.display import Image
import re

def fileId_from_url(url):
    raw_fileId = re.findall("~[A-z]+/[0-9]+", url)[0][1: ]
    return raw_fileId.replace('/', ':')

def DrawBar(a, b, c, d, e, f, g):
    py.sign_in('HCI_Candidate', 'U7NcQ0FZyKgSZGV8Qfou')
    #Your daily intakes
    trace1 = {
        "x": ["protein", "fat", "carbohydrate", "calories", "inorganic salts", "calcium", "water"], 
        "y": [a, b, c, d, e, f, g], 
        "marker": {"color": "#5B9FD3"}, 
        "name": "Your daily intake", 
        "type": "bar"
    }
    #Suggested daily intakes
    trace2 = {
        "x": ["protein /0.1g", "fat /0.1g", "carbohydrate /g", "calories", "inorganic salts /mg", "calcium /mg", "water /10g"], 
        "y": [820, 720, 500, 700, 2000, 900, 500], 
        "marker": {"color": "#48CA8F"}, 
        "name": "suggested daily intake", 
        "type": "bar"
    }
    
    data = Data([trace1, trace2])
    layout = {"barmode": "group", 
              "title": "Diet Graph", 
              "xaxis": {"title": "Nutrition"},
              "yaxis": {"title": "Quantity"}
             }

    fig = Figure(data=data, layout=layout)
    plot_url = py.plot(fig)
    return plot_url
    
def DrawPie(a, b, c, d, e, f, g):
    py.sign_in('HCI_Candidate', 'U7NcQ0FZyKgSZGV8Qfou')
    #Your daily intakes
    trace1 = {
        "labels": ["protein", "fat", "carbohydrate", "calories", "inorganic salts", "calcium", "water"],
        "labelssrc": "hmluedtke:3:2258a2", 
        "type": "pie", 
        "values": [a, b, c, d, e, f, g], 
        "valuessrc": "hmluedtke:3:0bb982"
    }

    data = Data([trace1])
    layout = {
        "autosize": True, 
        "colorway": ["#ff0000", "#ffa700", "#afff00", "#08ff00", "#00ff9f", "#00b7ff", "#0010ff", "#9700ff", "#ff00bf", "#ff0018"], 
        "dragmode": "zoom", 
        "paper_bgcolor": "rgb(255, 255, 255)",
        "selectdirection": "any", 
        "title": "Pie Chart", 
        "xaxis": {"autorange": True, "range": [-1, 6]}, 
        "yaxis": {"autorange": True, "range": [-1, 4]}
    }

    fig = Figure(data=data, layout=layout)
    plot_url = py.plot(fig)
    return plot_url

def DrawSnake(a0,a1,a2,a3,a4,a5,a6,b0,b1,b2,b3,b4,b5,b6,c0,c1,c2,c3,c4,c5,c6):
    py.sign_in('HCI_Candidate', 'U7NcQ0FZyKgSZGV8Qfou')
    trace1 = {
        "link": {"source": [0,0,0,0,0,0,0,1,1,1,1,1,1,1,2,2,2,2,2,2,2], 
                 "target": [3,4,5,6,7,8,9,3,4,5,6,7,8,9,3,4,5,6,7,8,9], 
                 "value": [a0,a1,a2,a3,a4,a5,a6,b0,b1,b2,b3,b4,b5,b6,c0,c1,c2,c3,c4,c5,c6], 
                }, 
        "node": {"color": ["blue", "red", "yellow", "green", "green",  "green", "green", "green", "green", "green"], "label": ["Apple", "Pear", "Cherry","N1","N2","N3","N4","N5","N6","N7"], "line": {"color": "black", "width": 0.5}, "pad": 15, "thickness": 20}, "orientation": "h", "type": "sankey"}
    
    data = Data([trace1])
    layout = {"font": {"size": 10}, "hovermode": "closest", "margin": {"r": 10, "t": 25, "b": 40, "l": 60}, "showlegend": False, "title": "Basic Sankey Diagram"}
    fig = Figure(data=data, layout=layout)
    plot_url = py.plot(fig)
    return plot_url
    
if __name__ == "__main__":
    apple = [20,75,143,126,244,239,124]
    noodles = [97,85,274,198,574,144,27]
    vegetables = [97,27,174,147,440,341,240]
    rice = [47,196,238,142,678,203,142]
    beef = [421,372,104,432,124,74,159]
    pork = [352,421,154,312,321,98,133]
    cherry = [98,345,124,354,240,106,254]
    pear = [35,71,125,243,214,133,351]
    
    food = [0,0,0,0,0,0,0] 
    a0 = apple[0]
    a1 = apple[1]
    a2 = apple[2]
    a3 = apple[3]
    a4 = apple[4]   
    a5 = apple[5]
    a6 = apple[6]
    b0 = pear[0]
    b1 = pear[1]
    b2 = pear[2]
    b3 = pear[3]
    b4 = pear[4]   
    b5 = pear[5]
    b6 = pear[6]
    c0 = cherry[0]
    c1 = cherry[1]
    c2 = cherry[2]
    c3 = cherry[3]
    c4 = cherry[4]   
    c5 = cherry[5]
    c6 = cherry[6]

    flag = 10
    while (flag > 0):
        getFood = input("Please tell me what you have eat today(apple,pear,cherry,rice,noodles) or print 'OK' to finish.\n")
        if(getFood=="apple"):
            food[0] = food[0] + apple[0]
            food[1] = food[1] + apple[1]
            food[2] = food[2] + apple[2]
            food[3] = food[3] + apple[3]
            food[4] = food[4] + apple[4]
            food[5] = food[5] + apple[5]
            food[6] = food[6] + apple[6]
            flag = flag-1
        elif(getFood=="pear"):
            food[0] = food[0] + pear[0]
            food[1] = food[1] + pear[1]
            food[2] = food[2] + pear[2]
            food[3] = food[3] + pear[3]
            food[4] = food[4] + pear[4]
            food[5] = food[5] + pear[5]
            food[6] = food[6] + pear[6]
            flag = flag-1
        elif(getFood=="cherry"):
            food[0] = food[0] + cherry[0]
            food[1] = food[1] + cherry[1]
            food[2] = food[2] + cherry[2]
            food[3] = food[3] + cherry[3]
            food[4] = food[4] + cherry[4]
            food[5] = food[5] + cherry[5]
            food[6] = food[6] + cherry[6]
            flag = flag-1
        elif(getFood=="rice"):
            food[0] = food[0] + rice[0]
            food[1] = food[1] + rice[1]
            food[2] = food[2] + rice[2]
            food[3] = food[3] + rice[3]
            food[4] = food[4] + rice[4]
            food[5] = food[5] + rice[5]
            food[6] = food[6] + rice[6]
            flag = flag-1
        elif(getFood=="noodles"):
            food[0] = food[0] + noodles[0]
            food[1] = food[1] + noodles[1]
            food[2] = food[2] + noodles[2]
            food[3] = food[3] + noodles[3]
            food[4] = food[4] + noodles[4]
            food[5] = food[5] + noodles[5]
            food[6] = food[6] + noodles[6]
            flag = flag-1
        elif(getFood=="vegetables"):
            food[0] = food[0] + vegetables[0]
            food[1] = food[1] + vegetables[1]
            food[2] = food[2] + vegetables[2]
            food[3] = food[3] + vegetables[3]
            food[4] = food[4] + vegetables[4]
            food[5] = food[5] + vegetables[5]
            food[6] = food[6] + vegetables[6]
            flag = flag-1
        elif(getFood=="beef"):
            food[0] = food[0] + beef[0]
            food[1] = food[1] + beef[1]
            food[2] = food[2] + beef[2]
            food[3] = food[3] + beef[3]
            food[4] = food[4] + beef[4]
            food[5] = food[5] + beef[5]
            food[6] = food[6] + beef[6]
            flag = flag-1
        elif(getFood=="OK"):
            flag = 0
        else:
            print("Sorry, it seems your food come from Mars")
            
            
    url_1 = DrawBar(food[0] ,food[1], food[2], food[3], food[4], food[5], food[6])
    url_2 = DrawPie(food[0] ,food[1], food[2], food[3], food[4], food[5], food[6])
    url_3 = DrawSnake(a0,a1,a2,a3,a4,a5,a6,b0,b1,b2,b3,b4,b5,b6,c0,c1,c2,c3,c4,c5,c6)
    fileID_1 = fileId_from_url(url_1)
    fileID_2 = fileId_from_url(url_2)
    fileID_3 = fileId_from_url(url_3)
    
    my_dboard = dashboard.Dashboard()
    box_1 = {
        'type': 'box',
        'boxType': 'plot',
        'fileId': fileID_1,
        'title': 'intake quantity'
    }
    box_2 = {
        'type': 'box',
        'boxType': 'plot',
        'fileId': fileID_2,
        'title': 'intake percentage'
    }
    box_3 = {
        'type': 'box',
        'boxType': 'plot',
        'fileId': fileID_3,
        'title': 'intake source',
    }
    
    my_dboard.insert(box_1)
    my_dboard.insert(box_2, 'above', 1)
    my_dboard.insert(box_3, 'left', 2)
    py.dashboard_ops.upload(my_dboard, 'Diet Intake Dashboard')


# In[ ]:




