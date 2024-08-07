import scrapy


class OpentenderSpider(scrapy.Spider):
    name = "opentender_spider"

    # List of country codes you want to scrape
    country_codes = ["LT", "LU"]

    def start_requests(self):
        for cc in self.country_codes:
            url = f"https://web.archive.org/web/20230601012240/https://opentender.eu/data/files/data-{cc}-csv.zip"
            # url = f"https://opentender.eu/data/downloads/data-{cc}-csv.zip"
            yield scrapy.Request(url, callback=self.parse, method="GET")

    def parse(self, response):
        # Save the file or process data here
        self.logger.info(f"Scraping URL: {response.url}")

        # Save the downloaded file
        country_code = response.url.split("-")[1]
        file_path = f"../data/data-{country_code}-csv.zip"

        with open(file_path, "wb") as f:
            f.write(response.body)
