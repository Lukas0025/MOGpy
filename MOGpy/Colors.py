import numpy

class Base:
    colors = [
        '#1f77b4',
        '#ff7f0e',
        '#2ca02c',
        '#d62728',
        '#9467bd',
        '#8c564b',
        '#e377c2',
        '#7f7f7f',
        '#bcbd22',
        '#17becf'
    ]

    bounds = None

class GeneticBase:
    colors = [
        '#64F73F',
        '#FFB340',
        '#EB413C',
        '#3C88EE',
        '#3C88EE'
    ]

    bounds = numpy.sort([
        1,
        2,
        3,
        4,
        5
    ])

class pupy:
    colors = [
        '#FF83FA',
        '#40E0D0',
        '#FF83FA',
        '#40E0D0',
        '#40E0D0'
    ]

    bounds = numpy.sort([
        1,
        2,
        3,
        4,
        5
    ])