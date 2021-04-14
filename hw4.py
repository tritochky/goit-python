import os
import sys

path = sys.argv[1]
string = 'Start in {}'.format(path)
print(string)

files = os.listdir(path)

IMAGES = []
AUDIO = []
VIDEO = []
DOCUMENTS = []
OTHER = []
EXTENSIONS = set()

REGISTERED_EXTENSIONS = {
    'JPEG': IMAGES,
    'PNG': IMAGES,
    'JPG': IMAGES,
    'AVI': VIDEO,
    'MP4': VIDEO,
    'MOV': VIDEO,
    'DOC': DOCUMENTS,
    'DOCX': DOCUMENTS,
    'TXT': DOCUMENTS,
    'MP3': AUDIO,
    'OGG': AUDIO,
    'WAV': AUDIO,
    'AMR': AUDIO,
}
for file in files:
    unknown = True
    for extension in REGISTERED_EXTENSIONS.items():
        ext, container = extension
        if file.upper().endswith(ext):
            EXTENSIONS.add(ext)
            container.append(file)
            unknown = False
            break
    if unknown:
        OTHER.append(file)

img = "Images: {}".format(IMAGES)
print(img)
vid = "Video files: {}".format(VIDEO)
print(vid)
doc = "Documents: {}".format(DOCUMENTS)
print(doc)
aud = "Audio files: {}".format(AUDIO)
print(aud)
know = "Unknown files: {}".format(OTHER)
print(know)
other = "There are files of types: {}".format(EXTENSIONS)
print(other)
