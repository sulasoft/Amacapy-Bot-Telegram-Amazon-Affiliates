import time
from time import sleep
import requests
from threading import Thread
import threading
from bs4 import BeautifulSoup
from pyshorteners import Shortener
import pandas as pd
from pandas import ExcelWriter
import re


def enable(e):
	status_script = e
	if status_script:
		status_search   = True
		status_settings = True
		# To verify that the user has already added their publishing data: amazon id, telegram token and chat id.
		# If he has not added them, it will not perform the search and will show error.
		while status_settings:
			verify_setting  = pd.read_excel('data/setting.xlsx', header = 0)
			setting_amazon_id 	   = verify_setting['amazon_id'].values
			setting_telegram_token = verify_setting['telegram_token'].values
			setting_chat_id 	   = verify_setting['chat_id'].values

			if len(setting_amazon_id) == 1 and len(setting_telegram_token) == 1 and len(setting_chat_id) == 1:		
				amazon_id      = setting_amazon_id[0]
				telegram_token = setting_telegram_token[0]
				chatid         = setting_chat_id[0]
				status_settings = False
			else:
				print('Add your Amazon ID, Telegram Token and Chat ID in the Settings tab.')
				sleep(2)
				

		# So that the program is always active waiting for requests to perform searches.
		while status_search:

			verify_search_product  = pd.read_excel('data/search_product.xlsx', header = 0)

			title_product 	      = verify_search_product['title'].values
			region_product 	      = verify_search_product['region'].values
			publish_product       = verify_search_product['pub'].values
			quick_search          = verify_search_product['quick'].values

			if len(verify_search_product) > 0 and not pd.isnull(title_product[0]):

				keyword = title_product[0]
				region  = region_product[0]

				headers = []
				headers.append({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36', 'referer': f'https://google{region}',})
				headers.append({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36', 'referer':f'https://google{region}',})

				headers = headers[1]

				if region == '.com':
					currency = 'USD'
				elif region =='.in':
					currency = 'Rs'
				if region == '.com.br':
					currency = 'BRL'
				else:
					currency = 'EUR'
			
				# When the person enters the specific URL of a product, the program will scrape that web page.
				if keyword.startswith("http"):

					print(f'Searching...{keyword}')

					try:
						# Lists that will store the data obtained from the entered URL.
						new_title_result 	= []
						new_price_result 	= []
						new_currency_result = []
						new_check_result	= []
						new_url_result	    = []
						
						url = keyword

						req = requests.get(url, headers=headers, timeout=10)

						soup = BeautifulSoup(req.text, "html.parser")
													
						product_title = soup.find('span',  id="productTitle").text.strip()

						product_price = 0
						
						# The price of the product is searched for in different classes, if not found
						# the price of the product is set to 0.
						for k in range(0, 5):
							if headers != headers[1]:
								headers = headers[0]
							else:
								headers = headers[1]
							try:
								req = requests.get(url, headers=headers, timeout=10)
								sleep(3)
								soup = BeautifulSoup(req.text, "html.parser")
								
								try:
									product_stock = soup.find_all('span', class_="a-size-medium a-color-price")
									if len(product_stock) != 0:
										for n in product_stock:
											stock = n.text.strip()
											if 'out of stock' in stock:
												product_stock = 'no'
												break
											elif 'agotado' in stock:
												product_stock = 'no'
												break
											elif 'indisponível' in stock:
												product_stock = 'no'
												break
											elif 'No disponible' in stock:
												product_stock = 'no'
												break
											elif 'Non disponibile' in stock:
												product_stock = 'no'
												break
											elif 'unavailable' in stock:
												product_stock = 'no'
											else:
												pass
								except:
									pass

								if product_stock == 'no':
									break

								
								product_price = soup.find_all('span', class_="a-price a-text-price a-size-medium apexPriceToPay")
								print(product_price)
								if len(product_price) == 0:
									product_price = soup.find_all(class_="olpWrapper a-size-small")
									if len(product_price) == 0:
										product_price = soup.find_all('span', id="color_name_0_price")
										
										if len(product_price) == 0:
											product_price = soup.find_all('span', class_="a-size-base a-color-price")
											
											if len(product_price) == 0 or len(product_price) >= 2:
												
												try:
													product_price = soup.find('span', class_="a-offscreen").text.strip()
												except:
													product_price = '0'
											else:
												product_price = soup.find('span', class_="a-size-base a-color-price").text.strip()
												print(product_price)
												if len(product_price) > 6:
													product_price = '0'
												else:
													break
										else:
											product_price = soup.find('span', id="color_name_0_price").text.strip()
											# Method used to clean some data including price and other characters.
											all_price = ''
											for i in product_price:
												if '$' in all_price:
													all_price = ''
													all_price = f'{i}'
													
												else:
													all_price = f'{all_price}{i}'
											product_price = all_price
											break
									else:
										product_price = soup.find_all('span', class_="olpWrapper a-size-small")
										for i in product_price:
											product_price = i.text.strip()
											break
										all_price = ''
										for i in product_price:
											if '$' in all_price:
												all_price = ''
												all_price = f'{i}'
												
											else:
												all_price = f'{all_price}{i}'
										product_price = all_price
										break

								else:
									product_price = soup.find_all('span', class_="a-price a-text-price a-size-medium apexPriceToPay")
									for i in product_price:
										product_price = i.find('span', class_="a-offscreen").text.strip()
										break
									
									break

						    
							except Exception as e:
								print(str(e))
								product_price = "0"
								pass

						
						if product_stock == 'no':
							pass
						else:
							# Sometimes the program does not get the price, so it assigns these values. 
							# If this is the case, then the value of the variable "product_price" is changed to 0.
							try:
								
								if product_price == '':
									product_price = '0'
								elif 'US$' in product_price:
									new_currency_result.append('USD')
									product_price = product_price.replace('US$', '')
								elif 'R$' in product_price:
									new_currency_result.append('BRL')
									product_price = product_price.replace('R$', '')
								elif '$' in product_price:
									new_currency_result.append('USD')
									product_price = product_price.replace('$', '')
								elif '€' in product_price:
									new_currency_result.append('EUR')
									product_price = product_price.replace('€', '')
								else:
									check_price = float(product_price)

								if len(new_currency_result) == 0:
									if '.com' in keyword:
										new_currency_result.append('USD')
									elif '.in' in keyword:
										new_currency_result.append('Rs')
									elif '.com.br' in keyword:
										new_currency_result('BRL')
									else:
										new_currency_result.append('EUR')
							except Exception as e:
								print(str(e))
								product_price = '0'
								pass
							# These methods are used to clean the data obtained.
							# To remove currency symbols and change commas to dots.
							if product_price != 0 and ',' in product_price or product_price != '0' and ',' in product_price:
								product_price = product_price.replace(',' , '.')
							
							product_price = float(product_price)

							# The original link is modified by adding the amazon affiliates tag.
							product_link = f'{keyword}&tag={amazon_id}'

							new_title_result.append(product_title)
							new_price_result.append(product_price)
							new_check_result.append('no')
							new_url_result.append(product_link)
							
							search_result_data = {}

							search_result_data['title']    = new_title_result
							search_result_data['price']    = new_price_result
							search_result_data['currency'] = new_currency_result
							search_result_data['check']    = new_check_result
							search_result_data['url']      = new_url_result

							search_result_data = pd.DataFrame(search_result_data, columns = ['title', 'price', 'currency', 'check', 'url'])

							print('Product price: ', product_price)

							with ExcelWriter('data/search_result.xlsx') as writer:
								search_result_data.to_excel(writer, 'Sheet', index=False)

							search_product_data = pd.DataFrame(columns = ['title', 'region', 'pub', 'quick'])

							with ExcelWriter('data/search_product.xlsx') as writer:
								search_product_data.to_excel(writer, 'Sheet', index=False)
				
					except Exception as e:
						print(str(e))
						
				# The products will be searched on Amazon through a keyword entered.			
				else:
					count_product = 0
					try:
						print(f'Searching... {keyword} on amazon{region}')

						# The Amazon URL is modified with the selected region and the keyword of the product to be searched.
						url = f'https://www.amazon{region}/s?k={keyword}'

						req = requests.get(url, headers=headers, timeout=10)

						sleep(3)

						soup = BeautifulSoup(req.text, "html.parser")

						# Search for products through different classes
						products_list = soup.find_all('div', class_="s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16")

						if len(products_list) == 0:
							products_list = soup.find_all('div', class_="sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20")
							if len(products_list) == 0:
								products_list = soup.find_all(class_='s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis s-latency-cf-section s-card-border')									
								if len(products_list) == 0:
									products_list = soup.find_all(class_='sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20')

						# Lists that will store product data.												
						titles_products   = []
						urls_products     = []
						prices_products   = []
						currency_products = []
						check_products    = []

						# To select each product that is stored in the list of found products.
						for product in products_list:
							
							print("--------------------------------------------------------------")

							product_title = product.find_all('span', class_="a-size-base-plus a-color-base a-text-normal")
							
							if len(product_title) <= 0:
								product_title  = product.find_all('h2', class_="a-size-mini a-spacing-none a-color-base s-line-clamp-2")
							
								if len(product_title) <= 0:
									product_title = product.find('span', class_="a-size-base-plus a-color-base a-text-normal").text.strip()
								else:
									product_title  = product.find('h2', class_="a-size-mini a-spacing-none a-color-base s-line-clamp-2").text.strip()
							else:
								product_title = product.find('span', class_="a-size-base-plus a-color-base a-text-normal").text.strip()

							print(product_title)

							# The link is modified to add the amazon affiliates tag.
							product_link   = 'https://amazon' + region + product.find('a', class_='a-link-normal s-no-outline').get('href') + '&tag='+ amazon_id

							print('Link:  ', product_link)

							product_price = product.find('span', class_="a-price-whole")

							"""
							If the product does not show a price, it may be a variable product, 
							so the product is accessed directly to try to find its price.
							"""
							if product_price is None and 'no' in quick_search:
								
								try:
									for i in range(0, 3):
										if headers != headers[1]:
											headers = headers[0]
										else:
											headers = headers[1]

										new_req = requests.get(product_link, headers=headers, timeout=10)
										new_soup = BeautifulSoup(new_req.text, "html.parser")
										product_stock = new_soup.find_all('span', class_="a-size-medium a-color-price")
										
										if len(product_stock) != 0:
											for n in product_stock:
												stock = n.text.strip()
												if 'out of stock' in stock:
													product_stock = 'no'
													break
												elif 'agotado' in stock:
													product_stock = 'no'
													break
												elif 'indisponível' in stock:
													product_stock = 'no'
													break
												elif 'No disponible' in stock:
													product_stock = 'no'
													break

												elif 'Non disponibile' in stock:
													product_stock = 'no'
													break
												elif 'unavailable' in stock:
													product_stock = 'no'
													break
												else:
													pass

										if product_stock == 'no':
											break

										product_price = new_soup.find_all('span', class_="a-price a-text-price a-size-medium apexPriceToPay")
										if len(product_price) == 0:
											product_price = new_soup.find_all(class_="a-button a-button-selected a-button-thumbnail a-button-toggle")
											if len(product_price) == 0:
												product_price = new_soup.find_all(class_="swatch-list-item-text inline-twister-swatch reduced-text-swatch-width a-declarative desktop-configurator-dim-row-0")
												if len(product_price) == 0:
													product_price = new_soup.find_all('span', id="color_name_0_price")
													if len(product_price) == 0:
														product_price = new_soup.find_all('span', class_="a-size-base a-color-price")
														if len(product_price) == 0 or len(product_price) >= 2:
															product_price = '0'
														else:
															product_price = new_soup.find('span', class_="a-size-base a-color-price").text.strip()
															if len(product_price) > 6:
																product_price = '0'
															else:
																break
													else:
														product_price = new_soup.find('span', id="color_name_0_price").text.strip()
														# Method used to clean some data including price and other characters.
														all_price = ''
														for i in product_price:
															if '$' in all_price:
																all_price = ''
																all_price = f'{i}'
																
															else:
																all_price = f'{all_price}{i}'
														product_price = all_price
														break
												else:
													product_price = new_soup.find_all(class_="swatch-list-item-text inline-twister-swatch reduced-text-swatch-width a-declarative desktop-configurator-dim-row-0")
													for i in product_price:
														product_price = i.text.strip()
														break
													all_price = ''
													for i in product_price:
														if '$' in all_price:
															all_price = ''
															all_price = f'{i}'
															
														else:
															all_price = f'{all_price}{i}'
													product_price = all_price
													break
											else:
												product_price = new_soup.find_all('span', class_="a-button a-button-selected a-button-thumbnail a-button-toggle")
												for i in product_price:
													product_price = i.text.strip()
													break
												all_price = ''
												for i in product_price:
													if '$' in all_price:
														all_price = ''
														all_price = f'{i}'
														
													else:
														all_price = f'{all_price}{i}'
												product_price = all_price
												break
										else:
											product_price = new_soup.find_all('span', class_="a-price a-text-price a-size-medium apexPriceToPay")
											for i in product_price:
												product_price = i.find('span', class_="a-offscreen").text.strip()
												break
											break

									if product_stock == 'no':
										pass
									else:	
										# Sometimes the program does not get the price, so it assigns these values. 
										# If this is the case, then the value of the variable "product_price" is changed to 0.
										try:
											if product_price == '':
												product_price = '0'
											elif 'US$' in product_price:
												product_price = product_price.replace('US$' , '')
											elif '$' in product_price:
												
												product_price = product_price.replace('$' , '')
											elif '€' in product_price:
												product_price = product_price.replace('€' , '')
											else:
												check_price = float(product_price)

										except Exception as e:
											print(str(e))
											product_price = '0'

										print('Product Price: ' + str(product_price))

										# These methods are used to clean the data obtained.
										# To remove currency symbols and change commas to dots.
										if product_price != 0 and ',' in product_price:
											product_price = product_price.replace(',' , '.')

										if 'US$' in product_price:
											product_price = product_price.replace('US$' , '')
										elif '$' in product_price:
											product_price = product_price.replace('$' , '')
										elif '€' in product_price:
											product_price = product_price.replace('€' , '')
										else:
											pass

										# The data found are added to the lists.
										titles_products.append(product_title)
										urls_products.append(product_link)
										currency_products.append(currency)
										check_products.append('no')
										prices_products.append(product_price)
										
								except Exception as e:
									print(str(e))

									try:
										product_price = new_soup.find_all('span', class_="olp-message a-color-price")
										if len(product_price) == 0:
											product_price = new_soup.find_all('span', id="color_name_0_price")
											if len(product_price) == 0:
												product_price = new_soup.find('span', class_="a-offscreen").text.strip()
											else:
												product_price = new_soup.find('span', id="color_name_0_price").text.strip()
												# Method used to clean some data including price and other characters.
												all_price = ''
												for i in product_price:
													if '$' in all_price:
														all_price = ''
														all_price = f'{i}'
														new_currency_result.append('USD')
													else:
														all_price = f'{all_price}{i}'
												product_price = all_price
										else:
											product_price = new_soup.find('span', class_="a-size-base a-color-price").text.strip()


									except Exception as e:
										print(str(e))
										product_price = "0"
								
									# The data found are added to the lists.
									titles_products.append(product_title)
									urls_products.append(product_link)
									currency_products.append(currency)
									check_products.append('no')
									prices_products.append(product_price)
								
						
							else:
								try:
									product_price = product.find('span', class_="a-price-whole").text.strip()
									
									product_price = product_price.replace('.' , '')
									product_price = product_price.replace(',' , '.')
									product_price = float(product_price)
								except Exception as e:
									print(str(e))
									product_price = 0
									pass
									
								# The data found are added to the lists.
								titles_products.append(product_title)
								urls_products.append(product_link)
								currency_products.append(currency)
								check_products.append('no')
								prices_products.append(product_price)
							
						
						# The data is added to the file "search_results.xlsx" which will store the search results.
						search_result_data = {}
						search_result_data['title']    = titles_products
						search_result_data['price']    = prices_products
						search_result_data['currency'] = currency_products
						search_result_data['check']    = check_products
						search_result_data['url']      = urls_products

						search_result_data = pd.DataFrame(search_result_data, columns = ['title', 'price', 'currency', 'check', 'url'])

						with ExcelWriter('data/search_result.xlsx') as writer:
							search_result_data.to_excel(writer, 'Sheet', index=False)

						# The data in the file that stores the search requests is deleted so that it does not continue searching.
						delete_product_data = pd.DataFrame(columns = ['title', 'region', 'pub', 'quick'])

						with ExcelWriter('data/search_product.xlsx') as writer:
							delete_product_data.to_excel(writer, 'Sheet', index=False)

					except Exception as e:
						print(str(e))

			else:
				# When there are no requests, the following message will be displayed.
				for i in range(3):
					sleep(2)
					print(f'Waiting for request...{i}')
					status_script = False
	



		