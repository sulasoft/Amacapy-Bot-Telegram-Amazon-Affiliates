import flet as ft
from flet import Page, Text, Row, TextField, ElevatedButton, Checkbox, Column, Container, IconButton, Theme
import time
from time import sleep
import requests
import io
from io import open
import webbrowser
import pandas as pd
from pandas import ExcelWriter
from datetime import datetime
from multiprocessing import Process
import search_products
import publish
from os import remove


# Starting the scripts that will search for products on Amazon and post on Telegram.
def script_search_products():
	search_products.enable(True)

def script_publish():
	publish.enable(True)



if __name__ == '__main__':
	
	processes_search_product = []
	processes_publish_product = []
	for i in range(0, 500):
		processes_search_product.append(Process(target=script_search_products))
		processes_publish_product.append(Process(target=script_publish))

#	thread_search_product = Process(target=script_search_products)
#	thread_publish_product = Process(target=script_publish)

	def main(page: ft.Page):
		
		# Defining the program title and design
		page.window_maximizable = True
		page.title = "Amacapy 2.0"
		page.vertical_alignment = "center"
		page.horizontal_alignment = "center"
		page.window_width = 720
		page.window_height = 680
		page.window_resizable = True
		page.theme_mode = ft.ThemeMode.DARK
		
		


		title_amacapy = Text(
		value="Amacapy",
		size=30,
		color="white",
		weight="bold",
		italic=True,
		)
		page.add(title_amacapy)

		def main_interface():

			# This function will display the screen with the list of products that will be ready to be published.
			def page_publish(self):
				try:
					# We read the file where the product data is stored
					verify_list_publish  = pd.read_excel('data/list_publish.xlsx', header = 0)

				except:
					sleep(2)
					try:
						# We read the file where the product data is stored
						verify_list_publish  = pd.read_excel('data/list_publish.xlsx', header = 0)
					except:
						remove('data/list_publish.xlsx')
						update_list_publish_data = pd.DataFrame(columns = ['title', 'price', 'currency', 'url'])
						with ExcelWriter('data/list_publish.xlsx') as writer:
							update_list_publish_data.to_excel(writer, 'Sheet', index=False)

				title_list_publish 	      = verify_list_publish['title'].values
				price_list_publish 	      = verify_list_publish['price'].values
				currency_list_publish  	  = verify_list_publish['currency'].values
				url_list_publish  	      = verify_list_publish['url'].values

				# Title that will appear in the publish products view.
				title_head_list_publish = Text(
				value="Products to Publish",
				size=20,
				color="white",
				weight="bold",
				italic=True,
				)

				all_results = ft.Column(scroll="always", expand=True)

				# The file is checked for stored data to be able to display it on the screen.
				if len(verify_list_publish) > 0:
					currency = f"({currency_list_publish[0]})"

					for i in range(len(verify_list_publish)):

						all_results.controls.append(
						ft.Row(spacing=28, run_spacing=5, controls=[
											Text(f"{i+1}. "),
											ft.IconButton(on_click=view_url_list_publish, data = i, icon="remove_red_eye_rounded", icon_size=20),
											ft.TextField(value=title_list_publish[i], label = i, on_blur=change_title_publish, text_align="start", keyboard_type = "text", width=250, height = 50, text_size=12, content_padding = 10),
											ft.TextField(value=price_list_publish[i], label = i, on_blur=change_price_publish, text_align="start", keyboard_type = "number", width=70, height = 50, text_size=12, content_padding = 10),
											ft.IconButton(on_click=delete_product_button, data = i,  icon="delete_forever_rounded", icon_size=20),
											], alignment="center", vertical_alignment = "center")
										
									) 

				# If the file has no data, then a message that there are no products is displayed.	
				else: 
					currency = ''
					all_results.controls.append(
						ft.Row(spacing=40, run_spacing=10, controls=[
											Text("You have not yet added articles for publication")
											], alignment="center", vertical_alignment = "center")
										
									) 
						
				page.clean() # We clean the screen before adding a new one.
				page.add(
					ft.Container(height = 50, content= title_head_list_publish, alignment=ft.alignment.center),
					ft.Divider(height=1, color="black"),
					ft.Row(spacing=1, controls=[
							Text('N°', color="white", width=55, text_align="center"),
							Text('View', color="white", width=60, text_align="center"), 
							Text('Product Title', color="white", width=290, text_align="center"),
							Text(f'Price {currency}', color="white", width=80, text_align="center"),
							Text('Del',width=80, text_align="center", color="white"), 
							],
							alignment="center", vertical_alignment = "center"),
					ft.Divider(height=1, color="black"),
					ft.Container(width= 650, height= 348, content=all_results),
					ft.Container(width= 650, height= 40, content=ft.Row(controls=[
							ft.ElevatedButton("Delete All", icon="delete_rounded", on_click=delete_all_products_publish)
							],
							alignment="end", vertical_alignment = "start")
					),
					ft.Row(controls=[
							Text('Publish every', width=90, text_align="start",color="white"),
							minutes_publish,
							Text('on', width=20, text_align="start", color="white"),
							ft.ElevatedButton('Telegram' ,icon="telegram_rounded", on_click=publish_on_telegram),
							],
							alignment="center", vertical_alignment = "center"),					
					ft.Container(content= ft.Row(controls=list_all_button_menu,
										alignment="center", vertical_alignment = "end"), 
								height = 50
							)
					)

			# The same process is repeated as in the page_publish function
			# But in this case to see the history of published products.
			def page_history(self):
				# The file that stores the history of published products is read.
				verify_history  = pd.read_excel('data/history.xlsx', header = 0)

				date_history 	      = verify_history['date'].values
				title_history 	      = verify_history['title'].values
				price_history 	      = verify_history['price'].values
				url_history  	      = verify_history['url'].values
				platform_history  	  = verify_history['platform'].values

				# Title that will appear in the history view.
				title_list_history = Text(
				value="History of published products",
				size=20,
				color="white",
				weight="bold",
				italic=True,
				)

				all_results = ft.Column(scroll="always", expand=True)

				# The file is checked for stored data to be able to display it on the screen.
				if len(verify_history) > 0:

					for i in range(len(verify_history)):
						new_date = date_history[i]
						new_date = pd.to_datetime(new_date)
						new_date = datetime.strftime(new_date, '%Y-%m-%d')
						
						all_results.controls.append(
						ft.Row(spacing=28, run_spacing=5, controls=[
											Text(f"{i+1}. "),
											ft.IconButton(on_click=view_url_history, data = i, icon="remove_red_eye_rounded", icon_size=20),
											ft.TextField(value=title_history[i], read_only = True, text_align="start", keyboard_type = "text", width=250, height = 50, text_size=12, content_padding = 10),
											ft.Text(color="white", value=price_history[i], width=80, text_align="center"),
											ft.Text(color="white", value=platform_history[i]),
											ft.Text(color="white", value=new_date)
											], alignment="center", vertical_alignment = "center")
										
									) 
				# If the file has no data, then a message that there are no products is displayed.			
				else:
					currency = ''
					all_results.controls.append(
						ft.Row(spacing=40, run_spacing=10, controls=[
											Text("You have not yet added articles for publication", color="white")
											], alignment="center", vertical_alignment = "center")
										
									) 
				# The view is cleaned before adding another one.		
				page.clean()
				page.add(
					ft.Container(height = 50, content= title_list_history, alignment=ft.alignment.center),
					ft.Divider(height=1, color="black"),
					ft.Row(spacing=10, controls=[
							Text('N°', width=20, text_align="center", color="white"),
							Text('View', width=80, text_align="center", color="white"), 
							Text('Product Title', width=270, text_align="center", color="white"),
							Text(f'Price', width=95, text_align="center", color="white"),
							Text(f'Platform', width=65, text_align="center",color="white"),
							Text(f'Date', width=100, text_align="center", color="white")
							],
							alignment="center", vertical_alignment = "center"),
					ft.Divider(height=1, color="black"),
					ft.Container(width= 710, height= 408, content=all_results),
					ft.Container(width= 710, height= 40, content=ft.Row(controls=[
							ft.ElevatedButton("Delete All", icon="delete_rounded", on_click=delete_all_history)
							],
							alignment="end", vertical_alignment = "start")
					),		
					ft.Container(content= ft.Row(controls=list_all_button_menu,
										alignment="center", vertical_alignment = "end"), 
								height = 50
							)
					)

			# Function to stop the publication of products
			def stop_publish_on(e):

				# To read the data contained in the file that stores the products to be published.
				verify_publish_on  = pd.read_excel('data/publish_on.xlsx', header = 0) 

				# To remove the data from the file of the products to be published.
				update_publish_on = pd.DataFrame(columns = ['title', 'price', 'url', 'min', 'telegram'])

				# This loop will check if the file still has data. If it has data, it will proceed to delete it.
				while len(verify_publish_on) !=0:
					try:
						with ExcelWriter('data/publish_on.xlsx') as writer:
							update_publish_on.to_excel(writer, 'Sheet', index=False)

						processes_publish_product[0].kill()
						processes_publish_product.pop(0)
						
					except Exception as e:
						print('Error: ' + str(e))
						sleep(1)
						with ExcelWriter('data/publish_on.xlsx') as writer:
							update_publish_on.to_excel(writer, 'Sheet', index=False)

						processes_publish_product[0].kill()
						processes_publish_product.pop(0)
						

					# The file is rechecked to see if it still has data.
					verify_publish_on  = pd.read_excel('data/publish_on.xlsx', header = 0)
					sleep(1)

					# The function that displays the products to be published is called
					page_publish(1)

			# This function will show when products are being published.
			def page_publish_on(e):

				# To read the data contained in the file that stores the products to be published.
				verify_publish_on  = pd.read_excel('data/publish_on.xlsx', header = 0)

				if len(verify_publish_on) == 0:
					pass
				else:
					processes_publish_product[0].start()
					page.clean()

					# Text that will display the message "Publishing products..."
					publish_text = Text(
					value=f"Publishing products...",
					size=15,
					color="white",
					italic=False,
					)

					# Text with the number of products still to be released
					yet_publish_text = Text(
					value=f"{len(verify_publish_on)} to publish",
					size=15,
					color="white",
					italic=False,
					)
					page.add(
						ft.Container(content= ft.Column(controls=[
											ft.Row(alignment="center", controls=[publish_text]),
											yet_publish_text,
											press_button_publish_on_stop
											], horizontal_alignment = "center", alignment="center"),
									height= 520


						),
						ft.Container(content= ft.Row(controls=list_all_button_menu,
											alignment="center", vertical_alignment = "end"), 
									height = 100
									)
						)

					
					# As long as there are products to be published, the screen will be updated.
					while len(verify_publish_on) !=0 and processes_publish_product[0].is_alive():
						verify_publish_on  = pd.read_excel('data/publish_on.xlsx', header = 0)
						publish_text = Text(
						value=f"Publishing products...",
						size=15,
						color="white",
						italic=False,
						)
						yet_publish_text = Text(
						value=f"{len(verify_publish_on)} to publish",
						size=15,
						color="white",
						italic=False,
						)
						page.clean()
						page.add(
						ft.Container(content= ft.Column(controls=[
											ft.Row(alignment="center", controls=[publish_text]),
											yet_publish_text,
											press_button_publish_on_stop
											], horizontal_alignment = "center", alignment="center"),
									height= 520


						),
						ft.Container(content= ft.Row(controls=list_all_button_menu,
											alignment="center", vertical_alignment = "end"), 
									height = 100
									)
						)
						sleep(5)
						verify_publish_on  = pd.read_excel('data/publish_on.xlsx', header = 0)

					# When there are no more products to be published, it will call the function that displays the products to be published.
					else:
						if processes_publish_product[0].is_alive():
							processes_publish_product[0].kill()
							processes_publish_product.pop(0)
						page_publish(1)

			# Function that adds the products to the file that will store the products that will be published.
			def publish_on_telegram(e):
				# To check the list of products to be published
				verify_list_publish = pd.read_excel('data/list_publish.xlsx', header = 0)
				title_publish 		= verify_list_publish['title'].values
				price_publish       = verify_list_publish['price'].values
				url_publish 		= verify_list_publish['url'].values
				
				# To obtain how often the products will be published.
				minutes         	= minutes_publish.value

				# They will be used to save the data stored in list_publish.xlsx and add them to publish_on.xlsx 
				# (this file stores the products that will be published).
				title_publish_on    = []
				price_publish_on    = []
				url_publish_on	    = []
				minutes_publish_on  = []
				telegram_publish_on = []

				for i in range(len(verify_list_publish)):
					title_publish_on.append(title_publish[i])
					price_publish_on.append(price_publish[i])
					url_publish_on.append(url_publish[i])
					minutes_publish_on.append(minutes)
					telegram_publish_on.append('yes')


				add_history = {'title': title_publish_on, 'price': price_publish_on, 'url': url_publish_on, 'min': minutes_publish_on,'telegram':telegram_publish_on}

				update_publish_on = pd.DataFrame(add_history, columns = ['title', 'price', 'url', 'min', 'telegram'])
				
				with ExcelWriter('data/publish_on.xlsx') as writer:
					update_publish_on.to_excel(writer, 'Sheet', index=False)

				page_publish_on(1)

			# Function to change the message that will be displayed in Telegram posts.
			def change_custom_message(e):
				verify_custom_message           = pd.read_excel('data/custom_message.xlsx', header = 0)
				before_title_message 	        = verify_custom_message['before_title'].values
				original_price_message	        = verify_custom_message['original_price'].values
				sale_price_message 	        	= verify_custom_message['sale_price'].values
				currency_message	            = verify_custom_message['currency'].values
				url_message				        = verify_custom_message['url'].values

				label_message = e.control.label
				add_custom_message = {}

				if 'Before' in label_message:
					before_title_message        = [form_before_title_message.value]

				elif 'Sale' in label_message:
					sale_price_message          = [form_sale_price_message.value]

				elif 'Original' in label_message:
					original_price_message      = [form_original_price_message.value]

				elif 'Currency' in label_message:
					currency_message  			= [form_currency_message.value]

				elif 'URL' in label_message:
					url_message                 = [form_url_message.value]

				else:
					pass

				add_custom_message['before_title']   = before_title_message
				add_custom_message['original_price'] = original_price_message
				add_custom_message['sale_price']	 = sale_price_message
				add_custom_message['currency']		 = currency_message
				add_custom_message['url']   		 = url_message

				update_custom_message = pd.DataFrame(add_custom_message, columns = ['before_title', 'original_price', 'sale_price', 'currency', 'url'])
				with ExcelWriter('data/custom_message.xlsx') as writer:
					update_custom_message.to_excel(writer, 'Sheet', index=False)

			# Function that will show the screen where the message of the products published in Telegram can be modified.
			def custom_message(e):
				verify_custom_message           = pd.read_excel('data/custom_message.xlsx', header = 0)
				before_title_message 	        = verify_custom_message['before_title'].values
				original_price_message	        = verify_custom_message['original_price'].values
				sale_price_message 	        	= verify_custom_message['sale_price'].values
				currency_message	            = verify_custom_message['currency'].values
				url_message				        = verify_custom_message['url'].values

				if len(verify_custom_message) != 0:
					form_before_title_message.value    = before_title_message[0]
					form_sale_price_message.value      = sale_price_message[0]
					form_original_price_message.value  = original_price_message[0]
					form_currency_message.value        = currency_message[0]
					form_url_message.value			   = url_message[0]

				title_custom_message = Text(
				value="Modify the publication message",
				size=20,
				color="white",
				weight="bold",
				italic=True,
				)    

				page.clean()
				page.add(
					ft.Container(height = 50, content= title_custom_message, alignment=ft.alignment.center),
					ft.Divider(height=1, color="black"),
					ft.Container(height= 449, content=ft.Column(controls=[
							form_before_title_message,
							form_sale_price_message,
							form_original_price_message,
							form_currency_message,
							form_url_message
							],
							alignment="center")),
										
					ft.Container(content= ft.Row(controls=list_all_button_menu,
										alignment="center", vertical_alignment = "end"), 
								height = 100
							)
					)

			# Function to delete product in the list of products to be published.
			def delete_product_button(e):
				id_number = e.control.data

				verify_list_publish  = pd.read_excel('data/list_publish.xlsx', header = 0)

				title_publish 	      = verify_list_publish['title'].values
				price_publish 	      = verify_list_publish['price'].values
				currency_publish   	  = verify_list_publish['currency'].values
				url_publish   	      = verify_list_publish['url'].values

				new_title_publish     = []
				new_price_publish     = []
				new_currency_publish  = []
				new_url_publish       = []

				for i in range(len(verify_list_publish)):
					if i == id_number:
						pass
					else:
						new_title_publish.append(title_publish[i])
						new_price_publish.append(price_publish[i])
						new_currency_publish.append(currency_publish[i])
						new_url_publish.append(url_publish[i])

				list_publish_data = {}

				list_publish_data['title']    = new_title_publish
				list_publish_data['price']    = new_price_publish
				list_publish_data['currency'] = new_currency_publish
				list_publish_data['url']      = new_url_publish

				list_publish_data = pd.DataFrame(list_publish_data, columns = ['title', 'price', 'currency', 'url'])

				with ExcelWriter('data/list_publish.xlsx') as writer:
					list_publish_data.to_excel(writer, 'Sheet', index=False)
				page_publish(0)

			# Function to change Amazon ID
			def change_amazon_id(e):
				new_amazon_id = e.control.value
				
				verify_setting  = pd.read_excel('data/setting.xlsx', header = 0)
				amazon_id 	   = verify_setting['amazon_id'].values
				telegram_token = verify_setting['telegram_token'].values
				chat_id 	   = verify_setting['chat_id'].values

				if len(verify_setting) > 0:
					amazon_id = new_amazon_id

					if pd.isnull(telegram_token[0]):
						telegram_token = ''
					else:
						telegram_token = telegram_token[0]

					if pd.isnull(chat_id[0]):
						chat_id = ''
					else:
						chat_id = chat_id[0]

				else:
					amazon_id      = new_amazon_id
					telegram_token = ''
					chat_id 	   = ''

				setting_data = {}
				setting_data['amazon_id'] = [amazon_id]
				setting_data['telegram_token'] = [telegram_token]
				setting_data['chat_id'] = [chat_id]

				setting_data = pd.DataFrame(setting_data, columns = ['amazon_id', 'telegram_token', 'chat_id'])
				with ExcelWriter('data/setting.xlsx') as writer:
					setting_data.to_excel(writer, 'Sheet', index=False)

			# Function to change telegram token
			def change_telegram_token(e):
				new_telegram_token = e.control.value
				
				verify_setting  = pd.read_excel('data/setting.xlsx', header = 0)
				amazon_id 	   = verify_setting['amazon_id'].values
				telegram_token = verify_setting['telegram_token'].values
				chat_id 	   = verify_setting['chat_id'].values

				if len(verify_setting) > 0:
					telegram_token = new_telegram_token

					if pd.isnull(amazon_id[0]):
						amazon_id = ''
					else:
						amazon_id = amazon_id[0]

					if pd.isnull(chat_id[0]):
						chat_id = ''
					else:
						chat_id = chat_id[0]

				else:
					amazon_id      = ''
					telegram_token = new_telegram_token
					chat_id 	   = ''

				setting_data = {}
				setting_data['amazon_id'] = [amazon_id]
				setting_data['telegram_token'] = [telegram_token]
				setting_data['chat_id'] = [chat_id]

				setting_data = pd.DataFrame(setting_data, columns = ['amazon_id', 'telegram_token', 'chat_id'])
				with ExcelWriter('data/setting.xlsx') as writer:
					setting_data.to_excel(writer, 'Sheet', index=False)

			# Function to change chat ID
			def change_chat_id(e):
				new_chat_id = e.control.value

				verify_setting  = pd.read_excel('data/setting.xlsx', header = 0)
				amazon_id 	   = verify_setting['amazon_id'].values
				telegram_token = verify_setting['telegram_token'].values
				chat_id 	   = verify_setting['chat_id'].values

				if len(verify_setting) > 0:
					chat_id = new_chat_id

					if pd.isnull(amazon_id[0]):
						amazon_id = ''
					else:
						amazon_id = amazon_id[0]

					if pd.isnull(telegram_token[0]):
						telegram_token = ''
					else:
						telegram_token = telegram_token[0]

				else:
					amazon_id      = ''
					telegram_token = ''
					chat_id 	   = new_chat_id

				setting_data = {}
				setting_data['amazon_id'] = [amazon_id]
				setting_data['telegram_token'] = [telegram_token]
				setting_data['chat_id'] = [chat_id]

				setting_data = pd.DataFrame(setting_data, columns = ['amazon_id', 'telegram_token', 'chat_id'])
				with ExcelWriter('data/setting.xlsx') as writer:
					setting_data.to_excel(writer, 'Sheet', index=False)

			# Function to change the title of the products that appear in the list of products to be published.
			def change_title_publish(e):
				new_title = e.control.value # Stores the text of the form that is being modified.
				id_number = e.control.label # Stores the label number of the text field being modified so that it can be identified.

				verify_list_publish  = pd.read_excel('data/list_publish.xlsx', header = 0)

				title_publish 	      = verify_list_publish['title'].values
				price_publish 	      = verify_list_publish['price'].values
				currency_publish   	  = verify_list_publish['currency'].values
				url_publish   	      = verify_list_publish['url'].values

				title_publish[id_number] = new_title

				list_publish_data = {}

				list_publish_data['title']    = title_publish
				list_publish_data['price']    = price_publish
				list_publish_data['currency'] = currency_publish
				list_publish_data['url'] = url_publish

				list_publish_data = pd.DataFrame(list_publish_data, columns = ['title', 'price', 'currency', 'url'])

				try:
					with ExcelWriter('data/list_publish.xlsx') as writer:
						list_publish_data.to_excel(writer, 'Sheet', index=False)
				except:
					sleep(1)
					with ExcelWriter('data/list_publish.xlsx') as writer:
						list_publish_data.to_excel(writer, 'Sheet', index=False)
				

			# Function to change the price of the products that appear in the list of products to be published.
			def change_price_publish(e):
				new_price = e.control.value # Stores the text of the form that is being modified.
				id_number = e.control.label # Stores the label number of the text field being modified so that it can be identified.

				verify_list_publish  = pd.read_excel('data/list_publish.xlsx', header = 0)

				title_publish 	      = verify_list_publish['title'].values
				price_publish 	      = verify_list_publish['price'].values
				currency_publish   	  = verify_list_publish['currency'].values
				url_publish   	      = verify_list_publish['url'].values

				price_publish[id_number] = new_price

				list_publish_data = {}

				list_publish_data['title']    = title_publish
				list_publish_data['price']    = price_publish
				list_publish_data['currency'] = currency_publish
				list_publish_data['url'] = url_publish

				list_publish_data = pd.DataFrame(list_publish_data, columns = ['title', 'price', 'currency', 'url'])

				try:
					with ExcelWriter('data/list_publish.xlsx') as writer:
						list_publish_data.to_excel(writer, 'Sheet', index=False)
				except:
					sleep(1)
					with ExcelWriter('data/list_publish.xlsx') as writer:
						list_publish_data.to_excel(writer, 'Sheet', index=False)

			# Function to change the title of the products that appear in the list of found products.
			def change_title_result(e):
				new_title = e.control.value # Stores the text of the form that is being modified.
				id_number = e.control.label # Stores the label number of the text field being modified so that it can be identified.

				verify_search_result  = pd.read_excel('data/search_result.xlsx', header = 0)

				title_result 	      = verify_search_result['title'].values
				price_result 	      = verify_search_result['price'].values
				currency_result   	  = verify_search_result['currency'].values
				check_result       	  = verify_search_result['check'].values
				url_result       	  = verify_search_result['url'].values

				title_result[id_number] = new_title

				search_result_data = {}

				search_result_data['title']    = title_result
				search_result_data['price']    = price_result
				search_result_data['currency'] = currency_result
				search_result_data['check']    = check_result
				search_result_data['url']      = url_result

				search_result_data = pd.DataFrame(search_result_data, columns = ['title', 'price', 'currency', 'check', 'url'])

				try:
					with ExcelWriter('data/search_result.xlsx') as writer:
						search_result_data.to_excel(writer, 'Sheet', index=False)
				except:
					sleep(1)
					with ExcelWriter('data/search_result.xlsx') as writer:
						search_result_data.to_excel(writer, 'Sheet', index=False)

			# Function to change the price of the products that appear in the list of found products.
			def change_price_result(e):
				new_price = e.control.value # Stores the text of the form that is being modified.
				id_number = e.control.label # Stores the label number of the text field being modified so that it can be identified.
				
				verify_search_result  = pd.read_excel('data/search_result.xlsx', header = 0)
				title_result 	      = verify_search_result['title'].values
				price_result 	      = verify_search_result['price'].values
				currency_result   	  = verify_search_result['currency'].values
				check_result       	  = verify_search_result['check'].values
				url_result       	  = verify_search_result['url'].values

				price_result[id_number] = new_price

				search_result_data = {}

				search_result_data['title']    = title_result
				search_result_data['price']    = price_result
				search_result_data['currency'] = currency_result
				search_result_data['check']    = check_result
				search_result_data['url']      = url_result

				search_result_data = pd.DataFrame(search_result_data, columns = ['title', 'price', 'currency', 'check', 'url'])

				try:
					with ExcelWriter('data/search_result.xlsx') as writer:
						search_result_data.to_excel(writer, 'Sheet', index=False)
				except:
					sleep(1)
					with ExcelWriter('data/search_result.xlsx') as writer:
						search_result_data.to_excel(writer, 'Sheet', index=False)

			# Function that enables and disables application development support
			def support_development(e):
				verify_status_support = pd.read_excel('data/support_dev.xlsx', header = 0)
				status 				  = e.control.value
				support_data = {}

				if status:
					switch_supp_dev.label   = 'Supporting Development On 😊'
					support_data['sup_tag'] = ['amla02-20']
					support_data['sup_dev'] = ['yes']

				else:
					switch_supp_dev.label   = 'Supporting Development Off 😢'
					support_data['sup_tag'] = ['amla02-20']
					support_data['sup_dev'] = ['no']

				update_status_support = pd.DataFrame(support_data, columns = ['sup_tag', 'sup_dev'])

				with ExcelWriter('data/support_dev.xlsx') as writer:
					update_status_support.to_excel(writer, 'Sheet', index=False)

				page.update()

			# Function that will add the products to the list of products to be published.
			def add_to_publish(self):
				
				# The data stored in the searched products is checked.
				verify_search_result  = pd.read_excel('data/search_result.xlsx', header = 0)
				# To be stored in the following variables:
				title_result 	      = verify_search_result['title'].values
				price_result 	      = verify_search_result['price'].values
				currency_result   	  = verify_search_result['currency'].values
				check_result       	  = verify_search_result['check'].values
				url_result       	  = verify_search_result['url'].values

				# The data stored in the list of products to be published are checked.
				verify_list_publish   = pd.read_excel('data/list_publish.xlsx', header = 0)
				# It will be stored in the following variables:
				title_publish 	      = verify_list_publish['title'].values
				price_publish 	      = verify_list_publish['price'].values
				currency_publish   	  = verify_list_publish['currency'].values
				url_publish   	      = verify_list_publish['url'].values

				count = 0 # Counter to be used to identify each item stored in the lists obtained from the Excel files.

				# The new variables will store the existing data in the list of products to be published and products found, 
				# and will also store the new data to be added.
				new_title_result 	   = []
				new_price_result 	   = []
				new_currency_result    = []
				new_check_result	   = []
				new_url_result	       = []

				new_title_publish      = []
				new_price_publish      = []
				new_currency_publish   = []
				new_url_publish        = []

				# It is verified that the file with the data of the products to be published has information.
				if len(verify_list_publish) > 0:
					# By means of a loop, the current information of the products to be published is stored in the new variables.
					for i in range(len(verify_list_publish)):
						new_title_publish.append(title_publish[i])
						new_price_publish.append(price_publish[i])
						new_currency_publish.append(currency_publish[i])
						new_url_publish.append(url_publish[i])

				# It is verified that the file with the data of the products to be published has information.
				if len(verify_search_result) > 0:
					# Through this loop we can check the products that have been selected to be published.
					# This information is stored in search_result.xlsx
					for check_status in check_result:
						# Products stored in the search_result.xlsx document that contain 
						# the value "no" in the check field will be stored in the new found products variables.
						if check_status == 'no':
							new_title_result.append(title_result[count])
							new_price_result.append(price_result[count])
							new_currency_result.append(currency_result[count])
							new_check_result.append(check_result[count])
							new_url_result.append(url_result[count])
						# On the other hand, if they have the value "yes", they will be stored in the variables 
						# that will be used to store the information in the list_publish.xlsx document.
						else:
							new_title_publish.append(title_result[count])
							new_price_publish.append(price_result[count])
							new_currency_publish.append(currency_result[count])
							new_url_publish.append(url_result[count])

						count+=1

					list_publish_data = {}
					list_publish_data['title']    = new_title_publish
					list_publish_data['price']    = new_price_publish
					list_publish_data['currency'] = new_currency_publish
					list_publish_data['url']      = new_url_publish

					list_publish_data = pd.DataFrame(list_publish_data, columns = ['title', 'price', 'currency', 'url'])

					with ExcelWriter('data/list_publish.xlsx') as writer:
						list_publish_data.to_excel(writer, 'Sheet', index=False)

					search_result_data = {}

					search_result_data['title']    = new_title_result
					search_result_data['price']    = new_price_result
					search_result_data['currency'] = new_currency_result
					search_result_data['check']    = new_check_result
					search_result_data['url']      = new_url_result

					search_result_data = pd.DataFrame(search_result_data, columns = ['title', 'price', 'currency', 'check', 'url'])

					with ExcelWriter('data/search_result.xlsx') as writer:
						search_result_data.to_excel(writer, 'Sheet', index=False)

					page_search_result(0)
				else:
					pass

			# Function to delete the products added in the search result.
			def select_all_search_result(e):
				# The data stored in the searched products is checked.
				verify_search_result  = pd.read_excel('data/search_result.xlsx', header = 0)

				# To be stored in the following variables:
				title_result 	      = verify_search_result['title'].values
				price_result 	      = verify_search_result['price'].values
				currency_result   	  = verify_search_result['currency'].values
				check_result       	  = verify_search_result['check'].values
				url_result       	  = verify_search_result['url'].values

				status_select = e.control.text

				# For all products to be selected, "yes" must be placed in the "check" column.
				new_check_values = []
				for i in range(len(verify_search_result)):
					if 'Unselect' in status_select:
						new_check_values.append('no')
					else:
						new_check_values.append('yes')

				update_data = {}
				update_data['title'] 	= title_result
				update_data['price'] 	= price_result
				update_data['currency'] = currency_result
				update_data['check'] 	= new_check_values
				update_data['url']		= url_result

				search_result_data = pd.DataFrame(update_data, columns = ['title', 'price', 'currency', 'check', 'url'])

				with ExcelWriter('data/search_result.xlsx') as writer:
					search_result_data.to_excel(writer, 'Sheet', index=False)
				sleep(1)
				page_search_result(1)


			# Function to delete the products added in the history.
			def delete_all_history(self):
				history_data = pd.DataFrame(columns = ['date', 'title', 'price', 'url', 'platform'])

				with ExcelWriter('data/history.xlsx') as writer:
					history_data.to_excel(writer, 'Sheet', index=False)
				sleep(1)
				page_history(1)

			# Function to delete the products added in the search result.
			def delete_all_search_result(self):
				search_result_data = pd.DataFrame(columns = ['title', 'price', 'currency', 'check', 'url'])

				with ExcelWriter('data/search_result.xlsx') as writer:
					search_result_data.to_excel(writer, 'Sheet', index=False)
				sleep(1)
				page_search_result(1)

			# Function to delete the products added to the list of products to be published.
			def delete_all_products_publish(self):
				list_publish_data = pd.DataFrame(columns = ['title', 'price', 'currency', 'url'])

				with ExcelWriter('data/list_publish.xlsx') as writer:
					list_publish_data.to_excel(writer, 'Sheet', index=False)
				sleep(1)
				page_publish(1)
			
			# Function to select the products shown in the search result that will be added to the list of products to be published.
			def check_button(e):
				e.control.selected = not e.control.selected
				e.control.update()

				verify_search_result  = pd.read_excel('data/search_result.xlsx', header = 0)
				title_result 	      = verify_search_result['title'].values
				price_result 	      = verify_search_result['price'].values
				currency_result   	  = verify_search_result['currency'].values
				check_result       	  = verify_search_result['check'].values
				url_result       	  = verify_search_result['url'].values
			   
				if e.control.selected == False:
					pass
				else:
					check_result[e.control.data] = 'yes'
				
				if e.control.selected == True:
					pass
				else:
					check_result[e.control.data] = 'no'

				search_result_data = {}
				search_result_data['title']    = title_result
				search_result_data['price']    = price_result
				search_result_data['currency'] = currency_result
				search_result_data['check']    = check_result
				search_result_data['url']      = url_result


				search_result_data = pd.DataFrame(search_result_data, columns = ['title', 'price', 'currency', 'check', 'url'])
				try:
					with ExcelWriter('data/search_result.xlsx') as writer:
						search_result_data.to_excel(writer, 'Sheet', index=False)
				except:
					sleep(1)
					with ExcelWriter('data/search_result.xlsx') as writer:
						search_result_data.to_excel(writer, 'Sheet', index=False)


			# Function to open the URL of the products added in the list of products to be published.
			def view_url_list_publish(e):
				try:
					verify_list_publish  = pd.read_excel('data/list_publish.xlsx', header = 0)
					title_publish 	     = verify_list_publish['title'].values
					url_publish       	 = verify_list_publish['url'].values
				except:
					sleep(1)
					verify_list_publish  = pd.read_excel('data/list_publish.xlsx', header = 0)
					title_publish 	     = verify_list_publish['title'].values
					url_publish       	 = verify_list_publish['url'].values

				webbrowser.open(url_publish[e.control.data])

			# Function to open the URL of the products added in the history of published products.
			def view_url_history(e):
				try:
					verify_history  = pd.read_excel('data/history.xlsx', header = 0)
					url_history     = verify_history['url'].values

				except:
					sleep(1)
					verify_history  = pd.read_excel('data/history.xlsx', header = 0)
					url_history     = verify_history['url'].values

				webbrowser.open(url_history[e.control.data])
			
			# Function to open the URL of the products added in the search result.			   
			def view_url_search_result(e):
				try:
					verify_search_result  = pd.read_excel('data/search_result.xlsx', header = 0)
					title_result 	      = verify_search_result['title'].values
					url_result       	  = verify_search_result['url'].values
				except:
					sleep(1)
					verify_search_result  = pd.read_excel('data/search_result.xlsx', header = 0)
					title_result 	      = verify_search_result['title'].values
					url_result       	  = verify_search_result['url'].values

				webbrowser.open(url_result[e.control.data])

			# Function that displays the search result page.
			def page_search_result(self):
				
				verify_search_result  = pd.read_excel('data/search_result.xlsx', header = 0)

				title_result 	      = verify_search_result['title'].values
				price_result 	      = verify_search_result['price'].values
				currency_result   	  = verify_search_result['currency'].values
				check_result       	  = verify_search_result['check'].values
				url_result       	  = verify_search_result['url'].values

				all_results = ft.Column(scroll="always", expand=True)

				show_price_0 = switch_show_price_0.value

				if 'no' in check_result:
					select_products = ft.ElevatedButton(text = "Select All", icon="check_box_outlined", on_click=select_all_search_result)
				else:
					select_products = ft.ElevatedButton(text = "Unselect All", icon="check_box_outline_blank_rounded", on_click=select_all_search_result)

				check = []

				if show_price_0:
					switch_show_price_0.label = 'Showing all products found'
					if len(verify_search_result) > 0:
						currency = f"({currency_result[0]})"
						for c in check_result:
							if c == 'yes':
								check.append(True)
							else:
								check.append(False)

						for i in range(len(check_result)):

							all_results.controls.append(
							ft.Row(spacing=28, run_spacing=5, controls=[
												Text(f"{i+1}. "),
												ft.IconButton(on_click=view_url_search_result, data = i, icon="remove_red_eye_rounded", icon_size=20),
												ft.TextField(value=title_result[i], label = i, on_blur=change_title_result, text_align="start", keyboard_type = "text", width=250, height = 50, text_size=12, content_padding = 10),
												ft.TextField(value=price_result[i], label = i, on_blur=change_price_result, text_align="start", keyboard_type = "number", width=70, height = 50, text_size=12, content_padding = 10),
												ft.IconButton(on_click=check_button, data = i,  icon="check_box_outline_blank_rounded", selected=check[i], selected_icon="check_box_rounded", icon_size=20),
												], alignment="center", vertical_alignment = "center")
											)
							
						
					else:
						currency = ''
						all_results.controls.append(
							ft.Row(spacing=40, run_spacing=10, controls=[
												Text("You have not yet searched for products")
												], alignment="center", vertical_alignment = "center")
										) 
				
				else:
					switch_show_price_0.label = 'Hiding unpriced products'
					if len(verify_search_result) > 0:
						currency = f"({currency_result[0]})"
						for i in range(len(verify_search_result)):
							if check_result[i] == 'yes':
								check.append(True)
							else:
								check.append(False)

							if price_result[i] == 0:
								pass
							else:
								all_results.controls.append(
								ft.Row(spacing=28, run_spacing=5, controls=[
													Text(f"{i+1}. "),
													ft.IconButton(on_click=view_url_search_result, data = i, icon="remove_red_eye_rounded", icon_size=20),
													ft.TextField(value=title_result[i], label = i, on_blur=change_title_result, text_align="start", keyboard_type = "text", width=250, height = 50, text_size=12, content_padding = 10),
													ft.TextField(value=price_result[i], label = i, on_blur=change_price_result, text_align="start", keyboard_type = "number", width=70, height = 50, text_size=12, content_padding = 10),
													ft.IconButton(on_click=check_button, data = i,  icon="check_box_outline_blank_rounded", selected=check[i], selected_icon="check_box_rounded", icon_size=20),
													], alignment="center", vertical_alignment = "center")
												)
					else:
						currency = ''
						all_results.controls.append(
							ft.Row(spacing=40, run_spacing=10, controls=[
												Text("You have not yet searched for products")
												], alignment="center", vertical_alignment = "center")
										) 


				page.clean()
				title_search_result = Text(
				value="Search Result",
				size=20,
				color="white",
				weight="bold",
				italic=True,
				)           

				page.add(
					ft.Container(height = 50, content= title_search_result, alignment=ft.alignment.center),
					ft.Divider(height=1, color="black"),
					ft.Row(spacing=1, controls=[
							Text('N°', width=55, text_align="center"),
							Text('View', width=60, text_align="center"), 
							Text('Product Title', width=290, text_align="center"),
							Text(f'Price {currency}', width=80, text_align="center"),
							Text('Check',width=80, text_align="center"), 
							],
							alignment="center", vertical_alignment = "center"),
					ft.Divider(height=1, color="black"),
					ft.Container(height= 358, content=all_results),
					ft.Row(controls=[
							ft.ElevatedButton("Add to Publish", icon="add_circle_outline_rounded", on_click=add_to_publish),
							ft.ElevatedButton("Delete All", icon="delete_rounded", on_click=delete_all_search_result),
							select_products
							],
							alignment="center", vertical_alignment = "start"),
					ft.Row(controls=[switch_show_price_0], alignment="center", vertical_alignment = "start"),					
					ft.Container(content= ft.Row(controls=list_all_button_menu,
										alignment="center", vertical_alignment = "end"), 
								height = 50
							)
					)

			def stop_search_product(e):
				processes_search_product[0].kill()
				
				processes_search_product.pop(0)
				# To read the data contained in the file that stores the products to be searched.
				verify_search_product  = pd.read_excel('data/search_product.xlsx', header = 0) 

				# The data in the file that stores the search requests is deleted so that it does not continue searching.
				delete_product_data = pd.DataFrame(columns = ['title', 'region', 'pub'])

				# This loop will check if the file still has data. If it has data, it will proceed to delete it.
				while len(verify_search_product) !=0:
					try:
						with ExcelWriter('data/search_product.xlsx') as writer:
							delete_product_data.to_excel(writer, 'Sheet', index=False)
					except:
						sleep(1)
						with ExcelWriter('data/search_product.xlsx') as writer:
							delete_product_data.to_excel(writer, 'Sheet', index=False)

					# The file is rechecked to see if it still has data.
					verify_search_product  = pd.read_excel('data/search_product.xlsx', header = 0)
					sleep(1)

					# The function that displays the main is called
					page_main(1)


			# Function to change the data of the products to be searched.
			def change_search_product(e):
				search_text        = search_form.value # Stores the data entered in the product search field.
				region 			   = select_region.value # Stores the selected Amazon region.
				quick_search       = switch_quick_search.value

				if quick_search:
					quick_search = 'yes'
				else:
					quick_search = 'no'

				search_product_data = {}

				search_product_data['title']   = [search_text]
				search_product_data['region']  = [region]
				search_product_data['pub'] 	   = ['no'] # It is saved as 'no', to identify that the product has not been selected for publication.
				search_product_data['quick']   = [quick_search]

				search_product_data = pd.DataFrame(search_product_data, columns = ['title', 'region', 'pub', 'quick'])

				verify_status_support = pd.read_excel('data/support_dev.xlsx', header = 0)
				sup_tag 			  = verify_status_support['sup_tag'].values
				sup_dev               = verify_status_support['sup_dev'].values

				support_data = {}

				if 'com' in region:
					sup_tag = 'amla02-20'
				else:
					sup_tag = 'amla07-21'

				support_data['sup_tag'] = [sup_tag]
				support_data['sup_dev'] = sup_dev

				update_status_support = pd.DataFrame(support_data, columns = ['sup_tag', 'sup_dev'])
				try:
					with ExcelWriter('data/support_dev.xlsx') as writer:
						update_status_support.to_excel(writer, 'Sheet', index=False)
				except:
					sleep(1)
					with ExcelWriter('data/support_dev.xlsx') as writer:
						update_status_support.to_excel(writer, 'Sheet', index=False)

				try:
					with ExcelWriter('data/search_product.xlsx') as writer:
						search_product_data.to_excel(writer, 'Sheet', index=False)
				except:
					sleep(1)
					with ExcelWriter('data/search_product.xlsx') as writer:
						search_product_data.to_excel(writer, 'Sheet', index=False)
			

			def search_products(e):
				change_search_product(e)
				sleep(1)
				try:
					verify_search_product  = pd.read_excel('data/search_product.xlsx', header = 0)
				except:
					sleep(2)
					verify_search_product  = pd.read_excel('data/search_product.xlsx', header = 0)
				count_progress = 0

				if len(verify_search_product) == 0:
					pass
				else:
					processes_search_product[0].start()

					page.clean()
					searching_text = Text(
					value="Searching...",
					size=15,
					color="white",
					italic=False,
					)
					progress_bar = ft.ProgressBar(width=400)
					page.add(
						ft.Container(content= ft.Column(controls=[
											title_amacapy,
											ft.Row(alignment="center", controls=[searching_text]),
											progress_bar,
											press_button_search_stop
											], horizontal_alignment = "center", alignment="center"),
									height= 520


						),
						ft.Container(content= ft.Row(controls=list_all_button_menu,
											alignment="center", vertical_alignment = "end"), 
									height = 100
									)
						)

					

					while len(verify_search_product) !=0: # and processes_search_product[0].is_alive():
						try:
							verify_search_product  = pd.read_excel('data/search_product.xlsx', header = 0)
						except:
							sleep(2)
							verify_search_product  = pd.read_excel('data/search_product.xlsx', header = 0)
						sleep(0.5)
						progress_bar.value = count_progress * 0.01
						count_progress+=1
						page.clean()
						page.add(
						ft.Container(content= ft.Column(controls=[
											title_amacapy,
											ft.Row(alignment="center", controls=[searching_text]),
											progress_bar,
											press_button_search_stop
											], horizontal_alignment = "center", alignment="center"),
									height= 520


						),
						ft.Container(content= ft.Row(controls=list_all_button_menu,
											alignment="center", vertical_alignment = "end"), 
									height = 100
									)
						)					
							
					else:
						if processes_search_product[0].is_alive():
							processes_search_product[0].kill()
							processes_search_product.pop(0)
						
						search_form.value = ''
						page_search_result(1)

			# Function that displays the main page.
			def page_main(e):
				page.clean()
				button_search = IconButton(on_click=search_products, icon="search_rounded")
				page.add(
					ft.Container(content= ft.Column(controls=[
										title_amacapy,
										ft.Row(alignment="center", controls=[search_form, 
										button_search]),
										select_region,
										ft.Row(alignment="center", controls=[switch_quick_search])
										], horizontal_alignment = "center", alignment="center"),
								height= 520


					),
					ft.Container(content= ft.Row(controls=list_all_button_menu,
										alignment="center", vertical_alignment = "end"), 
								height = 100
								)
					)

			# Function that displays the setting page.
			def page_settings(self):
				self.page.clean()
				self.title_settings = Text(
				value="Settings",
				size=20,
				color="white",
				weight="bold",
				italic=True,
				)
				verify_status_support = pd.read_excel('data/support_dev.xlsx', header = 0)
				sup_dev				  = verify_status_support['sup_dev'].values

				if sup_dev[0] == 'yes':
					switch_supp_dev.value = True
					switch_supp_dev.label   = 'Supporting Development On 😊'
				elif sup_dev[0] == 'no':
					switch_supp_dev.value = False
					switch_supp_dev.label = 'Supporting Development Off 😢'
				else:
					support_data = {}
					support_data['sup_tag']     = ['dsuaz']
					support_data['sup_dev'] = ['yes']
					update_status_support = pd.DataFrame(support_data, columns = ['sup_tag', 'sup_dev'])
					switch_supp_dev.value = True
					switch_supp_dev.label   = 'Supporting Development On 😊'

					with ExcelWriter('data/support_dev.xlsx') as writer:
						update_status_support.to_excel(writer, 'Sheet', index=False)


				verify_setting  = pd.read_excel('data/setting.xlsx', header = 0)
				amazon_id 	   = verify_setting['amazon_id'].values
				telegram_token = verify_setting['telegram_token'].values
				chat_id 	   = verify_setting['chat_id'].values

				if len(verify_setting) > 0:
					if pd.isnull(amazon_id[0]):
						form_amazon_id.value = ''
					else:
						form_amazon_id.value = amazon_id[0]

					if pd.isnull(telegram_token[0]):
						form_telegram_token.value = ''
					else:
						form_telegram_token.value = telegram_token[0]

					if pd.isnull(chat_id[0]):
						form_chat_id.value = ''
					else:
						form_chat_id.value = chat_id[0]

				else:
					form_amazon_id.value = ''
					form_telegram_token.value = ''
					form_chat_id.value = ''

				self.page.add(
					ft.Container(height = 50, content= self.title_settings, alignment=ft.alignment.center),
					ft.Divider(height=1, color="black"),
					ft.Container(content= ft.Column(alignment="center", controls=[
													ft.Text(value="Add your Amazon ID"),
													form_amazon_id,
													ft.Divider(height=30, color="transparent"),
													ft.Text(value="Add your Telegram data"), 
													form_telegram_token, 
													form_chat_id,
													ft.Divider(height=30, color="transparent"),
													ft.Text(value="Other options"),
													press_button_custom_message, 
													button_select_short_url], 
										horizontal_alignment = "center"),
								height= 449
					),
					ft.Container(content= ft.Row(controls=list_all_button_menu,
										alignment="center", vertical_alignment = "end"), 
								height = 100
								)
					)

			def select_short_url(e):
				short_url_label = e.control.label
				short_url_value = e.control.value

				if 'Tinyurl' in short_url_label:
					if short_url_value == True:
						short_url = 'tinyurl'
					else:
						short_url = 'no'
				elif 'Is.gd' in short_url_label:
					if short_url_value == True:
						short_url = 'isgd'
					else:
						short_url = 'no'
				elif 'Da.gd' in short_url_label:
					if short_url_value == True:
						short_url = 'dagd'
					else:
						short_url = 'no'
				else:
					short_url = 'no'

				short_url_data    = [short_url] 
				update_short_url  = pd.DataFrame(short_url_data, columns = ['short_url'])
				with ExcelWriter('data/short_url.xlsx') as writer:
					update_short_url.to_excel(writer, 'Sheet', index=False)

				page_short_url(1)

			# Function to display the menu with the short url.
			def page_short_url(e):
				verify_short_url     = pd.read_excel('data/short_url.xlsx', header = 0)
				short_url 	     	 = verify_short_url['short_url'].values

				if short_url[0] == 'tinyurl':
					switch_tinyurl_short_url.value = True
					switch_isgd_short_url.value = False
					switch_dagd_short_url.value = False
				elif short_url[0] == 'isgd':
					switch_tinyurl_short_url.value = False
					switch_isgd_short_url.value = True
					switch_dagd_short_url.value = False
				elif short_url[0] == 'dagd':
					switch_tinyurl_short_url.value = False
					switch_isgd_short_url.value = False
					switch_dagd_short_url.value = True
				else:
					switch_tinyurl_short_url.value = False
					switch_isgd_short_url.value = False
					switch_dagd_short_url.value = False

				title_settings = Text(
				value="Settings",
				size=20,
				color="white",
				weight="bold",
				italic=True,
				)

				page.clean()

				page.add(
					ft.Container(height = 50, content= title_settings, alignment=ft.alignment.center),
					ft.Divider(height=1, color="black"),
					ft.Container(content= ft.Column(alignment="center", 
													controls=[ft.Row(controls=[Text(value='Select Short URL', size=16)], alignment="center"),
															ft.Row(controls=[switch_tinyurl_short_url,
																			switch_isgd_short_url,
																			switch_dagd_short_url
																			], alignment="center") 
															], 
															horizontal_alignment = "center"),
															width=400, height= 449
					),
					ft.Container(content= ft.Row(controls=list_all_button_menu,
										alignment="center", vertical_alignment = "end"), 
								height = 100
								)
					)

			def urls_support(e):
				url = e.control.text

				if 'Paypal' in url:
					url = 'https://paypal.me/davidsulbaran'
				elif 'GitHub' in url:
					url = 'https://github.com/sulasoft'
				elif 'sulasoft' in url:
					url = 'https://sulasoft.com'
				elif 'Telegram' in url:
					url = 'https://t.me/+xzxygFLwEmI1NzVh'
				else:
					url = 'https://www.linkedin.com/in/david-sulbarán-azócar-180768244/'

				webbrowser.open(url)

			def page_support(e):
				page.clean()
				title_support = Text(
				value="Support",
				size=20,
				color="white",
				weight="bold",
				italic=True,
				)
				verify_status_support = pd.read_excel('data/support_dev.xlsx', header = 0)
				sup_dev				  = verify_status_support['sup_dev'].values

				if sup_dev[0] == 'yes':
					switch_supp_dev.value = True
					switch_supp_dev.label   = 'Supporting Development On 😊'
				elif sup_dev[0] == 'no':
					switch_supp_dev.value = False
					switch_supp_dev.label = 'Supporting Development Off 😢'
				else:
					support_data = {}
					support_data['sup_tag']     = ['dsuaz']
					support_data['sup_dev'] = ['yes']
					update_status_support = pd.DataFrame(support_data, columns = ['sup_tag', 'sup_dev'])
					switch_supp_dev.value = True
					switch_supp_dev.label   = 'Supporting Development On 😊'

					with ExcelWriter('data/support_dev.xlsx') as writer:
						update_status_support.to_excel(writer, 'Sheet', index=False)

				page.add(
					ft.Container(height = 50, content= title_support, alignment=ft.alignment.center),
					ft.Divider(height=1, color="black"),
					ft.Container(width=650, height = 449, content= ft.Column(alignment="center", controls=[
																	ft.Row(controls=[
																	ft.Text(value= "You can support the development by sharing a link to the developer's affiliate tag.")
																	], alignment="center", vertical_alignment = "center"),
																	ft.Row(controls=[
																	switch_supp_dev, button_info_supp
																	], alignment="center", vertical_alignment = "center"),
																	ft.Divider(height=60, color="transparent"),
																	ft.Row(controls=[
																	ft.Text(value="You can also contribute monetarily \n I would be very grateful ❤️", text_align ='center')
																	], alignment="center", vertical_alignment = "center"),
																	ft.Row(controls=[
																	ft.Text(value = "USDT \n Address", text_align ='center', size = 12, weight='bold'), 
																	usdt_address, 
																	ft.Text(value = "Tron (TRC20) \n Network", size = 10)
																	], alignment="center", vertical_alignment = "center"),
																	ft.Row(controls=[
																	paypal_button
																	], alignment="center", vertical_alignment = "center"),
																	ft.Divider(height=60, color="transparent"),
																	ft.Row(controls=[
																	ft.Text(value="My contact networks", text_align ='center')
																	], alignment="center", vertical_alignment = "center"),
																	ft.Row(controls=[
																	github_button, linkedin_button, sulasoftcom_button, telegram_channel_button
																	], alignment="center", vertical_alignment = "center"),
																	ft.Row(controls=[
																	ft.Text(value="Thank you! 😊", text_align ='center')
																	], alignment="center", vertical_alignment = "center")])
								),
					ft.Container(content= ft.Row(controls=list_all_button_menu,
										alignment="center", vertical_alignment = "end"), 
								height = 100
								)
					)
			
			switch_quick_search		    = ft.Switch(label = 'Quick search', value=True)
			search_form   				= TextField(label="Search...", width=400, height = 50, on_submit=search_products, text_align="start", keyboard_type = "text", text_size=12, content_padding = 10)
			select_region 				= ft.RadioGroup(content=ft.Row(alignment="center", controls=[
											ft.Text("Amazon "),
											ft.Radio(value=".com", label=".com"),
											ft.Radio(value=".es", label=".es"),
											ft.Radio(value=".it", label=".it"),
											ft.Radio(value=".in", label=".in")]), value = ".com")       
			
			minutes_publish              = TextField(value='0', label = 'Minutes', text_align="start", keyboard_type = "text", width=70, height = 50, text_size=12, content_padding = 10)
			press_button_publish_on_stop = ft.ElevatedButton("Stop", icon="stop_circle_rounded", on_click=stop_publish_on)
			press_button_search_stop     = ft.ElevatedButton("Stop", icon="stop_circle_rounded", on_click=stop_search_product)

			# To know if a product has been selected or not
			check_status = False

			# Menu
			press_button_main            = IconButton(on_click=page_main, icon="home_rounded", tooltip= 'Home')
			press_button_list_result     = IconButton(on_click=page_search_result, icon="format_list_numbered_rounded", tooltip= 'Search Result')
			press_button_list_publish    = IconButton(on_click=page_publish, icon="checklist_rounded", tooltip= 'Products to Publish')
			press_button_history         = IconButton(on_click=page_history, icon="history_rounded", tooltip= 'History')
			press_button_setting         = IconButton(on_click=page_settings, icon="settings_rounded", tooltip= 'Settings')
			press_button_info			 = IconButton(on_click=page_support, icon="info_rounded", tooltip= "Support")
			list_all_button_menu		 = [press_button_main, press_button_list_result, press_button_list_publish, press_button_history, press_button_setting, press_button_info]

			# Settings form
			form_amazon_id               = TextField(label="Amazon ID", text_align="center", on_blur=change_amazon_id, width=400, height = 45, text_size=13)
			form_telegram_token          = TextField(label="Telegram Token", text_align="center", on_blur=change_telegram_token, width=400, height = 45, text_size=13)
			form_chat_id                 = TextField(label="Chat ID Example: yourchatid", text_align="center", on_blur=change_chat_id, width=400, height = 45, text_size=13)

			# For modify message displayed in Telegram
			switch_tinyurl_short_url	 = ft.Switch(label= 'Tinyurl', on_change=select_short_url)
			switch_isgd_short_url		 = ft.Switch(label= 'Is.gd',on_change=select_short_url)
			switch_dagd_short_url		 = ft.Switch(label= 'Da.gd',on_change=select_short_url)
			button_select_short_url		 = ft.ElevatedButton("Modify Short URL", icon="edit_rounded", on_click=page_short_url)
			press_button_custom_message  = ft.ElevatedButton("Modify publication message", icon="edit_rounded", on_click=custom_message)
			form_before_title_message    = TextField(label="Before Title Message", text_align="center", on_blur=change_custom_message, width=400, height = 45, text_size=13)
			form_sale_price_message      = TextField(label="Sale Price Message", text_align="center", on_blur=change_custom_message, width=400, height = 45, text_size=13)
			form_original_price_message  = TextField(label="Original Price Message", text_align="center", on_blur=change_custom_message, width=400, height = 45, text_size=13)
			form_currency_message        = TextField(label="Currency ($, €)", text_align="center", on_blur=change_custom_message, width=400, height = 45, text_size=13)
			form_url_message             = TextField(label="URL Message", text_align="center", on_blur=change_custom_message, width=400, height = 45, text_size=13)
			

			# To support or not to support development
			usdt_address			     = ft.TextField(value='TJajbMu8Q1xPG38VzGHQTKT4Wo2T3x4nUR', read_only = True, text_align="start", keyboard_type = "text", width=300, height = 50, text_size=12, content_padding = 10)
			switch_supp_dev 			 = ft.Switch(on_change=support_development)
			paypal_button  				 = ft.ElevatedButton(text= "Paypal", icon = 'paypal',on_click=urls_support)
			github_button  				 = ft.TextButton(text = "GitHub", on_click=urls_support)
			sulasoftcom_button			 = ft.TextButton(text = "sulasoft.com", on_click=urls_support)
			linkedin_button  			 = ft.TextButton(text = "Linkedin", on_click=urls_support)
			telegram_channel_button		 = ft.TextButton(text = "Telegram", icon = 'telegram', on_click=urls_support)
			button_info_supp			 = ft.IconButton(icon="info_rounded", tooltip= "1 out of 6 published products contains the developer's amazon affiliates tag.")
			
			# Switch to view or not the products with price 0
			switch_show_price_0 		 = ft.Switch(on_change=page_search_result, value=True)


			page.add(
				ft.Row(page_main(0))
				) 

		main_interface()
   
	ft.app(target=main)
