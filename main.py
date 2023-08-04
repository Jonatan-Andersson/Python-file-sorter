from .FileSorterClass import FileSorter

def main():
    DEV_DEBUG = False
    DEBUG = True

    PATH_TO_TARGET_FOLDER = '/Users/<computer_username>/Desktop'
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


    newfilehandler = FileSorter(
        Path_to_target_folder=PATH_TO_TARGET_FOLDER,
        Dev_Debug= DEV_DEBUG,
        Debug=DEBUG,
        Time_between_sort=TIME_BETWEEN_SORT,
        Amount_of_replica_files=AMOUNT_OF_REPLICA_FILES
    )

    newfilehandler.Start()


if __name__ == "__main__":
    main()
