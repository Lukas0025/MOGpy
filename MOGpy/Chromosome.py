from .DummyNucleotide import DummyNucleotide
import matplotlib.pyplot as plt
from matplotlib import colors as plcolors
import numpy as np
from collections import Counter
from . import Colors
from .OrChromosome import OrChromosome

class Chromosome:
    def __init__(self, seq = []):
        self._seq = seq
        self._description = None

    def __mul__(self, chromosome2):
        if hasattr(chromosome2, '_chromosomes'):
            return OrChromosome.fromChromosome(self) * chromosome2

        return self.__class__(self._seq + chromosome2._seq)

    def describe(self):
        return {
            'Description': self._description,
            'Lenght': self.__len__()
        }

    def setDescription(self, description):
        self._description = description

    def copy(self):
        return self.__class__(self._seq)

    def __add__(self, chromosome2):
        chromosomes = [self]

        if hasattr(chromosome2, '_chromosomes'):
            chromosomes += chromosome2._chromosomes
        else:
            chromosomes.append(chromosome2)

        return OrChromosome(chromosomes)

    def __pow__(self, num):
        return self.pow(num)

    def pow(self, num):
        return self.__class__(self._seq * num)

    def __eq__(self, chromosome2):
        if hasattr(chromosome2, '_chromosomes'):
            return OrChromosome.fromChromosome(self) == chromosome2

        return self.getIds() == chromosome2.getIds()

    def __ne__(self, chromosome2):
        if hasattr(chromosome2, '_chromosomes'):
            return OrChromosome.fromChromosome(self) != chromosome2

        return self.getIds() != chromosome2.getIds()

    def __contains__(self, chromosome2):
        if hasattr(chromosome2, '_chromosomes'):
            return chromosome2 in OrChromosome.fromChromosome(self)

        return chromosome2.numSeq(";") in self.numSeq(";")

    def count(self, chromosome2):
        if hasattr(chromosome2, '_chromosomes'):
            return OrChromosome.fromChromosome(self).count(chromosome2)

        return self.numSeq(";").count(chromosome2.numSeq(";"))

    def __getitem__(self, i):
        return self._seq[i]
    
    def __len__(self):
        return len(self._seq)

    def reverse(self):
        return self.__class__(list(reversed(self._seq)))

    def re(self, regex):
        pass

    def find(self, chromosome):
        pass

    def reType(self, type):
        return type(self._seq)

    def seq(self, separator=""):
        return separator.join(self.getIds())

    def numSeq(self, separator=""):
        return separator.join(str(id) for id in self.getNumericIds())

    def getIds(self):
        return [i.getId() for i in self._seq]

    def getNumericIds(self):
        return [i.getNumericId() for i in self._seq]

    def show(self, ploter = plt, show = True, colors = Colors.Base):

        cmap = plcolors.ListedColormap(colors.colors)

        norm = None
        if colors.bounds is not None:
            norm = plcolors.BoundaryNorm(colors.bounds, cmap.N)

        ploter.imshow(
            [self.getNumericIds()],
            extent=[-0.5, len(self) - 0.5, 0, len(self) / 20],
            cmap=cmap,
            interpolation='nearest',
            origin='lower',
            norm=norm
        )

        ploter.locator_params(axis="both", integer=True, tight=True)
        
        ax = ploter.gca()
        ax.get_yaxis().set_visible(False)

        if show:
            ploter.show()

    def hist(self, ploter = plt, show = True, alpha = 1, density = True, colors = Colors.Base):
        
        histogram = Counter(self.getIds())

        bars   = histogram.keys()
        height = np.array(list(histogram.values()))

        if density:
            height = height / len(self)

        x_pos  = np.arange(len(bars))
        
        ploter.bar(x_pos, height, alpha = alpha, color = colors.colors)
        
        ploter.xlabel('Nucleotides')
        ploter.ylabel('Counts')

        if density:
            ploter.ylabel('Probability')
        
        ploter.xticks(x_pos, bars)
        
        if show:
            ploter.show()

    def gene(self, start, end):
        return self.__class__(self[start:end])

    @staticmethod
    def fromStr(string, uppercase = True, nucleotideClass = DummyNucleotide):
        if uppercase:
            string = string.upper()

        arr = []
        for part in string:
            arr.append(nucleotideClass(part))

        return Chromosome(arr)
