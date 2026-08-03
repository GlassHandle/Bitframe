from pathlib import Path
def read_file(path):
    with open(path, "rb") as f:
        return f.read()
def write_file(path, data):
    Path(path).parent.mkdir(
        parents=True,
        exist_ok=True,
    )
    with open(path, "wb") as f:
        f.write(data)