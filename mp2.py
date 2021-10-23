import requests
from requests import Session
from bs4 import BeautifulSoup
import re
from multiprocessing.dummy import Pool as ThreadPool

# another one user-agent # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11.6; rv:51.0.1) Gecko/20100101 Firefox/51.0.1',

with requests.Session() as session:
	# start of auth
	s = Session()
	AUTH_URL = 'https://auth.mail.ru/cgi-bin/auth'
	headers = {
		'Login': '12312.312312@mail.ru',
		'Password': '12123@b',
		'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0",
		'Content-Type': 'application/x-www-form-urlencoded',
		'Connection': 'keep-alive',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Referer': 'http://mail.ru/',
		'remember': 1,
	}
	# Отправляем данные в POST, в session записываются наши куки
	s.post(AUTH_URL, headers)
	# end auth

	def get_total_pages():
		tut = []
		base_url = 'https://my.mail.ru/community/fuck_humor18/friends?page=%s'
		for url in [base_url % i for i in range(1, 64)]:  
			tut.append(url)
		print(tut)
		#get_data_from_page(tut)
		pool = ThreadPool(8)
		results = pool.map(get_data_from_page, tut)

	def get_data_from_page(tut):
		
		f = open("emails.txt", 'a')
		email = []
		link = s.get(tut).text
		soup = BeautifulSoup(link, 'lxml')
		try:
			links = soup.find('div', class_="mens").find_all('span', class_="inviz")
		
			for e in links:
				emails = e.text
				f.write(emails + ', ')
				email.append(emails)
			print(email)
		except:
			pass


	def main():
		get_total_pages()
		



	if __name__ == '__main__':
		main()