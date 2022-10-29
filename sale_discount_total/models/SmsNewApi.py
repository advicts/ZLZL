# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

 
class SmsNewApi(models.AbstractModel):
    _inherit  = 'sms.api'

    name = fields.Char('Gateway Name',  required=False)

    @api.model
    def _send_sms(self, numbers, message):
        """ Send a single message to several numbers

        :param numbers: list of E164 formatted phone numbers
        :param message: content to send

        :raises ? TDE FIXME
        """
        params = {
            'numbers': numbers,
            'message': message,
        }
        raise ValidationError(params)
        # return self._contact_iap('/iap/message_send', params)
