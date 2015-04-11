from fabric.api import *

env.project_name = 'shanereustle'

def production():
	""" Use the actual webserver """
	
	env.settings = 'production'
	env.hosts = ['shanereustle.com']
	env.user = 'ubuntu'

def deploy():
	""" Deploy the code """
	
	require('settings', provided_by=[production])
	
	with cd('/home/ubuntu/sites/shanereustle'):
		run('git pull')

