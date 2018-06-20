import matplotlib.pyplot as plt
import os

def PlotWaveformToFile(data, path='graph.png', wave_type='binary'):
    removeImage(path)
    plt.rcParams["figure.figsize"] = [7,1.3]
    plt.plot(data, drawstyle='steps-mid')
    plt.xticks(range(0, len(data), 4))
    if wave_type == 'binary':
        plt.yticks([0,1])
        plt.ylim((-0.2,1.2))
    elif wave_type == '2b1q':
        plt.yticks([-3,-1,1,3])
        plt.ylim((-3.5,3.5))
    else:
        raise Exception("Graphing Error, unknown wave_type %s (Should be 'binary' or '2b1q')" %(wave_type,))
    plt.savefig(path)
    plt.close()

def removeImage(path):
    if os.path.isfile(path):
        os.remove(path)
