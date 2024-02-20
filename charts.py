#charts.py

import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A','B','C']
    values = [100,34,120]
    
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    plt.savefig('.pie.png')
    plt.close()