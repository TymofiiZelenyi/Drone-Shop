import flask 

user = flask.Blueprint(
    name= "user",
    import_name= "user",
    static_url_path= "/user/static",
    static_folder= "static",
    template_folder= "templates"
)