import zlib
import os

OBJECTS_PATH = ".git/objects"

obj_dirs = os.listdir(OBJECTS_PATH)
assert len(obj_dirs) != 0 and "No commits in this repo"
obj_dirs.pop(obj_dirs.index("pack"))
obj_dirs.pop(obj_dirs.index("info"))

obj_dir =  obj_dirs[1]

filename = OBJECTS_PATH + "/" + obj_dir + "/" + os.listdir(OBJECTS_PATH + "/" + obj_dir)[0]
data = ""
with open(filename,"rb") as f:
    data = f.read()
    
decompressed_data = zlib.decompress(data).decode()
print(decompressed_data)