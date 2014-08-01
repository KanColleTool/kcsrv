#!/usr/bin/env python
from flask.ext.script import Manager, Server
from flask.ext.migrate import MigrateCommand
from kcsrv import app

manager = Manager(app)
manager.add_command('runserver', Server(host='0.0.0.0', use_reloader=True))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()
