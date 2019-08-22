import os
from subprocess import Popen
import sys


def convert_pdf_to_txt(source_file, destination_file):
    full_path_to_utility = os.path.abspath('./resources/xpdf_64/') + '\\'
    command = r'pdftotext.exe -table -nopgbrk -enc UTF-8 "{}" "{}"'.format(source_file, destination_file)
    p = Popen(command, cwd=full_path_to_utility, shell=True)


def main():
    # print(str(sys.argv))
    try:
        if len(sys.argv) < 3:
            print("Wrong number of arguments. Example: \"pdf_to_txt_converter.py source_file destination_file\"")
        else:
            source_dir = sys.argv[1]
            destination_dir = sys.argv[2]
            convert_pdf_to_txt(source_dir, destination_dir)
    except Exception as e:
        print(str(e))


main()
# convert_pdf_to_txt(source_file = os.path.abspath('./resources/pdf/1.pdf'), destination_file = os.path.abspath('./resources/txt/31133.txt'))
