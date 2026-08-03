# BitFrame

BitFrame is an experimental binary-to-video encoder that converts any file into a sequence of lossless video frames and reconstructs the original file without data loss.

The project explores video as a storage medium rather than a visual one, where every pixel represents binary data instead of image content.

---

## Features

* Encode any file into a lossless video
* Decode the video back into the original file
* Preserve original filename and file size
* SHA-256 integrity verification
* Modular architecture
* Designed for future extensions

---

## Architecture

```
                 Encoding Pipeline

 ┌──────────────┐
 │   Input File │
 └──────┬───────┘
        │
        ▼
 ┌──────────────┐
 │ Read Bytes   │
 └──────┬───────┘
        │
        ▼
 ┌──────────────┐
 │ Build Header │
 └──────┬───────┘
        │
        ▼
 ┌──────────────┐
 │ Build Metadata│
 └──────┬────────┘
        │
        ▼
 ┌──────────────┐
 │ Binary Stream│
 └──────┬───────┘
        │
        ▼
 ┌──────────────┐
 │ Bytes → Bits │
 └──────┬───────┘
        │
        ▼
 ┌──────────────┐
 │ Split Frames │
 └──────┬───────┘
        │
        ▼
 ┌──────────────┐
 │ PNG Frames   │
 └──────┬───────┘
        │
        ▼
 ┌──────────────┐
 │ Lossless MKV │
 └──────────────┘
```

```
                 Decoding Pipeline

 ┌──────────────┐
 │ Lossless MKV │
 └──────┬───────┘
        │
        ▼
 ┌──────────────┐
 │ Extract PNGs │
 └──────┬───────┘
        │
        ▼
 ┌──────────────┐
 │ Read Bits    │
 └──────┬───────┘
        │
        ▼
 ┌──────────────┐
 │ Bit Stream   │
 └──────┬───────┘
        │
        ▼
 ┌──────────────┐
 │ Parse Header │
 └──────┬───────┘
        │
        ▼
 ┌──────────────┐
 │ Parse Metadata│
 └──────┬────────┘
        │
        ▼
 ┌──────────────┐
 │ Recover File │
 └──────┬───────┘
        │
        ▼
 ┌──────────────┐
 │ Verify Hash  │
 └──────────────┘
```

---

## Binary Format

### Header

| Offset | Size | Description     |
| -----: | ---: | --------------- |
|      0 |    4 | Magic Number    |
|      4 |    2 | Version         |
|      6 |    2 | Flags           |
|      8 |    8 | Metadata Length |

### Metadata

| Field           | Type     |
| --------------- | -------- |
| Filename Length | uint16   |
| Filename        | bytes    |
| Content Length  | uint64   |
| SHA-256         | 32 bytes |

### Payload

```
+----------------+
| Header         |
+----------------+
| Metadata       |
+----------------+
| Original File  |
+----------------+
```

---

## Project Structure

```
BitFrame
├── core
│   ├── bitstream.py
│   ├── constants.py
│   ├── frame.py
│   ├── hash.py
│   ├── metadata.py
│   ├── utils.py
│   └── video.py
│
├── encoder
│   └── encoder.py
│
├── decoder
│   └── decoder.py
│
├── frames
├── output
├── temp
│
├── main.py
├── requirements.txt
└── README.md
```
---
## Installation
```bash
git clone https://github.com/GlassHandle/BitFrame.git
cd BitFrame
pip install -r requirements.txt
```
Install FFmpeg and ensure it is available in your system PATH.
---
## Usage
Encode a file:
```bash
python main.py encode <input_file>
```
Specify an output video:
```bash
python main.py encode <input_file> -o output/output.mkv
```
Decode a video:
```bash
python main.py decode <input_video>
```
Specify an output directory:
```bash
python main.py decode <input_video> -o recovered/
```
---
## Roadmap
* [x] Binary header
* [x] Metadata serialization
* [x] Bitstream generation
* [x] Frame generation
* [x] Lossless video encoding
* [x] Video decoding
* [x] SHA-256 verification
### Planned
* [ ] Frame numbering
* [ ] CRC per frame
* [ ] Synchronization markers
* [ ] Reed–Solomon error correction
* [ ] Compression
* [ ] AES encryption
* [ ] Streaming encoder
* [ ] Multi-threaded processing
* [ ] GPU acceleration
* [ ] Graphical interface

---
## License
MIT License.
