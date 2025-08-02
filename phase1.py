import os
import random
import shutil

# === CONFIG ===

BASE_DIR    = os.path.abspath(os.path.dirname(r"C:\Users\Iskcon Kainth\OneDrive\Desktop\CNN\data"))
DATA_DIR    = os.path.join(BASE_DIR, "data")
ORIG_TRAIN  = os.path.join(DATA_DIR, "train")
TEST_DIR    = os.path.join(DATA_DIR, "test")
SPLIT_RATIO = 0.2
RANDOM_SEED = 42

# === SPLIT LOGIC ===
random.seed(RANDOM_SEED)

for category in ["real", "sketch"]:
    src_folder = os.path.join(ORIG_TRAIN, category)
    dst_folder = os.path.join(TEST_DIR, category)
    os.makedirs(dst_folder, exist_ok=True)

    files = [f for f in os.listdir(src_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    print(f"🔍 {category}: {len(files)} files found")

    n_test = int(len(files) * SPLIT_RATIO)
    test_files = random.sample(files, n_test)

    for fname in test_files:
        src_path = os.path.join(src_folder, fname)
        dst_path = os.path.join(dst_folder, fname)
        shutil.move(src_path, dst_path)
        print(f"✔️ Moved {fname} → test/{category}")

    print(f"📦 {n_test} files moved to test/{category}, {len(files)-n_test} remain in train/{category}\n")

print("✅ Dataset split complete: 80% train / 20% test")
