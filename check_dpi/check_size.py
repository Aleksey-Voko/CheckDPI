from pathlib import Path

from PIL import Image


def main():
    images = Path().glob('*.jpg')
    for in_path in images:
        in_dir = in_path.parent

        im = Image.open(in_path)
        width, height = im.size

        if height >= 1200 and width < 1200:
            out_dir = in_dir / 'MaxSize'
        else:
            out_dir = in_dir / 'MinSize'

        out_path = out_dir / in_path.name
        out_dir.mkdir(parents=True, exist_ok=True)
        print(out_path)
        out_path.write_bytes(in_path.read_bytes())

    print()
    print('=' * 28)
    print('Сортировка завершена')
    print('Для выхода нажмите Enter')
    input()


if __name__ == '__main__':
    main()

# compilation
# pyinstaller -F -i check_dpi/icon.ico check_dpi/check_size.py
