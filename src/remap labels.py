import os

# Path to filtered dataset
filtered_dataset_path = r'E:\1_Work_Files\Internship - Garuda Aerospace\MVD\Dataset\Filtered_MVD'

# Old ID to new ID remapping
remap_dict = {
    4: 0,    # Tank → tank
    16: 0,   # tank → tank
    5: 1,    # Truck → truck
    7: 1,    # army-truck → truck
    17: 1,   # truck → truck
    0: 2,    # Armored_car → armored_vehicle
    6: 2,    # apc → armored_vehicle
    11: 2,   # military-vehicle → armored_vehicle
    10: 3,   # hummer → hummer
    14: 4    # rocket-artillery → rocket_artillery
}

valid_ids = set(remap_dict.keys())

# Process each split
for split in ["train", "val", "test"]:
    label_dir = os.path.join(filtered_dataset_path, split, "labels")

    for label_file in os.listdir(label_dir):
        if not label_file.endswith(".txt"):
            continue

        label_path = os.path.join(label_dir, label_file)
        with open(label_path, "r") as f:
            lines = f.readlines()

        new_lines = []
        for line in lines:
            parts = line.strip().split()
            if len(parts) < 5:
                continue
            class_id = int(parts[0])
            if class_id in valid_ids:
                new_id = remap_dict[class_id]
                new_line = " ".join([str(new_id)] + parts[1:])
                new_lines.append(new_line + "\n")

        if new_lines:
            with open(label_path, "w") as f:
                f.writelines(new_lines)
        else:
            # If no valid objects remain, remove label file and image
            os.remove(label_path)
            image_path_base = os.path.splitext(label_file)[0]
            for ext in [".jpg", ".jpeg", ".png"]:
                image_path = os.path.join(filtered_dataset_path, split, "images", image_path_base + ext)
                if os.path.exists(image_path):
                    os.remove(image_path)
