from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep



class Linkedinbot:
	def __init__(self):
		self.jobs_collected = []
		self.url = "https://www.linkedin.com/jobs/search?keywords=python&location=usa"
		self.path = "/XXXXXXXXXXXXXXXXXXXXXXX/geckodriver"
		self.__start(self.path, self.url)


	def __start(self, path, url):
		print("Bot is Started")
		driver = webdriver.Firefox(options=self.__options(), executable_path=path)
		driver.get(url)
		sleep(3)
		self.__scroll(driver)
	

	def __jobs(self, driver):
		__jobs = driver.find_element_by_class_name("jobs-search__results-list")
		__list_of_jobs = __jobs.find_elements_by_tag_name("li")
		for __job in __list_of_jobs:
			job_post = __job.find_element_by_class_name("result-card__title")
			job_company = __job.find_element_by_class_name("result-card__subtitle")
			job_location = __job.find_element_by_class_name("job-result-card__location")
			job_time = __job.find_element_by_class_name("job-result-card__listdate")

			json_data = {
				"Job Title": job_post.text,
				"Company": job_company.text,
				"Location": job_location.text,
				"Time Posted": job_time.text
				}
			print(json_data)
			self.jobs_collected.append(json_data)





	def __scroll(self, driver):
		print("Bot is Scrolling")
		SCROLL_PAUSE_TIME = 2
		# Get scroll height
		last_height = driver.execute_script("return document.body.scrollHeight")
		while True:
		    # Scroll down to bottom
		    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		    # Wait to load page
		    sleep(SCROLL_PAUSE_TIME)
		    try:
		    	self.__jobs(driver)
		    except:
		    	pass
		    # Calculate new scroll height and compare with last scroll height
		    new_height = driver.execute_script("return document.body.scrollHeight")
		    if new_height == last_height:
		        break
		    last_height = new_height
		return


	def __options(self):
		"""
		Configuring options of the Bot
		"""
		options = Options()
		options.add_argument("Cache-Control=no-cache")
		options.add_argument("--no-sandbox")
		options.add_argument("--dns-prefetch-disable")
		options.add_argument("--disable-dev-shm-usage")
		options.add_argument("--disable-web-security")
		options.add_argument("--ignore-certificate-errors")
		options.page_load_strategy = 'none'
		options.add_argument("--ignore-certificate-errors-spki-list")
		options.add_argument("--ignore-ssl-errors")
		return options


lk = Linkedinbot()
