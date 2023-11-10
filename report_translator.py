import io

import PyPDF2
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from translate import Translator

import model


# verify whether the value has Chinese
def is_contains_chinese(value: str):
    for _char in value:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False


# translate to English by inputting Chinese
def translate_to_english(value: str) -> str:
    # return it if input is English
    if not is_contains_chinese(value):
        return value
    # translate if not
    translator = Translator(from_lang="zh", to_lang="en")
    translated_text = translator.translate(value)
    print(f"translate [{value}] to [{translated_text}]")
    return translated_text


# save English online report
def save_english_report(output_file_path: str,
                        pdf_template: model.PdfTemplate,
                        personal_information: model.PersonalInformation) -> None:

    # location of time, information and verification code
    time_x = 180
    time_y = 745.2
    personal_information_x = 180
    personal_information_y = 710.8
    verification_code_x = 252
    verification_code_y = 203.5
    qr_code_x = 75
    qr_code_y = 156
    certificate_photo_x = 460
    certificate_photo_y = 615

    # font
    pdfmetrics.registerFont(TTFont("Roboto-Regular", "font/Roboto-Regular.ttf"))
    pdfmetrics.registerFont(TTFont("Roboto-Medium", "font/Roboto-Medium.ttf"))

    # init canvas
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=A4)

    # set time
    can.setFont("Roboto-Regular", 8.6)
    can.setFillColor("rgb(153, 153, 153)")
    time_str = f"Date of Renewal: {pdf_template.date_of_renewal}    Date of Expiry: {pdf_template.date_of_expiry}"
    can.drawString(time_x, time_y, time_str)

    # set personal information
    can.setFont("Roboto-Regular", 8.6)
    can.setFillColor("rgb(0, 0, 0)")
    for value in vars(personal_information).values():
        can.drawString(personal_information_x, personal_information_y, value)
        personal_information_y -= 28

    # set verification code
    can.setFont("Roboto-Medium", 10)
    can.setFillColor("rgb(0, 186, 199)")
    can.drawString(verification_code_x, verification_code_y, pdf_template.verification_code)

    # set qr code and certificate photo
    can.drawImage(pdf_template.qr_code, qr_code_x, qr_code_y, 68, 68)
    can.drawImage(pdf_template.certificate_photo, certificate_photo_x, certificate_photo_y, 75.6, 100.8)

    can.save()

    # merge the template pdf and content
    template_pdf = PyPDF2.PdfReader(pdf_template.template_path)
    page = template_pdf.pages[0]
    packet.seek(0)
    page.merge_page(PyPDF2.PdfReader(packet).pages[0])

    # output the final report pdf
    output = PyPDF2.PdfWriter()
    output.add_page(page)
    output.write(output_file_path)