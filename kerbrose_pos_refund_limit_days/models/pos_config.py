from odoo import api, fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    limit_days_return = fields.Boolean()
    return_number_of_days = fields.Integer(help='Number of days to allow the POS returns')
