from parrent import MOGpy

def test_load():
    a = MOGpy.BioChromosome(["A", 1])

    assert a[0] == "A" and a[1] == 1
    assert len(a) == 2

def test_loadStr():
    a = MOGpy.BioChromosome.fromStr("agc")

    assert a[0].getId() == "A" and a[1].getId() == "G" and a[2].getId() == "C"
    assert len(a) == 3

def test_comp():
    a = MOGpy.BioChromosome.fromStr("acac")
    b = MOGpy.BioChromosome.fromStr("acac")
    c = MOGpy.BioChromosome.fromStr("cucu")

    assert a == a
    assert a == b
    assert a != c
    assert not(a != b)
    assert not(b == c)

def test_concat():
    a = MOGpy.BioChromosome.fromStr("agag")
    b = MOGpy.BioChromosome.fromStr("cucu")
    c = MOGpy.BioChromosome.fromStr("agagcucu")

    assert a + b == c
    assert len(a) + len(b) == len(c)

def test_contains():
    a = MOGpy.BioChromosome.fromStr("agag")
    b = MOGpy.BioChromosome.fromStr("gaga")
    c = MOGpy.BioChromosome.fromStr("ccuuagagcucu")

    assert a in c
    assert not(a in b)
    assert not(b in c)
    assert not(c in b)

def test_count():
    a = MOGpy.BioChromosome.fromStr("a")
    b = MOGpy.BioChromosome.fromStr("cucu")
    c = MOGpy.BioChromosome.fromStr("ccuuagagcucu")

    assert a.count(a) == 1
    assert a.count(b) == 0
    assert c.count(a) == 2
    assert c.count(b) == 1

def test_reverse():
    a = MOGpy.BioChromosome.fromStr("actgu")
    b = MOGpy.BioChromosome.fromStr("ugtca")

    assert a.reverse() == b

def test_reverse_loop():
    a = MOGpy.BioChromosome.fromStr("actgu")

    assert a.reverse().reverse() == a

def test_power():
    a = MOGpy.BioChromosome.fromStr("a")
    b = MOGpy.BioChromosome.fromStr("aaa")

    assert a.pow(3) == b

def test_power_opt():
    a = MOGpy.BioChromosome.fromStr("acg")
    b = MOGpy.BioChromosome.fromStr("acgacgacg")

    assert a ** 3 == b

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