import os
import tempfile

import pytest

from app import create_app


@pytest.fixture(scope="session")
def client():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if not os.path.exists(BASE_DIR + '/app/tmp'):
        os.mkdir(BASE_DIR + '/app/tmp')
    test_db_fd, test_db_path = tempfile.mkstemp('.db')
    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': "sqlite://%s" % test_db_path,
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    })
    client = app.test_client()
    yield client
    os.close(test_db_fd)
    os.unlink(BASE_DIR + '/app' + test_db_path)
    os.rmdir(BASE_DIR + '/app/tmp')
