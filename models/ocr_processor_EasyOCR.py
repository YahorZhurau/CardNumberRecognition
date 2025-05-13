import easyocr
import numpy as np


class OCRProcessor_EasyOCR:
    """
    Class for text recognition using EasyOCR
    """

    def __init__(self, languages: list = None, only_16: bool = True):
        """
        :param languages: List of languages(for example, ["en"])
        """
        if languages is None:
            languages = ['en']
        self.reader = easyocr.Reader(languages)
        self.only_16 = only_16

    def extract_text(self, image: np.ndarray) -> str:
        """
        Recognizes text on image and return card number (16 digits)
        :param image: The original image (numpy array)
        :return: The card number (str) or an empty string
        """
        try:
            text_detections = []

            results = self.reader.readtext(image,
                                           width_ths=0.9,
                                           allowlist='0123456789')

            for result in results:
                text = result[1]
                cleaned_text = text.replace(" ", "")

                if len(cleaned_text) == 16:
                    return cleaned_text

                text_detections.append(cleaned_text)

            if text_detections and not self.only_16:
                return sorted(text_detections, key=lambda x: abs(16 - len(x)))[0]

            return ""

        except Exception as e:
            print(f"error in text recog: {e}")
            return ""
