import struct
from pathlib import Path
from core.constants import MAGIC
from core.constants import VERSION
from core.constants import FLAGS
from core.hash import sha256
def build_metadata(filepath, data):
    filename = Path(filepath).name.encode()
    metadata = (struct.pack(">H", len(filename))+ filename+ struct.pack(">Q", len(data))+ sha256(data))
    return metadata
def build_header(metadata):
    return struct.pack(">4sHHQ",MAGIC,VERSION,FLAGS,len(metadata),)
def parse_header(stream):
    magic, version, flags, metadata_length = struct.unpack(">4sHHQ",stream[:16],)
    return {
        "magic": magic,
        "version": version,
        "flags": flags,
        "metadata_length": metadata_length,
    }
def parse_metadata(data):
    offset = 0
    filename_length = struct.unpack(">H",data[offset:offset+2],)[0]
    offset+=2
    filename=data[offset:offset+filename_length].decode()
    offset += filename_length
    content_length = struct.unpack(">Q",data[offset:offset+8],)[0]
    offset += 8
    sha = data[
        offset:offset+32
    ]
    return {
        "filename": filename,
        "content_length": content_length,
        "sha256": sha,
    }