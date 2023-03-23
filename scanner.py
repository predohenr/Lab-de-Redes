import scapy.all as scapy
from threading import Timer

class RepeatTimer(Timer):
	def run(self):
		while not self.finished.wait(self.interval):
			self.function(*self.args, **self.kwargs)
def scan(ip):
	print(f"[+] Scanning {ip}...")
	arp_request= scapy.ARP(pdst=ip)
	broadcast= scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
	arp_request_broadcast = broadcast/arp_request
	answered_list=scapy.srp(arp_request_broadcast, timeout = 1)[0]
	client_list=[]
	for packet in answered_list:
		client_dict={'ip': packet[1].psrc, 'mac': packet[1].hwsrc}
		client_list.append(client_dict)
	print(client_list)
	stop = input("digite 's' para parar o programa\n")
	if stop == 's':
		 timer.cancel()

#FAÇA AQUI A PARTE DO CODIGO QUE DA AO USUARIO PODER DE DECIDIR
#QUANDO PARAR O SCRIPT

subnet='10.0.84.0/24'
timer=RepeatTimer(1.0,scan,[subnet])
timer.start()
