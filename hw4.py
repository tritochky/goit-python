import pathlib
import sys


images = []
videos = []
documents = []
musics = []
archives = []
unknown = []
images_end = []
videos_end = []
documents_end = []
musics_end = []
archives_end = []
unknown_end = []

def sort_files(path):
    global images
    global videos
    global documents
    global musics
    global archives
    global unknown
    global images_end
    global videos_end
    global documents_end
    global musics_end
    global archives_end
    global unknown_end
    if path.exists():
        if path.is_dir():
            for item in path.iterdir():
                sort_files(item)
        else:    
            if path.suffix in (['.jpeg', '.png', '.jpg', '.svg']):
                images.append(path.name)
                images_end.append(path.suffix)
            elif path.suffix in (['.avi', '.mp4', '.mov', '.mkv']):
                videos.append(path.name)
                videos_end.append(path.suffix)
            elif path.suffix in (['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx']):
                documents.append(path.name)
                documents_end.append(path.suffix)
            elif path.suffix in (['.mp3', '.ogg', '.wav', '.amr']):
                musics.append(path.name)
                musics_end.append(path.suffix)
            elif path.suffix in (['.zip', '.gz', '.tar']):
                archives.append(path.name)
                archives_end.append(path.suffix)
            else:
                unknown.append(path.name)
                unknown_end.append(path.suffix)
    else:
        print("File not exists")


def main():
    path = sys.argv[1]
    path = pathlib.Path(path)
    sort_files(path)
    print("Images {} with expensions {}".format(images, images_end))
    print("Video {} with expensions {}".format(videos, videos_end))
    print("Documents {} with expensions {}".format(documents, documents_end))
    print("Music {} with expensions {}".format(musics, musics_end))
    print("Archives {} with expensions {}".format(archives, archives_end))
    print("Unknown files {} with expensions {}".format(unknown, unknown_end))


if __name__ == '__main__':
    main()
    
