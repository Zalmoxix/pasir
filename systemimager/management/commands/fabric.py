from django.core.management.base import BaseCommand, CommandError
import sys
from optparse import make_option
import argparse
import subprocess


'''
class Command(BaseCommand):
	option_list = BaseCommand.option_list + (
		make_option('-c',
			action='store',
			dest='command',
			type='string',
			help='Comando de prueba'),
		)
	
	def handle(self,*args, **options):
		if (options['command'] == "-c" or options['command'] == "-crea_fichero"):
			string="fab crea_fichero"
			subprocess.check_output(string, shell=True)
'''	
class Command(BaseCommand):
	help = 'Comando de administracion SystemImager desde linea de comandos'

	def add_arguments(self, parser):
		parser.add_argument('-c')
		args= parser.parse_args()

	def handle(self, *args, **options):
		if args.command=='-c':
			print hola
			string="fab crea_fichero"+sys.argv[1]
			subprocess.check_output(string, shell=True)
			

        

