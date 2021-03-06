import pathlib
import sys
import re
import shutil


def handle_image(path: pathlib.Path, root_folder: pathlib.Path):
    target_folder = root_folder / "images"
    target_folder.mkdir(exist_ok=True)
    path.replace(target_folder/path.name)


def handle_video(path: pathlib.Path, root_folder: pathlib.Path):
    target_folder = root_folder / "videos"
    target_folder.mkdir(exist_ok=True)
    path.replace(target_folder / path.name) 


def handle_document(path: pathlib.Path, root_folder: pathlib.Path):
    target_folder = root_folder / "documents"
    target_folder.mkdir(exist_ok=True)
    path.replace(target_folder / path.name)


def handle_archive(path: pathlib.Path, root_folder: pathlib.Path):
    target_folder = root_folder / "archives"
    name, _ = split_extension(path.name)
    target_folder.mkdir(exist_ok=True)
    archive_folder = target_folder / name
    archive_folder.mkdir(exist_ok=True)
    try:
        shutil.unpack_archive(str(path.absolute()), str(archive_folder.absolute()))
    except shutil.ReadError:
        archive_folder.rmdir()
        return
    path.unlink()


def handle_folder(path: pathlib.Path):
    try:
        path.rmdir()
    except OSError:
        pass

IMAGES = []
AUDIO = []
VIDEO = []
DOCUMENTS = []
ARCHIVES = []
FOLDERS = []
REGISTERED_EXTENSIONS = {
    'JPEG': IMAGES,
    'PNG': IMAGES,
    'JPG': IMAGES,
    'SVG': IMAGES,
    'AVI': VIDEO,
    'MP4': VIDEO,
    'MOV': VIDEO,
    'MKV': VIDEO,
    'DOC': DOCUMENTS,
    'DOCX': DOCUMENTS,
    'TXT': DOCUMENTS,
    'XLSX': DOCUMENTS,
    'PPTX': DOCUMENTS,
    'PDF': DOCUMENTS,
    'MP3': AUDIO,
    'OGG': AUDIO,
    'WAV': AUDIO,
    'AMR': AUDIO,
    'ZIP': ARCHIVES,
    'GZ': ARCHIVES,
    'TAR': ARCHIVES,
}


def normaliz(name: str) -> str:
    symbol_map = {ord("А"): "A", ord("а"): "a", ord("Б"): "B", ord("б"): "b", ord("В"): "V", ord("в"): "v", ord("Г"): "G", ord("г"): "g", ord("Д"): "D", ord("д"): "d", ord("Е"): "E", ord("е"): "e", ord("Ё"): "YO", ord("ё"): "yo", ord("Ж"): "ZH", ord("ж"): "zh", ord("З"): "Z", ord("з"): "z", ord("И"): "I", ord("и"): "i", ord("Й"): "Y", ord("й"): "y", ord("К"): "K", ord("к"): "k", ord("Л"): "L", ord("л"): "l", ord("М"): "M", ord("м"): "m", ord("Н"): "N", ord("н"): "n", ord("О"): "O", ord("о"): "o", ord("П"): "P", ord("п"): "p", ord("Р"): "R", ord("р"): "r", ord("С"): "S", ord("с"): "s", ord("Т"): "T", ord("т"): "t", ord("У"): "U", ord("у"): "u", ord("Ф"): "F", ord("ф"): "f", ord("Х"): "H", ord("х"): "h", ord("Ц"): "C", ord("ц"): "c", ord("Ч"): "CH", ord("ч"): "ch", ord("Ш"): "SH", ord("ш"): "sh", ord("Щ"): "SCH", ord("щ"): "sch", ord("Ъ"): "", ord("ъ"): "", ord("Ы"): "I", ord("ы"): "i", ord("Ь"): "", ord("ь"): "", ord("Э"): "E", ord("э"): "e", ord("Ю"): "YU", ord("ю"): "yu", ord("Я"): "YA", ord("я"): "ya", ord("Є"): "YE", ord("є"): "ye", ord("Ї"): "YI", ord("ї"): "yi"}
    new_name = name.translate(symbol_map)
    t_name = re.sub(r'[^\w\s]', '_', new_name)
    return t_name


def split_extension(file_name: str):
    ext_start = 0
    for idx, char in enumerate(file_name):
        if char == ".":
            ext_start = idx
    name = file_name[:ext_start]
    extension = file_name[ext_start+1:].upper()
    if not ext_start:
        return file_name, ""
    return name, extension


def scan(folder: pathlib.Path):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ("images", "videos", "documents", "archives"):
                FOLDERS.append(item)
                scan(item)
            continue

        name, extension = split_extension(file_name=item.name)
        new_name = normalize(name)
        new_item = folder / ".".join([new_name, extension.lower()])
        item.rename(new_item)
        if extension:
            try:
                container = REGISTERED_EXTENSIONS[extension]
                container.append(new_item)
            except KeyError:
                continue


def main(folder: pathlib.Path) -> None:
    scan(folder)

    for file in IMAGES:
        handle_image(file, folder)

    for file in VIDEO:
        handle_video(file, folder)

    for file in DOCUMENTS:
        handle_document(file, folder)

    for file in ARCHIVES:
        handle_archive(file, folder)

    for f in FOLDERS[::-1]:
        handle_folder(f)


if __name__ == "__main__":
    path = sys.argv[1]
    print(f"Start in {path}")

    arg = pathlib.Path(path)
    main(arg.absolute())