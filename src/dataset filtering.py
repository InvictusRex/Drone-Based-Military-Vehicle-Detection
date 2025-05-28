import os
import shutil

# Set source and destination directories
base_dir = r'E:\1_Work_Files\Internship - Garuda Aerospace\MVD\Dataset\Military Vehicle Detection.v1i.yolov8'
filtered_dir = r'E:\1_Work_Files\Internship - Garuda Aerospace\MVD\Dataset\Filtered_MVD'

# Use class IDs (from data.yaml)
target_class_ids = {0, 4, 5, 6, 7, 10, 11, 14, 16, 17}  # From your data.yaml

splits = ["train", "val", "test"]

# Create folder structure
for split in splits:
    os.makedirs(os.path.join(filtered_dir, split, "images"), exist_ok=True)
    os.makedirs(os.path.join(filtered_dir, split, "labels"), exist_ok=True)

def contains_target_class(label_path, target_ids):
    with open(label_path, "r") as f:
        for line in f:
            if not line.strip():
                continue
            class_id = int(line.strip().split()[0])
            if class_id in target_ids:
                return True
    return False

for split in splits:
    img_dir = os.path.join(base_dir, split, "images")
    lbl_dir = os.path.join(base_dir, split, "labels")

    out_img_dir = os.path.join(filtered_dir, split, "images")
    out_lbl_dir = os.path.join(filtered_dir, split, "labels")

    for lbl_file in os.listdir(lbl_dir):
        if not lbl_file.endswith(".txt"):
            continue

        label_path = os.path.join(lbl_dir, lbl_file)
        if contains_target_class(label_path, target_class_ids):
            shutil.copy(label_path, os.path.join(out_lbl_dir, lbl_file))

            base_name = os.path.splitext(lbl_file)[0]
            for ext in [".jpg", ".jpeg", ".png"]:
                img_path = os.path.join(img_dir, base_name + ext)
                if os.path.exists(img_path):
                    shutil.copy(img_path, os.path.join(out_img_dir, base_name + ext))
                    break
