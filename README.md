<h1 align="center"> Amacapy </h1>
<p>Amacapy is a program that focuses on web scraping amazon.com, amazon.es and amazon.it. The data extracted are the price, title and URL of the products searched, then with the help of a Telegram bot created with Bot Father, these are published in a certain time.</p>

<h2 align="center"> <a target=”_blank” href='https://sulasoft.com/telegram-bot-for-amazon-affiliates/'>Download the new version here.</a> </h2>



<h2 align="center"> Old version </h2>
<p><b> Libraries and technologies used: </b></p>
<li> Python 3.10.1. </li> 
<li> Beautifulsoup4 v4.11.1 and Requests v2.28.1 (For the web scraping) </li> 
<li> Flet v0.3.2. (For the graphical interface) </li> 
<li> Pandas v1.5.2. (For saving and manipulating information from xlsx files) </li> 
<li> Pyshorteners v1.0.1. (To shorten the links of the publications) </li> 


<h2 align="center"> How to use Amacapy? </h2>
<li> 1. Create a bot with BotFather. </li>
<ul>1.1. Start a new conversation with the BotFather in Telegram. </ul>
<ul>1.2. Send /newbot to create a new Telegram bot. </ul>
<ul>1.3. When asked, enter a name for the bot. </ul>
<ul>1.4. Give the Telegram bot a unique username. </ul>
<ul>1.5. Copy and save the Telegram bot's access token for later steps. </ul>


<li> 2. Install the necessary libraries. You can do it in the following way: </li>
<ul>2.1. Open the terminal in the path of the Amacapy program. </ul>
<ul>2.2. Type: pip install -r requirements.txt. </ul>
<ul>2.3. Wait for the installation to finish. </ul>

<li> 3. Open the "main.py" file containing the main program. </li>

<li> 4. Add your data (amazon id, telegram token, chat id) in the configuration. </li>
<ul>4.1. Amazon ID: Your amazon affiliates tag. </ul>
<ul>4.2. Telegram Token: It is the token obtained when creating the telegram bot with Bot Father. </ul>
<ul>4.3. Chat ID: The name of the Telegram channel or Telegram group. Make sure the chat ID has no symbols or special characters. </ul>
<p>Example: </p>
<img src="https://i.ibb.co/sVyRqkR/settings.jpg" width='450'>

<li> 5. Search products. </li>
<ul> 5.1. You can place the direct URL of a product or enter the keyword of the product you want to search for. </ul>
<ul> 5.2. Select Amazon region. </ul>
<ul> 5.3. Activate or deactivate quick search. (Optional).</ul>
<ul> 5.4. Press Enter in the search bar or click on the search symbol to start retrieving products.</ul>
<p>Example: </p>
<img src="https://i.ibb.co/S0GZq5G/search-products.jpg" width='450'>

<li> 6. Search results. </li>
<ul> 6.1. Modify the title or price of the products only by editing the text field. </ul>
<ul> 6.2. Select in "Check" the products you want to publish.</ul>
<ul> 6.3.Click on the button "Add to publish" to add them to the list of products to be published.</ul>
<p>Example: </p>
<img src="https://i.ibb.co/5YdRsTz/search-results.jpg" width='450'>

<li> 7. Publication list. </li>
<ul> 7.1. Verify name and price of the products to be published. </ul>
<ul> 7.2. Add how often (in minutes) you want the products to be published on Telegram.</ul>
<ul> 7.3. Press the Telegram button to start publishing. While it is posting, you cannot do other things in the program unless you press the "stop" button.</ul>
<p>Example: </p>
<img src="https://i.ibb.co/0Y24HkB/products-to-publish.jpg" width='450'>

<li> 7. History of published products. </li>
<ul> 7.1. You can see the URL, title, price and publication date of the product. </ul>
<p>Example: </p>
<img src="https://i.ibb.co/8BmQ5K8/history.jpg" width='450'>

<li> 8. Modify the text displayed in the Telegram post (Optional). </li>
<ul> 8.1. Go to "Settings" and click on the "Modify publication message" button located in other options. </ul>
<p>Example: </p>
<img src="https://i.ibb.co/2gqVdq3/modify-publication-message.jpg" width='450'>


<li> 9.Add link shortener (Optional). </li>
<ul> 9.1. Go to "Settings" and click on the "Modify Short URL" button located in other options. </ul>
<ul> 9.2. Select between Tinyurl, Is.gd and Da.gd. </ul>
<p>Example: </p>
<img src="https://i.ibb.co/s3jDRT0/short-url.jpg" width='450'>

<li> 10. Supporting the developer. </li>
<ul> 10.1. Activating the option that allows you to publish 1 product with the amazon affiliate tag of the Amacapy developer. It is published every 5 products published. (option enabled by default, you can disable it manually). </ul>
<p>Example: </p>
<img src="https://i.ibb.co/YhNV6Y6/support.jpg" width='450'>


<h2 align="center"> Where are the data stored? (Do not manually delete or modify these files) </h2>
<li> 1. The configuration is stored in the file: setting.xlsx. </li>
<li> 2. The search_product.xlsx file stores the data entered in the search screen (product keyword and Amazon region). </li>
<li> 3. The search result is stored in the file: search_result.xlsx. </li>
<li> 4. Products added to the publication list are stored in: list_publish.xlsx. </li>
<li> 5. The publish_on.xlsx file stores the products that are being published. </li>
<li> 6. The history.xlsx file stores the products that have been published, including their publication date. </li>
<li> 7. The custom Telegram post message is stored in the file custom_message.xlsx. </li>
<li> 8. The link shortener data is stored in the file: short_url.xlsx. </li>
<li> 9. The support_dev.xlsx file stores whether or not the developer will be supported by the affiliate link. </li>


<h3 align="center"> Thank you for using the program, you can support me through <a target=”_blank” href='https://paypal.me/davidsulbaran'>Paypal.</a> </h3>
<h3 align="center"> You can contact me on <a target=”_blank” href='https://t.me/+xzxygFLwEmI1NzVh'>Telegram.</a> </h3>



