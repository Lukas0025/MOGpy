from parrent import MOGpy

def test_load():
    a = MOGpy.Chromosome.fromStr("agc")
    b = a.reverse()

    c = a + b

    assert len(c) == 2
    assert c[0] == a           or c [1] == a
    assert c[0] == a.reverse() or c [1] == a.reverse()


def test_loadBio():
    a = MOGpy.BioChromosome.fromStr("agc")
    b = a.reverse()

    c = a + b

    assert len(c) == 2
    assert c[0] == a           or c [1] == a
    assert c[0] == a.reverse() or c [1] == a.reverse()

def test_getChromosomes():
    a = MOGpy.BioChromosome.fromStr("agc")
    b = a.reverse()

    c = a + b

    assert len(c.getChromosomes()) == 2
    assert a in c.getChromosomes()
    assert b in c.getChromosomes()


def test_multiOr():
    a = MOGpy.BioChromosome.fromStr("agc")
    b = a.reverse()
    t = MOGpy.BioChromosome.fromStr("t")

    c = (a + b) + (a + t)

    assert len(c) == 4
    assert a in c.getChromosomes()
    assert b in c.getChromosomes()
    assert t in c.getChromosomes()

def test_seq():
    a = MOGpy.BioChromosome.fromStr("agc")
    b = a.reverse()

    c = a + b

    assert len(c.seq()) == 2
    assert "AGC" in c.seq()
    assert "CGA" in c.seq()

def test_concat():
    a = MOGpy.BioChromosome.fromStr("agc")
    b = a.reverse()
    t = MOGpy.BioChromosome.fromStr("t")

    c = a + b
    d = c * a
    e = a * c

    assert len(d) == 2
    assert len(e) == 2
    assert "AGCAGC" in d.seq()
    assert "CGAAGC" in d.seq()
    assert "AGCAGC" in e.seq()
    assert "AGCCGA" in e.seq()

def test_count():
    a = MOGpy.BioChromosome.fromStr("a")
    t = MOGpy.BioChromosome.fromStr("t")
    g = MOGpy.BioChromosome.fromStr("g")
    test = MOGpy.BioChromosome.fromStr("aaaaagtaaaataggggtgaaaa")

    f = (a + g) * t * (a + g)

    assert len(f) == 4
    assert test.count(f) == 3

def test_invCount():
    a = MOGpy.BioChromosome.fromStr("a")
    t = MOGpy.BioChromosome.fromStr("t")
    g = MOGpy.BioChromosome.fromStr("g")

    test = MOGpy.BioChromosome.fromStr("a")

    f = (a + g) * t * (a + g)

    assert len(f) == 4
    assert f.count(test) == 4

def test_eq():
    a = MOGpy.BioChromosome.fromStr("a")
    t = MOGpy.BioChromosome.fromStr("t")
    g = MOGpy.BioChromosome.fromStr("g")

    test  = MOGpy.BioChromosome.fromStr("a")
    test1 = MOGpy.BioChromosome.fromStr("atg")
    test2 = MOGpy.BioChromosome.fromStr("ata")

    f = (a + g) * t * (a + g)

    assert not(f == test)
    assert f == test1
    assert test1 == f
    assert f == test2

def test_ne():
    a = MOGpy.BioChromosome.fromStr("a")
    t = MOGpy.BioChromosome.fromStr("t")
    g = MOGpy.BioChromosome.fromStr("g")

    test  = MOGpy.BioChromosome.fromStr("a")
    test1 = MOGpy.BioChromosome.fromStr("atg")
    test2 = MOGpy.BioChromosome.fromStr("ata")

    f = (a + g) * t * (a + g)

    assert f != test
    assert test != f
    assert not(f != test1)
    assert not(f != test2)

def test_contains():
    a = MOGpy.BioChromosome.fromStr("a")
    t = MOGpy.BioChromosome.fromStr("t")
    g = MOGpy.BioChromosome.fromStr("g")

    test  = MOGpy.BioChromosome.fromStr("ag")
    test1 = MOGpy.BioChromosome.fromStr("ggatggg")
    test2 = MOGpy.BioChromosome.fromStr("ggatagg")

    f = (a + g) * t * (a + g)

    assert not(f in test)
    assert not(test in f)
    assert f in test1
    assert f in test2

def test_reverse():
    a = MOGpy.BioChromosome.fromStr("ag")
    b = MOGpy.BioChromosome.fromStr("ta")

    test  = MOGpy.BioChromosome.fromStr("ga")
    test1 = MOGpy.BioChromosome.fromStr("at")

    f = a + b
    f = f.reverse()

    assert len(f) == 2
    assert test in f
    assert test1 in f

def test_powOp():
    a = MOGpy.BioChromosome.fromStr("ag")
    b = MOGpy.BioChromosome.fromStr("ta")

    f = (a + b) ** 2

    # (ag + ta) (ag + ta) = agag, agta, taag, tata

    assert len(f) == 4
    assert MOGpy.BioChromosome.fromStr("agag") in f
    assert MOGpy.BioChromosome.fromStr("agta") in f
    assert MOGpy.BioChromosome.fromStr("tata") in f
    assert MOGpy.BioChromosome.fromStr("taag") in f

def test_pow():
    a = MOGpy.BioChromosome.fromStr("ag")
    b = MOGpy.BioChromosome.fromStr("ta")

    f = (a + b).pow(2)

    assert len(f) == 4
    assert MOGpy.BioChromosome.fromStr("agag") in f
    assert MOGpy.BioChromosome.fromStr("agta") in f
    assert MOGpy.BioChromosome.fromStr("tata") in f
    assert MOGpy.BioChromosome.fromStr("taag") in f

def test_complement():
    a = MOGpy.BioChromosome.fromStr("ttaagatttgcgctttgccaactgtacacccaacctcgg")
    b = MOGpy.BioChromosome.fromStr("ta")

    test  = MOGpy.BioChromosome.fromStr("AATTCTAAACGCGAAACGGTTGACATGTGGGTTGGAGCC")
    test1 = MOGpy.BioChromosome.fromStr("at")

    f = (a + b)
    f = f.complement()

    assert len(f) == 2
    assert test in f
    assert test1 in f

def test_invComplement():
    a = MOGpy.BioChromosome.fromStr("at")
    b = MOGpy.BioChromosome.fromStr("cg")

    test  = MOGpy.BioChromosome.fromStr("ta")
    test1 = MOGpy.BioChromosome.fromStr("gc")

    f = (a + b)
    f = f.invComplement()

    assert len(f) == 2
    assert test in f
    assert test1 in f
