# -*- coding: utf-8 -*-

from odoo import models, fields, api



class AccountMoveInherit(models.Model):
    _inherit = 'account.move'

    month = fields.Selection([
        ('january', 'January 2021'),
        ('february', 'February 2021'),
        ('march', 'March 2021'),
        ('april', 'April 2021'),
        ('may', 'May 2021'),
        ('jun', 'June 2021'),
        ('july', 'July 2021'),
        ('august', 'August 2021'),
        ('september', 'September 2021'),
        ('october', 'October 2021'),
        ('november', 'November 2021'),
        ('december', 'December 2021'),
    ], default='january')
