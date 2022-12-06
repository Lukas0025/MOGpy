from parrent import MOGpy

def test_load():
    a = MOGpy.Chromosome(["A", 1])

    assert a[0] == "A" and a[1] == 1
    assert len(a) == 2

def test_loadStr():
    a = MOGpy.Chromosome.fromStr("abc")

    assert a[0].getId() == "A" and a[1].getId() == "B" and a[2].getId() == "C"
    assert len(a) == 3

def test_comp():
    a = MOGpy.Chromosome.fromStr("abab")
    b = MOGpy.Chromosome.fromStr("abab")
    c = MOGpy.Chromosome.fromStr("cucu")

    assert a == a
    assert a == b
    assert a != c
    assert not(a != b)
    assert not(b == c)

def test_concat():
    a = MOGpy.Chromosome.fromStr("abab")
    b = MOGpy.Chromosome.fromStr("cucu")
    c = MOGpy.Chromosome.fromStr("ababcucu")

    assert a + b == c
    assert len(a) + len(b) == len(c)

def test_contains():
    a = MOGpy.Chromosome.fromStr("abab")
    b = MOGpy.Chromosome.fromStr("baba")
    c = MOGpy.Chromosome.fromStr("ccuuababcucu")

    assert a in c
    assert not(a in b)
    assert not(b in c)
    assert not(c in b)

def test_count():
    a = MOGpy.Chromosome.fromStr("a")
    b = MOGpy.Chromosome.fromStr("cucu")
    c = MOGpy.Chromosome.fromStr("ccuuababcucu")

    assert a.count(a) == 1
    assert a.count(b) == 0
    assert c.count(a) == 2
    assert c.count(b) == 1

def test_reverse():
    a = MOGpy.Chromosome.fromStr("actgu")
    b = MOGpy.Chromosome.fromStr("ugtca")

    assert a.reverse() == b

def test_reverse_loop():
    a = MOGpy.Chromosome.fromStr("actgu")

    assert a.reverse().reverse() == a

def test_power():
    a = MOGpy.Chromosome.fromStr("a")
    b = MOGpy.Chromosome.fromStr("aaa")

    assert a.pow(3) == b

def test_power_opt():
    a = MOGpy.Chromosome.fromStr("acg")
    b = MOGpy.Chromosome.fromStr("acgacgacg")

    assert a ** 3 == b