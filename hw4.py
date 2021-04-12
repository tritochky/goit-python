import pathlib
import sys


def sort_files():
    if item.endwith(['jpeg', 'png', 'jpg', 'svg']):
        images = images.append(item.name)
    elif item.endwith(['avi', 'mp4', 'mov', 'mkv']):
        videos = videos.append(item.name)
    elif item.endwith(['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx']):
        documents = documents.append(item.name)
    elif item.endwith(['mp3', 'ogg', 'wav', 'amr']):
        musics = musics.append(item.name)
    elif item.endwith(['zip', 'gz', 'tar']):
        archives = archives.append(item.name)
    else:
        unknown = unknown.append(item.name)
    return sort_files()


def run_through_dir():
    for item in path.iterdir():
        if item.is_file():
            sort_files()
        else:
            run_through_dir()
    return  run_through_dir()


if __name__ == '__main__':

    images = []
    videos = []
    documents = []
    musics = []
    archives = []
    unknown = []

    files = {('jpeg', 'png', 'jpg', 'svg'): "images", ('avi', 'mp4', 'mov', 'mkv'): "videos", ('doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'): "documents", ('mp3', 'ogg', 'wav', 'amr'): "musics", ('zip', 'gz', 'tar'): "archives"}

    if len(sys.argv) < 2:
        user_dir = ""
    else:       
        user_dir = sys.argv[1]
    
    path = pathlib.Path(user_dir)

    if path.exists():
        if path.is_dir():
            run_through_dir             
        else:
            sort_files()
    else:
        print(f'path {path.absolute()} not exists')

    print(''.join(images) + ' '.join(videos) + ' '.join(documents) + ' '.join(musics) + ' '.join(archives) + ' '.join(unknown))

