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
  company_name = []
  company_url = []
  req = requests.get(URL)
  
  soup = BeautifulSoup(req.text, 'html.parser')

  main = soup.find('div', {'id':'MainSuperBrand'})

  box = main.find('ul', {'class':'goodsBox'})

  lists = box.find_all('li', {'class':'impact'})
  
  for list in lists:
    company = list.find('span', {'class':'company'}).string
    url = list.find('a')['href']
    company_name.append(company)
    company_url.append(url)
    
  return company_name, company_url

# def extract_url():
#   company_url = []
#   req = requests.get(URL)
  
#   soup = BeautifulSoup(req.text, 'html.parser')

#   main = soup.find('div', {'id':'MainSuperBrand'})

#   box = main.find('ul', {'class':'goodsBox'})

#   lists = box.find_all('li', {'class':'impact'})
  
#   for list in lists:
#     link = list.find('a')['href']
#     company_url.append(link)

#   return company_url
  
def extract_jobs(company_url):
  for url in company_url:
    req = requests.get(url)
  
    soup = BeautifulSoup(req.text, 'html.parser')
  
    main = soup.find('div', {'id':'NormalInfo'})
  
    table = main.find('table')
  
    tbody = table.find('tbody')

    tr_list = tbody.find_all('tr')

    for tr in tr_list:
      place = tr.find('td', {'class':'local'}).text
      title = tr.find('td', {'class':'title'}).text
      time = tr.find('td', {'class':'data'}).text
      pay = tr.find('td', {'class':'pay'}).text
      last = tr.find('td', {'class':'last'}).text
      return {
        'place': place,
        'title': title,
        'time': time,
        'pay': pay,
        'last': last
      }
    
# def save_to_file(company = extract_company()):
#   file = open(f'{company}.csv', mode='w')
#   writer = csv.writer(file)
#   writer.writerow(['place', 'title', 'time', 'pay', 'date'])
#   for job in company:
#     writer.writerow(list(job.values()))
#   return
  
if __name__ == '__main__':
  os.system("clear")

  company, url = extract_company_and_url()
  
  print(company)
  print(url)
  # print(extract_jobs(extract_url()))
  # save_to_file()