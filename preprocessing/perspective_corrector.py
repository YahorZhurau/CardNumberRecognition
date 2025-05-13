import cv2
import numpy as np


class PerspectiveCorrector:
    """
    Class for using perspective transformation.
    """

    @staticmethod
    def order_points(pts: np.ndarray) -> np.ndarray:
        """
        Упорядочивает углы прямоугольника.
        :param pts: Координаты углов [(x1, y1), (x2, y2), ...].
        :return: Упорядоченные координаты [(x1, y1), (x2, y2), (x3, y3), (x4, y4)].
        """
        rect = np.zeros((4, 2), dtype="float32")
        s = pts.sum(axis=1)
        rect[0] = pts[np.argmin(s)]  # Верхний левый угол
        rect[2] = pts[np.argmax(s)]  # Нижний правый угол
        diff = np.diff(pts, axis=1)
        rect[1] = pts[np.argmin(diff)]  # Верхний правый угол
        rect[3] = pts[np.argmax(diff)]  # Нижний левый угол
        return rect

    @staticmethod
    def correct_perspective(image: np.ndarray, card_corners: np.ndarray) -> np.ndarray:
        """
        Use a perspective transformation to straighten the card
        :param image: (numpy array).
        :param card_corners: Coordinates of the four corners of the card [(x1, y1), (x2, y2), ...].
        :return: Aligned image of card
        """
        # Sort corners
        rect = PerspectiveCorrector.order_points(card_corners)

        (tl, tr, br, bl) = rect
        width_top = np.linalg.norm(tr - tl)
        width_bottom = np.linalg.norm(br - bl)
        max_width = max(int(width_top), int(width_bottom))

        height_left = np.linalg.norm(tl - bl)
        height_right = np.linalg.norm(tr - br)
        max_height = max(int(height_left), int(height_right))

        dst = np.array([
            [0, 0],
            [max_width - 1, 0],
            [max_width - 1, max_height - 1],
            [0, max_height - 1]
        ], dtype="float32")

        M = cv2.getPerspectiveTransform(rect, dst)

        warped = cv2.warpPerspective(image, M, (max_width, max_height))
        return warped

    @staticmethod
    def prepare_image(image: np.ndarray) -> np.ndarray:
        """
        Processing images with filters to prepare for text recognition
        :param image: (numpy array)
        :return: Prepared image to recog (numpy array)
        """
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        denoised_image = cv2.fastNlMeansDenoising(gray_image, None, 10, 7, 21)
        clahe = cv2.createCLAHE(clipLimit=3, tileGridSize=(8, 8))
        cl_image = clahe.apply(denoised_image)
        return cl_image
