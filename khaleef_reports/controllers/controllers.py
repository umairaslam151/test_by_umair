# -*- coding: utf-8 -*-
# from odoo import http


# class KhaleefReports(http.Controller):
#     @http.route('/khaleef_reports/khaleef_reports/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/khaleef_reports/khaleef_reports/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('khaleef_reports.listing', {
#             'root': '/khaleef_reports/khaleef_reports',
#             'objects': http.request.env['khaleef_reports.khaleef_reports'].search([]),
#         })

#     @http.route('/khaleef_reports/khaleef_reports/objects/<model("khaleef_reports.khaleef_reports"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('khaleef_reports.object', {
#             'object': obj
#         })
