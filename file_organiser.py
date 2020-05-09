import os
import shutil

Directory_dict = {
    "PDF": ["pdf"],
    "DOCUMENTS": ["oxps", "epub", "pages", "docx", "doc", "fdf", "ods",
                  "odt", "pwi", "xsn", "xps", "dotx", "docm", "dox",
                  "rvg", "rtf", "rtfd", "wpd", "xls", "xlsx", "ppt",
                  "pptx"],
    "SPREADSHEETS": ["xls", "xlsx", "xlsm", "xlsb" "csv", "tsv", "prn", "dif"],
    "ARCHIVES": ["a", "ar", "cpio", "iso", "tar", "gz", "rz", "7z",
                 "dmg", "rar", "xar", "zip"],
    "AUDIO": ["aac", "aa", "aac", "dvf", "m4a", "m4b", "m4p", "mp3",
              "msv", "ogg", "oga", "raw", "vox", "wav", "wma"],
    "PLAINTEXT": ["txt", "in", "out"],
    "IMAGES": ["jpeg", "jpg", "tiff", "gif", "bmp", "png", "bpg", "svg",
               "heif", "psd"],
    "VIDEOS": ["avi", "flv", "wmv", "mov", "mp4", "webm", "vob", "mng",
               "qt", "mpg", "mpeg", "3gp", "mkv"],
    "HTML": ["html5", "html", "htm", "xhtml"],
    "JAVASCRIPT": ["js"],
    "JAVA": ["jar", "js"],
    "CSS": ["css"],
    "PYTHON": ["py"],
    "XML": ["xml"],
    "EXE": ["exe"],
    "SHELL": ["sh"],
    "JSON": ["json"]
}


def get_key(val):
    """Function to check if file type is in dictionary """
    for key, value in Directory_dict.items():
        if val in value:
            return key
    return "MISC"


def organise_directory():
    """Function to organise the contents of a directory"""
    file_list = filter(os.path.isfile, os.listdir())
    # Iterate over all of the files in the list to find format
    for file_path in file_list:
        file_format = file_path.split('.')[-1].lower()
        directory = get_key(file_format)

        # Create a directory if one does not exist
        try:
            os.mkdir(directory)
            shutil.move(file_path, directory)
        except FileExistsError:
            shutil.move(file_path, directory)


if __name__ == "__main__":
    organise_directory()
