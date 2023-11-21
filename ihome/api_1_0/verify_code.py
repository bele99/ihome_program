
from . import api
from ihome.utils.captcha.captcha import captcha
from ihome import redis_store, constants
from flask import current_app, jsonify, make_response
from ihome.utils.response_code import RET

# GET 127.0.0.1/api/v1.0/image_codes/<image_code_id>
@api.route("/image_codes/<image_code_id>")
def get_image_code(image_code_id):
    """
    get image code
    :params image_code_id: the code of image ID
    :return: the image of code   error: return json
    """

    # Processing the business logic for the image of code
    # generate the image of code
    name, text, image_data = captcha.generate_captch()
    
    # Save the actual value and number of the verification code in Redis and set the validity period.
    # redis：  text   list   hash   set
    # "key": xxx
    # The time can only be set globally when using the hash to maintain the validity period.
    # "image_codes": {"id1":"abc", "":"", "":""} hash  hset("image_codes", "id1", "abc")  hget("image_codes", "id1")

    # "image_code_1": "value"
    # "image_code_2": "value"

    # redis_store.set("image_code_%s" % image_code_id, text)
    # redis_store.expire("image_code_%s" % image_code_id, constants.IMAGE_CODE_REDIS_EXPIRES)
    #                   recording name              period of validity                  recording value
    try:
        redis_store.setex("image_code_%s" % image_code_id, constants.IMAGE_CODE_REDIS_EXPIRES, text)
    except Exception as e:
        # Recording log
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR,  errmsg="Failed to save image verification code!!!")

    # return image
    resp = make_response(image_data)
    resp.headers["Content-Type"] = "image/jpg"
    return resp



