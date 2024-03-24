from dynaconf import FlaskDynaconf  # type: ignore


def init_app(app):  # type: ignore
    FlaskDynaconf(
        app=app,
        extensions_list=True,
        settings_files=['settings.toml', '.secrets.toml'],
    )
