import numpy as np
from .permutation import generate
from .permutation import inverse
WIDTH=1920
HEIGHT=1080
SIZE=WIDTH*HEIGHT
def transform(frame,seed):
    p=generate(seed)
    a=frame.reshape(SIZE)
    b=np.empty_like(a)
    b[p]=a
    return b.ravel()

def reconstruct(frame,seed):
    p=generate(seed)
    inv=inverse(p)
    a=frame.reshape(SIZE)
    b=np.empty_like(a)
    b[inv]=a
    return b.ravel()