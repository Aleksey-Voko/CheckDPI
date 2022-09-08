from pathlib import Path

from PIL import Image


def main():
    images = Path().glob('*.jpg')
    for in_path in images:
        in_dir = in_path.parent

        im = Image.open(in_path)
        file_size = in_path.stat().st_size
        width, height = im.size
        quality = int(101 - ((width * height) * 3) / file_size)

        if quality >= 90:
            out_dir = in_dir / 'PerfectQty'
        else:
            out_dir = in_dir / 'NoPerfectQty'

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
# pyinstaller -F -i check_dpi/icon.ico check_dpi/main.py
