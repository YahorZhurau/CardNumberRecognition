# CardNumberRecognition
## Описание проекта

Проект "Распознавание номеров карт" предназначен для автоматической обработки изображений банковских карт. Он решает следующие задачи:
1. **Детекция карты**:
   - Используется модель YOLO для обнаружения карты на изображении.
2. **Выравнивание изображения**:
   - Карта выравнивается с помощью перспективного преобразования, чтобы устранить искажения.
3. **Распознавание текста**:
   - Номер карты распознается с использованием OCR (EasyOCR)
   - Поддерживается два режима работы:
     - Строго 16 цифр.
     - Наиболее близкое значение к 16 символам.
4. **Сохранение результатов**:
   - Выровненное изображение сохраняется с добавленным номером карты в верхнем левом углу.

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
Прогон всех файлов из _input в _output
```bash
python main.py
```

### 5. Удаление окружения
```bash
conda deactivate
conda remove --name myenv --all
```
