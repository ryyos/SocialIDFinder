from src.service.instagram import Instagram
from src.service.tiktok import Tiktok
from src.service.facebook import Facebook
from src.service.linkedin import Linkedin

if __name__ == '__main__':
    ig = Linkedin()
    print(ig.main('https://www.linkedin.com/in/herlambang-kurniawan-5b2692288/'))
    ...