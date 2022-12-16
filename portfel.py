import okama as ok
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

class Portfel:
    """Portfel это класс для работы с портфелем акций"""
    def __init__(self):      
        self.AllTickers = []
        """все тикеры компаний"""
        self.Tickers = []
        """все тикеры нашего портфеля"""
        self.Companies = []
        """все компании"""
        bs = BeautifulSoup(requests.get('https://www.tradingview.com/markets/stocks-russia/market-movers-large-cap/').text, 'lxml')
        ticker = bs.find_all('a', 'apply-common-tooltip tickerNameBox-hMpTPJiS tickerName-hMpTPJiS')
        for t in ticker:
            self.AllTickers.append(t.text)
        companies = bs.find_all('sup', 'apply-common-tooltip tickerDescription-hMpTPJiS')
        for c in companies:
            self.Companies.append(c.text)
    def AddCompanyToPort(self, company):
        """Добавляет акцию компании в наш портфель"""
        self.Tickers.append(self.AllTickers[self.Companies.index(company)]+".MOEX")
    def CreatePortfel(self):
        """Создаёт портфель с полученными акциями"""
        self.Port = ok.Portfolio(self.Tickers, ccy='RUB')
    def MakeForecastDiagramm(self, year=5, perc = [10, 50, 90]):
        """Рисует график предпологаемого дохода данного портфеля, можно изменить на сколько лет делать расчёт и колличество перцентилей"""
        self.Port.plot_forecast(years=year, percentiles=perc)
        plt.show()
    def MakeEfficientyFrontDiagramm(self, ports=1000):
        """Рисует диагрумму горизонта эффективности и возможных портфелей"""
        x = ok.EfficientFrontier(self.Tickers, ccy='RUB')
        fig = plt.figure()
        x.plot_assets(kind='mean')
        ax = plt.gca()
        mc = x.get_monte_carlo(n=1000, kind='mean')
        ax.scatter(mc.Risk, mc.Return, linewidth=0, color='green')
        df = x.ef_points
        ax.plot(df['Risk'], df['CAGR'], color='black', linestyle='dashed', linewidth=3)
        ax.set_xlabel('Risk (Standard Deviation)')
        ax.set_ylabel('Return')
        ax.legend()
        plt.show()
        
        
        







#examples
port = Portfel()
port.AddCompanyToPort('GAZPROM')
port.AddCompanyToPort('ROSNEFT')
port.AddCompanyToPort('LUKOIL')
port.CreatePortfel()
port.MakeForecastDiagramm(year=8, perc=[10,20,30,40,50,60,70,80,90,99])