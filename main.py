import camelot
import pandas

pdf_path = "./dev_resources/source.pdf"
output_file = ""

def main():

    print(f"running against pdf: {pdf_path}")

    pdf_pages = "6" # change this later to read the whole pdf
    tables_extract = camelot.read_pdf(pdf_path, pages=pdf_pages, flavor="lattice")
    
    print(f"{tables_extract.n} tables found")
    print(f"Example of first table:")
    print(tables_extract[0].df)

if __name__ == __name__:
    main()