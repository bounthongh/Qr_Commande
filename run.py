# pylint: disable=C0111
# pylint: disable=C0103

import os
from app import create_app

config_name = os.getenv('API_venv')
if config_name is None:
    config_name = "development"
api = create_app(config_name)

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=8085)
