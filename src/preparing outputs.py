import os

def rename_files_sequentially(folder_path):
    # Get a list of all files (excluding directories)
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    files.sort()  # Optional: sort alphabetically before renaming

    for idx, filename in enumerate(files, start=1):
        _, ext = os.path.splitext(filename)
        new_name = f"{idx}{ext}"
        src = os.path.join(folder_path, filename)
        dst = os.path.join(folder_path, new_name)

        # Rename the file
        os.rename(src, dst)
        print(f"Renamed: {filename} -> {new_name}")

# Example usage
rename_files_sequentially(r'E:\1_Work_Files\D_Research Paper - Military Vehicle Detection & Tracking\Drone-Based-Military-Vehicle-Detection\YOLOv8s Results & Metrics\Prediction Outputs')
