from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    pos_limit_days_return = fields.Boolean(
        related='pos_config_id.limit_days_return', readonly=False,
    )
    pos_return_number_of_days = fields.Integer(
        related='pos_config_id.return_number_of_days', readonly=False,
        help='Number of days to allow the POS returns')
