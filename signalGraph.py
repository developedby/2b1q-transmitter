import matplotlib.pyplot as plt
import os

def PlotWaveformToFile(data, path='graph.png'):
    removeImage(path)
    plt.rcParams["figure.figsize"] = [3,2]
    plt.plot(data, drawstyle='steps-mid')
    plt.savefig(path)
         
    return path

def removeImage(path):
    if os.path.isfile(path):
        os.remove(path)
        plt.close()
