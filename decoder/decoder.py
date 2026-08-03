from core.video import video_to_frames
from core.frame import load_frames
from core.bitstream import bits_to_bytes
from core.metadata import parse_header
from core.metadata import parse_metadata
from core.hash import sha256
from core.utils import write_file
class Decoder:
    def __init__(self, video):
        self.video = video
    def decode(self, output="output"):
        video_to_frames(self.video,"temp",)
        bits=load_frames("temp",)
        stream=bits_to_bytes(bits)
        header=parse_header(stream)
        metadata_start=16
        metadata_end=(metadata_start+header["metadata_length"])
        metadata=parse_metadata(stream[metadata_start:metadata_end])
        file_start=metadata_end
        file_end=(file_start+metadata["content_length"])
        data=stream[file_start:file_end]
        if sha256(data) != metadata["sha256"]:
            raise ValueError("Checksum mismatch!")
        write_file(
            f"{output}/{metadata['filename']}",data,)
        print("Recovered successfully!")