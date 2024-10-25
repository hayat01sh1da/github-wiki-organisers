import sys
import os
import shutil
import re
import glob
sys.path.append('./src')
from application import Application

class Directory(Application):
    def __init__(self, base_path = os.path.join('..', '..')):
        super().__init__(base_path)
        self.source_path_maps = {}
        self.target_dirs      = None

    def run(self):
        self.__target_paths__()
        self.__owner_and_wiki_maps__()
        self.__source_path_maps__()
        self.__target_dirs__()
        self.__mkdirs__()
        self.__mv_wikis_to_dirs__()
        self.__delete_empty_dirs__()

    # private

    # @return None
    def __source_path_maps__(self):
        for target_path in self.target_paths:
            dirname                         = os.path.dirname(target_path)
            filename                        = os.path.basename(target_path)
            self.source_path_maps[filename] = os.path.join(dirname, filename)

    # @return [list<str>]
    def __target_dirs__(self):
        self.target_dirs = list(self.owner_and_wiki_maps.keys())

    # @return None
    def __mkdirs__(self):
        if self.target_dirs:
            for target_dir in self.target_dirs:
                path = os.path.join(self.base_path, re.sub(r'@', '', target_dir))
                if not os.path.exists(path):
                    os.makedirs(path)
                else:
                    continue
        else:
            return

    # @return [str]
    def __mv_wikis_to_dirs__(self):
        for owner, wikis in self.owner_and_wiki_maps.items():
            for wiki in wikis:
                dest_path = os.path.join(self.base_path, re.sub(r'@', '', owner), wiki)
                if self.source_path_maps[wiki] == dest_path:
                    continue
                else:
                    shutil.move(self.source_path_maps[wiki], dest_path)

    # @return None
    def __delete_empty_dirs__(self):
        paths = list(set((glob.glob(os.path.join(self.base_path, '**'), recursive = True))))

        for path in paths:
            # [NOTE] Navigation pages are needed.
            if path == self.path_to_home or path == self.path_to_sidebar:
                continue
            # [NOTE] Wiki-related files are needed.
            elif path in glob.glob(os.path.join(self.base_path, '**', '*.md'), recursive = True) or path in glob.glob(os.path.join(self.base_path, '**', '*.png'), recursive = True):
                continue
            # [NOTE] Python files for automation are needed.
            elif path in glob.glob(os.path.join(self.base_path, '**', '*.py'), recursive = True):
                continue
            else:
                if len(os.listdir(path)) == 0:
                    os.removedirs(path)
