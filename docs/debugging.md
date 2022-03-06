# Debugging

## Flask Shell

```
source env/bin/activate
FLASK_APP=app.py flask shell
>>> from project.users.models import User
>>> user = User(username='test3', email='test3@example.com')
>>> db.session.add(user)
>>> db.session.commit()
User.query.all()
```
