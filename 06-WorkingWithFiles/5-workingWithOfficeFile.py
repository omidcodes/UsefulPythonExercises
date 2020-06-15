# pip install python-docx
# https://python-docx.readthedocs.io/en/latest/user/documents.html
import docx


def office_file(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
        print(para.text)

    # print(fullText)   #Fulltext as list
    doc.save('mytest_copy.docx')  # Copying file


office_file('mytest.docx')
