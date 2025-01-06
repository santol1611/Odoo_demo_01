# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer"
    
    
    price = fields.Float(string="Price", required=True)
    status = fields.Selection([
        ('accepted', 'Accepted'),
        ('refused', 'Refused'),
        ('pending', 'Pending')],
        string="Status", copy=False,) 
    
    partner_id = fields.Many2one(comodel_name='res.partner', 
                                 string="Partner", required=True)
    property_id = fields.Many2one(comodel_name='estate.property', 
                                  string="Property", required=True)
    