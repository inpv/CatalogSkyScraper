# CatalogSkyScraper
<p><b>Description</b>:</p>
<p>A simple crawler/scraper/parser built to download product descriptions and images from SKU catalogs en masse and generate an .xls file with descriptions' html and images' links to import to a website afterwards.</p>
<p>Useful for distributors companies' website admins, especially in case the suppliers don't provide you with exact info about the goods in uploadable format.</p>
<p><b>Inner workings</b>:</p>
<p>The desired catalog sku pages are opened, then a list of sku links is formed for individual sku pages and for their respective images, using page locators. Then these individual sku pages are opened and descriptions and/or their images are scraped and downloaded to their directories as .html and .png files. The descriptions can be parsed and altered to a needed format using BeautifulSoup as well. Then an .xls file is created and the rows are filled with sku articles as IDs, as well as their respective descriptions and local image links. This file is ready to be uploaded to your website.</p>
<p>Built with pytest and Selenium using Page Object pattern and has inbuilt allure integration for visual results control.</p>
<p>Best used in headless mode with parallelization for faster scraping.</p>
<p><b>Requirements</b>:</p>
<ul>
<li>pytest</li>
<li>selenium</li>
<li>wget</li>
<li>webdriver_manager</li>
<li>allure</li>
<li>openpyxl</li>
</ul>

<p><b>TODO</b>:</p>
(as of 04.09.2022)
<ul>
<li>parallelization</li>
<li>allure integration</li>
</ul>
