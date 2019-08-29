import os
from subprocess import Popen
import sys


def convert_pdf_to_txt(source_file, destination_file):
    full_path_to_utility = os.path.abspath('./resources/xpdf_32/') + os.path.sep
    command = r'pdftotext.exe -table -nopgbrk -enc UTF-8 "{}" "{}"'.format(source_file, destination_file)
    # command = r'pdftotext.exe -raw -nopgbrk -enc UTF-8 "{}" "{}"'.format(source_file, destination_file)
    process = Popen(command, cwd=full_path_to_utility, shell=True)


def convert_pdf_from_dir_to_txt(source_dir, destination_dir):
    try:
        source_dir = os.path.abspath(source_dir)
        destination_dir = os.path.abspath(destination_dir)
        all_files = os.listdir(source_dir)
        pdf_files = list(filter( lambda name: name[-4:] == '.pdf', all_files))
        for file in pdf_files:
                txt_file_name = os.path.basename(file).replace('.pdf', '.txt')
                convert_pdf_to_txt(source_dir+os.path.sep+file, destination_dir+os.path.sep+txt_file_name)

    except Exception as e:
        print(str(e))

def main():
    # print(str(sys.argv))
    try:
        if len(sys.argv) < 3:
            print("Wrong number of arguments. Example: \"pdf_to_txt_converter.py source_directory destination_directory\"")
        else:
            source_dir = sys.argv[1]
            destination_dir = sys.argv[2]
            convert_pdf_from_dir_to_txt(source_dir, destination_dir)
    except Exception as e:
        print(str(e))


main()
# convert_pdf_to_txt(source_file = os.path.abspath('./resources/pdf/1.pdf'), destination_file = os.path.abspath('./resources/txt/31133.txt'))
# convert_pdf_from_dir_to_txt(os.path.abspath('resources/pdf/'), os.path.abspath('resources/txt/'))
# convert_pdf_from_dir_to_txt(os.path.abspath('resources/pdf/'), os.path.abspath('resources/txt/'))