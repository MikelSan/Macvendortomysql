from typing import IO
import urllib.request as urllib
import sys


def dlProgress(count, blockSize, totalSize):
    """
        Creates a progress bar to indicate the download progress
    """
    percent = int(count*blockSize*100/totalSize)
    sys.stdout.write("\r%d%%" % percent)
    sys.stdout.flush()


def downloadFile(url: str, file_name: str):
    """
        Downloads the given file from the given URL

        Args:
            url {str}: Url to search the file
            file_name {str}: Name of the file to download
    """
    download_url = url+file_name

    print("Downloading from", download_url)
    urllib.urlretrieve(download_url, file_name, reporthook=dlProgress)


def openPythonFile(file_name: str):
    """
        Creates or opens the file if exists. And starts writing on it.

        If the file was already on the system, it will rewrite it.

        Args:
            file_name {str}: name of the file, no extension

        Return:
            python_file {IO}: file object
    """
    python_file = open(file_name + '.py', 'w')
    python_file.write('# -*- coding: utf-8 -*-\noui = {\n')

    return python_file


def closePythonFile(python_file: IO):
    """
        Closes the file, closing first the object inside it.

        Args:
            python_file {IO}:
    """
    python_file.write('}')

    # close file
    python_file.close()

    # write update to console
    print("\noui.py updated")


def getValuesFromLine(line_to_split: bytes):
    """
        Splits the line into 2 values if possible.

        Otherwise, it creates an empty line.

        Args:
            line_to_split {bytes}: line to split

        Return:
            v1 {str}: mac value, first element of split
            v2 {str}: vendor value, second element of split
    """
    
    try:
        v1, v2 = line_to_split.strip().split("(hex)")
    except Exception:
        v1 = v2 = ''

    return v1, v2
