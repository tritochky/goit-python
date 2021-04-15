import pathlib
import sys


def sort_files():
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
    if path.exists():
        if path.is_file():
            for item in path.iterdir():
                if item.endwith(['jpeg', 'png', 'jpg', 'svg']):
                    images = images.append(item.name)
                    images.append('\n')
                    images_end.append(item.suffix)
                elif item.endwith(['avi', 'mp4', 'mov', 'mkv']):
                    videos = videos.append(item.name)
                    videos.append('\n')
                    videos_end.append(item.suffix)
                elif item.endwith(['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx']):
                    documents = documents.append(item.name)
                    documents.append('\n')
                    documents_end.append(item.suffix)
                elif item.endwith(['mp3', 'ogg', 'wav', 'amr']):
                    musics = musics.append(item.name)
                    musics.append('\n')
                    musics_end.append(item.suffix)
                elif item.endwith(['zip', 'gz', 'tar']):
                    archives = archives.append(item.name)
                    archives.append('\n')
                    archives_end.append(item.suffix)
                else:
                    unknown = unknown.append(item.name)
                    unknown.append('\n')
                    unknown_end.append(item.suffix)
        else:
            sort_files(item)
        print("Images {} with expensions {}".format(images, images_end))
        print("Video {} with expensions {}".format(videos, videos_end))
        print("Documents {} with expensions {}".format(documents, documents_end))
        print("Music {} with expensions {}".format(musics, musics_end))
        print("Archives {} with expensions {}".format(archives, archives_end))
        print("Unknown files {} with expensions {}".format(unknown, unknown_end))
    else:
        print("File not exists")


def main():
    path = sys.argv[1]
    path = pathlib.Path(path)
    sort_files(path)

if __name__ == '__main__':
    main()
