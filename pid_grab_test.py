
import subprocess, os, time, signal


video_path: str = 
vlc_command: str = "/Applications/VLC.app/Contents/MacOS/VLC --video-wallpaper -L".split(' ')
process = subprocess.Popen(vlc_command)
print (f"PID: {process.pid}")
time.sleep(3)
os.kill(process.pid, signal.SIGKILL)