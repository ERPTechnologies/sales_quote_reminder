from odoo import api, fields, models, _
from datetime import datetime, timedelta


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = "Sale Order"

    def validity_due_reminder_action_email(self):
        sales = self.env['sale.order'].search([])
        if sales:
            for order in sales:
                email_to = []
                for follower in order.message_follower_ids:
                    email_to.append(follower.partner_id.id)
                if not isinstance(order.validity_date, bool):
                    date_two_days_ago = order.validity_date - timedelta(days=2)
                    if order.validity_date == datetime.now().date():
                        template_id = self.env['ir.model.data'].get_object_reference('salequote_validity',
                        'validity_due_reminder_email_template')[1]
                        template_browse = self.env['mail.template'].browse(template_id)
                        due_date = order.validity_date
                        if template_browse:
                            values = template_browse.generate_email(order.id, fields=None)
                            values['subject'] = "Reminder about " + order.name + " due on " + str(due_date)
                            values['email_from'] = self.env['res.users'].browse(self.env['res.users']._context['uid']).partner_id.email
                            values['res_id'] = False
                            values['author_id'] = self.env['res.users'].browse(self.env['res.users']._context['uid']).partner_id.id
                            values['recipient_ids'] = [(6, 0, email_to)]
                            if not values['email_to'] and not values['email_from']:
                                pass

                            msg_id = self.env['mail.mail'].create({
                                'body_html': values['body_html'],
                                'subject': values['subject'],
                                'email_to': values['email_to'],
                                'auto_delete': True,
                                'email_from': values['email_from'],
                                'references': values['mail_server_id'], })
                            mail_mail_obj = self.env['mail.mail']
                            if msg_id:
                                mail_mail_obj.sudo().send(msg_id)


                    elif datetime.now().date() == date_two_days_ago:
                        template_id = self.env['ir.model.data'].get_object_reference('salequote_validity',
                        'validity_before_due_reminder_email_template')[1]
                        template_browse = self.env['mail.template'].browse(template_id)
                        due_date = order.date_due
                        if template_browse:
                            values = template_browse.generate_email(order.id, fields=None)
                            values['subject'] = "Reminder about " + order.name + " due on " + str(due_date)
                            values['email_from'] = self.env['res.users'].browse(self.env['res.users']._context['uid']).partner_id.email
                            values['res_id'] = False
                            values['author_id'] = self.env['res.users'].browse(self.env['res.users']._context['uid']).partner_id.id
                            values['recipient_ids'] = [(6, 0, email_to)]
                            if not values['email_to'] and not values['email_from']:
                                pass
                            msg_id = self.env['mail.mail'].create({
                                'body_html': values['body_html'],
                                'subject': values['subject'],
                                'email_to': values['email_to'],
                                'auto_delete': True,
                                'email_from': values['email_from'],
                                'references': values['mail_server_id'], })
                            mail_mail_obj = self.env['mail.mail']
                            if msg_id:
                                mail_mail_obj.sudo().send(msg_id)
                    else:
                        pass

            return True