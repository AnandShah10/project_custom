===============
Project Custom Module
===============

Description
-----------

The "Project Custom" module enhances the functionality of the project management system in Odoo by introducing new features and constraints.

1. **Abstract Class for Start Date and End Date**:
   - An abstract class named `startend_mixin` is defined to enforce constraints on start date and end date. The start date should not be greater than the end date and vice versa.

2. **Inherited Fields in project.task**:
   - Two fields, `date_start` and `date_end`, are added to the `project.task` model by inheriting from the `startend_mixin` abstract class. These fields are not defined in the `project.task` class but are inherited from the base abstract class.

3. **Explanation of `_inherits` Usage**:
   - In the `project.task.checklist` model class, the `_inherits` attribute is used to inherit from the existing Odoo model `project.task`. This syntax allows the `project.task.checklist` model to inherit all fields and methods from the `project.task` model.

Functionality
-------------

1. **Wizard for Exporting Overlapping Tasks**:
   - A wizard is created to allow users to select a date range. Based on the selected date range, overlapping tasks for that period are exported into Excel and PDF files.

2. **Alphabetical Sorting of Tasks**:
   - All tasks displayed in tree/kanban/searches/dropdown-selection views are sorted in alphabetical order based on the Task Title field.

3. **Email Validation on res.partner**:
   - A module is implemented to add email validation on `res.partner` using Python constraints. Additionally, a SQL constraint is added for the email field to ensure uniqueness.

4. **Restriction on Deleting In-Progress Tasks**:
   - Users are restricted from deleting tasks that are in progress. This restriction is enforced using a User Error.

Usage
-----

Please follow the instructions provided in the module to utilize the functionalities and constraints described above.

