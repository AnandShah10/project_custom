from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError
import xlwt


class StartEndMixin(models.AbstractModel):
    _name = "startend.mixin"
    _description = "Start date End date Mixin"

    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")

    def _check_start_end_dates(self, start_date, end_date):
        if start_date and end_date and (start_date > end_date):
            raise ValidationError(_("End Date Should Not Be Less Than Start Date!"))


class TaskChecklist(models.Model):
    """
        Explanation of _inherits usage:
        The `_inherits` attribute is used here to inherit the fields and behaviors of the 'project.task' model into the 'project.task.checklist' model.
        This allows the 'project.task.checklist' model to inherit all the fields and functionalities of 'project.task' while adding its own specific fields and behaviors.
        """

    _name = 'project.task.checklist'
    _description = 'Task Checklist'
    _inherits = {'project.task': 'task_id'}

    task_id = fields.Many2one('project.task', string='Task', required=True, ondelete='cascade')


class ProjectModel(models.Model):
    _inherit = 'project.task'
    _order = 'name'
    date_start1 = fields.Date(string='Start Date', compute='_compute_dates', inverse='inverse_compute', store=True)
    date_end1 = fields.Date(string='End Date', compute='_compute_dates', inverse='inverse_compute', store=True)
    startend_mixin_id = fields.Many2one('startend.mixin', string='StartEnd Mixin')

    @api.depends('startend_mixin_id.start_date', 'startend_mixin_id.end_date')
    def _compute_dates(self):
        for record in self:
            if record.startend_mixin_id.start_date and record.startend_mixin_id.end_date:
                record.date_start1 = record.startend_mixin_id.start_date
                record.date_end1 = record.startend_mixin_id.end_date
            else:
                pass

    @api.depends('startend_mixin_id.start_date', 'startend_mixin_id.end_date')
    def inverse_compute(self):
        for record in self:
            if record.date_start1 and record.date_end1:
                record.startend_mixin_id.start_date = record.date_start1
                record.startend_mixin_id.end_date = record.date_end1
            else:
                pass

    @api.constrains('date_start1', 'date_end1')
    def _check_start_end_dates_project(self):
        for i in self:
            i.startend_mixin_id._check_start_end_dates(i.date_start1, i.date_end1)
