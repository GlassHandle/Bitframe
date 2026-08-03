import argparse

from encoder.encoder import Encoder
from decoder.decoder import Decoder
def main():
    parser = argparse.ArgumentParser(
        description="Encode files into videos and decode videos back into files."
    )
    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )
    enc = subparsers.add_parser(
        "encode",
        help="Encode a file into a video",
    )
    enc.add_argument(
        "input",
        help="Input file",
    )
    enc.add_argument(
        "-o",
        "--output",
        default="output/output.mkv",
        help="Output video",
    )
    dec = subparsers.add_parser(
        "decode",
        help="Decode a video",
    )
    dec.add_argument(
        "input",
        help="Input video",
    )
    dec.add_argument(
        "-o",
        "--output",
        default="output/",
        help="Output directory",
    )
    args = parser.parse_args()
    if args.command == "encode":
        encoder = Encoder(args.input)
        encoder.export_video(args.output,)
    elif args.command == "decode":
        decoder = Decoder(args.input)
        decoder.decode(args.output)
        pass
if __name__ == "__main__":
    main()