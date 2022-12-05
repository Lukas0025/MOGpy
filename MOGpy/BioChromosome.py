from .Chromosome import Chromosome, plt
from .BioNucleotide import BioNucleotide
from . import Colors

class BioChromosome(Chromosome):
    def __init__(self, seq = []):
        super().__init__(seq)

    def __add__(self, chromosome2):
        return super().__add__(chromosome2).reType(BioChromosome)

    def __pow__(self, num):
        return super().__pow__(num).reType(BioChromosome)

    def pow(self, num):
        return super().pow(num).reType(BioChromosome)

    def show(self, ploter=plt, show=True, colors=Colors.GeneticBase):
        return super().show(ploter, show, colors)

    def reverse(self):
        return super().reverse().reType(BioChromosome)

    def complement(self):
        seq = [i.complement() for i in self._seq]
        return BioChromosome(seq)

    def invComplement(self):
        seq = [i.invComplement() for i in self._seq]
        return BioChromosome(seq)

    def fromStr(string, uppercase = True, nucleotideClass = BioNucleotide):
        if uppercase:
            string = string.upper()

        arr = []
        for part in string:
            arr.append(nucleotideClass(part))

        return BioChromosome(arr)
