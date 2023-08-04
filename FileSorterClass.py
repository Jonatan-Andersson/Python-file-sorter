import os
# import sys
from termcolor import colored
import time
import random


DEV_DEBUG = False

DEBUG = True

PATH_TO_TARGET_FOLDER = '/Users/jonatanandersson/Desktop'
TIME_BETWEEN_SORT  = 60*60
AMOUNT_OF_REPLICA_FILES = 300000

KEYWORD_BEFORE_FOLDER = "auto"
SCRIPTS_FOLDER_PATH = f"/<{KEYWORD_BEFORE_FOLDER}>Scripts"
IMAGES_FOLDER_PATH = f"/<{KEYWORD_BEFORE_FOLDER}>Images"
DOCUMENTS_FOLDER_PATH  = f"/<{KEYWORD_BEFORE_FOLDER}>Documents"
MOVIES_FOLDER_PATH = f"/<{KEYWORD_BEFORE_FOLDER}>Movies"

ScriptFolderExists = False
ImageFolderExists = False
DocumentFolderExists = False
MovieFolderExists = False

class FileSorter():
    def __init__(
            self,
            Path_to_target_folder:str,
            Time_between_sort:int,
            Amount_of_replica_files:int,
            Dev_Debug:bool=False,
            Debug:bool=True,
            keyword_before_folder:str="auto"
    ) -> None:

        self.DEV_DEBUG = Dev_Debug
        self.DEBUG = Debug
        self.PATH_TO_TARGET_FOLDER = Path_to_target_folder
        self.TIME_BETWEEN_SORT = Time_between_sort
        self.AMOUNT_OF_REPLICA_FILES = Amount_of_replica_files

        self.KEYWORD_BEFORE_FOLDER = keyword_before_folder
        self.SCRIPTS_FOLDER_PATH = f"/<{self.KEYWORD_BEFORE_FOLDER}>Scripts"
        self.IMAGES_FOLDER_PATH = f"/<{self.KEYWORD_BEFORE_FOLDER}>Images"
        self.DOCUMENTS_FOLDER_PATH  = f"/<{self.KEYWORD_BEFORE_FOLDER}>Documents"
        self.MOVIES_FOLDER_PATH = f"/<{self.KEYWORD_BEFORE_FOLDER}>Movies"

        self.ScriptFolderExists = False
        self.ImageFolderExists = False
        self.DocumentFolderExists = False
        self.MovieFolderExists = False

        self.ScriptsFileTypes = [
            '.py',
            '.pyc',
            '.exe',
            '.java',
            '.cs',
            '.c'
            '.cpp',
            '.js',
            '.go',
            '.css',
            '.html',
            '.jsx',
        ]

        self.ImagesFileTypes= [
            '.img',
            '.jpg',
            '.jpeg',
            '.apng',
            '.avif',
            '.gif',
            '.jpeg',
            '.jfif',
            '.pjpeg',
            '.pjp',
            '.png',
            '.svg',
            '.webp'
        ]

        self.DocumentsFileTypes = [
            '.pdf',
            '.doc',
            '.docx',
            '.odt',
            '.xls',
            '.xlsx',
            '.ods',
            '.ppt',
            '.pptx',
            '.txt',
        ]

        self.MoviesFileTypes = [
            '.webm',
            '.mkv',
            '.flv',
            '.vob',
            '.ogv',
            '.ogg',
            '.drc',
            '.gifv',
            '.mng',
            '.avi',
            '.MTS',
            '.M2TS',
            '.TS',
            '.mov',
            '.qt',
            '.wmv',
            '.yuv',
            '.rm',
            '.rmvb',
            '.viv',
            '.asf',
            '.amv',
            '.mp4',
            '.m4p',
            '.m4v',
            '.mpg',
            '.mp2',
            '.mpeg',
            'mpe',
            '.mpv',
            '.m2v',
        ]

    def Get_packages(self):
        try:import os
        except ImportError as e: print(f"Error -> {e}")
        
        try:from termcolor import colored
        except ImportError as e: print(f"Error -> {e}")
        
        try:import time
        except ImportError as e: print(f"Error -> {e}")

        try:import random
        except ImportError as e: print(f"Error -> {e}")


    def Validate_sorting_folders(self, path):
        self.ScriptFolderExists = os.path.isdir(f"{path}{self.SCRIPTS_FOLDER_PATH}")
        if DEV_DEBUG: print(f"[ScriptFolderExists] set to [{self.ScriptFolderExists}]")

        self.ImageFolderExists = os.path.isdir(f"{path}{self.IMAGES_FOLDER_PATH}")
        if DEV_DEBUG: print(f"[ImageFolderExists] set to [{self.ImageFolderExists}]")

        self.DocumentFolderExists = os.path.isdir(f"{path}{self.DOCUMENTS_FOLDER_PATH}")
        if DEV_DEBUG: print(f"[DocumentFolderExists] set to [{self.DocumentFolderExists}]")
        
        self.MovieFolderExists = os.path.isdir(f"{path}{self.MOVIES_FOLDER_PATH}")
        if DEV_DEBUG: print(f"[MovieFolderExists] set to [{self.MovieFolderExists}]")

    
    def Create_missing_sorting_folders(self):
        #runs the checksortingfolder func and then creats path for the bools that havent been set to true
        self.Validate_sorting_folders(self.PATH_TO_TARGET_FOLDER)

        if False == self.ScriptFolderExists: 
            try:os.mkdir(f"{self.PATH_TO_TARGET_FOLDER}{self.SCRIPTS_FOLDER_PATH}"); print(colored(f"[ CREATED ] >>> [{self.PATH_TO_TARGET_FOLDER}{self.SCRIPTS_FOLDER_PATH}]", "green"))
            except:
                if self.DEV_DEBUG:print(f"Folder exists {self.PATH_TO_TARGET_FOLDER}{self.SCRIPTS_FOLDER_PATH}")
        
        if False == self.ImageFolderExists:
            try:os.mkdir(f"{self.PATH_TO_TARGET_FOLDER}{self.IMAGES_FOLDER_PATH}"); print(colored(f"[ CREATED ] >>> [{self.PATH_TO_TARGET_FOLDER}{self.IMAGES_FOLDER_PATH}]", "green"))
            except:
                if self.DEV_DEBUG:print(f"Folder exists {self.PATH_TO_TARGET_FOLDER}{self.IMAGES_FOLDER_PATH}")

        if False == self.DocumentFolderExists: 
            try:os.mkdir(f"{self.PATH_TO_TARGET_FOLDER}{self.DOCUMENTS_FOLDER_PATH}"); print(colored(f"[ CREATED ] >>> [{self.PATH_TO_TARGET_FOLDER}{self.DOCUMENTS_FOLDER_PATH}]", "green"))
            except:
                if self.DEV_DEBUG:print(f"Folder exists {self.PATH_TO_TARGET_FOLDER}{self.DOCUMENTS_FOLDER_PATH}")
        
        if False == self.MovieFolderExists: 
            try:os.mkdir(f"{self.PATH_TO_TARGET_FOLDER}{self.MOVIES_FOLDER_PATH}"); print(colored(f"[ CREATED ] >>> [{self.PATH_TO_TARGET_FOLDER}{self.MOVIES_FOLDER_PATH}]", "green"))
            except:
                if self.DEV_DEBUG:print(f"Folder exists {self.PATH_TO_TARGET_FOLDER}{self.MOVIES_FOLDER_PATH}")


    def Get_files_from_folder(self):
        return os.listdir(self.PATH_TO_TARGET_FOLDER)


    def Get_file_type(self, filename):
        # this will return a tuple of root and extension
        split_tup = os.path.splitext(filename)
        # print(split_tup)
        
        # extract the file name and extension
        # file_name = split_tup[0]
        file_extension = split_tup[1]
        
        # print("File Name: ", file_name)
        # print("File Extension: ", file_extension)

        return file_extension

    def Identify_type(self, filetype):
        if filetype in self.ScriptsFileTypes:
            return "Script"
        
        elif filetype in self.ImagesFileTypes:
            return "Image"
        
        elif filetype in self.DocumentsFileTypes:
            return "Document"

        elif filetype in self.MoviesFileTypes:
            return "Movie"

        else:
            # print("*did not recognize file type")
            return "None"


    def Does_file_exist(self, filepath):
        if self.DEV_DEBUG: print(f"* [{filepath}] DOES FILE EXIST ? [{os.path.exists(filepath)}]")
        if os.path.exists(filepath): return True
        else: return False

    def Sort_files(self):
        self.Validate_sorting_folders(self.PATH_TO_TARGET_FOLDER)

        def Move_file(file_type_folder_path, filepath, randomNumber, file_type):
            if file_type_folder_path != None:
                if DEBUG:print(colored(f"* [{file_type}] {file}", "blue"))

                if False == self.Does_file_exist(f"{self.PATH_TO_TARGET_FOLDER}/{file_type_folder_path}/{file}"):
                    os.rename(filepath, f"{self.PATH_TO_TARGET_FOLDER}/{file_type_folder_path}/{file}")
                    if DEBUG:print(colored(f"* [{file}] -> [{file_type_folder_path}/{file}]", "green"))

                elif self.Does_file_exist(f"{self.PATH_TO_TARGET_FOLDER}/{file_type_folder_path}/{file}"):
                    if DEBUG:print(colored(f"* [Path Exists] [{file_type_folder_path}/{file}] -> [{file_type_folder_path}/({randomNumber}){file}]", "yellow"))
                    os.rename(filepath, f"{self.PATH_TO_TARGET_FOLDER}/{file_type_folder_path}/({randomNumber}){file}")


        for file in self.Get_files_from_folder():
            filepath = f"{self.PATH_TO_TARGET_FOLDER}/{file}"
            randomNumber = random.randint(0,AMOUNT_OF_REPLICA_FILES)
            file_type = self.Identify_type(self.Get_file_type(file))

            match file_type:
                case "Script" : Move_file(SCRIPTS_FOLDER_PATH, filepath=filepath, randomNumber=randomNumber, file_type=file_type)
                case "Image" : Move_file(IMAGES_FOLDER_PATH, filepath=filepath, randomNumber=randomNumber, file_type=file_type)
                case "Document" : Move_file(DOCUMENTS_FOLDER_PATH, filepath=filepath, randomNumber=randomNumber, file_type=file_type)
                case "Movie" : Move_file(MOVIES_FOLDER_PATH, filepath=filepath, randomNumber=randomNumber, file_type=file_type)
                case _:
                    #print(f"* [None] {file}")
                    pass
    
    def Wait(self):
        time.sleep(self.TIME_BETWEEN_SORT)

    def Start(self):
        while True:
            self.Get_packages()
            self.Sort_files()
            self.Wait()

