from sample import Sample
import matplotlib.pyplot as plt
from copy import copy
import numpy as np
from ternary_diagram import TernaryDiagram
from matplotlib import rcParams
import matplotlib.colors
import pandas as pd
from mpl_toolkits.axes_grid1 import make_axes_locatable
rcParams.update({'figure.autolayout': True})

class Plot:
    def __init__(self):
        self.groups = dict()
        pass

    def maturity(self, filenames=None):
        fig, ax = plt.subplots()
        td = TernaryDiagram(['DBE12', 'DBE9', 'DBE15'], ax=ax)

        self.markers = ["o", "v", "^", "s", "h", "D"]
        self.colors = ["red", "green", "blue", "yellow", "purple", "orange"]

        for g in self.groups.keys():
            points = [ [a.maturity["DBE 12 da Classe N"], a.maturity["DBE 9 da Classe N"], a.maturity["DBE 15 da Classe N"]] for a in self.groups[g] ]
            for i in range(len(points)):
                points[i] = np.divide(points[i], sum(points[i]))
            td.scatter(points, color = self.colors.pop(), label=g)        
        ax.legend()

        if filenames[0] is None:
            plt.show()
        else:
            plt.savefig("output/" + filenames[0], dpi=400, bbox_inches="tight")

        fig, ax = plt.subplots()
        td = TernaryDiagram(['DBE5', 'DBE11', 'DBE9'], ax=ax)

        self.markers = ["o", "v", "^", "s", "h", "D"]
        self.colors = ["red", "green", "blue", "yellow", "purple", "orange"]

        for g in self.groups.keys():
            points = [ [a.maturity["DBE 5 da Classe O2"], a.maturity["DBE 11 da Classe O2"], a.maturity["DBE 9 da Classe O2"]] for a in self.groups[g] ]
            for i in range(len(points)):
                points[i] = np.divide(points[i], sum(points[i]))
            td.scatter(points, color = self.colors.pop(), label=g)        
        ax.legend()

        if filenames[1] is None:
            plt.show()
        else:
            plt.savefig("output/" + filenames[1], dpi=400, bbox_inches="tight")

        fig, ax = plt.subplots()
        td = TernaryDiagram(['DBE6', 'DBE13', 'DBE9'], ax=ax)

        self.markers = ["o", "v", "^", "s", "h", "D"]
        self.colors = ["red", "green", "blue", "yellow", "purple", "orange"]

        for g in self.groups.keys():
            points = [ [a.maturity["DBE 6 da Classe O2"], a.maturity["DBE 13 da Classe O2"], a.maturity["DBE 9 da Classe O2"]] for a in self.groups[g] ]
            for i in range(len(points)):
                points[i] = np.divide(points[i], sum(points[i]))
            td.scatter(points, color = self.colors.pop(), label=g)        
        ax.legend()

        if filenames[2] is None:
            plt.show()
        else:
            plt.savefig("output/" + filenames[2], dpi=400, bbox_inches="tight")


        fig, ax = plt.subplots()
        self.markers = ["o", "v", "^", "s", "h", "D"]
        self.colors = ["red", "green", "blue", "yellow", "purple", "orange"]
        ax.set_xlabel("DBE9/DBE12 da Classe N")
        ax.set_ylabel("DBE5/DBE9 da Classe O2")
        for g in self.groups.keys():
            y = [ a.maturity["DBE9/DBE12 da Classe N"] for a in self.groups[g] ]
            x = [ a.maturity["DBE5/DBE9 da Classe O2"] for a in self.groups[g] ]
            if np.nan not in x and np.nan not in y: 
                ax.scatter(x, y, color=self.colors.pop(), marker=self.markers.pop(), label=g)
        ax.legend()

        if filenames[3] is None:
            plt.show()
        else:
            plt.savefig("output/" + filenames[3], dpi=400, bbox_inches="tight")


    def biodegradation(self, filenames=None):
        fig, ax = plt.subplots()

        self.markers = ["o", "v", "^", "s", "h", "D"]
        self.colors = ["red", "green", "blue", "yellow", "purple", "orange"]

        ms = copy(self.markers)
        cs = copy(self.colors)

        ax.set_xlabel("Índice SA (%)")
        ax.set_ylabel("Razão A/C modificada")
        for g in self.groups.keys():
            y = [ a.biodegradation["A/C mod."] for a in self.groups[g] ]
            x = [ a.biodegradation["Indice S/A (%)"] for a in self.groups[g] ]
            if np.nan not in x and np.nan not in y: 
                ax.scatter(x, y, color=cs.pop(), marker=ms.pop(), label=g)
        ax.legend()

        if filenames[0] is None:
            plt.show()
        else:
            plt.savefig("output/" + filenames[0], dpi=400, bbox_inches="tight")

        fig, ax = plt.subplots()
        ms = copy(self.markers)
        cs = copy(self.colors)
        ax.set_xlabel("Índice SA modificada (%)")
        ax.set_ylabel("Razão A/C modificada")
        for g in self.groups.keys():
            y = [ a.biodegradation["A/C mod."] for a in self.groups[g] ]
            x = [ a.biodegradation["S/A mod. (%)"] for a in self.groups[g] ]
            if np.nan not in x and np.nan not in y: 
                ax.scatter(x, y, color=cs.pop(), marker=ms.pop(), label=g)
        ax.legend()

        if filenames[1] is None:
            plt.show()
        else:
            plt.savefig("output/" + filenames[1], dpi=400, bbox_inches="tight")

        fig, ax = plt.subplots()
        ms = copy(self.markers)
        cs = copy(self.colors)
        ax.set_xlabel("Índice MA1")
        ax.set_ylabel("Razão A/C")
        for g in self.groups.keys():
            y = [ a.biodegradation["A/C"] for a in self.groups[g] ]
            x = [ a.biodegradation["Indice MA1"] for a in self.groups[g] ]
            if np.nan not in x and np.nan not in y: 
                ax.scatter(x, y, color=cs.pop(), marker=ms.pop(), label=g)
        ax.legend()

        if filenames[2] is None:
            plt.show()
        else:
            plt.savefig("output/" + filenames[2], dpi=400, bbox_inches="tight")

        fig, ax = plt.subplots()
        ms = copy(self.markers)
        cs = copy(self.colors)
        ax.set_xlabel("Índice MA2")
        ax.set_ylabel("Razão A/C")
        for g in self.groups.keys():
            y = [ a.biodegradation["A/C"] for a in self.groups[g] ]
            x = [ a.biodegradation["Indice MA2"] for a in self.groups[g] ]
            if np.nan not in x and np.nan not in y: 
                ax.scatter(x, y, color=cs.pop(), marker=ms.pop(), label=g)
        ax.legend()

        if filenames[3] is None:
            plt.show()
        else:
            plt.savefig("output/" + filenames[3], dpi=400, bbox_inches="tight")

    def paleoenvironment(self, filenames=None):
        fig, ax = plt.subplots()

        self.markers = ["o", "v", "^", "s", "h", "D"]
        self.colors = ["red", "green", "blue", "yellow", "purple", "orange"]

        ms = copy(self.markers)
        cs = copy(self.colors)

        ax.set_xlabel("∑(DBE 2 a 14) / \n[∑(DBE 2 a 14) + ∑(DBE 15 a 29)] da class NO")
        ax.set_ylabel("∑(DBE 6 a 10) / \n[∑(DBE 6 a 10) + ∑(DBE 10 a 27)] da class N")
        for g in self.groups.keys():
            y = [ a.paleoenvironment["Razao Rocha 5"] for a in self.groups[g] ]
            x = [ a.paleoenvironment["Razao Rocha 6"] for a in self.groups[g] ]
            if np.nan not in x and np.nan not in y: 
                ax.scatter(x, y, color=cs.pop(), marker=ms.pop(), label=g)
        ax.legend()
        if filenames[0] is None:
            plt.show()
        else:
            plt.savefig("output/" + filenames[0], dpi=400)

        fig, ax = plt.subplots()
        ms = copy(self.markers)
        cs = copy(self.colors)
        ax.set_xlabel("∑(DBE 8, 9)da class N + ∑(DBE 9,10) da class NO / \n[∑(DBE 8, 9, 13, 16) da class N + ∑(DBE 9, 10, 19, 20)] da class NO")
        ax.set_ylabel("∑(DBE 4 a 12)da class O1 + (DBE 12) da class O2 / \n[∑(DBE 4, 12, 14, 16) da class O1 + ∑(DBE 12, 13)] da class O2")
        for g in self.groups.keys():
            y = [ a.paleoenvironment["Razao Rocha 7"] for a in self.groups[g] ]
            x = [ a.paleoenvironment["Razao Rocha 8"] for a in self.groups[g] ]
            if np.nan not in x and np.nan not in y: 
                ax.scatter(x, y, color=cs.pop(), marker=ms.pop(), label=g)
        ax.legend()
        if filenames[1] is None:
            plt.show()
        else:
            plt.savefig("output/" + filenames[1], dpi=400)

        fig, ax = plt.subplots()
        ms = copy(self.markers)
        cs = copy(self.colors)
        ax.set_xlabel("∑(DBE 4 a 10) /\n[∑(DBE 4 a 10) + ∑(DBE 11 a 23)] da class O1")
        ax.set_ylabel("∑(DBE 1 a 7) /\n[∑(DBE 1 a 7) + ∑(DBE 8 a 25)] da class O2")
        for g in self.groups.keys():
            y = [ a.paleoenvironment["Razao Rocha 1"] for a in self.groups[g] ]
            x = [ a.paleoenvironment["Razao Rocha 2"] for a in self.groups[g] ]
            if np.nan not in x and np.nan not in y: 
                ax.scatter(x, y, color=cs.pop(), marker=ms.pop(), label=g)
        ax.legend()
        if filenames[2] is None:
            plt.show()
        else:
            plt.savefig("output/" + filenames[2], dpi=400)

        fig, ax = plt.subplots()
        ms = copy(self.markers)
        cs = copy(self.colors)
        ax.set_xlabel("(DBE 4) da class O1 (%)")
        ax.set_ylabel("(DBE 10) da class NO (%)")
        for g in self.groups.keys():
            y = [ a.paleoenvironment["Razao Rocha 3 (%)"] for a in self.groups[g] ]
            x = [ a.paleoenvironment["Razao Rocha 4 (%)"] for a in self.groups[g] ]
            if np.nan not in x and np.nan not in y: 
                ax.scatter(x, y, color=cs.pop(), marker=ms.pop(), label=g)
        ax.legend()

        plt.autoscale()
        if filenames[3] is None:
            plt.show()
        else:
            plt.savefig("output/" + filenames[3], dpi=400)

    def class_dbe(self, class_, filename=None):
        fig, ax = plt.subplots()
        self.markers = ["o", "v", "^", "s", "h", "D"]
        self.colors = ["red", "green", "blue", "yellow", "purple", "orange"]
        min_dbe = 1000
        max_dbe = -1
        for g in self.groups.keys():
            for s in self.groups[g]:
                x, y = s.class_dbe(class_)
                if len(x) != 0:
                    y = np.divide(y, sum(y)*0.01)
                    ax.plot(x, y, linestyle="solid", label=s.name, marker = self.markers.pop())
                    min_dbe = min(min(x), min_dbe)
                    max_dbe = max(max(x), max_dbe)

        ax.legend()
        ax.set_title("Classe " + class_)
        ax.set_ylabel("Abundância Relativa (%)")
        ax.set_xlabel("DBE")
        ax.set_xticks(range(min_dbe, max_dbe+1))

        if filename is None:
            plt.show()
        else:
            plt.savefig("output/" + filename, dpi=400, bbox_inches="tight")

    def c_dbe(self, hclass, dbe, filename=None):
        fig, ax = plt.subplots()
        markers = ["o", "v", "^", "s", "h", "D"]
        colors = ["red", "green", "blue", "yellow", "purple", "orange"]
        cs = list()
        for g in self.groups.keys():
            for s in self.groups[g]:
                if hclass in s.hclasses:
                    if dbe in s.hclasses[hclass].dbes:
                        cs.extend(s.hclasses[hclass].dbes.keys())
        cs = sorted(np.unique(cs))
        for g in self.groups.keys():
            for s in self.groups[g]:
                if hclass in s.hclasses:
                    if dbe in s.hclasses[hclass].dbes:
                        y = list()
                        for c in cs:
                            if c in s.hclasses[hclass].dbes[dbe].c_intensity:
                                y.append(s.hclasses[hclass].dbes[dbe].c_intensity[c])
                            else:
                                y.append(0.0)
                        y = np.divide(y, sum(y)*0.01)
                        ax.plot(cs, y, linestyle="solid", label=s.name, marker=markers.pop(), color=colors.pop())
        
        ax.legend()
        ax.set_title("Classe %s, DBE%.0f" %(hclass, dbe))
        ax.set_ylabel("Abundância Relativa (%)")
        ax.set_xlabel("Número de Carbonos")
        ax.set_xticks(cs)

        if filename is None:
            plt.show()
        else:
            plt.savefig("output/" + filename, dpi=400, bbox_inches="tight")

    #def heteroatomic_dist(self, sample, filename=None):
    def heteroatomic_dist(self, filename=None):
        data = dict()
        columns = list()
        hclasses = list()

        for k in self.groups.keys():
            for s in self.groups[k]:
                for hc in s.hclasses.keys():
                    if hc not in hclasses:
                        hclasses.append(hc)
                        
        for k in self.groups.keys():
            for s in self.groups[k]:
                columns.append(s.name)
                intensities = list()
                for hc in hclasses:
                    if hc in s.hclasses:
                        intensities.append(s.hclasses[hc].intensity)
                    else:
                        intensities.append(0.0)
                intensities = np.divide(intensities, s.intensity*0.01)
                data[s.name] = intensities

        df = pd.DataFrame(data, columns=columns, index=hclasses)
        df.plot.bar()
        plt.xlabel("Classes Heteroatômicas")
        plt.ylabel("Abundância Relativa (%)")

        if filename is None:
            plt.show()
        else:
            plt.savefig("output/" + filename, dpi=400, bbox_inches="tight")

    def add_group(self, samples, name):
        if len(samples) == 0:
            raise Exception("Grupo vazio")
        
        for s in samples:
            if type(s) is not Sample:
                raise Exception("Os membros do grupo devem ser apenas amostras (tipo Sample)!")
        
        self.groups[name] = samples

