from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# WebDriver 설정
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # 브라우저 창을 표시하지 않음
driver = webdriver.Chrome(service=service, options=options)

# URL 설정
url = "https://prod.danawa.com/list/?cate=112757&shortcutKeyword=%EB%AA%A8%EB%8B%88%ED%84%B0"
driver.get(url)

# 페이지 로드 대기
driver.implicitly_wait(5)

# 필터링: 예시로 "브랜드" 필터를 클릭하는 코드 (필요에 따라 수정)
try:
    samsung_checkbox = driver.find_element(By.XPATH, '//*[@id="searchMakerRep702"]')
    if not samsung_checkbox.is_selected():
        samsung_checkbox.click()

    # 필터가 적용될 때까지 대기 (필요에 따라 조정)
    time.sleep(5)
except Exception as e:
    print(f"필터 적용 중 오류 발생: {e}")

# 필터링된 데이터 크롤링
main_prodlist = driver.find_element(By.CLASS_NAME, "main_prodlist")
products = main_prodlist.find_elements(By.CLASS_NAME, "prod_layer")

product_data = []
for product in products:
    try:
        product = product.find_element(By.CLASS_NAME, "prod_main_info")
        name = product.find_element(By.CLASS_NAME, "prod_name").text.strip()
        price_section = product.find_element(By.CLASS_NAME, "price_sect")
        price = price_section.find_element(By.TAG_NAME, "a").text.strip()
        spec_list = product.find_element(By.CLASS_NAME, "spec_list").text.strip()
        release_date = (
            product.find_element(By.CLASS_NAME, "mt_date")
            .find_element(By.TAG_NAME, "dd")
            .text.strip()
        )
        product_data.append(
            {
                "name": name,
                "price": price,
                "spec_list": spec_list,
                "release_date": release_date,
            }
        )
    except Exception as e:
        continue

# WebDriver 종료
driver.quit()

for data in product_data:
    print(
        f"Product Name: {data['name']} | Price: {data['price']} | Spec-list: {data['spec_list']} | Release: {data['release_date']}"
    )
