# Import libraries
import csv

# An empty list to hold read-in sales data
sales_records = []
with open('sales.csv', 'r') as data_file:
    csv_reader = csv.reader(data_file)
    header = next(csv_reader)
    for record in csv_reader:
        sales_records.append(record)
#sales_records = sales_records[1:]

def display_total_records():
    "This function displays the total number of records in the data"
    total_records = len(sales_records)
    print(total_records)

def retrieve_record():
    "This function retrieves and displays a record specified by a user based on a specified id"
    input_id = int(input('Enter the id of the record you want to retrieve: '))
    output_record = []
    for record in sales_records:
        if record[0] == ' ':
                pass
        elif int(record[0]) == input_id:
                output_record.append(record)
        else:
            break
    if len(output_record) == 0:
        print('Record ID not found. Please enter a valid record ID')
    else:
        for item in output_record:
            print(item)



#retrieve_record()
