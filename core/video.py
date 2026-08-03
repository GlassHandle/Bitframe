import subprocess
from pathlib import Path
def frames_to_video(
    frames_folder,
    output_file,
    fps=30,
):
    frames_folder=Path(frames_folder)
    pattern = str(frames_folder / "frame_%d.png")
    command = ["ffmpeg","-y","-framerate",str(fps),"-i",pattern,"-c:v","ffv1",output_file,]
    subprocess.run(command,check=True,)
def video_to_frames(video,output_folder,):
    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True,exist_ok=True,)
    pattern=str(output_folder/"frame_%d.png")
    command=["ffmpeg","-y","-i",video,pattern,]
    subprocess.run(command,check=True,)