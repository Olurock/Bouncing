import timeit
from array import array

nb_samples = 44100

buf = array('h', b"\x00\x00" * nb_samples)

buf1 = array('h', b"\x00\x00" * nb_samples)
buf2 = array('h', b"\x00\x00" * nb_samples)
buf3 = array('h', b"\x00\x00" * nb_samples)
buf4 = array('h', b"\x00\x00" * nb_samples)
buffers = [buf1, buf2, buf3, buf4]

def func1():
    for i in range(0, nb_samples):
        buf[i] = 0
    return buf


def func2():
    return buf[0:nb_samples]


def func3():
    for i in range(0, nb_samples):
        buf[i] = 0
        for j in range(0, len(buffers)):
            buf[i] += buffers[j][i]
    return buf


def func4():
    s = [sum(x) for x in zip(*buffers)]
    return array('h', s)


def func5():
    s = map(sum, zip(*buffers))
    return array('h', s)


print(timeit.repeat(setup="from __main__ import func4", stmt="func4()",
                          repeat=3, number=100))
print(timeit.repeat(setup="from __main__ import func5", stmt="func5()",
                          repeat=3, number=100))