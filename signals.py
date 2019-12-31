

class simple_moving_average_signal:
    def __init__(self,list_of_dictionaries,date):
        self.list_of_dictionaries = list_of_dictionaries
        self.date = date

        
    def signal_simple_price_volume(self,key):
        'add the buy/sell signal to every dictionary and put those in a new list when asking simple moving average'
        final_list = []
        days_not_count = int(self.date) - 1
        LoD = self.list_of_dictionaries
        observed_days = LoD[int(self.date):]
        
        for i in range(days_not_count):
            LoD[i]['buy'] = ""
            LoD[i]['sell'] = ""
            final_list.append(LoD[i])

        for a in LoD[days_not_count:]:

            order = LoD.index(a)
            previous_one = LoD[order-1]
            if type(previous_one['indicator'])==float:

                if a[key] > a['indicator'] and previous_one[key] < previous_one['indicator']:
                    a['buy'] = 'BUY'
                    a['sell'] = ''
                    final_list.append(a)
                elif a[key] < a['indicator'] and previous_one[key] > previous_one['indicator']:
                    a['buy'] = ''
                    a['sell'] = 'SELL'
                    final_list.append(a)
                else:
                    a['buy'] = ""
                    a['sell'] = ""
                    final_list.append(a)
            else:
                a['buy'] = ""
                a['sell'] = ""
                final_list.append(a)
        return(final_list)          

class directional_indicator_signal:
    def __init__(self,list_of_dictionaries,date):
        self.list_of_dictionaries = list_of_dictionaries
        self.date = date

    def signal_directional_indicator_price_volume(self,buy,sell):
        'add the buy/sell signal to every dictionary and put those in a new list when asking directional'
        final_list = []
        days_not_count = int(self.date) - 1
        LoD = self.list_of_dictionaries

        for i in LoD[:1]:
            LoD[0]['buy'] = ""
            LoD[0]['sell'] = ""
            final_list.append(LoD[0])

        for i in LoD[1:]:
            order = LoD.index(i)
            if LoD[order]['indicator'] > int(buy) and int(buy) > LoD[order-1]['indicator']:
                i['buy']= 'BUY'
                i['sell'] = ""
                final_list.append(i)
            elif LoD[order]['indicator'] < int(sell) and int(sell) < LoD[order-1]['indicator']:
                i['buy'] = ""
                i['sell'] = 'SELL'
                final_list.append(i)
            else:
                i['buy'] = ""
                i['sell'] = ""
                final_list.append(i)
        return(final_list)


class true_range:
    def __init__(self,list_of_dictionaries):
        self.list_of_dictionaries = list_of_dictionaries
        
    def signal_true_range(self, buy , sell):
        'add the buy/sell signal to every dictionary and put those in a new list when asking true range'
        final_list = []
        for i in range(len(self.list_of_dictionaries)):
            LoD = self.list_of_dictionaries
            if i == 0:
                LoD[0]['buy'] = ""
                LoD[0]['sell'] = ""
                final_list.append(LoD[0])
            else:
                true_range = LoD[i]['indicator']
                previous_day_close_price = LoD[i-1]['close']
                result = 100*(true_range/previous_day_close_price)
                if buy[0] == '>':
                    if result > float(buy[1:]):
                        LoD[i]['buy'] = 'BUY'
                    else:
                        LoD[i]['buy'] = ""
                    if sell[0] == '>':
                        if result > float(sell[1:]):
                            LoD[i]['sell'] = 'SELL'
                            final_list.append(LoD[i])
                        else:
                            dictionary['sell'] = ""
                            final_list.append(LoD[i])
                    elif sell[0] == '<':
                        if result < float(sell[1:]):
                            LoD[i]['sell'] = 'SELL'
                            final_list.append(LoD[i])
                        else:
                            LoD[i]['sell'] = ""
                            final_list.append(LoD[i])
                if buy[0] == '<':
                    if result < float(buy[1:]):
                        LoD[i]['buy'] = 'BUY'
                    else:
                        LoD[i]['buy'] = ""
                    if sell[0] == '>':
                        if result > float(sell[1:]):
                            LoD[i]['sell'] = 'SELL'
                            final_list.append(LoD[i])
                        else:
                            LoD[i]['sell'] = ""
                            final_list.append(LoD[i])
                    elif sell[0] == '<':
                        if result < float(sell[1:]):
                            LoD[i]['sell'] = 'SELL'
                            final_list.append(LoD[i])
                        else:
                            LoD[i]['sell'] = ""
                            final_list.append(LoD[i])
        return final_list
                    
'''
    def signal_simple_volume(self):
        final_list = []
        days_not_count = int(self.date) - 1
        LoD = self.list_of_dictionaries
        observed_days = LoD[int(self.date):]
        
        for i in range(days_not_count):
            LoD[i]['buy'] = ""
            LoD[i]['sell'] = ""
            final_list.append(LoD[i])

        for a in LoD[days_not_count:]:

            order = LoD.index(a)
            previous_one = LoD[order-1]
            if type(previous_one['indicator'])== float:
                if a['volume'] > a['indicator'] and previous_one['volume'] < previous_one['indicator']:
                    a['buy'] = 'BUY'
                    a['sell'] = ''
                    final_list.append(a)
                elif a['volume'] < a['indicator'] and previous_one['volume'] > previous_one['indicator']:
                    a['buy'] = ''
                    a['sell'] = 'SELL'
                    final_list.append(a)
                else:
                    a['buy'] = ""
                    a['sell'] = ""
                    final_list.append(a)
            else:
                a['buy'] = ""
                a['sell'] = ""
                final_list.append(a)
        return(final_list)

    def signal_directional_indicator_volume(self,buy,sell):
        final_list = []
        days_not_count = int(self.date) - 1
        LoD = self.list_of_dictionaries

        for i in LoD[:1]:
            LoD[0]['buy'] = ""
            LoD[0]['sell'] = ""
            final_list.append(LoD[0])

        for i in LoD[1:]:
            order = LoD.index(i)
            if LoD[order]['indicator'] > int(buy) and int(buy) > LoD[order-1]['indicator']:
                i['buy']= 'BUY'
                i['sell'] = ""
                final_list.append(i)
            elif LoD[order]['indicator'] < int(sell) and int(sell) < LoD[order-1]['indicator']:
                i['buy'] = ""
                i['sell'] = 'SELL'
                final_list.append(i)
            else:
                i['buy'] = ""
                i['sell'] = ""
                final_list.append(i)
        return(final_list)
'''
