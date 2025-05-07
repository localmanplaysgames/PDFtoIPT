import os
import sys
import camelot
from pypdf import PdfReader

# get and validate the name of the pdf to be scanned from the user
def user_file_selection():
    while True:        
        user_pdf_input = input("What .pdf do you want the tables from? It must be in the same folder as this application. Do not include the file extension.\n>>> ").lower()

        if user_pdf_input == "exit":
            print("Okay bye.")
            sys.exit()

        try:
            if user_pdf_input == "":
                raise Exception("Filename not provided.")
            if ".pdf" in user_pdf_input:
                raise Exception("I told you not to provide the file extension.")
            if f"{user_pdf_input}.pdf" not in os.listdir("."):
                raise Exception("That file isn't in the current directory.")
            return f"./{user_pdf_input}.pdf"
        
        except Exception as e:
            print(f"Error: {e}\nPlease try again or submit 'exit' to quit.\n")

# count the number of pages in the provided pdf file
def total_pages(pdf):
    return len(PdfReader(pdf).pages)

# get and validate the pages the user is interested in
def user_page_selection(total_pages):
    while True:
        try:
            user_page_start = input(f"There are {total_pages} pages in this pdf. What page do you want to start the scan on?\n>>> ")
            
            if user_page_start.lower() == "exit":
                print("Okay bye.")
                sys.exit()

            user_page_start = int(user_page_start)

            if user_page_start < 1:
                raise Exception("Page number can't be less than 1.")
            if user_page_start > total_pages:
                raise Exception("You can't start at a page number higher than the total number of pages.")

            while True:
                try:
                    user_page_end = input("What page do you want to end the scan on? If you only want one page, enter the same as the start page. \n>>> ")

                    if user_page_end.lower() == "exit":
                        print("Okay bye.")
                        sys.exit()

                    user_page_end = int(user_page_end)

                    if user_page_end < 1:
                        raise Exception("Page number can't be less than 1.")
                    if user_page_end < user_page_start:
                        raise Exception("You can't end on a page before the start page.")
                    if user_page_end > total_pages:
                        raise Exception("You can't end at a page number higher than the total number of pages.")

                    return user_page_start, user_page_end

                except ValueError:
                    print("Error: That's not a valid number. Please try again.")
                except Exception as e:
                    print(f"Error: {e}\nPlease try again or submit 'exit' to quit.\n")

        except ValueError:
            print("Error: That's not a valid number. Please try again.")
        except Exception as e:
            print(f"Error: {e}\nPlease try again or submit 'exit' to quit.\n")

# turn the number of pages into a "n, n, n" string that camelot can understand
def page_range(start, end):
    if start == end:
        return str(start)
    return ",".join(str(i) for i in range(start, end + 1))

# pass the pdf and page range into camelot then extract and load the tables
def extract_tables(pdf, range):
    return camelot.read_pdf(pdf, pages=range, flavor="lattice")

def main():

    pdf_path = user_file_selection() 
    print(f"Running against pdf: {pdf_path}...")

    user_selection = user_page_selection(total_pages(pdf_path))
    print(f"Scanning pages {user_selection[0]} to {user_selection[1]} for tables...")

    tables = extract_tables(pdf_path, page_range(user_selection[0], user_selection[1]))
    print(f"{tables.n} tables found") ## reprompt for new page range if nil
    #print(f"Example of first table:") 
    #print(tables[0].df)

if __name__ == __name__:
    main()