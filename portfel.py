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
        
    def MakeForecastDiagramm(self, year=5, perc = [1, 10, 50, 90, 99]):
        """Рисует график предпологаемого дохода данного портфеля, можно изменить на сколько лет делать расчёт и колличество перцентилей"""
        self.Port.plot_forecast(years=year, percentiles=perc)
        plt.show()
        
    def MakeEfficientyFrontDiagramm(self, ports=1000):
        """Рисует диагрумму горизонта эффективности и возможных портфелей"""
        x = ok.EfficientFrontier(self.Tickers, ccy='RUB')
        fig = plt.figure()
        x.plot_assets(kind='mean')
        ax = plt.gca()
        self.mc = x.get_monte_carlo(n=ports, kind='mean')
        ax.scatter(self.mc.Risk, self.mc.Return, linewidth=0, color='green')
        df = x.ef_points
        ax.plot(df['Risk'], df['Mean return'], color='black', linestyle='dashed', linewidth=3)
        ax.set_xlabel('Risk (Standard Deviation)')
        ax.set_ylabel('Return')
        ax.legend()
        plt.show()
        
    def SetWeights(self, weights):
        self.Port.weights = weights
        
    def GetWeights(self, risk, ret):
        """Возвращает веса акций по риску и доходу портфеля заданными пользователем
        WARNING: прежде чем запускать эту функцию, должна быть запущена хоть раз функция MakeEfficientyFrontDiagramm"""
        x = ok.EfficientFrontier(self.Tickers, ccy='RUB')
        rez = []
        for port in self.mc.values:
            if round(risk,4) == round(port[0],4) and round(ret,4) == round(port[1],4):
                for i in range(2, len(self.Tickers) + 1):
                    rez.append(round(port[i],4))
                break
        if len(rez) == 0:
            return 'Портфель не найден'
        else:
            rez.append(1 - sum(rez)) 
            self.SetWeights(rez)
            return rez
        
                
        
        







#examples
# port = Portfel()
# port.AddCompanyToPort('GAZPROM')
# port.AddCompanyToPort('ROSNEFT')
# port.AddCompanyToPort('LUKOIL')
# port.AddCompanyToPort('NOVATEK')
# port.CreatePortfel()
# port.MakeEfficientyFrontDiagramm()
