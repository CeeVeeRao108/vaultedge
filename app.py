from flask import *  
import PyPDF2
import pdffinal
app = Flask(__name__)  
 

  
@app.route('/')  
def upload():  
    return render_template("file_upload_form.html")  
     
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        r = int(request.form.get('rotang'))
        pn = int(request.form.get('page'))
        pn=pn-1
        f.save( "tmp/"+f.filename)  
        pdf_in = open("tmp/"+f.filename, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_in)
        pdf_writer = PyPDF2.PdfFileWriter()

        
        page = pdf_reader.getPage(pn)
        page.rotateClockwise(r)
        pdf_writer.addPage(page)
          

        pdf_out = open("tmp/"+'rotated.pdf', 'wb')
        pdf_writer.write(pdf_out)
        pdf_out.close()
        pdf_in.close()
        
        pdffinal.cropper(f.filename,pn)
        return render_template("success.html", name = f.filename)


@app.route("/download")
def download():
    filename="resume.pdf"
    return send_file(filename,as_attachment=True)
      
if __name__ == '__main__':  
    app.run(debug = True)  