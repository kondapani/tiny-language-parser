import sys

def parse_tiny(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            
        for line in lines:
            print(f"Processing line: {line.strip()}")
        
        print("Parsing complete.")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python parser_2897958.py <filename>")
    else:
        parse_tiny(sys.argv[1])
