from core.utils import read_file
from core.metadata import build_metadata
from core.metadata import build_header
from core.bitstream import bytes_to_bits
from core.frame import split_frames
from core.frame import save_frames
from core.video import frames_to_video
class Encoder:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = read_file(filepath)
        self.metadata = build_metadata(filepath,self.data,)
        self.header=build_header(self.metadata,)
        self.stream=(self.header+self.metadata +self.data)
        self.bits = bytes_to_bits(
            self.stream,
        )
    def export_frames(self,folder="frames"):
        frames = split_frames(self.bits,)
        save_frames(frames,folder,)
    def export_video(self,output="output/output.mkv",fps=30,):
        self.export_frames()
        frames_to_video("frames",output,fps,)