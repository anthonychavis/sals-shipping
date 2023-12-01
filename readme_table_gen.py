tables_col_headers = (
    'Package Weight (lbs)', 'Price / Pound ($ / lb)', 'Flat Fee ($)'
)
tables_row_headers = (
    ('less than or equal to 2'), ('more than 2, less than or equal to 6'), ('more than 6, less than or equal to 10'), ('more than 10')
)

drone_table_data = (
    ('4.50'), ('9.00'), ('12.00'), ('14.25')
)
ground_table_data = (
    ('1.50'), ('3.00'), ('4.00'), ('4.75')
)


def table_rows_list(table_data, flat_charge):
    table = [tables_col_headers, (':---------', ':---------:', ':---------:')]
    for i, x in enumerate(table_data):
        # row = [tables_row_headers[i]]
        # row.append(x)
        # row.append(flat_charge)
        row = (tables_row_headers[i], x, flat_charge)
        table.append(row)
    # print(f'• {table}')
    return table

# drone_table = table_rows_list(drone_table_data, '0.00')
# ground_table = table_rows_list(ground_table_data, '20.00')

# print(f'♦♦ {drone_table}')

def set_table(table_data, flat_charge):
    table = table_rows_list(table_data, flat_charge)
    md_table = ''
    # for x in table_data:
    for x in table:
        md_table += f'| {" | ".join(x)} |\n'
    return md_table

# print(f'►► {set_table(drone_table)}')
# print(f'►► {set_table(ground_table)}')

# print()
# print(f'{set_table(drone_table)}\n {set_table(ground_table)}\n Premium Ground Shipping = $125.00\n')

# insert_mess = f'#### Drone Shipping\n {set_table(drone_table)}\n #### Ground Shipping\n {set_table(ground_table)}\n **Premium Ground Shipping** = $125.00\n'
insert_mess = f'#### Drone Shipping\n {set_table(drone_table_data, "0.00")}\n #### Ground Shipping\n {set_table(ground_table_data, "20.00")}\n #### **Premium Ground Shipping** = $125.00\n'

# FILE HANDLING
def table_to_readme(readme_content, insert_line, table_mess):
    # split original readme at \n
    # lines = readme_content.splitlines(keepends=True)
    lines = readme_content.splitlines()
    # insert thing at specified line based on original readme file
    lines.insert(insert_line, table_mess)
    # return ''.join(lines)
    return '\n'.join(lines)

# Read original README content
with open("README.md", "r") as readme_file:
    readme_content = readme_file.read()

# Insert table mess into README at specified line
readme_content = table_to_readme(readme_content, 27, insert_mess)

# return new README to the readme file
with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)
