#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: itabas <itabas016@gmail.com>

from memory import create_app

app = create_app('config')
if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=int(app.config['PORT']), debug=app.config['DEBUG'])
