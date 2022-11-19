import numpy as np
import math
import fractions 
from sympy import *
import matplotlib.pyplot as plt

def get_data():
    print("Getting data")

    from bs4 import BeautifulSoup
    import urllib.request
    wiki = "https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Canada"
    soup = BeautifulSoup(urllib.request.urlopen(wiki), 'html.parser')
    stat  = soup.findAll('td', {"colspan" : "2" })
    data = list()
    for i in stat:
        if "-" not in i.text and  not contains_any(i.text, {"a","b","c","d","e","f"})  :
            data.append( i.text.split())
    return list( int(i[0])  for i in data)
   

def contains_any(str, set):
    """ Check whether sequence str contains ANY of the items in set. """
    return 1 in [c in str for c in set]

def linear_regression(A, y):
    print("linear regression")
    x = np.matmul(np.transpose(A), A)
    x = np.matmul(np.linalg.inv(x), np.transpose(A))
    x = np.matmul(x, y)
    return  x



def prediction_plot(A, y):
    print("plotting")
    x_scatter =  list( i   for i in  range(0, len(y) ) )
    y_scatter =  list( cases[i]   for i in  range(0, len(y) ) )
    
    
    x = np.linspace(0, len(x_scatter), 100)
    y = np.exp( c1  + c2 * x)
    
    plt.plot( x_scatter, y_scatter, 'ro' )
    plt.title("COVID-19 Cases In Canada")
    plt.ylabel( "Number Of Confirmed Cases")
    plt.xlabel( "Days After Patient Zero (Feb-27-2020)")
    #plt.yscale("log")
    plt.xlim(0, len(x_scatter))
    plt.plot(x, y)
