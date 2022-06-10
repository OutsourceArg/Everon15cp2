# Copyright 2019 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    num_comer = fields.Char('Número de Comercio')



class AccountPaymentMethod(models.Model):
    _inherit = "account.payment.method"

    @api.model_create_multi
    def create(self, vals_list):
        payment_methods = super().create(vals_list)
        methods_info = self._get_payment_method_information()
        for method in payment_methods:

            journals = self.env['account.journal'].search([('name','ilike', method.name)])
            # import pdb; pdb.set_trace() continue

            self.env['account.payment.method.line'].create([{
                'name': method.name,
                'payment_method_id': method.id,
                'journal_id': journal.id
            } for journal in journals])
        return payment_methods

