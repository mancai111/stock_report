class true_range:
    def __init__(self, list_of_dictionaries):
        self.list_of_dictionaries = list_of_dictionaries

    def calculate_true_range(self):
        'add true range to every dictionary and return new list of updated dictionaries'
        new_list = []
        for i in range(len(self.list_of_dictionaries)):
            LoD = self.list_of_dictionaries
            if i == 0:
                LoD[0]['indicator'] = ""
                new_list.append(LoD[0])
            else:
                today_high_price = LoD[i]['high']
                today_low_price = LoD[i]['low']
                previous_day_close_price = LoD[i-1]['close']
                       
                if previous_day_close_price > today_high_price:
                    LoD[i]['indicator'] = previous_day_close_price - today_low_price
                    new_list.append(LoD[i])
                       
                elif previous_day_close_price < today_low_price:
                    LoD[i]['indicator'] = today_high_price - previous_day_close_price
                    new_list.append(LoD[i])
                else:
                    LoD[i]['indicator'] = today_high_price-today_low_price
                    new_list.append(LoD[i])
        return(new_list)





class simple_moving: 
    def __init__(self, list_of_dictionaries, date):
        self.list_of_dictionaries = list_of_dictionaries
        self.date = date
        
    def calculate_simple_moving_price_volume(self,key):
        'add simple moving price/volume average to every dictionary and return new list of updated dictionaries'
        new_list = []
        days_not_count = int(self.date) - 1
        LoD = self.list_of_dictionaries
        observed_days = LoD[int(self.date):]

        
        for i in range(days_not_count):
            LoD[i]['indicator'] = ""
            new_list.append(LoD[i])


        for n in LoD[days_not_count:]:
            order = LoD.index(n)
            total_close_price_volume = 0
            for close in LoD[order-days_not_count:(order+1)]: #
                total_close_price_volume += close[key]
            LoD[order]['indicator'] = (total_close_price_volume/int(self.date))
            new_list.append(LoD[order])
        return(new_list)




                


                
class directional_indicator:
    def __init__(self,list_of_dictionaries,date):
        self.list_of_dictionaries = list_of_dictionaries
        self.date = date

    def calculate_directional_price_volume(self, key):
        'add directional price/volume to every dictionary and return new list of updated dictionaries'
        new_list = []
        LoD = self.list_of_dictionaries
        days_not_count = int(self.date) - 1

        for i in LoD[:days_not_count]:
            order = LoD.index(i)
            up = 0
            down = 0
            if order == 0:
                i['indicator'] = 0
                new_list.append(i)
            else:
                for a in LoD[:order]:
                    if a[key] < LoD[LoD.index(a)+1][key]:
                        up+=1
                    else:
                        pass
                for a in LoD[:order]:
                    if a[key] > LoD[LoD.index(a)+1][key]:
                        down +=1
                    else:
                        pass
                total = up - down
                i['indicator'] = total
                new_list.append(i)
                
                     
        for i in LoD[days_not_count:]:
            order = LoD.index(i)
            up = 0
            down = 0
            for a in LoD[(order-days_not_count):order]:
                if a[key] < LoD[LoD.index(a)+1][key]:
                    up+=1
                else:
                    pass
            for a in LoD[(order-days_not_count):order]:
                if a[key] > LoD[LoD.index(a)+1][key]:
                    down += 1
                else:
                    pass
            total = up - down
            i['indicator'] = total
            new_list.append(i)
        return(new_list)
                
