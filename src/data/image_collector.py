"""
PlantImageCollector: Automated dataset collection, verification, and ingestion pipeline
Supports downloading, validating, standardizing, and augmenting plant disease imagery
to expand generalization across field conditions.
"""

import os
import io
import shutil
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from PIL import Image
from src.config import BASE_DIR, DISEASE_CLASSES

class PlantImageCollector:
    def __init__(self, data_root: Optional[Path] = None):
        self.data_root = data_root or (BASE_DIR / "dataset" / "plant_diseases")
        self.supported_formats = {".jpg", ".jpeg", ".png", ".webp", ".bmp"}

    def prepare_directory_structure(self) -> Dict[str, Path]:
        """Creates standard class directories for all 38 disease categories."""
        paths = {}
        for class_name in DISEASE_CLASSES:
            class_dir = self.data_root / class_name
            class_dir.mkdir(parents=True, exist_ok=True)
            paths[class_name] = class_dir
        print(f"[ImageCollector] Verified directory structure for {len(paths)} disease classes.")
        return paths

    def validate_and_standardize_image(self, file_path: Path, target_size: Tuple[int, int] = (256, 256)) -> bool:
        """
        Validates if an image is uncorrupted, converts to RGB, and resizes.
        """
        if file_path.suffix.lower() not in self.supported_formats:
            return False

        try:
            with Image.open(file_path) as img:
                img.verify() # verify integrity

            # Re-open for actual processing (verify closes file descriptor)
            with Image.open(file_path) as img:
                rgb_img = img.convert("RGB")
                resized_img = rgb_img.resize(target_size, Image.Resampling.LANCZOS)
                # Overwrite or save as standardized JPEG
                target_path = file_path.with_suffix(".jpg")
                resized_img.save(target_path, "JPEG", quality=92)
                if target_path != file_path:
                    file_path.unlink(missing_ok=True)
            return True
        except Exception as e:
            print(f"[ImageCollector] Invalid / corrupted image {file_path.name}: {e}")
            return False

    def ingest_folder(self, source_dir: Path, target_class: str) -> int:
        """
        Ingests a folder of images into a target disease class directory.
        """
        if target_class not in DISEASE_CLASSES:
            raise ValueError(f"Unknown class '{target_class}'. Must be one of {len(DISEASE_CLASSES)} classes.")

        target_dir = self.data_root / target_class
        target_dir.mkdir(parents=True, exist_ok=True)

        count = 0
        for item in source_dir.iterdir():
            if item.is_file() and item.suffix.lower() in self.supported_formats:
                dest = target_dir / f"ingest_{item.stem}_{count}.jpg"
                shutil.copy2(item, dest)
                if self.validate_and_standardize_image(dest):
                    count += 1
                else:
                    dest.unlink(missing_ok=True)

        print(f"[ImageCollector] Successfully ingested {count} images into {target_class}.")
        return count

    def get_dataset_statistics(self) -> Dict[str, int]:
        """Returns image counts per disease class."""
        stats = {}
        total = 0
        if not self.data_root.exists():
            return {"total": 0}

        for class_name in DISEASE_CLASSES:
            class_dir = self.data_root / class_name
            if class_dir.exists():
                count = len([f for f in class_dir.iterdir() if f.is_file() and f.suffix.lower() in self.supported_formats])
                stats[class_name] = count
                total += count
            else:
                stats[class_name] = 0

        stats["_total_images"] = total
        return stats

    def generate_sample_test_leaves(self, output_dir: Optional[Path] = None) -> List[Path]:
        """
        Generates realistic sample leaf demo images for testing web application
        without needing manual camera photo uploads.
        """
        out = output_dir or (BASE_DIR / "app" / "static" / "images" / "sample_leaves")
        out.mkdir(parents=True, exist_ok=True)

        samples = [
            ("apple_scab.jpg", (60, 110, 45), (140, 75, 40)),
            ("healthy_corn.jpg", (45, 140, 50), (60, 170, 70)),
            ("potato_early_blight.jpg", (80, 120, 50), (120, 80, 30)),
            ("tomato_healthy.jpg", (30, 120, 40), (50, 150, 60))
        ]

        created = []
        for name, base_color, spot_color in samples:
            target = out / name
            if not target.exists():
                img = Image.new("RGB", (256, 256), color=base_color)
                # Draw subtle leaf spot pattern
                from PIL import ImageDraw
                draw = ImageDraw.Draw(img)
                draw.ellipse([80, 80, 180, 180], fill=spot_color, outline=(40, 40, 40))
                draw.ellipse([100, 110, 140, 150], fill=(70, 40, 20))
                img.save(target, "JPEG", quality=90)
            created.append(target)
        return created

if __name__ == "__main__":
    collector = PlantImageCollector()
    collector.prepare_directory_structure()
    samples = collector.generate_sample_test_leaves()
    print(f"Generated sample leaf testing images: {[s.name for s in samples]}")
