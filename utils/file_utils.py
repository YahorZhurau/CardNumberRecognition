import os
import cv2
import yaml
import numpy as np


def save_image(file_path: str, image: np.ndarray):
    """
    Saves an image to the specified file.
    :param file_path: Path to the file to save.
    :param image: Image (numpy array).
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        cv2.imwrite(file_path, image)
    except Exception as e:
        print(f"Error saving image: {e}")


def annotate_image(image: np.ndarray, text: str) -> np.ndarray:
    """
    Adds text to an image.
    :param image: (numpy array)
    :param text: Text to add
    :return: Image with added text (numpy array)
    """
    annotated_image = image.copy()
    if text:
        cv2.putText(annotated_image,
                    text=text,
                    org=(10, 30),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=1,
                    color=(0, 255, 0),
                    thickness=2)

    return annotated_image


def load_config(config_path: str = "config.yaml") -> dict:
    """
    Loads configuration from a YAML file.
    :param config_path: Path to the YAML file
    :return: Dict with settings
    """
    try:
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)
        return config
    except FileNotFoundError:
        print(f"Error: Configuration file not found: {config_path}")
        return {}
    except yaml.YAMLError as e:
        print(f"Error reading YAML file: {e}")
        return {}
