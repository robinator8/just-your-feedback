from pyramid.config import Configurator


def main(global_config, **settings):
    """
    Configurator docs: https://docs.pylonsproject.org/projects/pyramid/en/latest/api/config.html
    """
    with Configurator(settings=settings) as config:
        config.include('pyramid_jinja2')

        # Include views
        config.include('webapp.views.example')
        config.include('webapp.views.home')

        config.scan('webapp.views')
        return config.make_wsgi_app()
