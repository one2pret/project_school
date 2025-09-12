from odoo import api, fields, models, _
from datetime import datetime
import base64
import io
import csv


class StudentExportWizard(models.TransientModel):
    _name = "malakademik.student.export.wizard"
    _description = "Export Students to Dapodik CSV"

    class_id = fields.Many2one("malakademik.classroom", string="Classroom")
    include_header = fields.Boolean(string="Include Header", default=True)
    delimiter = fields.Selection([
        (",", ", (Comma)"),
        (";", "; (Semicolon)"),
        ("\t", "Tab"),
    ], string="Delimiter", default=",")
    file_data = fields.Binary(string="File", readonly=True)
    file_name = fields.Char(string="Filename", readonly=True)

    def _map_gender(self, gender):
        # Dapodik commonly uses L (Laki-laki) / P (Perempuan)
        return {"male": "L", "female": "P"}.get(gender or "", "")

    def _map_status(self, status):
        # Map internal status to text
        return {"active": "Aktif", "inactive": "Tidak Aktif"}.get(status or "", "")

    def _csv_rows(self):
        domain = []
        if self.class_id:
            domain.append(("class_id", "=", self.class_id.id))
        students = self.env["malakademik.student"].search(domain, order="class_id,name")
        # Define basic Dapodik-like columns
        header = [
            "NISN",
            "Nama",
            "JK",
            "Tempat Lahir",
            "Tanggal Lahir",
            "Alamat",
            "Status",
            "Kelas",
        ]
        rows = []
        for s in students:
            rows.append([
                s.nisn or "",
                s.name or "",
                self._map_gender(s.gender),
                s.birth_place or "",
                s.birth_date and s.birth_date.strftime("%Y-%m-%d") or "",
                s.address or "",
                self._map_status(s.status),
                s.class_id and s.class_id.name or "",
            ])
        return header, rows

    def action_export(self):
        header, rows = self._csv_rows()
        buf = io.StringIO()
        writer = csv.writer(buf, delimiter=self.delimiter)
        if self.include_header:
            writer.writerow(header)
        writer.writerows(rows)
        content = buf.getvalue().encode("utf-8")
        buf.close()
        fname = f"export_siswa_dapodik_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        self.write({
            "file_data": base64.b64encode(content),
            "file_name": fname,
        })
        return {
            "type": "ir.actions.act_window",
            "res_model": self._name,
            "view_mode": "form",
            "res_id": self.id,
            "target": "new",
        }

