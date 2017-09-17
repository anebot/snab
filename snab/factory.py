# -*- coding: utf-8 -*-
"""
    SNAB
    ~~~~~~

    SimpleNote as Blog is an application for publishing 
    your SimpleNote notes as blog posts.

    Tag your notes simply with one of the values defined at SN_PUBLISH_TAGS
    and they will be published.
    
    :copyright: (c) 2017 by Artur Nebot.
    :license: BSD, see LICENSE for more details.
"""

import os
from flask import Flask, g
from werkzeug.utils import find_modules, import_string

def create_app(config=None):
    app = Flask('snab')
    app.config.update(config or {})
    app.config.from_envvar('SNAB_SETTINGS', silent=True)

    register_blueprints(app)

    return app


def register_blueprints(app):
    """Register all blueprint modules

    Reference: Armin Ronacher, "Flask for Fun and for Profit" PyBay 2016.
    """
    for name in find_modules('snab.blueprints'):
        mod = import_string(name)
        if hasattr(mod, 'bp'):
            app.register_blueprint(mod.bp)
    return None
