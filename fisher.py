"""
 Create on 2018/07/24.

"""
from app import create_app

__author__ = '红文'

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])
