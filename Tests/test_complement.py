from parrent import MOGpy

def test_complement():
    base       = MOGpy.BioChromosome.fromStr("ttaagatttgcgctttgccaactgtacacccaacctcgg")
    complement = MOGpy.BioChromosome.fromStr("AATTCTAAACGCGAAACGGTTGACATGTGGGTTGGAGCC")

    assert base.complement() == complement

def test_invComplement():
    base        = MOGpy.BioChromosome.fromStr("AATTCTAAACGCGAAACGGTTGACATGTGGGTTGGAGCC")
    rComplement = MOGpy.BioChromosome.fromStr("ttaagatttgcgctttgccaactgtacacccaacctcgg")

    assert base.invComplement() == rComplement

def test_loop():
    base        = MOGpy.BioChromosome.fromStr("AATTCTAAACGCGAAACGGTTGACATGTGGGTTGGAGCC")

    assert base.complement().invComplement() == base