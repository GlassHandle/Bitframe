# BitFrame

BitFrame is an experimental binary-to-video encoder that converts arbitrary files into a sequence of lossless video frames and reconstructs the original file without data loss.

Rather than storing visual information, BitFrame treats every pixel as binary data, effectively using video as a portable lossless storage medium.

---

## Features

- Encode any file into a lossless video
- Decode the video back into the original file
- Preserve original filename and file size
- SHA-256 integrity verification
- Optional deterministic seeded frame transformation
- Modular architecture
- Designed for future extensions

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
 │Build Metadata│
 └──────┬───────┘
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
 ┌────────────────────┐
 │Frame Transformation│
 └──────┬─────────────┘
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
 ┌────────────────────┐
 │Reverse Transform   │
 └──────┬─────────────┘
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
 │Parse Metadata│
 └──────┬───────┘
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

## BitFrame Format Specification

### Header

| Offset | Size | Description |
|------:|----:|-------------|
| 0 | 4 | Magic Number |
| 4 | 2 | Version |
| 6 | 2 | Flags |
| 8 | 8 | Metadata Length |

### Metadata

| Field | Type |
|------|------|
| Filename Length | uint16 |
| Filename | bytes |
| Content Length | uint64 |
| SHA-256 | 32 bytes |

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

## Frame Transformation

BitFrame optionally supports deterministic frame transformation using a user-provided seed.

The first frame is intentionally left unmodified to preserve the metadata required for decoding. Every subsequent frame is transformed using a deterministic permutation generated from the supplied seed.

Using the same seed during decoding reconstructs the original frames exactly. Using an incorrect seed produces an invalid reconstruction, which is detected automatically through SHA-256 verification.

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
├── transform
│   ├── __init__.py
│   ├── permutation.py
│   ├── seed.py
│   └── transform.py
│
├── frames
├── output
├── temp
│
├── main.py
├── requirements.txt
├── README.md
└── LICENSE
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

Encode using frame transformation:

```bash
python main.py encode <input_file> --transform-seed 42
```

Specify an output file:

```bash
python main.py encode <input_file> -o output/output.mkv
```

Decode a video:

```bash
python main.py decode <input_video>
```

Decode a transformed video:

```bash
python main.py decode <input_video> --transform-seed 42
```

Specify an output directory:

```bash
python main.py decode <input_video> -o recovered/
```

---

## Roadmap

### Completed

- [x] Binary header
- [x] Metadata serialization
- [x] Bitstream generation
- [x] Frame generation
- [x] Deterministic frame transformation
- [x] Lossless FFV1 video encoding
- [x] Lossless video decoding
- [x] SHA-256 integrity verification

### Planned

- [ ] Compression
- [ ] Multiple transformation algorithms
- [ ] Reed–Solomon error correction
- [ ] Frame synchronization markers
- [ ] Streaming encoder
- [ ] Multi-threaded processing
- [ ] GPU acceleration
- [ ] Graphical interface
- [ ] Performance benchmarks

---
## License
This project is licensed under the MIT License.