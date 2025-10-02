# -*- coding: utf-8 -*-
import logging
import json
from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)


class WhatsappWebhookController(http.Controller):

    @http.route('/api/v1/whatsapp/webhook', type='json', auth='public', methods=['POST'], csrf=False, cors="*")
    def whatsapp_webhook(self):
        """Endpoint called by 360dialog when messages/events happen"""
        payload = request.jsonrequest or {}
        _logger.info("Received WhatsApp webhook: %s", json.dumps(payload))

        try:
            request.env['wa.webhook.messages'].sudo().create({
                'json_content': json.dumps(payload)
            })
        except Exception as e:
            _logger.error("Failed to store WhatsApp webhook: %s", e)

        return {"status": "ok"}
