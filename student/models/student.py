from odoo import api, fields, models


class StudentStudentInfo(models.Model):
    _name = "student.student.info"
    _description = "Student Student Info"

    name = fields.Char(string='Name')
    age = fields.Char(string='Age')
    class_name = fields.Char(string='Class Name')
