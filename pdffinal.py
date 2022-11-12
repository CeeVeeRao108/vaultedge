import PyPDF2 


def cropper(pdf,pn):
    
    pdfFileObj = open("tmp/"+pdf, 'rb')
    pdfFileObj2 = open("tmp/"+"rotated.pdf", 'rb')
      
    # creating pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    reread=PyPDF2.PdfFileReader(pdfFileObj2)
    repla=reread.getPage(0)
      
      
    
        # creating pdf writer object for (i+1)th split
    pdfWriter = PyPDF2.PdfFileWriter()
          
        # output pdf file name
    outputpdf = pdf.split('.pdf')[0]  + '.pdf'
          
        # adding pages to pdf writer object
    for page in range(0,3):
        if page==pn:
            pdfWriter.addPage(repla)
        else:
            pdfWriter.addPage(pdfReader.getPage(page))
          
        # writing split pdf pages to pdf file
    with open(outputpdf, "wb") as f:
        pdfWriter.write(f)
  
        # interchanging page split start position for next split
        
       
    # closing the input pdf file object
    pdfFileObj.close()