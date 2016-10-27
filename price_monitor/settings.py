# -*- coding: utf-8 -*-


BOT_NAME = 'price_monitor'
SPIDER_MODULES = ['price_monitor.spiders']
NEWSPIDER_MODULE = 'price_monitor.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'price_monitor (+http://www.yourdomain.com)'
ROBOTSTXT_OBEY = True
DOWNLOAD_DELAY = 3

# DO NOT COMMIT THIS!!!!!!!!
SHUB_KEY = 'd7cf14b3fdf749cfac1cb99897f92788'

# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#     'price_monitor.pipelines.CollectionStoragePipeline': 400,
# }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'price_monitor.middlewares.MyCustomSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'price_monitor.middlewares.MyCustomDownloaderMiddleware': 543,
# }

# AUTOTHROTTLE_ENABLED = True
# HTTPCACHE_ENABLED = True
