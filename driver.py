import logfile
import webscrape

logfile.set_custom_log_info('error.log')

news_scrap=webscrape.Scrapper(webscrape.url_global,logfile)
news_scrap.retrieve_webpage()
news_scrap.write_webpage_as_html()
news_scrap.read_webpage_from_html()
news_scrap.convert_data_to_bs4()
news_scrap.parse_soup_to_html()
