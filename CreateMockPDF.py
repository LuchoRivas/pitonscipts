from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def generate_pdf(filename, text):
    c = canvas.Canvas(filename, pagesize=letter)
    c.drawString(100, 750, text)
    c.save()

if __name__ == "__main__":
    # filename (opc)
    user_filename = input("Name your file (no extension) or just press any key: ")
    if not user_filename:
        user_filename = "example"  # default name

    # random text
    import random
    import string
    text = ''.join(random.choices(string.ascii_letters + string.digits, k=100))

    # .pdf extension to the file
    filename = user_filename + ".pdf"
    generate_pdf(filename, text)
    print(f"File created! - {filename}")
