import numpy as np
from .seed import rng
from core.constants import WIDTH,HEIGHT
SIZE=WIDTH*HEIGHT
def generate(seed):
    r=rng(seed)
    p=np.arange(SIZE)
    r.shuffle(p)
    return p
def inverse(p):
    inv=np.empty_like(p)
    for i,v in enumerate(p):
        inv[v]=i
    return inv