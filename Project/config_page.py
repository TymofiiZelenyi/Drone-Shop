from flask_login import current_user
import flask, functools

def config_page(rule_name: str):
    def manage(function: object):
        @functools.wraps(function)
        def inner(*args, **kwargs):
            context =  function(*args, **kwargs)
            return flask.render_template(
                template_name_or_list= rule_name,
                current_user = current_user,
                **context
            )
        return inner
    return manage