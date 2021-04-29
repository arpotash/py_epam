import hashlib
import random
import struct
import time
from multiprocessing import Pool


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def distribution_pool():
    sequence = [num for num in range(500)]
    p = Pool(50)
    result = sum(p.map(slow_calculate, sequence))
    return result
