import logging
from pathlib import Path

import pandas as pd
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
    table_output = root / "data/raw/tables"

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
                f"Successfully opened {pdf_name}.\n Total pages: {len(pdf.pages)}"
            )
            for page in pdf.pages[131:135]:
                width = page.width
                height = page.height
                left_column = (0, 0, width / 2, height)
                right_column = (width / 2, 0, width, height)
                left_text = page.crop(left_column).extract_text()
                right_text = page.crop(right_column).extract_text()
                page_contents = left_text + "\n" + right_text
                print(f"--- Page {page.page_number} ---\n{page_contents}\n")
                tables = page.extract_tables(custom_settings)
                tables = pd.DataFrame(tables)
                tables.to_csv(f"{table_output}/test.csv", index=True)
    except Exception as e:
        logging.error(f"An error occured during extraction: {e}")


def main():
    project_root = get_project_root()
    print(project_root)
    rules = "Trespasser v2.1.3 - Rulebook.pdf"
    extract_raw_text(rules)


if __name__ == "__main__":
    main()
