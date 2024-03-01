from PIL import Image
import os
import argparse
import ast


def collect_images_to_tiff(folders_list, output_filename):
    images = []

    for folder in folders_list:
        for filename in os.listdir(folder):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                img = Image.open(os.path.join(folder, filename)).convert('RGBA')
                images.append(img)

    if images:
        images[0].save(output_filename, save_all=True, append_images=images[1:])
    else:
        print("Нет изображений для сохранения")


def main():
    parser = argparse.ArgumentParser(description='Собирает изображения из заданных папок и объединяет их в один многостраничный файл TIFF.')
    parser.add_argument('folders', type=str, help='Строка, представляющая список папок с изображениями для объединения')
    parser.add_argument('output', help='Имя выходного файла TIFF')

    args = parser.parse_args()

    try:
        folders_list = ast.literal_eval(args.folders)
        if not isinstance(folders_list, list):
            raise ValueError("Аргумент должен быть списком")
    except (SyntaxError, ValueError):
        raise ValueError("Ошибка при разборе списка папок. Убедитесь, что используется правильный формат списка Python.")

    collect_images_to_tiff(folders_list, args.output)

if __name__ == "__main__":
    main()
