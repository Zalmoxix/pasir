from fabric.api import run
from fabric.api import env
from fabric.api import *
import sys
import subprocess

#######################################

env.hosts = [
    'root@192.168.3.109',
    ]
server = '192.168.3.1'

#######################################


def hello():
    print("Hello world!")

def host_type():
    run('uname -s')

def crea_fichero(fichero=sys.argv[0]):
	run('touch '+fichero)
    
def diskspace():
    run('df')

def prepara_cliente():
	run('si_prepareclient --server '+server+" --no-uyok --yes >> "+server+".log")

def get_imagen(golden=sys.argv[0], imagen=sys.argv[1]):
	string="sudo si_getimage --golden-client "+golden+" --image "+imagen
	subprocess.check_output(string, shell=True)
