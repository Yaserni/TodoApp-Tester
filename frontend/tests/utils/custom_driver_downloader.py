import os
import zipfile

import requests

CHROMEDRIVER_URL = "https://storage.googleapis.com/chrome-for-testing-public/138.0.7204.168/win64/chromedriver-win64.zip"
DRIVER_DIR = os.path.join(os.getcwd(), "drivers")
CHROMEDRIVER_ZIP = os.path.join(DRIVER_DIR, "chromedriver.zip")
CHROMEDRIVER_EXE_PATH = os.path.join(DRIVER_DIR, "chromedriver.exe")


def ensure_chromedriver():
    if os.path.exists(CHROMEDRIVER_EXE_PATH):
        return CHROMEDRIVER_EXE_PATH

    os.makedirs(DRIVER_DIR, exist_ok=True)
    response = requests.get(CHROMEDRIVER_URL)
    with open(CHROMEDRIVER_ZIP, "wb") as file:
        file.write(response.content)

    with zipfile.ZipFile(CHROMEDRIVER_ZIP, 'r') as zip_ref:
        zip_ref.extractall(DRIVER_DIR)

    for root, _, files in os.walk(DRIVER_DIR):
        for f in files:
            if f == "chromedriver.exe":
                extracted_path = os.path.join(root, f)
                if extracted_path != CHROMEDRIVER_EXE_PATH:
                    os.rename(extracted_path, CHROMEDRIVER_EXE_PATH)

    os.remove(CHROMEDRIVER_ZIP)
    return CHROMEDRIVER_EXE_PATH
