from bs4 import BeautifulSoup
import pandas as pd
import os


def extract_movie_info(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    movies_data = []

    try:
        # 영화 목록 찾기
        movie_items = soup.select(
            "#mor_history_id_0 > div > div.flipsnap_view > div > div > c-flicking-item > c-layout > div > c-list-doc > ul > li"
        )

        for item in movie_items:
            try:
                # 영화 제목 추출
                title = item.select_one(
                    "div.item-bundle-mid > div.item-title > c-title > strong > a"
                ).text.strip()

                # 관객 수 추출
                audience_text = item.select_one(
                    "div.item-bundle-mid > div.item-contents > c-contents-desc > p > a"
                ).text.strip()
                audience_num = int(
                    float(
                        audience_text.replace("누적 ", "")
                        .replace("만명", "")
                        .replace(",", "")
                    )
                    * 10000
                )

                movies_data.append({"Title": title, "Audience": audience_num})

            except Exception as e:
                print(f"Error extracting movie info: {e}")
                continue

    except Exception as e:
        print(f"Error processing HTML: {e}")

    return movies_data


def process_saved_pages():
    # 연도별 영화 데이터를 저장할 딕셔너리
    year_movies = {}

    # movie_pages 디렉토리의 모든 HTML 파일을 정렬된 순서로 처리
    for filename in sorted(os.listdir("movie_pages")):
        if filename.endswith(".html"):
            year = filename.split("_")[0]
            print(f"Processing {filename}")

            # 해당 연도의 영화가 아직 30개가 안 되는 경우에만 처리
            if year not in year_movies:
                year_movies[year] = []

            if len(year_movies[year]) >= 30:
                continue

            with open(f"movie_pages/{filename}", "r", encoding="utf-8") as f:
                html_content = f.read()

            movies = extract_movie_info(html_content)
            for movie in movies:
                # 중복 검사 및 30개 제한
                if len(year_movies[year]) < 30 and movie["Title"] not in [
                    m["Title"] for m in year_movies[year]
                ]:
                    movie["Year"] = year
                    year_movies[year].append(movie)

    # 모든 영화 데이터를 하나의 리스트로 합치기
    all_movies = []
    for year in sorted(year_movies.keys(), reverse=True):  # 최신 연도부터 정렬
        all_movies.extend(year_movies[year])
        print(f"Year {year}: {len(year_movies[year])} movies collected")

    # DataFrame 생성 및 CSV 저장
    if all_movies:
        df = pd.DataFrame(all_movies)
        df.to_csv("movie_data.csv", index=False, encoding="utf-8-sig")
        print(f"\nSuccessfully saved {len(all_movies)} movies to movie_data.csv")
        print("\nData Preview:")
        print(df.head())
        print(f"\nTotal movies by year:")
        print(df.groupby("Year").size())
    else:
        print("No data collected!")


if __name__ == "__main__":
    process_saved_pages()
