from paddleocr import PaddleOCR, draw_ocr
from PIL import Image


def extract_text(img_path, ocr):
    """
    Returns list detected text with bbox, text and confidence value in following format:
    [bbox, (text,confidence), ....]
    """
    results = ocr.ocr(img_path, cls=True)
    result = results[0]
    return result


def parse_result(result):
    """
    Returns a tuple of bboxes_list, detected_text_list, confidence_list
    """
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    return boxes, txts, scores


def get_annotated_img(img_path, boxes, txts, scores):
    """
    Returns PIL image by drawing bounding boxes on the image and detected texts
    """
    img = Image.open(img_path).convert("RGB")
    im_show = draw_ocr(img, boxes, txts, scores, font_path="fonts/simfang.ttf")
    im_show = Image.fromarray(im_show)
    return im_show


# # need to run only once to download and load model into memory
# ocr = PaddleOCR(use_angle_cls=True, lang="en")

# # Load image
# img_path = "6a0120a5e89f23970c022ad3adf890200b-800wi.jpg"

# # Extract text
# result = extract_text(img_path, ocr)

# # Parse result
# boxes, txts, scores = parse_result(result)

# print(txts)
# print()
# pure_string = ' '.join(txts)
# print(pure_string)

def get_ocr_result(img_path):
    ocr = PaddleOCR(use_angle_cls=True, lang="en")
    # Extract text
    print("image path in get ocr " + img_path)
    path = img_path
    result = extract_text(path, ocr)

    # Parse resul
    _, txts, _ = parse_result(result)

    pure_string = ' '.join(txts)
    
    return pure_string

# get_ocr_result('media/hi.png')