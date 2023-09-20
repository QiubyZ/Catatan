from threading import Thread
from time import sleep

kumpulan_data = 10000
eksekusi_perdata = 5
list_threads = []

def Minta(data):
	print(f"Meminta data {data}")
	sleep(3)
	print(f"Data terambil {data}")

for datas in range(kumpulan_data):
	t = Thread(target=Minta, args=(datas,))
	list_threads.append(t)
	
for i in range(0, len(list_threads), eksekusi_perdata):
	batch_thread = list_threads[i:i+eksekusi_perdata]
	for start_thread in batch_thread:
		start_thread.start()
		
	for result in batch_thread:
		result.join()
