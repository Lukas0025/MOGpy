class DummyNucleotide:
    def __init__(self, id):
        self._id = id

    def getId(self):
        return self._id

    def getNumericId(self):
        return ord(self._id)

    def describe(self):
        return "dummyNucleotide {} with number {}".format(self.getId(), self.getNumericId())