from ultralytics import YOLO
import numpy as np


class CardDetector:
    """
    Class for detection card on image with yolo-seg model
    """

    def __init__(self, model_path: str):
        """
        :param model_path: path to YOLO weights (.pt)
        """
        self.model = YOLO(model_path)

    def detect_card(self, image: np.ndarray) -> list:
        """
        :param image: (numpy array)
        :return: polygons list [(x1, y1), (x2, y2), ...]
        """
        results = self.model(image)
        polygons = []
        for result in results:
            if result.masks is not None:
                polygons.extend(result.masks.xy)
        return polygons
