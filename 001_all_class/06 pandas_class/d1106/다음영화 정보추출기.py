from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os


def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver


def save_page(driver, year, page):
    # 저장할 디렉토리 생성
    if not os.path.exists("movie_pages"):
        os.makedirs("movie_pages")

    # 페이지 HTML 저장
    filename = f"movie_pages/{year}_page_{page}.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print(f"Saved {filename}")


def scroll_down(driver):
    # 현재 스크롤 위치에서 500픽셀 아래로 스크롤
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(1)


def scrape_pages():
    driver = setup_driver()
    years = [2023, 2022, 2021, 2020]

    try:
        for year in years:
            print(f"\n{'='*50}")
            print(f"Processing year {year}")
            print(f"{'='*50}")

            # 첫 페이지 접근
            url = f"https://search.daum.net/search?w=tot&q={year}년영화순위&DA=MOR&rtmaxcoll=MOR"
            driver.get(url)
            time.sleep(3)

            # 각 페이지 저장
            for page in range(1, 4):
                print(f"\nProcessing page {page} for year {year}")

                # 스크롤 다운
                scroll_down(driver)

                # 현재 페이지 저장
                save_page(driver, year, page)

                # 마지막 페이지가 아니면 다음 페이지로 이동
                if page < 3:
                    try:
                        next_button = WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable(
                                (
                                    By.CSS_SELECTOR,
                                    "#mor_history_id_0 > div > div.compo-paging > button.btn_next",
                                )
                            )
                        )
                        # 버튼이 확실히 보이도록 스크롤
                        driver.execute_script(
                            "arguments[0].scrollIntoView({block: 'center'});",
                            next_button,
                        )
                        time.sleep(1)
                        next_button.click()
                        time.sleep(2)
                        print(f"Moved to page {page + 1}")
                    except Exception as e:
                        print(f"Error clicking next button: {e}")
                        break

            time.sleep(2)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()
        print("Page collection completed!")


if __name__ == "__main__":
    scrape_pages()
