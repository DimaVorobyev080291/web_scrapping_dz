## Домашнее задание к лекции «Веб-скрапинг» ##
## Студент Воробьев Дмитрий ##
## Прошу посмотреть что да как , подсказать что с этим делать что бы на доработки исправить ##

BeautifulSoup постоянно сыплет вординги :
dimavorobev@MacBook-Air-Dima web_scrapping_dz % /usr/local/bin/python3 /Users/dimavorobev/web_scrapping_dz/m
ain.py
Traceback (most recent call last):
  File "/Users/dimavorobev/web_scrapping_dz/main.py", line 16, in <module>
    vacancys = vacancy_list_tag.find_all(class_="vacancy-card--z_UXteNo7bRGzxWVcL7y font-inter")
               ^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'find_all'

dimavorobev@MacBook-Air-Dima web_scrapping_dz % /usr/local/bin/python3 /Users/dimavorobev/web_scrapping_dz/m
ain.py
Traceback (most recent call last):
  File "/Users/dimavorobev/web_scrapping_dz/main.py", line 27, in <module>
    span_tag = city_tag.find("span")
               ^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'find'

из за этого не смог добраться до зарплаты, постоянные ошибки с остальной частью с горем пополам еще справляетьс. Хотя тоже не с первого раза .
Пробовал останавливать процес не сильно помогло .

## selenium ## 
вообще перестал работать такое чуство что поймал бан с ним .  

