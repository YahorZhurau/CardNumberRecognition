from pipeline.image_pipeline import ImagePipeline
from utils.file_utils import load_config


def main():
    config = load_config("config.yaml")
    if not config:
        print("error: cannot load config")
        return

    pipeline = ImagePipeline(config)

    pipeline.process_images()


if __name__ == "__main__":
    main()
