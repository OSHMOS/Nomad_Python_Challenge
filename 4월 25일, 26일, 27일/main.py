import os
import csv
import requests
from bs4 import BeautifulSoup

URL = "http://www.alba.co.kr"
# https://hochicken.alba.co.kr/job/brand/main.asp
# 첫 페이지에 있는 슈퍼브랜드 채용정보 회사 스크랩
# ul class goodsBox
# li class impact

# 각각 회사 페이지에서 알바 정보 스크랩
# div id NormalInfo
# table > tBody > tr class ''
# 각각의 .csv 파일로 만들어 저장하기

def extract_company_and_url():
  company_list = []
  url_list = []

  req = requests.get(URL)
  
  soup = BeautifulSoup(req.text, 'html.parser')

  main = soup.find('div', {'id':'MainSuperBrand'})

  box = main.find('ul', {'class':'goodsBox'})

  lists = box.find_all('li', {'class':'impact'})
  
  for list in lists:
    company = list.find('span', {'class':'company'}).string
    url = list.find('a')['href']
    company_list.append(company)
    url_list.append(url)
    
  return company_list, url_list

def extract_jobs(url):
    info_list = []
    req = requests.get(url)
  
    soup = BeautifulSoup(req.text, 'html.parser')
  
    main = soup.find('div', {'id':'NormalInfo'})
  
    table = main.find('table')
  
    tbody = table.find('tbody')

    tr_list = tbody.find_all('tr')

    for tr in tr_list:
      place = tr.find('td', {'class':'local'}).text.strip()
      title = tr.find('td', {'class':'title'}).text.strip()
      time = tr.find('td', {'class':'data'}).text.strip()
      pay = tr.find('td', {'class':'pay'}).text.strip()
      last = tr.find('td', {'class':'last'}).text.strip()
      info_list.append(place, title, time, pay, last)
      
      return info_list
      # return {
      #   'place': place,
      #   'title': title,
      #   'time': time,
      #   'pay': pay,
      #   'last': last
      # }
    
def save_to_file(company):
  file = open(f'{company}.csv', mode='w')
  writer = csv.writer(file)
  writer.writerow(['place', 'title', 'time', 'pay', 'date'])
  # for job in company:
  #   writer.writerow(list(job.values()))
  return
  
if __name__ == '__main__':
  os.system("clear")

  company_list, url_list = extract_company_and_url()
  
  # for url in url_list:
  #   print(extract_jobs(url))
  for company in company_list:
    save_to_file(company)
    # print(company)