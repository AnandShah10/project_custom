from odoo import models


class PatientcardXlsx(models.AbstractModel):
    _name = 'report.project_custom.report_project_custom_1'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        print('lines,,,,,,,,,,,,,,,,,,,,,,', lines, data)
        format1 = workbook.add_format({'font_size': 14, 'align': 'vcenter', 'bold': True})
        format2 = workbook.add_format({'font_size': 12, 'align': 'vcenter'})
        sheet = workbook.add_worksheet('Task Report')
        row = 1
        col = 1
        sheet.write(row, col, 'Name', format1)
        sheet.write(row, col + 1, 'Project name', format1)
        sheet.write(row, col + 2, 'User name', format1)
        sheet.set_column(1, 3, 30)
        sheet.set_column(2, 3, 30)
        sheet.set_column(3, 3, 30)
        print("hello-----------------------")
        for task in data['tasks']:
            print('task????????????????????', task)
            row += 1
            sheet.write(row, col, task['name'], format2)
            sheet.write(row, col + 1, task['project_id'], format2)
            sheet.write(row, col + 2, task['user_id'], format2)
        print("hi...............")
