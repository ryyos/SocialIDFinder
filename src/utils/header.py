from fake_useragent import FakeUserAgent

class Header:

    @staticmethod
    def ex():return {"User-Agent": FakeUserAgent().random}
