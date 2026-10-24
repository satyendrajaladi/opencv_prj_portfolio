import easyocr
import numpy as np
from functools import lru_cache
from pathlib import Path
from typing import Sequence, cast

OCRDetection = tuple[list[list[int | float]], str, float]


@lru_cache(maxsize=4)
def _get_reader(languages: tuple[str, ...], gpu: bool) -> easyocr.Reader:
    return easyocr.Reader(list(languages), gpu=gpu)


def read_text(
    image: str | Path | np.ndarray,
    languages: Sequence[str] = ("en",),
    gpu: bool = False,
) -> list[OCRDetection]:
    """Recognize text in an image and return EasyOCR's bounding boxes, text, and confidence."""
    normalized_languages = tuple(languages)
    if not normalized_languages or any(not language.strip() for language in normalized_languages):
        raise ValueError("At least one non-empty OCR language is required.")
    if isinstance(image, np.ndarray) and image.size == 0:
        raise ValueError("The image array must not be empty.")

    reader = _get_reader(normalized_languages, gpu)
    source = str(image) if isinstance(image, Path) else image
    return cast(
        list[OCRDetection],
        reader.readtext(source, detail=1, paragraph=False),
    )
