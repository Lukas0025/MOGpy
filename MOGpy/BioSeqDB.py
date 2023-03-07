from .BioChromosome import BioChromosome

# Nucleotides
a = BioChromosome.fromStr("A")
c = BioChromosome.fromStr("C")
t = BioChromosome.fromStr("T")
g = BioChromosome.fromStr("G")
u = BioChromosome.fromStr("U")
n = BioChromosome.fromStr("N")

space = BioChromosome.fromStr("-")

class DNA:
    # Stop codons
    amber = BioChromosome.fromStr("TAG")
    ochre = BioChromosome.fromStr("TAA")
    opal  = BioChromosome.fromStr("TGA")
    umber = opal
    stop = amber + ochre + opal
    # Start Codons
    gtg      = BioChromosome.fromStr("GTG")
    ttg      = BioChromosome.fromStr("TTG")
    start    = BioChromosome.fromStr("ATG")
    startAll = start + ttg + gtg

class RNA:
    # Stop codons
    amber = BioChromosome.fromStr("UAG")
    ochre = BioChromosome.fromStr("UAA")
    opal  = BioChromosome.fromStr("UGA")
    umber = opal
    stop = amber + ochre + opal
    # Start Codons
    gug      = BioChromosome.fromStr("GUG")
    uug      = BioChromosome.fromStr("UUG")
    start    = BioChromosome.fromStr("AUG")
    startAll = start + uug + gug