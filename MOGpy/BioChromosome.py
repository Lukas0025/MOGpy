from .Chromosome import Chromosome
from .BioNucleotide import BioNucleotide

class BioChromosome(Chromosome):
    def __init__(self, seq = []):
        super().__init__(seq)

    def __add__(self, chromosome2):
        return super().__add__(chromosome2).reType(BioChromosome)

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
