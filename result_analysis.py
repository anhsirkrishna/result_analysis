import openpyxl
wb = openpyxl.load_workbook('endsem_results.xlsx')

for sheet in wb.get_sheet_names():
	print(sheet)
	