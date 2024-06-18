import requests
from bs4 import BeautifulSoup
import os
import tqdm # To show the progeress dynamically


urls = ['https://engineering.case.edu/bearingdatacenter/normal-baseline-data',
       'https://engineering.case.edu/bearingdatacenter/12k-drive-end-bearing-fault-data',
       'https://engineering.case.edu/bearingdatacenter/48k-drive-end-bearing-fault-data',
       'https://engineering.case.edu/bearingdatacenter/12k-fan-end-bearing-fault-data']

download_dirs = ['data/normal', 'data/12k-drive-end', 'data/48k-drive-end', 'data/12k-fan-end']

for url, download_dir in zip(urls, download_dirs):
    print('Saving data to:', download_dir)

    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
        
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    links = soup.find_all('a', href=True)
    file_links = [link['href'] for link in links if link['href'].endswith(('.mat'))]


    for file_link in tqdm.tqdm(file_links):
        file_name = file_link.split('/')[-1]
        file_path = os.path.join(download_dir, file_name)
        response = requests.get(file_link)
        with open(file_path, 'wb') as f:
            f.write(response.content)
