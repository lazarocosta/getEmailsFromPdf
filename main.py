# This is a sample Python script.
import os
import re

# importing required modules
import PyPDF4

arrayResult = []

dir_list = os.listdir(os.getcwd() + "./icse2022-artigos")
# print(dir_list)
for file in dir_list:
    pdfFileObj = open("./icse2022-artigos/" + file, 'rb')

    # creating a pdf reader object
    pdfReader = PyPDF4.PdfFileReader(pdfFileObj)

    # creating a page object
    pageObj = pdfReader.getPage(0)

    # extracting text from page
    text = pageObj.extractText()
    # print(pageObj.extractText())

    myResult = [x.group() for x in
                re.finditer(r'(\{)?(,|-|[A-Z]|[a-z]|_|\.|[0-9])*(\})?\@([A-Z]|[a-z]|_|\.|[0-9]|-|)*',
                            text,
                            flags=re.IGNORECASE | re.MULTILINE)]

    for email in myResult:
        if "}" in email and "{" in email:
            email = email.replace('}', '')
            email = email.replace('{', '')
            x = email.split("@")
            termination = x[1]
            emails = x[0].split(",")
            z = 1
            new_list = [x + "@" + termination for x in emails]
            arrayResult += new_list
        else:
            if "," in email:
                email = email.replace(',', '')
            arrayResult.append(email)

    print(file)
    print(myResult)

    # closing the pdf file object
    pdfFileObj.close()

# remove duplicated
arrayResult = [*set(arrayResult)]

# erase file content
open(os.getcwd() + "/result.txt", 'w').close()

f = open(os.getcwd() + "/result.txt", "w")
for result in arrayResult:
    f.write(result + "\n")
f.close()

print("concluded")

if __name__ == '__main__':
    print("start function")
