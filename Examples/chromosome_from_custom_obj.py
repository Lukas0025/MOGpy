from MOGpy import Chromosome

# definition of nucleotide for Chromosome
class myNucleotide:
    def __init__(self, id):
        self._id = id

    def getId(self): # needed
        return self._id # must be unicate in whole chromosome

    def getNumericId(self): # needed
        return len(self._id) # must be unicate in whole chromosome

    def describe(self): # optimal
        return "mynucleotide {} with number {}".format(self.getId(), self.getNumericId())

# load chromosome as chromosome on generic objects
a  = Chromosome([myNucleotide("hello"), myNucleotide("word"), myNucleotide("1")])
wd = Chromosome([myNucleotide("word")])

print(a.seq(";"))

# concate chromosomes
b = wd + a

print(b.seq(";"))

# show histogram
b.hist()

# show chromosome
b.show()

# count of CG in chromosome
print("count of WORD in A => {}".format(
    a.count(wd)
))

# compare chromosomes
print("a == word => {}".format(
    a == wd
))

# is chromosome in another
print("word in a => {}".format(
    wd in a
))

# access nucleotide in chromosome
print("a on 0 position {}".format(
    a[0]
))

# print description of nucleotide
print("a on 0 position describe {}".format(
    a[0].describe()
))