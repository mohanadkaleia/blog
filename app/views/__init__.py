from .blog import app as blog_app

def register(app):
    app.register_blueprint(blog_app)
