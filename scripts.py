import fitz

doc = fitz.Document('1-ProVen-VCT-Annual-Report_Accounts_2.pdf')

page8 = doc.loadPage(7)  # somehow page 7 is 8 and 9 is 9.
page9 = doc.loadPage(8)  # still trying to figure out why that is so...

page8_text = page8.getText(output='text')
page9_text = page9.getText(output='text')

text_file = open(doc.name+'.txt', "w+")
text_file.write(page9_text)
text_file.close()

