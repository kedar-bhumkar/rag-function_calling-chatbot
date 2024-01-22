import csv

def parse_csv(file_path):
    data = {}
    
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 2:
                concept, comments = row
                data[concept.strip()] = comments.strip()

    return data

def print_output(data):
    for concept, comments in data.items():
        print(f'The following concept \'{concept}\' is explained by this explanation \'{comments}\'.')




def getData():
    file_path = ".\data\support-bot.csv"  # Replace with the path to your CSV file
    return parse_csv(file_path)

if __name__ == "__main__":
    parsed_data = getData()
    #print_output(parsed_data)

