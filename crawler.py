import requests
from bs4 import BeautifulSoup

def crawl_naver_news():
    # 네이버 뉴스 URL
    url = 'https://news.naver.com/'

    # GET 요청
    response = requests.get(url)

    # 요청이 성공했는지 확인
    if response.status_code == 200:
        # BeautifulSoup으로 HTML 파싱
        soup = BeautifulSoup(response.text, 'html.parser')

        # 뉴스 헤드라인 선택 (예: 첫 번째 섹션의 뉴스 헤드라인)
        headlines = soup.select('.h1 > a')  # 선택자 변경 가능

        print("네이버 뉴스 헤드라인:")
        for headline in headlines:
            print(headline.get_text().strip())
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    crawl_naver_news()
