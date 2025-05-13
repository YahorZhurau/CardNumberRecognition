import os
import cv2

import numpy as np

from models.card_detector import CardDetector
from preprocessing.polygon_processor import PolygonProcessor
from preprocessing.perspective_corrector import PerspectiveCorrector
from models.ocr_processor_EasyOCR import OCRProcessor_EasyOCR as OCRProcessor
from utils.file_utils import save_image, annotate_image
from utils.logging_utils import setup_logger


class ImagePipeline:
    """
    Class for managing the process
    """

    def __init__(self, config: dict):
        """
        :param config: dict with config
        """

        # logger
        self.logger = setup_logger(log_file=config.get("log_file"))

        # config settings
        self.input_dir = config.get("input_dir")
        self.output_dir = config.get("output_dir")
        self.model_path = config.get("model_path")
        self.languages = config.get("languages")
        self.only_16 = config.get("only_16")

        if not self.input_dir or not self.output_dir or not self.model_path:
            self.logger.error("Error: Required parameters are missing from the config")
            raise ValueError("Error: Required parameters are missing from the config")

        # Making dir
        os.makedirs(self.output_dir, exist_ok=True)

        self.card_detector = CardDetector(model_path=self.model_path)
        self.polygon_processor = PolygonProcessor()
        self.perspective_corrector = PerspectiveCorrector()
        self.ocr_processor = OCRProcessor(languages=self.languages, only_16=self.only_16)

    def process_images(self):
        """
        Processes all images in _input_dir.
        """
        try:
            for file in os.listdir(self.input_dir):
                image_path = os.path.join(self.input_dir, file)

                image = self._load_image(image_path)
                if image is None:
                    continue

                self._process_single_image(image, file)

        except Exception as e:
            self.logger.error(f"Error in image processing: {e}")

    def _load_image(self, image_path: str) -> np.array:
        """
        :param image_path: Path to image
        :return: (numpy array) or None
        """
        try:
            image = cv2.imread(image_path, cv2.IMREAD_COLOR)
            if image is None:
                self.logger.error(f"error - Can't load image: {image_path}")
            return image
        except Exception as e:
            self.logger.error(f"error - Can't load image {image_path}: {e}")
            return None

    def _process_single_image(self, image: np.ndarray, file: str):
        """
        :param image:(numpy array)
        :param file: path to save(str)
        """
        try:
            # 1: Card Detetion
            polygons = self.card_detector.detect_card(image)
            if not polygons:
                self.logger.warning("Card is not detected")
                return

            for polygon in polygons:
                try:
                    # 2: Approximate to 4
                    card_corners = self.polygon_processor.approximate_to_4(polygon)

                    # 3: Perspective transformation
                    aligned_image = self.perspective_corrector.correct_perspective(image, card_corners)
                    prepared_image = self.perspective_corrector.prepare_image(aligned_image)

                    # 4: Text recognition
                    card_number = self.ocr_processor.extract_text(prepared_image)
                    if card_number:
                        self.logger.info(f"CARD NUMBER: {card_number}")
                    else:
                        self.logger.warning("Can't recog card number")

                    annotated_image = annotate_image(prepared_image, card_number)

                    # 5: Saving the result
                    save_path = os.path.join(self.output_dir, file)
                    save_image(save_path, annotated_image)
                    self.logger.info(f"image saved: {save_path}")

                except ValueError as e:
                    self.logger.error(f"eroor in polygon processing {file}: {e}")

        except Exception as e:
            self.logger.error(f"error in image processing {file}: {e}")
