import os
import requests

def awake():
  print('Welcome to IsItDown.py!')
  print('Please write a URL or URLs you want to check. (separated by comma)')
  
def main():
  url_list = list(input().split(','))
  for url in url_list:
    url = url.lower().strip()
    if '.' not in url:
      print(f'{url} is not a valid URL')
      restart()
    else:
      if 'http' not in url:
        url = f'http://{url}'
        response = requests.get(url)
        if response.status_code == 200:
          print(f'{url} is up!')
        else:
          print(f'{url} is down!')
      else:
        url = url
        try:
          raise ValueError
        except ValueError:
          response = requests.get(url)
          if response.status_code == 404:
            print(f'{url} is down!')
          else:
            print(f'{url} is up!')
          
  restart()

def restart():
  btn = input('Do you want to start over? y/n ')
  if btn == 'y':
    os.system('clear')
    awake()
    main()
  elif btn == 'n':
    print('k.bye!')
  else:
    print("That's not a valid answer")
    restart
    
if __name__ == '__main__':
  awake()
  main()