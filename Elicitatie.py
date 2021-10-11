import scrapy
from scrapy import FormRequest
from scrapy import Request


class ElicitatieSpider(scrapy.Spider):
    name = 'Elicitatie'
    request_notices = "http://www.e-licitatie.ro/api-pub/NoticeCommon/GetCNoticeList/"
    # test = ["http://www.e-licitatie.ro"]

    def start_requests(self):
        headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://www.e-licitatie.ro/pub/notices/contract-notices/list/2/1',
    'Accept-Language': 'en-US,en;q=0.9'
    }
        
        # data = {"sysNoticeTypeIds":[2],"sortProperties":[],"pageSize":5,"hasUnansweredQuestions":false,"startPublicationDate":"2021-09-27T17:05:00.379Z","startTenderReceiptDeadline":null,"sysProcedureStateId":2,"pageIndex":0,"endPublicationDate":"2021-09-26T21:00:00.000Z"}
        formdata = {
            "sysNoticeTypeIds":"{0 : '2', sysProcedureStateId : '2'}",
            #"sortProperties":[],
            "pageSize":"100",
            #"hasUnansweredQuestions":false,
            "startPublicationDate":"2021-09-27T17:05:00.379Z",
            #"startTenderReceiptDeadline":"",
            "endPublicationDate" : "2021-09-26T21:00:00.000Z",
            #"sysProcedureStateId":"2",
            "pageIndex":"0"
            }
        # yield Request(url="http://www.e-licitatie.ro", callback=self.parse_product)
        yield FormRequest(url=self.request_notices, formdata=data, headers=headers, callback=self.parse_product)

    def parse_product(self, response):
        print(response.text)