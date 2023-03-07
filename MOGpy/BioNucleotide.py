from .DummyNucleotide import DummyNucleotide

bioNucleotideLUT = {
    "A": "adenine",
    "C": "cytosine",
    "G": "guanine",
    "T": "thymine",
    "U": "uracil",
    "N": "not defined",
    "-": "space"
}

bioNucleotideNumLUT = {
    "A": 1,
    "C": 2,
    "G": 3,
    "T": 4,
    "U": 5,
    "N": 6,
    "-": 7
}

complementLUT = {
    "A": "T",
    "U": "A",
    "T": "A",
    "G": "C",
    "C": "G",
    "N": "N",
    "-": "-"
}

invComplementLUT = {v: k for k, v in complementLUT.items()}

class BioNucleotide(DummyNucleotide):
    def __init__(self, id):

        if not(id in "ACGTUN-"):
            raise ValueError("Unknow nucleotide ID {}".format(id))

        super().__init__(id)

    def getNumericId(self):
        return bioNucleotideNumLUT[self.getId()]

    def complement(self):
        return BioNucleotide(complementLUT[self.getId()])

    def invComplement(self):
        return BioNucleotide(invComplementLUT[self.getId()])

    def describe(self):
        return bioNucleotideLUT[self.getId()]