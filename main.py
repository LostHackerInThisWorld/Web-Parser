import requests

def main():
	url = str(input("Сайт который нужно спарсить -> "))

	website = requests.get(url)

	try:
		if website.status_code == 200:
			with open('websitecode.txt', 'w') as f:
				f.write(str(website.text))
				f.close()
				print("Страница сохранена в файл " + str(f.name) + "!\n")
				input("Enter, чтобы выйти.")
				main()
		else:
			print("Неверный адрес страницы или у вас нет доступа к ней!\n")
			main()
	except Exception as exception:
		print(exception)
		
main()