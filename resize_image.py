import os
from PIL import Image

# --- CONFIG ---
IMG_SIZE = (224, 224)
BASE_DIR = r"C:\Users\Iskcon Kainth\OneDrive\Desktop\CNN\data"
SUBFOLDERS = ["train/real", "train/sketch", "test/real", "test/sketch"]

# --- Resize Function ---
def resize_and_save(folder):
    full_path = os.path.join(BASE_DIR, folder)
    resized, skipped, failed = 0, 0, 0

    for fname in os.listdir(full_path):
        fpath = os.path.join(full_path, fname)
        try:
            with Image.open(fpath) as img:
                img = img.convert("RGB")
                if img.size != IMG_SIZE:
                    # Resize only if needed
                    img = img.resize(IMG_SIZE, Image.Resampling.LANCZOS)
                    img.save(fpath)
                    resized += 1
                else:
                    skipped += 1
        except Exception as e:
            failed += 1
            print(f"❌ Failed to process {fpath}: {e}")

    print(f"✅ {folder} | Resized: {resized} | Skipped (already 224x224): {skipped} | Failed: {failed}")

# --- Run for Each Folder ---
for sub in SUBFOLDERS:
    print(f"\n📦 Processing: {sub}")
    resize_and_save(sub)

print("\n🎯 All done! Images verified & standardized to 224x224 where needed.")
