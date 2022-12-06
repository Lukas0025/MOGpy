from .Chromosome import Chromosome, plt
from .BioNucleotide import BioNucleotide
from . import Colors

class BioChromosome(Chromosome):
    def __init__(self, seq = []):
        super().__init__(seq)

    def show(self, ploter=plt, show=True, colors=Colors.GeneticBase):
        return super().show(ploter, show, colors)

    def complement(self):
        seq = [i.complement() for i in self._seq]
        return self.__class__(seq)

    def invComplement(self):
        seq = [i.invComplement() for i in self._seq]
        return self.__class__(seq)

    @staticmethod
    def fromStr(string, uppercase = True, nucleotideClass = BioNucleotide):
        if uppercase:
            string = string.upper()

        arr = []
        for part in string:
            arr.append(nucleotideClass(part))

        return BioChromosome(arr)
