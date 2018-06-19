import matplotlib.pyplot as plt
import os

def PlotWaveformToFile(data, path='graph.png'):
    removeImage(path)
    plt.rcParams["figure.figsize"] = [7,1.3]
    plt.plot(data, drawstyle='steps-mid')
    plt.xticks(range(0, len(data), 4))
    plt.savefig(path)
    plt.close()

def removeImage(path):
    if os.path.isfile(path):
        os.remove(path)
        
