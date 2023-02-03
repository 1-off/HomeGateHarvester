# Load the CSV file into a pandas DataFrame
df = pd.read_csv('houses.csv')

# Write the DataFrame to an Excel file
df.to_excel('output.xlsx', index=False)



def csv_to_sheet(file_name):
    # Open the CSV file
    with open(file_name, 'r') as file:
        # Read the contents of the file into a variable
        reader = csv.reader(file)

        # Open the output file in write mode
        with open(file_name.split('.')[0] + '.ods', 'w') as output_file:
            # Write the contents of the CSV file to the output file
            for row in reader:
                output_file.write(','.join(row) + '\n')

csv_to_sheet('houses.csv')
