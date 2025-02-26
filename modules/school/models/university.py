from odoo import models, fields, api
import base64
import pandas as pd

class University(models.Model):
    _name = 'university'
    _description = 'University Management'

    name = fields.Char(string="University Name", required=True)
    address = fields.Char(string="Address")
    states_university = fields.Selection([
        ('received', 'Đã nhận'),
        ('interning', 'Đang thực tập'),
        ('returned', 'Hoàn thành')
    ], string="State", default='draft')

    listinfo = fields.One2many('university.student.info', 'university_id', string="Student Info")
    excel_file = fields.Binary(string="Upload Excel File")
    file_name = fields.Char(string="File Name")

    @api.onchange('excel_file')
    def _import_excel_file(self):
        if self.excel_file:
            try:
                # Đọc file Excel
                data = base64.b64decode(self.excel_file)
                df = pd.read_excel(data, engine='openpyxl')

                # Lấy thông tin sinh viên từ file Excel
                for _, row in df.iterrows():
                    self.listinfo.create({
                        'name': row['Name'],
                        'student_id': row['Student ID'],
                        'email': row['Email'],
                        'university_id': self.id,
                    })
            except Exception as e:
                raise ValueError("Error processing file: %s" % str(e))
