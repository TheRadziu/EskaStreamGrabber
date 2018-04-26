################# Developed by TheRadziu #################

from urllib2 import urlopen
import re
import argparse
import os

#Check if script is run through Kodi, if yes, set isKodi value to True, otherwise False
try:
		import xbmc
		isKodi = True
except ImportError:
	isKodi = False
	print ('This isnt Kodi')

#Some hardcoded shit I needed
current_dir = os.path.dirname(os.path.abspath(__file__))
lista_stacji = '-rock | Eska ROCK\n-kultowa-godzina | Eska ROCK Kultowa Godzina\n-hot-rock | Eska ROCK Hot Rock\n-alternative | Eska ROCK Alternative\n-polska | Eska ROCK Polska'
extension = '.mp3'

#Arguments'n'stuff..
parser = argparse.ArgumentParser(usage='%(prog)s [-stacja]', add_help=False)
stacje = parser.add_mutually_exclusive_group(required=True)
stacje.add_argument('-rock', action='store_true', help='Eska ROCK')
stacje.add_argument('-kultowa-godzina', action='store_true', help='Eska ROCK Kultowa Godzina')
stacje.add_argument('-hot-rock', action='store_true', help='Eska ROCK Hot Rock')
stacje.add_argument('-alternative', action='store_true', help='Eska ROCK Alternative')
stacje.add_argument('-polska', action='store_true', help='Eska ROCK Polska')
stacje.add_argument('-lista', action='store_true', help='Lista Stacji')
stacje.add_argument('-help', '-h', '-pomoc', action='store_true', help='Pomoc')
args, leftovers = parser.parse_known_args()

def main(): 
	#Grab tokens
	source_site = urlopen(url_radio).read().decode('utf-8')
	m = re.compile('.+http://waw.ic.smcdn.pl/'+ url_stream_file +''+ extension +'([^\']*).*')

	#Create URL if tokens are present
	for line in source_site.splitlines():
		res = m.match(line)
		if res is not None:
			res_string = "http://waw.ic.smcdn.pl/"+ url_stream_file +".aac{}".format(res.groups()[0].decode("utf-8"))
			
	#Get full path with filename
	full_path = current_dir + "/" + file_name + ".m3u"
		
	#Save to file
	f = open(str(full_path),"w+")
	f.write('#EXTINF:0 group-title="Eska Rock",'+ file_name)
	f.write('\n'+ res_string)
	f.close()
	
	#If run on kodi, stop previous file and play selected Station
	if isKodi == True:
		play_file = 'PlayMedia(%s)' % full_path
		xbmc.executebuiltin("PlayerControl(Stop)")
		xbmc.executebuiltin(play_file)

if args.lista == True:
	print ('Aktualnie wspierane stacje przez skrypt to:')
	print (lista_stacji)
	exit()
elif args.help == True:
	print ('Eska Stream Grabber. Napisane przez TheRadziu & juliosueiras\n Skrypt wymaga wybrania conajmniej jednej stacji:\n')
	print (lista_stacji)
	exit()
elif args.rock == True:
	print ('Wybrano: Eska ROCK')
	url_radio = 'http://www.eskago.pl/radio/eska-rock'
	url_stream_file = 't041-1'
	extension = '.aac'
	file_name = 'Eska Rock'
	main()
elif args.kultowa_godzina == True:
	print ('Wybrano: Eska ROCK Kultowa Godzina')
	url_radio = 'http://www.eskago.pl/radio/eska-rock-kultowa-godzina'
	url_stream_file = 't013-1'
	file_name = 'Eska Rock Kultowa Godzina'
	main()
elif args.hot_rock == True:
	print ('Wybrano: Eska ROCK Hot Rock')
	url_radio="http://www.eskago.pl/radio/eska-rock-hot-rock"
	url_stream_file="t028-1"
	file_name="Eska Rock Hot Rock"
	main()
elif args.alternative == True:
	print ('Wybrano: Eska ROCK Alternative')
	url_radio = 'http://www.eskago.pl/radio/eska-rock-alternative'
	url_stream_file = 't015-1'
	file_name = 'Eska Rock Alternative'
	main()
elif args.polska == True:
	print  ('Wybrano: Eska ROCK Polska')
	url_radio = 'http://www.eskago.pl/radio/eska-rock-polska'
	url_stream_file = 't008-1'
	file_name = 'Eska Rock Polska'
	main()