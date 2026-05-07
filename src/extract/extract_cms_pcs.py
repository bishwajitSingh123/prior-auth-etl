import os
import pandas as pd
import logging
from pathlib import Path

# Set up paths
BASE_DIR = Path(__file__).resolve().parent.parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
LOG_DIR = BASE_DIR / "logs"

# Ensure directories exist
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Set up logging
log_file = LOG_DIR / "extract_cms_pcs.log"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def extract_cms_pcs():
    source_file_csv = RAW_DIR / "cms_pcs.csv"
    source_file_xlsx = RAW_DIR / "cms_pcs.xlsx"

    source_file = None
    if source_file_csv.exists():
        source_file = source_file_csv
    elif source_file_xlsx.exists():
        source_file = source_file_xlsx

    if not source_file:
        logging.warning("Source file missing: cms_pcs")
        print("Warning: Source file missing: cms_pcs")
        return

    try:
        logging.info(f"Reading source file: {source_file}")
        if source_file.suffix == '.csv':
            df = pd.read_csv(source_file)
        else:
            df = pd.read_excel(source_file)

        output_file = PROCESSED_DIR / "cms_pcs_extracted.csv"
        df.to_csv(output_file, index=False)
        logging.info(f"Successfully extracted data to {output_file}")
        print(f"Successfully extracted data to {output_file}")
    except Exception as e:
        logging.error(f"Error extracting data: {str(e)}")
        print(f"Error extracting data: {str(e)}")

if __name__ == "__main__":
    extract_cms_pcs()
