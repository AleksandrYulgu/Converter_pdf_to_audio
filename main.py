

from converter import converter_pdf_to_str
from start import start
from fina_data import say_text_as_audio


def main():
    file_path = start()
    print(file_path)
    converted_file = converter_pdf_to_str(file_path)
    print(converted_file)
    say_text_as_audio(converted_file)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