def dbe_c(sample, hclass, filename=None):
    hc = sample.hclasses[hclass]
    cs = list()
    dbes = sorted(list(hc.dbes.keys()))
    data = list()
    for dbe in dbes:
        for c in hc.dbes[dbe].c_intensity.keys():
            if c not in cs:
                cs.append(c)
    cs.sort()
    for c in cs:
        line = list()
        for dbe in dbes:
            if c in hc.dbes[dbe].c_intensity:
                line.append(hc.dbes[dbe].c_intensity[c])
            else:
                line.append(0.0)
        data.append(line)
    m = max([ max(a) for a in data ])
    data = np.divide(data, m)
    fig, ax = plt.subplots()
    colors = [(0, (1,1,1)), (0.1,(0,0,1)), (0.3,(0,0.7,0)), (0.5,(1,1,0)), (0.6,(1,1,0)), (1,(1,0,0))]
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("test", colors, N=1000)
    data = np.transpose(data)
    im = ax.imshow(data,interpolation="nearest", cmap=cmap)
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    cbar = ax.figure.colorbar(im, cax=cax, **{})
    cbar.ax.set_ylabel("Abundância (Normalizada)", rotation=-90, va="bottom")
    ax.invert_yaxis()
    ax.set_title("%s Classe %s" % (sample.name, hc.name))
    ax.set_xlabel("Número de Carbono")
    ax.set_ylabel("DBE")

    xt = np.multiply(range(int((len(cs)+1)/5)), 5)
    yt = np.multiply(range(int((len(dbes)+1)/5)), 5)

    labels = ["%.0f" % dbes[i] for i in yt if i < len(dbes)]
    ax.set_yticks(ticks=yt, labels=labels)
    labels = ["%.0f" % cs[i] for i in xt if i < len(cs)]
    ax.set_xticks(ticks=xt, labels=labels)

    plt.tight_layout()
    
    if filename is None:
        plt.show()
    else:
        plt.savefig("output/" + filename, dpi=400, bbox_inches="tight")