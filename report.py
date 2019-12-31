import indicator
import api
import signals

def print_header(symbol:str):
    'print out the header'
    information = dict()
    company_diction = api.load_company(symbol)
    stats_diction = api.load_stats(symbol)

    information = {'symbol':company_diction['symbol'],
               'companyName':company_diction['companyName'],
               'sharesOutstanding':stats_diction['sharesOutstanding']
               }
    
    A = information['symbol']
    B = information['companyName']
    C = information['sharesOutstanding']
    print(A)
    print(B)
    print(C)    

def run() -> None:
    'run the program'
    symbol_name = input()
    time_period = input()
    indicator_signal = input()
    answer_parts = indicator_signal.split()
    print_header(symbol_name) 
    link = api.build_time_period(time_period , symbol_name)
    data_list = api.get_result(link)

    if indicator_signal.startswith('TR'): 
        updated_list = indicator.true_range(data_list).calculate_true_range()
        signals.true_range(updated_list)
        call_the_signal = signals.true_range(updated_list)
        complete_list =call_the_signal.signal_true_range(answer_parts[1],answer_parts[2])
        basic_report(complete_list)
        
    elif indicator_signal.startswith('MP'):
        updated_list = indicator.simple_moving(data_list,answer_parts[1]).calculate_simple_moving_price_volume('close')
        signals.simple_moving_average_signal(updated_list,answer_parts[1])
        call_the_signal = signals.simple_moving_average_signal(updated_list,answer_parts[1])
        complete_list = call_the_signal.signal_simple_price_volume('close') 
        basic_report(complete_list)

    elif indicator_signal.startswith('MV'):
        updated_list = indicator.simple_moving(data_list,answer_parts[1]).calculate_simple_moving_price_volume('volume')
        signals.simple_moving_average_signal(updated_list,answer_parts[1])
        call_the_signal = signals.simple_moving_average_signal(updated_list,answer_parts[1])
        complete_list = call_the_signal.signal_simple_price_volume('volume') 
        basic_report(complete_list)


        
    elif indicator_signal.startswith('DP'):
        updated_list = indicator.directional_indicator(data_list,answer_parts[1]).calculate_directional_price_volume('close')
        signals.directional_indicator_signal(updated_list, answer_parts[1])
        call_the_signal = signals.directional_indicator_signal(updated_list, answer_parts[1])

        complete_list = call_the_signal.signal_directional_indicator_price_volume(answer_parts[2],answer_parts[3])

        basic_report(complete_list)

    elif indicator_signal.startswith('DV'):
        updated_list = indicator.directional_indicator(data_list,answer_parts[1]).calculate_directional_price_volume('volume')
        signals.directional_indicator_signal(updated_list, answer_parts[1])
        call_the_signal = signals.directional_indicator_signal(updated_list, answer_parts[1])
        complete_list = call_the_signal.signal_directional_indicator_price_volume(answer_parts[2],answer_parts[3])
        basic_report(complete_list)

    else:
        pass
    
def basic_report(data_list):
    'print each line of report'
    for data in data_list:
        date = str(data['date'])
        open_price = str(format(data['open'],'.4f'))
        close_price = str(format(data['close'],'.4f'))
        high = str(format(data['high'],'.4f'))
        low = str(format(data['low'],'.4f'))
        volume = str(data['volume'])
        buy = str(data['buy'])
        sell = str(data['sell'])
        report_line = date + '\t' + open_price + '\t' + close_price + '\t' + high + '\t'+ low + '\t' + volume + '\t'        
        if type(data['indicator']) == float:
            indicator = str(format(data['indicator'],'.4f'))
            update = indicator + '\t' + buy + '\t' + sell
            complete_report_line = report_line + update
        else:
            indicator = str(data['indicator'])
            update = indicator + '\t' + buy + '\t' + sell
            complete_report_line = report_line + update        
        print(complete_report_line)


if __name__ == '__main__':
    run()
    print("Data provided for free by IEX\tView IEX's Terms of Use\thttps://iextrading.com/api-exhibit-a/")

