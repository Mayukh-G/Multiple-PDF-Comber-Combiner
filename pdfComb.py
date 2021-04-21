# Author: Mayukh Gautam

import PyPDF2 as pyDF
import pathlib as plib

TEST_DIR = open("Testdir.txt").read()

# overwrite -> TRUE : Uses dir in the file called Testdir.txt, FALSE : prompts user
# combine -> TRUE : Combines all pdfs into one big pdf, FALSE : Combs through every pdf, attempts to combine info into a text into a text file.


def start(overwrite=False, combine=False) -> bool:
    """
    Example of how to use to combine all pdfs in a dir that will be promted from the user
    >>> import pdfComb
    >>> pdfComb.start(combine=True)
    """
    inp = TEST_DIR if overwrite else input('Enter Full path starting from drive to directory with pdf files to comb:\n')
    d = plib.Path(inp)
    if not d.is_dir():
        print("Directory Not found")
        return False

    pdfs = []
    for f in d.iterdir():
        if f.is_file() and "output" not in f.name:
            pdfs.append(f)

    pdf_objs = [pyDF.PdfFileReader(open(inp + "\\" + pdf.name, 'rb')) for pdf in pdfs]

    if combine:
        merger = pyDF.PdfFileMerger()
        for obj in pdf_objs:
            merger.append(obj)

        with open(inp + "\\" + "output.pdf", "wb") as f:
            merger.write(f)
        return True

    else:
        long_string = ''
        for obj in pdf_objs:
            sub_string = ''
            for r in range(obj.numPages):
                page = obj.getPage(r)
                sub_string += page.extractText()
            long_string += sub_string + "\n\n\n\t ======================= \n\n\n"

        output_file = open(inp + "\\" + "output.txt", 'w')
        output_file.write(long_string)
        output_file.close()
        return True


if __name__ == '__main__':
    while not start(overwrite=True, combine=True):
        pass
