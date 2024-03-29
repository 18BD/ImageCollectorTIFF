# ImageCollectorTIFF

ImageCollectorTIFF — это инструмент на Python, предназначенный для сбора изображений из различных папок и их объединения в один многостраничный файл TIFF.

## Особенности

- Поддержка различных форматов изображений: PNG, JPEG, BMP и другие.
- Возможность обрабатывать изображения из нескольких папок.
- Создание многостраничного TIFF файла из собранных изображений.
- Простой и понятный интерфейс командной строки.

## Начало работы

### Предварительные требования

Для работы с ImageCollectorTIFF убедитесь, что у вас установлены:

- Python 3.6 или выше
- Библиотека Pillow

### Установка

1. Клонируйте репозиторий на локальный компьютер:

```bash
git clone https://github.com/yourusername/ImageCollectorTIFF.git
```

2. Перейдите в директорию проекта:

```bash
cd ImageCollectorTIFF
```

3. Установите необходимые зависимости:

```bash
pip install -r requirements.txt
```

### Использование

Чтобы использовать ImageCollectorTIFF, выполните следующую команду в терминале, указав пути к папкам с изображениями и имя выходного файла:

```bash
python create_tif.py "['путь_к_папке1', 'путь_к_папке2']" выходной_файл.tif
```

### Примеры

Объединение изображений из папок folder1 и folder2 в файл Result.tif:

```bash
python create_tif.py "['folder1', 'folder2']" Result.tif
```
