import spacy
from spacypdfreader import pdf_reader

nlp = spacy.load("fr_core_news_sm")
doc = pdf_reader("C:/Users/trimbuj/Desktop/2001_renault.pdf", nlp)

# Get the page number of any token.
print(doc[0]._.page_number)  # 1
print(doc[-1]._.page_number) # 4

# Get page meta data about the PDF document.
print(doc._.pdf_file_name)
print(doc._.page_range)
print(doc._.first_page)
print(doc._.last_page)
# Get all of the text from a specific PDF page.
#print(doc._.page(2))         # "able to display the destination page (unless..."
file2 = open("C:/Users/trimbuj/Desktop/testesssssss.txt","w+", encoding="utf-8")
file2.write(str(doc._.page(8))) #on r��crit dans le fichier texte le texte propre sans tableau, sans image et mots sp�ciaux
file2.close
