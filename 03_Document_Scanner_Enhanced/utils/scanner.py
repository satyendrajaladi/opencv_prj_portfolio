
import cv2
from pathlib import Path
from utils.document_analyzer import analyze
from utils.logger import write_report


def scan_documents():
    input_dir=Path('input_images')
    debug_dir=Path('output/debug_images')
    scan_dir=Path('output/scanned_docs')

    debug_dir.mkdir(parents=True,exist_ok=True)
    scan_dir.mkdir(parents=True,exist_ok=True)

    report=[]

    for image_path in input_dir.glob('*.png'):
        img=cv2.imread(str(image_path))
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        blur=cv2.GaussianBlur(gray,(5,5),0)
        edges=cv2.Canny(blur,75,200)

        cv2.imwrite(str(debug_dir/f'{image_path.stem}_gray.png'),gray)
        cv2.imwrite(str(debug_dir/f'{image_path.stem}_edges.png'),edges)
        cv2.imwrite(str(scan_dir/f'{image_path.stem}_scan.png'),edges)

        blur_score, brightness, status = analyze(gray)

        report.append({
            'file':image_path.name,
            'brightness':round(brightness,2),
            'blur_score':round(blur_score,2),
            'status':status
        })

        print(f'Processed {image_path.name}')

    write_report(report,'output/reports/document_report.csv')
    print(f'FILES PROCESSED: {len(report)}')
