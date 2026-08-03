from pathlib import Path
import numpy as np
from PIL import Image
from core.constants import WIDTH
from core.constants import HEIGHT
from core.constants import BITS_PER_FRAME
def split_frames(bits):
    pad = (-len(bits)) % BITS_PER_FRAME
    if pad:
        bits = np.pad(bits,(0, pad),constant_values=0,)
    return bits.reshape(-1,BITS_PER_FRAME,)
def load_frames(folder):
    folder=Path(folder)
    files=sorted(folder.glob("*.png"),key=lambda x: int(x.stem.split("_")[1]),)
    frames=[]
    for file in files:
        frames.append(image_to_frame(file))
    return np.concatenate(frames)
def frame_to_image(frame):
    img=frame.reshape(HEIGHT,WIDTH,).astype(np.uint8)
    img*=255
    return Image.fromarray(img,mode="L",)
def save_frames(frames, folder):
    folder=Path(folder)
    folder.mkdir(parents=True,exist_ok=True,)
    for i, frame in enumerate(frames):
        frame_to_image(frame).save(folder/f"frame_{i}.png")
def image_to_frame(path):
    img = Image.open(path)
    arr = np.asarray(img,dtype=np.uint8,)
    arr=(arr > 127).astype(np.uint8)
    return arr.reshape(-1)