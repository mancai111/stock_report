import urllib.request
import urllib.error
import json
import urllib.parse

stock_site = 'https://api.iextrading.com/1.0/stock'

def build_time_period(time:str, company:str)->str:
    if time == 'M':        
        time_period = '1m'        
        target_url = stock_site + '/' + company + '/chart/'+ time_period        
        return target_url    
    elif time == 'Y':       
        time_period = '1y'       
        target_url = stock_site + '/' + company + '/chart/'+ time_period       
        return target_url   
    elif time == 'F':     
        time_period = '5y'    
        target_url = stock_site + '/' + company + '/chart/'+ time_period      
        return target_url

    
def get_result(url:str):
    response = None
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)
    finally:
        if response != None:
            response.close()
            
def load_company(symbol:str):
    open_company = urllib.request.urlopen(stock_site + '/' + symbol + '/' + 'company')    
    company_diction = json.loads(open_company.read())
    open_company.close()
    return company_diction

def load_stats(symbol:str):
    open_stats = urllib.request.urlopen(stock_site + '/' + symbol + '/' + 'stats')
    stats_diction = json.loads(open_stats.read())
    open_stats.close()
    return stats_diction
