# CardNumberRecognition

## Структура проекта
```bash
project/
│
├── config.yaml          # Конфигурационный файл
├── main.py              # Точка входа в приложение
├── requirements.txt     # Список зависимостей
├── pipeline/            # Пайплайн обработки изображений
│   └── image_pipeline.py
├── models/              # Модели для детекции и OCR
│   ├── card_detector.py
│   └── ocr_processor.py
├── preprocessing/       # Предобработка изображений
│   ├── polygon_processor.py
│   └── perspective_corrector.py
└── utils/               # Вспомогательные утилиты
    ├── file_utils.py
    └── logging_utils.py
```

## Установка

### 1. Клонирование репозитория
```bash
git clone https://github.com/YahorZhurau/CardNumberRecognition.git
cd CardNumberRecognition
```

### 2. Создание окружения
```bash
conda create --name myenv python=3.9
conda activate myenv
```

### 3. Установка библиотек
```bash
pip install -r requirements.txt
```

### 4. Использование
```bash
python main.py
```

### 5. Удаление окружения
```bash
conda deactivate
conda remove --name myenv --all
```
