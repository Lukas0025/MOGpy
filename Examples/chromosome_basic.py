from MOGpy import Chromosome

# load chromosome for str
a  = Chromosome.fromStr("CGTAACAAGGTTTCCGTAGGTGAACCTGCGGAAGGATCATTGATGAGACCGTGG")
cg = Chromosome.fromStr("CG")

# print loaded chromosome
print(a.seq())

# show chromosome a
a.show()

# show histogram
a.hist()

# concate chromosomes
b = cg * a

# print concatenate chromosomes
print(b.seq())

# count of CG in chromosome
print("count of CG in A => {} == {}".format(
    a.count(cg),
    a.count(Chromosome.fromStr("cg"))
))

# compare chromosomes
print("a == cg => {}".format(
    a == cg
))

# is chromosome in another
print("cg in a => {}".format(
    cg in a
))

# access nucleotide in chromosome
print("a on 0 position {}".format(
    a[0]
))

# print description of nucleotide
print("a on 0 position describe {}".format(
    a[0].describe()
))