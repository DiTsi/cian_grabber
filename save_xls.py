from selenium import webdriver
from time import sleep
import os
from datetime import datetime

# download_path = "./downloads"
url = "https://www.cian.ru/cat.php?currency=2&deal_type=sale&engine_version=2&foot_min=20&include_new_moscow=0&is_first_floor=0&loggia=1&max_house_year=2018&maxprice=6500000&metro%5B0%5D=1&metro%5B100%5D=86&metro%5B101%5D=87&metro%5B102%5D=87&metro%5B103%5D=88&metro%5B104%5D=89&metro%5B105%5D=90&metro%5B106%5D=91&metro%5B107%5D=91&metro%5B108%5D=92&metro%5B109%5D=93&metro%5B10%5D=10&metro%5B110%5D=95&metro%5B111%5D=96&metro%5B112%5D=97&metro%5B113%5D=98&metro%5B114%5D=99&metro%5B115%5D=100&metro%5B116%5D=100&metro%5B117%5D=101&metro%5B118%5D=102&metro%5B119%5D=103&metro%5B11%5D=10&metro%5B120%5D=103&metro%5B121%5D=103&metro%5B122%5D=104&metro%5B123%5D=105&metro%5B124%5D=106&metro%5B125%5D=107&metro%5B126%5D=107&metro%5B127%5D=108&metro%5B128%5D=110&metro%5B129%5D=111&metro%5B12%5D=11&metro%5B130%5D=111&metro%5B131%5D=112&metro%5B132%5D=113&metro%5B133%5D=114&metro%5B134%5D=115&metro%5B135%5D=116&metro%5B136%5D=117&metro%5B137%5D=117&metro%5B138%5D=118&metro%5B139%5D=119&metro%5B13%5D=12&metro%5B140%5D=120&metro%5B141%5D=121&metro%5B142%5D=121&metro%5B143%5D=122&metro%5B144%5D=123&metro%5B145%5D=124&metro%5B146%5D=125&metro%5B147%5D=127&metro%5B148%5D=128&metro%5B149%5D=129&metro%5B14%5D=13&metro%5B150%5D=129&metro%5B151%5D=129&metro%5B152%5D=130&metro%5B153%5D=131&metro%5B154%5D=132&metro%5B155%5D=132&metro%5B156%5D=133&metro%5B157%5D=134&metro%5B158%5D=135&metro%5B159%5D=137&metro%5B15%5D=14&metro%5B160%5D=140&metro%5B161%5D=141&metro%5B162%5D=142&metro%5B163%5D=143&metro%5B164%5D=144&metro%5B165%5D=145&metro%5B166%5D=146&metro%5B167%5D=147&metro%5B168%5D=148&metro%5B169%5D=149&metro%5B16%5D=15&metro%5B170%5D=149&metro%5B171%5D=150&metro%5B172%5D=151&metro%5B173%5D=152&metro%5B174%5D=152&metro%5B175%5D=154&metro%5B176%5D=155&metro%5B177%5D=156&metro%5B178%5D=157&metro%5B179%5D=158&metro%5B17%5D=15&metro%5B180%5D=159&metro%5B181%5D=229&metro%5B182%5D=236&metro%5B183%5D=237&metro%5B184%5D=237&metro%5B185%5D=272&metro%5B186%5D=275&metro%5B187%5D=281&metro%5B188%5D=283&metro%5B189%5D=284&metro%5B18%5D=15&metro%5B190%5D=285&metro%5B191%5D=287&metro%5B192%5D=289&metro%5B193%5D=290&metro%5B194%5D=291&metro%5B195%5D=292&metro%5B196%5D=293&metro%5B197%5D=294&metro%5B198%5D=295&metro%5B199%5D=296&metro%5B19%5D=16&metro%5B1%5D=2&metro%5B200%5D=296&metro%5B201%5D=297&metro%5B202%5D=298&metro%5B203%5D=299&metro%5B204%5D=300&metro%5B205%5D=301&metro%5B206%5D=302&metro%5B207%5D=303&metro%5B208%5D=304&metro%5B209%5D=305&metro%5B20%5D=17&metro%5B210%5D=306&metro%5B211%5D=307&metro%5B212%5D=308&metro%5B213%5D=309&metro%5B214%5D=310&metro%5B215%5D=311&metro%5B216%5D=311&metro%5B217%5D=337&metro%5B218%5D=338&metro%5B219%5D=339&metro%5B21%5D=18&metro%5B220%5D=350&metro%5B221%5D=351&metro%5B222%5D=352&metro%5B223%5D=353&metro%5B224%5D=354&metro%5B22%5D=18&metro%5B23%5D=20&metro%5B24%5D=21&metro%5B25%5D=21&metro%5B26%5D=21&metro%5B27%5D=26&metro%5B28%5D=27&metro%5B29%5D=27&metro%5B2%5D=2&metro%5B30%5D=28&metro%5B31%5D=28&metro%5B32%5D=29&metro%5B33%5D=30&metro%5B34%5D=31&metro%5B35%5D=32&metro%5B36%5D=33&metro%5B37%5D=35&metro%5B38%5D=36&metro%5B39%5D=37&metro%5B3%5D=3&metro%5B40%5D=38&metro%5B41%5D=40&metro%5B42%5D=41&metro%5B43%5D=42&metro%5B44%5D=43&metro%5B45%5D=44&metro%5B46%5D=45&metro%5B47%5D=45&metro%5B48%5D=46&metro%5B49%5D=46&metro%5B4%5D=4&metro%5B50%5D=46&metro%5B51%5D=47&metro%5B52%5D=47&metro%5B53%5D=48&metro%5B54%5D=49&metro%5B55%5D=50&metro%5B56%5D=50&metro%5B57%5D=50&metro%5B58%5D=50&metro%5B59%5D=51&metro%5B5%5D=5&metro%5B60%5D=53&metro%5B61%5D=53&metro%5B62%5D=54&metro%5B63%5D=54&metro%5B64%5D=55&metro%5B65%5D=56&metro%5B66%5D=56&metro%5B67%5D=58&metro%5B68%5D=60&metro%5B69%5D=60&metro%5B6%5D=5&metro%5B70%5D=61&metro%5B71%5D=61&metro%5B72%5D=61&metro%5B73%5D=62&metro%5B74%5D=62&metro%5B75%5D=63&metro%5B76%5D=64&metro%5B77%5D=64&metro%5B78%5D=66&metro%5B79%5D=68&metro%5B7%5D=6&metro%5B80%5D=70&metro%5B81%5D=71&metro%5B82%5D=72&metro%5B83%5D=73&metro%5B84%5D=74&metro%5B85%5D=75&metro%5B86%5D=77&metro%5B87%5D=78&metro%5B88%5D=79&metro%5B89%5D=80&metro%5B8%5D=8&metro%5B90%5D=80&metro%5B91%5D=81&metro%5B92%5D=83&metro%5B93%5D=84&metro%5B94%5D=84&metro%5B95%5D=85&metro%5B96%5D=85&metro%5B97%5D=85&metro%5B98%5D=86&metro%5B99%5D=86&metro%5B9%5D=9&min_balconies=1&min_house_year=1985&mintarea=31&offer_type=flat&only_foot=2&quality=1&room1=1&room2=1&room9=1&sort=price_object_order&wp=1"
download_path = os.path.realpath("./downloads")
filename = "offers.xlsx"

options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : download_path}
options.add_experimental_option('prefs', prefs)
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/60.0.3112.50 Safari/537.36"')
# user_agent = 'I LIKE CHOCOLATE'
# options.add_argument(f'user-agent={user_agent}')
# options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)


driver.get(url)
sleep(5)

# e = driver.page_source
driver.find_element_by_xpath("//*[contains(text(), 'Сохранить файл в Excel')]").click()

fullpath = download_path + "/" + filename
while not os.path.exists(fullpath):
    sleep(1)

now = datetime.now()
date = now.strftime("%Y.%m.%d_%H.%M.%S")
fullpath_new = fullpath[:-5] + "_" + date + ".xlsx"

if os.path.isfile(fullpath):

    os.rename(fullpath, fullpath_new)
else:
    driver.close()
    raise ValueError("{} isn't a file!".format(fullpath))

driver.close()
exit(0)
