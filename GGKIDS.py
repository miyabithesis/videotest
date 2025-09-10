def count_frames_ffprobe(video_path):
    cmd = [
        "ffprobe", "-v", "error",
        "-select_streams", "v:0",
        "-count_frames",
        "-show_entries", "stream=nb_read_frames",
        "-of", "default=nokey=1:noprint_wrappers=1",
        video_path
    ]
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode().strip()
        return int(output)
    except Exception as e:
        print(f"Error for {video_path}: {e}")
        return None

def count_all_frames_in_folder_ffprobe(folder_path, prefix="set9_", start=9, end=88, extension=".avi"):
    for i in range(start, end + 1):
        filename = f"{prefix}{i}{extension}"
        video_path = os.path.join(folder_path, filename)

        if not os.path.isfile(video_path):
            print(f"⚠️  File not found: {filename}")
            continue

        total_frames = count_frames_ffprobe(video_path)
        if total_frames is not None:
            print(f"{filename} = {total_frames}")
        else:
            print(f"❌ Failed to count frames for: {filename}")

# Example usage:
folder_path = r'C:\Users\Titus\Desktop\Thesis\SET9'
count_all_frames_in_folder_ffprobe(folder_path)
