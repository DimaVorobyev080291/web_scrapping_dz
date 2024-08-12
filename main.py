import time
import json
import fake_headers
import requests
from bs4 import BeautifulSoup

headers = fake_headers.Headers(browser="firefox", os="mac")

main_html = requests.get(
    "https://spb.hh.ru/search/vacancy?text=python+django+flask&salary=&ored_clusters=true&area=1&area=2&hhtmFrom=vacancy_search_list&hhtmFromLabel=vacancy_search_line", headers=headers.generate()
).text

main_soup = BeautifulSoup(main_html, features="lxml")
vacancy_list_tag = main_soup.find(id="a11y-main-content")
# time.sleep(4)
vacancys = vacancy_list_tag.find_all(class_="vacancy-card--z_UXteNo7bRGzxWVcL7y font-inter")
# time.sleep(4)

information_vacancy =[]

for vacancy in vacancys:
    a_tag = vacancy.find("a")
    link = a_tag["href"]
    info_section_tag = vacancy.find(class_="info-section--N695JG77kqwzxWAnSePt")
    company = info_section_tag.find("a")
    city_tag = info_section_tag.find(class_="narrow-container--lKMghVwoLUtnGdJIrpW4")
    span_tag = city_tag.find("span")
    city = span_tag.find("span")

    information_vacancy.append(
        {
            "title": a_tag.text,
            "link": link,
            "company": company.text,
            "city": city.text
        }
    )

with open('info_vacancy.json', 'w', ) as json_file :
            json.dump(information_vacancy, json_file, ensure_ascii=False)

# main_soup2 = BeautifulSoup(main_html, features="lxml")
# vacancy_list_tag = main_soup2.find(id="a11y-main-content")
# time.sleep(4)
# vacancys = vacancy_list_tag.find_all(class_="vacancy-card--z_UXteNo7bRGzxWVcL7y font-inter")
# time.sleep(4)

# for vacancy in vacancys:
#     salary_section = vacancy.find(class_="narrow-container--lKMghVwoLUtnGdJIrpW4")
#     # salary = salary_section.find("span")