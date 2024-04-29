from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class ExportTasksWizard(models.TransientModel):
    _name = 'report.project_custom'
    _description = 'Export Tasks Wizard'
    _inherit = 'report.report_xlsx.abstract'

    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)

    def _get_overlapping_tasks(self):

        domain = [('date_start1', '<=', self.end_date), ('date_end1', '>=', self.start_date)]
        overlapping_tasks = self.env['project.task'].search(domain)
        print('overlapping_tasks-------', overlapping_tasks)
        return overlapping_tasks

    def export_tasks_to_excel(self):
        overlapping_tasks = self._get_overlapping_tasks()
        if not overlapping_tasks:
            raise UserError("No overlapping tasks found for the selected date range.")
        task_list = []
        for task in overlapping_tasks:
            user_name = ()
            for user in task.user_ids:
                user_name += (user.name,)

            vals = {
                'name': task.name,
                'user_id': ','.join(user_name),
                'project_id': task.project_id.name,
            }
            task_list.append(vals)
        data = {
            'model': 'report.project_custom',
            'form_data': self.read()[0],
            'tasks': task_list,
        }
        print(data)
        return self.env.ref('project_custom.action_xls_report_project').report_action(self, data=data)

    def export_tasks_to_pdf(self):
        data = {
            'form': self.read()[0]
        }
        print('data----', data)
        print('--------------------------------------------------------------')
        overlapping_tasks = self._get_overlapping_tasks()
        task_list = []
        for app in overlapping_tasks:
            users = tuple()
            for user in app.user_ids:
                users += (user.name,)
            vals = {
                'name': app.name,
                'project_id': app.project_id.name,
                'user_ids': str(','.join(users))
            }
            task_list.append(vals)
        data['tasks'] = task_list
        print('data----', data)
        if not overlapping_tasks:
            raise UserError("No overlapping tasks found for the selected date range.")
        print('report------')

        return self.env['ir.actions.report'].search(
            [('report_name', '=', 'project_custom.report_project_custom')]).report_action(
            self, data=data)
