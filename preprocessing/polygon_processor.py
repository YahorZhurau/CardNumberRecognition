import cv2
import numpy as np


class PolygonProcessor:
    """
    Class for processing polygons (approximation to a quadrilateral)
    """

    @staticmethod
    def approximate_to_4(polygon: list) -> np.ndarray:
        """
        :param polygon: [(x1, y1), (x2, y2), ...].
        :return: Four corners of the card [(x1, y1), (x2, y2), (x3, y3), (x4, y4)].
        """
        # Преобразуем полигон в формат, подходящий для OpenCV
        polygon = np.array(polygon, dtype=np.int32).reshape((-1, 1, 2))

        # Аппроксимируем полигон до четырехугольника
        epsilon = 0.02 * cv2.arcLength(polygon, True)
        approx = cv2.approxPolyDP(polygon, epsilon, True)

        if len(approx) == 4:
            return approx.reshape(-1, 2)
        else:
            raise ValueError("Failed to approximate polygon to 4")
