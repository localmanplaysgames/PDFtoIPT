import camelot
#import pandas
from pypdf import PdfReader

pdf_path = "./dev_resources/source.pdf"
output_file = ""

# count the number of pages in the provided pdf file
def total_pages(pdf):
    return len(PdfReader(pdf).pages)

# turn the number of pages into a "n, n, n" string that camelot can understand
def page_range(pdf):
    return ",".join(str(i) for i in range(1, total_pages(pdf) + 1))

# pass the pdf into camelot and get the tables
def extract_tables(pdf):
    return camelot.read_pdf(pdf, pages=page_range(pdf), flavor="lattice")

def main():

    print(f"Running against pdf: {pdf_path}...")

    pages = total_pages(pdf_path)
    print(f"Scanning {pages} pages for tables...")

    tables = extract_tables(pdf_path)
    print(f"{tables.n} tables found")
    print(f"Example of first table:")
    print(tables[0].df)

if __name__ == __name__:
    main()