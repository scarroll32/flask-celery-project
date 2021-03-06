import pytest
from pytest_factoryboy import register

from project import create_app, db as _db
from project.users.factories import UserFactory

register(UserFactory)


@pytest.fixture
def app():
    app = create_app('testing')
    return app


@pytest.fixture
def db(app):
    """
    https://github.com/pytest-dev/pytest-flask/issues/70
    """
    with app.app_context():
        _db.create_all()
        _db.session.commit()

        yield _db

        _db.session.remove()
        _db.drop_all()
