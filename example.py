from src.services.extractor import Extractor
from src.utils.printer import Printer

urls = []
url = input("Enter url: ")
urls.append(url)
extractor = Extractor()
links = extractor.extract(urls, timeout=10)

for url, extracted_links in links.items():
    Printer.message(f"Url: {url}")
    for link in extracted_links:
        Printer.success(f" { link}")
    Printer.message("###############")
