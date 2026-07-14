import logging
from pathlib import Path

import pdfplumber

# allows logging to show time and level of message
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_project_root() -> Path:
    """returs the root directory of project"""
    return Path(__file__).resolve().parent.parent.parent


def extract_raw_text(pdf_name: str):
    """Locates the pdf and attempts to extract text"""
    root = get_project_root()
    pdf_path = root / "data" / pdf_name
    filename = "raw.txt"
    text_output = root / "data" / "raw" / filename

    custom_settings = {
        "vertical_strategy": "text",
        "horizontal_strategy": "lines",
        "snap_tolerance": 5,
        "join_tolerance": 3,
    }

    # checking if file exists before opening
    if not pdf_path.is_file():
        logging.error(f"File not found at {pdf_path}")
        return
    try:
        with pdfplumber.open(pdf_path) as pdf:

            logging.info(
                f"Successfully opened {pdf_name}.\nTotal pages: {len(pdf.pages)}"
            )
            all_text = ""
            for page in pdf.pages[131:135]:
                print(f"******* {page}*******")
                width = page.width
                height = page.height
                left_column = (0, 0, width / 2, height - 50)
                right_column = (width / 2, 0, width, height - 50)
                page_number = (0, height - 50, width, height)
                left_text = page.crop(left_column).extract_text()
                right_text = page.crop(right_column).extract_text()
                page_text = page.crop(page_number).extract_text()
                page_contents = left_text + "\n" + right_text + "\n" + page_text
                if page_contents:
                    all_text += page_contents + "\n"
                print(f"--- Page {page.page_number} ---\n{page_contents}\n")


        with open(text_output, "w", encoding="utf-8") as file:
            file.write(all_text)
        print(f"File saved to {text_output}")
        return all_text

    except Exception as e:
        logging.error(f"An error occured during extraction: {e}")


def main():
    project_root = get_project_root()
    print(project_root)
    rules = "Trespasser v2.1.3 - Rulebook.pdf"
    all_text = extract_raw_text(rules)
    lines = all_text.splitlines()
    print(lines)




if __name__ == "__main__":
    main()
