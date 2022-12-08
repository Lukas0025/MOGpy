import numpy as np
from .Chromosome import Colors, plt

class OrChromosome:
    def __init__(self, chr):
        self._chromosomes = chr

    def exec(self, method, params):
        out = []
        
        for chromosome in self._chromosomes:
            out.append(getattr(chromosome, method)(*params)) 

        return out

    def exec2d(self, method, array):
        out = []

        for item in array:

            out += self.exec(method, (item,))

        return out
    
    @staticmethod
    def fromChromosome(chr):
        if not(hasattr(chr, '_chromosomes')):
            chr = OrChromosome([chr])

        return chr

    def seq(self, separator=""):
        return self.exec("seq", (separator))

    def numSeq(self, separator=""):
        return self.exec("seq", (separator))

    def show(self, ploter = plt, show = True, colors = None):
        if colors is None:
            return self.exec("show", (ploter, show))

        return self.exec("show", (ploter, show, colors))

    def hist(self, ploter = plt, show = True, alpha = 1, density = True, colors = None):
        if colors is None:
            return self.exec("hist", (ploter, show, alpha, density))

        return self.exec("hist", (ploter, show, alpha, density, colors))

    def getChromosomes(self):
        return self._chromosomes

    def _getConCatChromosomes(self, input):
        chromosomes = self._chromosomes

        if hasattr(input, '_chromosomes'):
            chromosomes += input._chromosomes
        else:
            chromosomes.append(input)

        return chromosomes

    def __len__(self):
        return len(self._chromosomes)

    def __getitem__(self, i):
        return self._chromosomes[i]
    
    def __add__(self, chromosome2):
        return self.__class__(self._getConCatChromosomes(chromosome2))

    def __mul__(self, chromosome2):
        chromosome2 = self.fromChromosome(chromosome2)
        return self.__class__(self.exec2d("__mul__", chromosome2))

    def count(self, chromosome2):
        chromosome2 = self.fromChromosome(chromosome2)
        return np.array(self.exec2d("count", chromosome2)).sum()

    def __eq__(self, chromosome2):
        chromosome2 = self.fromChromosome(chromosome2)
        return True in self.exec2d("__eq__", chromosome2)

    def __ne__(self, chromosome2):
        chromosome2 = self.fromChromosome(chromosome2)
        return all(self.exec2d("__ne__", chromosome2))

    def __contains__(self, chromosome2):
        chromosome2 = self.fromChromosome(chromosome2)
        return True in self.exec2d("__contains__", chromosome2)

    def __pow__(self, num):
        return self.pow(num)
    
    def pow(self, num):
        res = self.__class__(self._chromosomes)
        for i in range(1, num):
            res = res * res

        return res

    def reverse(self):
        return self.__class__(self.exec("reverse", ()))

    ## Suported only by BioChromosome
    def complement(self):
        return self.__class__(self.exec("complement", ()))

    def invComplement(self):
        return self.__class__(self.exec("invComplement", ()))