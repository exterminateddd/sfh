from sys import path
path.insert(0, '/home/exter/projects/sfh/sfh-test-flask')

activate_this = '/home/exter/.local/share/virtualenvs/sfh-test-flask-DcAqW0j6/bin/activate_this.py'

with open(activate_this) as f:
    exec(file.read(), dict(__file__=activate_this))

from main import app as application
