from src.service.instagram import Instagram
from src.service.tiktok import Tiktok
from src.service.facebook import Facebook
from src.service.linkedin import Linkedin
from src.service.youtube import Youtube
from src.service.twiter import Twiter

if __name__ == '__main__':
    ig = Twiter()
    print(ig.main('https://twitter.com/CErine_JKT48'))
    ...