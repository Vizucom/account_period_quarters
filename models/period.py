from openerp import api, fields, models
from datetime import date, datetime


class AccountPeriod(models.Model):
    """ Adds yearly quarter attribute to periods """

    _inherit = "account.period"

    quarter = fields.Integer(string="Quarter", compute='_compute_quarter', store=True)


    @api.depends("date_start")
    def _compute_quarter(self):
        """ Quarter is computed based on the month of the periods start date."""
        for period in self:
            date = datetime.strptime(period.date_start, "%Y-%m-%d")
            if date.month in [1,2,3]:
                period.quarter = 1
            elif date.month in [4,5,6]:
                period.quarter = 2
            elif date.month in [7,8,9]:
                period.quarter = 3
            elif date.month in [10,11,12]:
                period.quarter = 4


