# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "internal_aireldentalchairs"
app_title = "Aireldentalchair.com"
app_publisher = "UandH Technologies"
app_description = "Aireldentalchair.com website"
app_icon = "fa fa-globe"
app_color = "black"
app_email = "info@Aireldentalchair.com"
app_url = "https://aireldentalchair.com"
app_version = "0.0.1"
hide_in_installer = True

website_context = {
	"brand_html": "<img class='mr-2 d-inline-block align-top' src='/assets/internal_aireldentalchairs/img/erpnext-logo-blue.svg' />ERPNext",
	"hide_login": 1,
	"favicon": "/assets/internal_aireldentalchairs/img/erpnext-logo-blue.png"
}

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/internal_aireldentalchairs/css/internal_aireldentalchairs.css"
# app_include_js = "/assets/internal_aireldentalchairs/js/internal_aireldentalchairs.js"

# include js, css files in header of web template
web_include_css = "/assets/internal_aireldentalchairs/css/custom.css"
web_include_js = "/assets/internal_aireldentalchairs/js/payment.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
home_page = "index"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "internal_aireldentalchairs.install.before_install"
# after_install = "internal_aireldentalchairs.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "internal_aireldentalchairs.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"internal_aireldentalchairs.tasks.all"
# 	],
# 	"daily": [
# 		"internal_aireldentalchairs.tasks.daily"
# 	],
# 	"hourly": [
# 		"internal_aireldentalchairs.tasks.hourly"
# 	],
# 	"weekly": [
# 		"internal_aireldentalchairs.tasks.weekly"
# 	]
# 	"monthly": [
# 		"internal_aireldentalchairs.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "internal_aireldentalchairs.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "internal_aireldentalchairs.event.get_events"
# }

fixtures = ["Contact Us Settings"]
