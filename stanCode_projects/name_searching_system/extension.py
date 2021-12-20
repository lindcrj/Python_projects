"""
File: extension.py
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        male_num = 0
        female_num = 0
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        ##################
        #                #
        #      TODO:     #
        #                #
        ##################
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        tr = soup.tbody.find_all('tr')
        for ttr in tr:
            tdd_list = ttr.find_all('td')
            if tdd_list[0].text != '':
                td_list = tdd_list
                male = str(td_list[2].text).replace(',', '')
                male = int(male)
                female = str(td_list[4].text).replace(',', '')
                female = int(female)
                male_num += male
                female_num += female
        print('Male Number: ' + str(male_num))
        print('Female Number: ' + str(female_num))




if __name__ == '__main__':
    main()
