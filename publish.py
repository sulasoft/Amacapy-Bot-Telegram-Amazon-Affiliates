import time
from time import sleep
import requests
from threading import Thread
import threading
from bs4 import BeautifulSoup
from pyshorteners import Shortener
import pandas as pd
from pandas import ExcelWriter
from datetime import datetime


def enable(e):
	status_script = e
	if status_script:
		# To keep the program active waiting for requests.
		status_publish = True

		count_products = 0

		# To know if URL shorteners will be used or not.
		verify_short_url  = pd.read_excel('data/short_url.xlsx', header = 0)
		url_short = verify_short_url['short_url'].values
		sleep(1)

		# To verify program development support data.
		verify_support_dev  = pd.read_excel('data/support_dev.xlsx', header = 0)
		sup_tag 	        = verify_support_dev['sup_tag'].values
		sup_dev 	        = verify_support_dev['sup_dev'].values

		sup_tag = sup_tag[0]
		sup_dev = sup_dev[0]

		while status_publish:
			try:
				# It is confirmed that there are products added to be published.
				verify_publish  = pd.read_excel('data/publish_on.xlsx', header = 0)
				

				if len(verify_publish) > 0:
					title_publish 	      = verify_publish['title'].values
					price_publish 	      = verify_publish['price'].values
					url_publish           = verify_publish['url'].values
					min_publish			  = verify_publish['min'].values
					telegram_publish      = verify_publish['telegram'].values

					# To get the configuration data, such as Telegram Token and Chat ID.
					verify_setting  	  = pd.read_excel('data/setting.xlsx', header = 0)
					telegram_token 		  = verify_setting['telegram_token'].values
					chat_id 	   		  = verify_setting['chat_id'].values

					# To obtain the data stored with the custom message for the publications.
					verify_custom_message           = pd.read_excel('data/custom_message.xlsx', header = 0)
					before_title_message 	        = verify_custom_message['before_title'].values
					original_price_message	        = verify_custom_message['original_price'].values
					sale_price_message 	        	= verify_custom_message['sale_price'].values
					currency_message	            = verify_custom_message['currency'].values
					url_message				        = verify_custom_message['url'].values			
					
					for i in range(len(verify_publish)):
						sleep(2)
						# Check again that there are products to be published.
						new_verify_publish  = pd.read_excel('data/publish_on.xlsx', header = 0)

						if len(new_verify_publish) > 0:
							
							new_url_publish = url_publish[i]
							
							# When the published products counter reaches 3, a product will be published with the developer's affiliate tag.
							# This will only happen if the user has the option activated to support the development of the program.
							if count_products == 5 and 'yes' in sup_dev:
								headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36', 'referer': f'https://google.com',}

								try:
									req = requests.get(url_publish[i], headers=headers, timeout=10)

									soup = BeautifulSoup(req.text, "html.parser")

									product_link = soup.find('link', rel='canonical').get('href') + '/&tag=' + sup_tag

								except:

									req = requests.get(url_publish[i], headers=headers, timeout=10)

									soup = BeautifulSoup(req.text, "html.parser")

									product_link = soup.find('link', rel='canonical').get('href') + '/&tag=' + sup_tag

								try:
									new_url_publish = Shortener().tinyurl.short(product_link)
								except:
									sleep(3)
									new_url_publish = Shortener().tinyurl.short(product_link)
									pass

								print('Thank you! 😊')
								count_products = 0
							else:
								count_products += 1


							# To verify if any url shortener will be used.
							try:
								if url_short[0] == 'tinyurl':
									new_url_publish = Shortener().tinyurl.short(new_url_publish)
								elif url_short[0] == 'isgd':
									new_url_publish = Shortener().isgd.short(new_url_publish)
								elif url_short[0] == 'dagd':
									new_url_publish = Shortener().dagd.short(new_url_publish)
								else:
									pass
							except:
								sleep(3)
								if url_short[0] == 'tinyurl':
									new_url_publish = Shortener().tinyurl.short(new_url_publish)
								elif url_short[0] == 'isgd':
									new_url_publish = Shortener().isgd.short(new_url_publish)
								elif url_short[0] == 'dagd':
									new_url_publish = Shortener().dagd.short(new_url_publish)
								else:
									pass

							# It will publish on Telegram the products that were selected to be published.
							if 'yes' in telegram_publish[i]:
								try:
									requests.post('https://api.telegram.org/bot' + telegram_token[0] + "/sendMessage",
										data = {'chat_id' : f'@{chat_id[0]}', 
												'text': 
												before_title_message[0] + ' ' + title_publish[i] + '\n \n' + sale_price_message[0] + ' ' + str(price_publish[i]) + ' ' + currency_message[0] + '\n' + original_price_message[0]  + ' ' + str(round(price_publish[i] + (price_publish[i]*30/100 ), 2)) + ' ' + currency_message[0] + '\n' + url_message[0] + ' ' + new_url_publish
												})
								except:
									sleep(10)
									requests.post('https://api.telegram.org/bot' + telegram_token[0] + "/sendMessage",
										data = {'chat_id' : f'@{chat_id[0]}', 
												'text': 
												before_title_message[0] + ' ' + title_publish[i] + '\n \n' + sale_price_message[0] + ' ' + str(price_publish[i]) + ' ' + currency_message[0] + '\n' + original_price_message[0]  + ' ' + str(round(price_publish[i] + (price_publish[i]*30/100 ), 2)) + ' ' + currency_message[0] + '\n' + url_message[0] + ' ' + new_url_publish
												})

							
							# It will save the current date.		
							date_publish = datetime.now()
							
							try:
								# To remove the published product from the list of requests.
								verify_publish  = pd.read_excel('data/publish_on.xlsx', header = 0)
								verify_publish = verify_publish.drop(0)
								update_publish_data = pd.DataFrame(verify_publish, columns = ['title', 'price', 'url', 'min', 'telegram'])
							
								with ExcelWriter('data/publish_on.xlsx') as writer:
									update_publish_data.to_excel(writer, 'Sheet', index=False)
							except:
								try:
									sleep(3)
									# To remove the published product from the list of requests.
									verify_publish  = pd.read_excel('data/publish_on.xlsx', header = 0)
									verify_publish = verify_publish.drop(0)
									update_publish_data = pd.DataFrame(verify_publish, columns = ['title', 'price', 'url', 'min', 'telegram'])
								
									with ExcelWriter('data/publish_on.xlsx') as writer:
										update_publish_data.to_excel(writer, 'Sheet', index=False)
								except:
									update_publish_data = pd.DataFrame(columns = ['title', 'price', 'url', 'min', 'telegram'])
								
									with ExcelWriter('data/publish_on.xlsx') as writer:
										update_publish_data.to_excel(writer, 'Sheet', index=False)

							# To remove the published product from the list of products to be published.
							try:
								verify_list_publish  = pd.read_excel('data/list_publish.xlsx', header = 0)
								verify_list_publish = verify_list_publish.drop(0)
								update_list_publish_data = pd.DataFrame(verify_list_publish, columns = ['title', 'price', 'currency', 'url'])
							
								with ExcelWriter('data/list_publish.xlsx') as writer:
									update_list_publish_data.to_excel(writer, 'Sheet', index=False)
							except:
								try:
									sleep(3)
									verify_list_publish  = pd.read_excel('data/list_publish.xlsx', header = 0)
									verify_list_publish = verify_list_publish.drop(0)
									update_list_publish_data = pd.DataFrame(verify_list_publish, columns = ['title', 'price', 'currency', 'url'])
								
									with ExcelWriter('data/list_publish.xlsx') as writer:
										update_list_publish_data.to_excel(writer, 'Sheet', index=False)
								except:
									update_list_publish_data = pd.DataFrame(columns = ['title', 'price', 'currency', 'url'])
									with ExcelWriter('data/list_publish.xlsx') as writer:
										update_list_publish_data.to_excel(writer, 'Sheet', index=False)

							# To add the published product to the history.
							try:
								verify_history   = pd.read_excel('data/history.xlsx', header = 0)
								add_history = {'date': date_publish.today(), 'title': title_publish[i], 'price': price_publish[i], 'url': url_publish[i], 'platform': 'Telegram'}
								add_history = pd.DataFrame(add_history, index=[0])

								verify_history  = pd.concat([verify_history, add_history], axis=0)
								update_history_data = pd.DataFrame(verify_history, columns = ['date', 'title', 'price', 'url', 'platform'])
							
								with ExcelWriter('data/history.xlsx') as writer:
									update_history_data.to_excel(writer, 'Sheet', index=False)
							except:
								try:
									sleep(3)
									verify_history   = pd.read_excel('data/history.xlsx', header = 0)
									add_history = {'date': date_publish.today(), 'title': title_publish[i], 'price': price_publish[i], 'url': url_publish[i], 'platform': 'Telegram'}
									add_history = pd.DataFrame(add_history, index=[0])

									verify_history  = pd.concat([verify_history, add_history], axis=0)
									update_history_data = pd.DataFrame(verify_history, columns = ['date', 'title', 'price', 'url', 'platform'])
							
									with ExcelWriter('data/history.xlsx') as writer:
										update_history_data.to_excel(writer, 'Sheet', index=False)

								except:
									update_history_data = pd.DataFrame(columns = ['date', 'title', 'price', 'url', 'platform'])
							
									with ExcelWriter('data/history.xlsx') as writer:
										update_history_data.to_excel(writer, 'Sheet', index=False)

							sleep(float(min_publish[i])*60)

						else:
							break

				else:
					# If there are no requests, it will wait for a new one.
					print('Waiting for publish...')
					sleep(1)
					status_script = False


			except Exception as e:
				print('Error ' + str(e))

