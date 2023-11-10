import report_translator
import model
import format_date
from report_translator import save_english_report
import yaml


def read_configuration(path: str) -> (str, model.PdfTemplate, model.PersonalInformation):
    # read yaml
    with open(path, 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)

    # create model PdfTemplate and PersonalInformation and translate to English
    pdf_template = model.PdfTemplate(
        template_path=config["template_path"],
        date_of_renewal=format_date.get_renewal_date(config["date_of_renewal"]),
        date_of_expiry=format_date.get_expiry_date(config["duration_of_expiry"]),
        qr_code=config["qr_code"],
        certificate_photo=config["certificate_photo"],
        verification_code=config["verification_code"]
    )
    personal_information = model.PersonalInformation(
        name=report_translator.translate_to_english(config["name"]).upper(),
        sex=report_translator.translate_to_english(config["sex"]).title(),
        id_number=config["id_number"],
        ethnic_background="The " + report_translator.translate_to_english(config["ethnic_background"]).title(),
        date_of_birth=format_date.format_date(config["date_of_birth"]),
        higher_education_institution=report_translator.translate_to_english(config["higher_education_institution"]).title(),
        education_level=report_translator.translate_to_english(config["education_level"]).title(),
        major=report_translator.translate_to_english(config["major"]).title(),
        form_of_learning=report_translator.translate_to_english(config["form_of_learning"]).title(),
        start_date=format_date.format_date(config["start_date"]),
        length_of_program=report_translator.translate_to_english(config["length_of_program"]).title(),
        type_of_education=report_translator.translate_to_english(config["type_of_education"]).title(),
        status_of_student_record=report_translator.translate_to_english(config["status_of_student_record"]).title(),
        anticipated_graduation_date=format_date.format_date(config["anticipated_graduation_date"])
    )

    return config["output_file_path"], pdf_template, personal_information


if __name__ == '__main__':
    # read configuration
    output_file_path, pdf_template, personal_information = read_configuration("configuration.yaml")

    # save_english_report
    save_english_report(output_file_path, pdf_template, personal_information)