from src.service.instagram import Instagram
from src.service.tiktok import Tiktok
from src.service.facebook import Facebook
from src.service.linkedin import Linkedin
from src.service.youtube import Youtube

if __name__ == '__main__':
    ig = Youtube()
    print(ig.main('https://www.youtube.com/@JKT48'))
    ...