import xlrd
loc = ("/home/phltrkpi/Downloads/master_excel.xlsx")

def remove_space(string):
	return string.replace(" ", "-")

wd = xlrd.open_workbook(loc)
sheet = wd.sheet_by_index(0)
sheet.cell_value(0,0)

user_input = input("Enter Model Number:")
model_number = remove_space(user_input)

for i in range(sheet.nrows):
	var = "<tag>" + model_number + sheet.cell_value(i,0) + "<tag>"
	print(var)
	