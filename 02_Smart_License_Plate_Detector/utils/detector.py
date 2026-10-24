import cv2
from pathlib import Path

from utils.logger import save_log
from utils.ocr_reader import read_text
from config import INPUT_FOLDER, OUTPUT_FOLDER


def detect_license_plate():
    output_folder = Path(OUTPUT_FOLDER) / "annotated_images"
    output_folder.mkdir(parents=True, exist_ok=True)

    for img_path in list(Path(INPUT_FOLDER).glob("*.jpg")) + list(Path(INPUT_FOLDER).glob("*.png")) + list(Path(INPUT_FOLDER).glob("*.jpeg")):
        img=cv2.imread(str(img_path))
        if img is None:
            raise OSError(f"Unable to read image: {img_path}")

        detections = read_text(img)
        recognized_text = [
            f"{text.strip()} ({confidence:.2f})"
            for _, text, confidence in detections
            if text.strip()
        ]

        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        edges=cv2.Canny(gray,100,200)
        out = output_folder / f"{img_path.stem}_processed.png"
        if not cv2.imwrite(str(out), edges):
            raise OSError(f"Unable to write processed image: {out}")

        ocr_summary = ", ".join(recognized_text) or "no text detected"
        save_log(f"Processed {img_path.name}; OCR: {ocr_summary}")
