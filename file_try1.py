#https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
#https://stackoverflow.com/questions/2759067/rename-multiple-files-in-a-directory-in-python
#https://stackoverflow.com/questions/1810743/how-to-set-the-current-working-directory
#https://stackoverflow.com/questions/34837707/extracting-text-from-a-pdf-file-using-python
#https://pypi.org/project/wordsegment/
#https://stackoverflow.com/questions/8546245/python-concat-string-with-list

import os
from pdfrw import PdfReader

def read_pdf_title(file):
    #title = 'hello world'
    temp = PdfReader(file).Info.Title
    if temp is None:
        title = 'untitled'
    else:
        title = temp[1 : (len(temp)-1)]
    return title

def num_untitle(dir):
    i = 0
    for file in os.listdir(dir):
        if file.endswith('.pdf'):
            if file.find('untitled') != -1:
                i = i + 1
    num = i
    return num

def read_pdf_title_actual(file):
    import PyPDF2
    from wordsegment import load, segment
    pdf_file = open(file, 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    page = read_pdf.getPage(0)
    page_content = page.extractText()
    temp =  page_content[0: page_content.find('\n')]
    load()
    temp = segment(temp)
    title = ' '.join(temp)
    #title = 'untitled'
    pdf_file.close()
    if title == '':
        title = 'untitled'
    return title

if __name__ == '__main__':
    print('Welcome, you can change all the name of your pdf file here.')
    print('Enter the directory that need prcessing down below. And use back slash or double back slash in the dir.')

    user_input = input("Please enter the diractory: ")
    #user_input = "D:\\try\\dl\\try1\\5\\try"

    print(user_input)
    assert os.path.isdir(user_input), "Diractory not found at "+str(user_input)
    os.chdir(user_input)

    for file in os.listdir(user_input):
        if file.endswith('.pdf'):
            title = read_pdf_title(file)
            if title == 'untitled':
                title = read_pdf_title_actual(file)
            try:
                os.rename(file, title + '.pdf')
            except OSError :
                temp = num_untitle(user_input)
                os.rename(file, 'untitled (' + str(temp) + ').pdf')