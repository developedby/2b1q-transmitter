import matplotlib.pyplot as plt
import os

def PlotWaveformToFile(data, path='graph.png'):
    removeImage(path)
    plt.plot(data, drawstyle='steps-mid')
    return path

def removeImage(path):
    if os.path.isfile(path):
        os.remove(path)
