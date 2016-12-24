from urllib import request

goog_url = 'http://chart.finance.yahoo.com/table.csv?s=GOOG&a=10&b=23&c=2016&d=11&e=23&f=2016&g=d&ignore=.csv'

def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest = r'goog.csv'
    fx = open(dest, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_stock_data(goog_url)