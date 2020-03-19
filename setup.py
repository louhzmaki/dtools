import os
import sys
from setuptools import setup, find_packages

try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

requirements = [str(ir.req) for ir in parse_requirements("requirement", session=False)]

if not os.path.exists("/etc/fdfs"):
	os.mkdir("/etc/fdfs")
os.system("\cp ./conf/client.conf /etc/fdfs/")

setup(
	name = "dtools",
	version = "1.0",
	author = "louhuazhe",
	author_email = "707553427@qq.com",
	license ='ehualu',
	description = "data operator tool",
	url = "https://github.com/louhzmaki/dtools",
	packages=find_packages(),
	package_data={'': ['*.*']},
	install_requires=requirements,
	entry_points = {
		'console_scripts':[
			"dtools = dtools.__init__:choose"
		]
	},
	classifiers=[
        	'Programming Language :: Python',
        	'Operating System :: Microsoft :: Windows',
        	'Operating System :: Unix'
    	],
)
