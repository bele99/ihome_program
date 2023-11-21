# coding:utf-8

from flask import Blueprint, current_app, make_response
from flask_wtf import csrf

# Provide a blueprint for static files (web_html)
html = Blueprint("web_html", __name__)

# 127.0.0.1:5000/()
# 127.0.0.1:5000/(index.html)
# 127.0.0.1:5000/register.html
# 127.0.0.1:5000/favicon.ico   # The browser considers the website identifier and will request this resource.

@html.route("/<re(r'.*'):html_file_name>")
def get_html(html_file_name):
    """ provide the html file """
    
    # if html_file_name is "null", indicating that the access path is /, and the request is for the homepage.
    if not html_file_name:
        html_file_name = "index.html"

    # if html_file_name is not favicon.ico
    if html_file_name != "favicon.ico":
        html_file_name = "html/" + html_file_name

    # create a csrf_token value
    csrf_token = csrf.generate_csrf()

    # 
    resp = make_response(current_app.send_static_file(html_file_name))

    # set up cookie value
    resp.set_cookie("csrf_token", csrf_token)

    return resp