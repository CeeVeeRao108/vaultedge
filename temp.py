 import PyPDF2

def cropper(inp):
    pdfs = [('tmp\\'+inp), 'tmp\\'+"rotated.pdf"]
    pdfMerger = PyPDF2.PdfFileMerger()
    
    for pdf in pdfs:
        pdfMerger.append(pdf)
    with open("final.pdf", 'wb') as f:
        pdfMerger.write(f)
    