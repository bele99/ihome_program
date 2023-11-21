# coding:utf-8

from . import api
from ihome import db, models
# Import logging
from flask import current_app
from flask import session, make_response

@api.route("/index")
def index():
    try:
        current_app.logger.error("error info")
        current_app.logger.warn("warn info")
        current_app.logger.info("info info")
        current_app.logger.debug("debug info")
        return "index page"
    except Exception as e:
        current_app.logger.exception("An error occurred: %s", str(e))
        return "Internal Server Error", 500
        
@api.route('/set_session')
def set_session():
    # Simulating getting session_id from Flask-Session
    session_id = session.get('_id', b'').decode('utf-8')
    
    # Set the cookie using the decoded session_id
    response = make_response("Setting session")
    response.set_cookie(app.config["SESSION_COOKIE_NAME"], session_id)
    
    return response