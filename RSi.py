from api import Client
client = Client()
import time
#login
client.login(11393978, Kokot123)
client.check_if_market_open([BITCOIN])
#client.open_trade('buy', BDE30, 0.1)
#client.get_trades()
trades = client.update_trades()
print(---------------------------------------)
trade_ids = [trade_id for trade_id in trades.keys()]
candle = 0
kurz = 0
kokot = 0
bolean = True
bolean2 = False
bolean3 = False
bolean4 = False
close = 0
dick = 0
dick2 = 0
typeoforder = None
takeprofit = None
typeoforder2 = None
takeprofit2 = None
stoploss = None
tradeforDE = []
tradeforUS = []
def truncate(n, decimals=0)
    multiplier = 10  decimals
    return int(n  multiplier)  multiplier

komodita = DE30
komodita2 = US500



while True
    while bolean
        print(1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111)
        candle = client.get_lastn_candle_history(komodita, 300, 24)
        # client.close_all_trades()
        print(candle[0])

        kurz = candle[23][close]
        sviecaposledna = client.get_lastn_candle_history(komodita, 300, 2)
        lastclose = sviecaposledna[0][close]
        kokot = client.get_lastn_candle_history(komodita, 60, 1)
        kurz2 = kokot[0]['close']
        import pandas as pd
        import numpy as np
        candles = [None]24
        candlescounter=0


        for i in range(24)
            candles[i] = candle[candlescounter][close]
            candlescounter+=1


        df = pd.DataFrame(
            {'close' candles})
        n = 14


        def rma(x, n, y0)
            a = (n - 1)  n
            ak = a  np.arange(len(x) - 1, -1, -1)
            return np.append(y0, np.cumsum(ak  x)  ak  n + y0  a  np.arange(1, len(x) + 1))


        df['change'] = df['close'].diff()
        df['gain'] = df.change.mask(df.change  0, 0.0)
        df['loss'] = -df.change.mask(df.change  0, -0.0)
        df.loc[n, 'avg_gain'] = rma(df.gain[n + 1].values, n, df.loc[n, 'gain'].mean())
        df.loc[n, 'avg_loss'] = rma(df.loss[n + 1].values, n, df.loc[n, 'loss'].mean())
        df['rs'] = df.avg_gain  df.avg_loss
        df['rsi_14'] = 100 - (100  (1 + df.rs))

        print(df.round(2))

        avgnarast = df.round(2)[avg_gain][22]
        avgpokles = df.round(2)[avg_loss][22]

        currentgain = kurz - lastclose
        curentloss = kurz - lastclose

        vrchny = float(avgnarast)  13
        vrchny = float(vrchny) + abs(float(currentgain))

        spodny = float(avgpokles)  13
        spodny = float(spodny) + abs(float(curentloss))

        spodnyzlomok = float(vrchny)  float(spodny)

        spodnyzlomok = float(spodnyzlomok) + 1

        celyzlomok = 100  float(spodnyzlomok)

        RSI2 = 100 - float(celyzlomok)

        print(RSI2)
        prva1 = 1  14
        prva = float(df.round(2)[gain][23])  float(prva1)
        druha1 = 1  14
        druha2 = 1 - float(druha1)
        druha = float(df.round(2)[avg_gain][22]  float(druha2))
        newavggain = float(prva) + float(druha)

        first1 = 1  14
        first = float(df.round(2)[loss][23])  float(first1)
        second1 = 1  14
        second2 = 1 - float(second1)
        second = float(df.round(2)[avg_loss][22]  float(second2))
        newavgloss = float(first) + float(second)

        RS2 = float(newavggain)  float(newavgloss)
        RS3 = float(RS2) + 1
        celazatvorka = 100  float(RS3)
        RSINEW = 100 - float(celazatvorka)
        stopkokot = 0
        print(RSINEW)

        IDs = [None]10
        nerealnytakeprofitbuy = 16000
        nerealnytakeprofitshort = 500
        #RSINEW = 80

        tradforDEcounter = 0

        if len(tradeforDE) == 0
            if RSINEW  31
                stopkokot = float(kurz2)  100
                stopkokot = float(stopkokot)  0.3
                stoploss = float(kurz2) - float(stopkokot)
                print(stoploss)
                stoploss = truncate(stoploss, 1)
                for x in range(5)

                    kkt = [trade_id for trade_id in trades.keys()]
                    client.open_trade('buy', komodita, 0.02, float(stoploss), nerealnytakeprofitbuy)
                    kkt2 = [trade_id for trade_id in trades.keys()]
                    letters = kkt2


                    def filterVowels(letter)
                        vowels = kkt
                        if (letter in vowels)
                            return False
                        else
                            return True


                    filteredVowels = filter(filterVowels, letters)
                    for vowel in filteredVowels
                        print(vowel)
                    tradeforDE.append(int(vowel))
                    print(tradeforDE)
                    tradforDEcounter += 1
                bolean = False
                bolean2 = True
                typeoforder = 1
                dick = 0
                print(tradeforDE)
            if RSINEW  69
                stopkokot = float(kurz2)  100
                stopkokot = float(stopkokot)  0.3
                stoploss = float(kurz2) + float(stopkokot)
                print(stoploss)
                stoploss = truncate(stoploss, 1)
                for x in range(5)
                    kkt = [trade_id for trade_id in trades.keys()]
                    client.open_trade('sell', komodita, 0.02, float(stoploss), nerealnytakeprofitshort)
                    print(stoploss,nerealnytakeprofitshort)
                    kkt2 = [trade_id for trade_id in trades.keys()]
                    letters = kkt2
                    def filterVowels(letter)
                        vowels = kkt
                        if (letter in vowels)
                            return False
                        else
                            return True
                    filteredVowels = filter(filterVowels, letters)
                    for vowel in filteredVowels
                        print(vowel)
                    tradeforDE.append(int(vowel))
                    print(tradeforDE)
                    tradforDEcounter += 1
                bolean = False
                bolean2 = True
                typeoforder = 0
                dick = 0
                print(tradeforDE)

        else
            bolean = False
            bolean2 = True


    while bolean2
        print(2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222)
        candle = client.get_lastn_candle_history(komodita, 300, 24)
        # client.close_all_trades()
        print(candle[0])
        trade_ids = [trade_id for trade_id in trades.keys()]
        kurz = candle[23][close]
        sviecaposledna = client.get_lastn_candle_history(komodita, 300, 2)
        lastclose = sviecaposledna[0][close]
        kokot = client.get_lastn_candle_history(komodita, 60, 1)
        kurz2 = kokot[0]['close']
        import pandas as pd
        import numpy as np

        candles = [None]  24
        candlescounter = 0

        for i in range(24)
            candles[i] = candle[candlescounter][close]
            candlescounter += 1

        df = pd.DataFrame(
            {'close' candles})
        n = 14


        def rma(x, n, y0)
            a = (n - 1)  n
            ak = a  np.arange(len(x) - 1, -1, -1)
            return np.append(y0, np.cumsum(ak  x)  ak  n + y0  a  np.arange(1, len(x) + 1))


        df['change'] = df['close'].diff()
        df['gain'] = df.change.mask(df.change  0, 0.0)
        df['loss'] = -df.change.mask(df.change  0, -0.0)
        df.loc[n, 'avg_gain'] = rma(df.gain[n + 1].values, n, df.loc[n, 'gain'].mean())
        df.loc[n, 'avg_loss'] = rma(df.loss[n + 1].values, n, df.loc[n, 'loss'].mean())
        df['rs'] = df.avg_gain  df.avg_loss
        df['rsi_14'] = 100 - (100  (1 + df.rs))

        print(df.round(2))

        avgnarast = df.round(2)[avg_gain][22]
        avgpokles = df.round(2)[avg_loss][22]
        currentgain = kurz - lastclose
        curentloss = kurz - lastclose
        vrchny = float(avgnarast)  13 + abs(float(currentgain))
        spodny = float(avgpokles)  13 + abs(float(curentloss))
        spodnyzlomok = float(vrchny)  float(spodny)+ 1
        RSI2 = 100 -  100  float(spodnyzlomok)
        print(RSI2)

        prva1 = 1  14
        prva = float(df.round(2)[gain][23])  float(prva1)
        druha2 = 1 - 1  14
        druha = float(df.round(2)[avg_gain][22]  float(druha2))
        newavggain = float(prva) + float(druha)

        first1 = 1  14
        first = float(df.round(2)[loss][23])  float(first1)
        second2 = 1 - 1  14
        second = float(df.round(2)[avg_loss][22]  float(second2))
        newavgloss = float(first) + float(second)

        RS3 = float(newavggain)  float(newavgloss) + 1
        RSINEW = 100 - 100  float(RS3)
        stopkokot = 0
        print(RSINEW)
        print(trade_ids)
        #RSINEW = int(input(Enter1))

        pole = [35, 40, 45, 50, 55]
        pole2 = [65, 60, 55, 50, 45]


        if len(tradeforDE)!=0
            if typeoforder == 1
                try
                    # if RSINEW  64
                    #   client.close_all_trades()
                    #  bolean2 = False
                    # bolean = True

                    if RSINEW  pole[dick]
                        client.close_trade(int(tradeforDE[0]))
                        tradeforDE.pop(0)
                        dick += 1
                        bolean2 = False
                        bolean3 = True
                    else
                        bolean2 = False
                        bolean3 = True
                except
                    print(DIck)
                    bolean2 = False
                    bolean3 = True


            elif typeoforder == 0
                try
                    # if RSINEW  34
                    #   client.close_all_trades()
                    #  bolean2 = False
                    # bolean = True

                    if RSINEW  pole2[dick]
                        client.close_trade(int(tradeforDE[0]))
                        tradeforDE.pop(0)
                        dick += 1
                        bolean2 = False
                        bolean3 = True

                    else
                        bolean2 = False
                        bolean3 = True


                except
                    print(DIck)
                    bolean2 = False
                    bolean3 = True

            else
                bolean2 = False
                bolean3 = True
        else
            bolean2 = False
            bolean3 = True




            # if len(client.get_trades()) == 0
            #   bolean2 = False
            #  bolean = True




    #-------------------------------------------------------------------------------

    while bolean3
        print(33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333)
        candle = client.get_lastn_candle_history(komodita2, 300, 24)
        # client.close_all_trades()
        print(candle[0])

        kurz = candle[23][close]
        sviecaposledna = client.get_lastn_candle_history(komodita2, 300, 2)
        lastclose = sviecaposledna[0][close]
        kokot = client.get_lastn_candle_history(komodita2, 60, 1)
        kurz2 = kokot[0]['close']
        import pandas as pd
        import numpy as np

        candles = [None]  24
        candlescounter = 0

        for i in range(24)
            candles[i] = candle[candlescounter][close]
            candlescounter += 1

        df = pd.DataFrame(
            {'close' candles})
        n = 14


        def rma(x, n, y0)
            a = (n - 1)  n
            ak = a  np.arange(len(x) - 1, -1, -1)
            return np.append(y0, np.cumsum(ak  x)  ak  n + y0  a  np.arange(1, len(x) + 1))


        df['change'] = df['close'].diff()
        df['gain'] = df.change.mask(df.change  0, 0.0)
        df['loss'] = -df.change.mask(df.change  0, -0.0)
        df.loc[n, 'avg_gain'] = rma(df.gain[n + 1].values, n, df.loc[n, 'gain'].mean())
        df.loc[n, 'avg_loss'] = rma(df.loss[n + 1].values, n, df.loc[n, 'loss'].mean())
        df['rs'] = df.avg_gain  df.avg_loss
        df['rsi_14'] = 100 - (100  (1 + df.rs))

        print(df.round(2))

        avgnarast = df.round(2)[avg_gain][22]
        avgpokles = df.round(2)[avg_loss][22]

        currentgain = kurz - lastclose
        curentloss = kurz - lastclose

        vrchny = float(avgnarast)  13
        vrchny = float(vrchny) + abs(float(currentgain))

        spodny = float(avgpokles)  13
        spodny = float(spodny) + abs(float(curentloss))

        spodnyzlomok = float(vrchny)  float(spodny)

        spodnyzlomok = float(spodnyzlomok) + 1

        celyzlomok = 100  float(spodnyzlomok)

        RSI2 = 100 - float(celyzlomok)

        print(RSI2)
        prva1 = 1  14
        prva = float(df.round(2)[gain][23])  float(prva1)
        druha1 = 1  14
        druha2 = 1 - float(druha1)
        druha = float(df.round(2)[avg_gain][22]  float(druha2))
        newavggain = float(prva) + float(druha)

        first1 = 1  14
        first = float(df.round(2)[loss][23])  float(first1)
        second1 = 1  14
        second2 = 1 - float(second1)
        second = float(df.round(2)[avg_loss][22]  float(second2))
        newavgloss = float(first) + float(second)

        RS2 = float(newavggain)  float(newavgloss)
        RS3 = float(RS2) + 1
        celazatvorka = 100  float(RS3)
        RSINEW = 100 - float(celazatvorka)
        stopkokot = 0
        print(RSINEW)

        nerealnytakeprofitbuy2 = 16000
        nerealnytakeprofitshort2 = 500
        #RSINEW = 20
        tradeforUScounter = 0
        if len(tradeforUS) == 0
            if RSINEW  31
                stopkokot = float(kurz2)  100
                stopkokot = float(stopkokot)  0.3
                stoploss = float(kurz2) - float(stopkokot)
                print(stoploss)
                stoploss = truncate(stoploss, 1)
                for x in range(5)

                    kkt = [trade_id for trade_id in trades.keys()]
                    client.open_trade('buy', komodita2, 0.02, float(stoploss), nerealnytakeprofitbuy2)
                    kkt2 = [trade_id for trade_id in trades.keys()]
                    letters = kkt2


                    def filterVowels(letter)
                        vowels = kkt
                        if (letter in vowels)
                            return False
                        else
                            return True


                    filteredVowels = filter(filterVowels, letters)
                    for vowel in filteredVowels
                        print(vowel)
                    tradeforUS.append(int(vowel))
                    print(tradeforUS)
                    tradeforUScounter += 1
                bolean = False
                bolean2 = True
                typeoforder2 = 1
                dick2 = 0

            if RSINEW  69
                stopkokot = float(kurz2)  100
                stopkokot = float(stopkokot)  0.3
                stoploss = float(kurz2) + float(stopkokot)
                print(stoploss)
                stoploss = truncate(stoploss, 1)
                for x in range(5)

                    kkt = [trade_id for trade_id in trades.keys()]
                    client.open_trade('sell', komodita2, 0.02, float(stoploss), nerealnytakeprofitshort2)
                    kkt2 = [trade_id for trade_id in trades.keys()]
                    letters = kkt2


                    def filterVowels(letter)
                        vowels = kkt
                        if (letter in vowels)
                            return False
                        else
                            return True


                    filteredVowels = filter(filterVowels, letters)
                    for vowel in filteredVowels
                        print(vowel)
                    tradeforUS.append(int(vowel))
                    print(tradeforUS)
                    tradeforUScounter += 1
                bolean = False
                bolean2 = True
                typeoforder2 = 0
                dick2 = 0

        else
            bolean3 = False
            bolean4 = True

    while bolean4
        print(44444444444444444444444444444444444444444444444444444444444444444444444444444444444444444)
        candle = client.get_lastn_candle_history(komodita2, 300, 24)
        # client.close_all_trades()
        print(candle[0])
        trade_ids = [trade_id for trade_id in trades.keys()]
        kurz = candle[23][close]
        sviecaposledna = client.get_lastn_candle_history(komodita2, 300, 2)
        lastclose = sviecaposledna[0][close]
        kokot = client.get_lastn_candle_history(komodita2, 60, 1)
        kurz2 = kokot[0]['close']
        import pandas as pd
        import numpy as np

        candles = [None]  24
        candlescounter = 0

        for i in range(24)
            candles[i] = candle[candlescounter][close]
            candlescounter += 1

        df = pd.DataFrame(
            {'close' candles})
        n = 14


        def rma(x, n, y0)
            a = (n - 1)  n
            ak = a  np.arange(len(x) - 1, -1, -1)
            return np.append(y0, np.cumsum(ak  x)  ak  n + y0  a  np.arange(1, len(x) + 1))


        df['change'] = df['close'].diff()
        df['gain'] = df.change.mask(df.change  0, 0.0)
        df['loss'] = -df.change.mask(df.change  0, -0.0)
        df.loc[n, 'avg_gain'] = rma(df.gain[n + 1].values, n, df.loc[n, 'gain'].mean())
        df.loc[n, 'avg_loss'] = rma(df.loss[n + 1].values, n, df.loc[n, 'loss'].mean())
        df['rs'] = df.avg_gain  df.avg_loss
        df['rsi_14'] = 100 - (100  (1 + df.rs))

        print(df.round(2))

        avgnarast = df.round(2)[avg_gain][22]
        avgpokles = df.round(2)[avg_loss][22]
        currentgain = kurz - lastclose
        curentloss = kurz - lastclose
        vrchny = float(avgnarast)  13 + abs(float(currentgain))
        spodny = float(avgpokles)  13 + abs(float(curentloss))
        spodnyzlomok = float(vrchny)  float(spodny) + 1
        RSI2 = 100 - 100  float(spodnyzlomok)
        print(RSI2)

        prva1 = 1  14
        prva = float(df.round(2)[gain][23])  float(prva1)
        druha2 = 1 - 1  14
        druha = float(df.round(2)[avg_gain][22]  float(druha2))
        newavggain = float(prva) + float(druha)

        first1 = 1  14
        first = float(df.round(2)[loss][23])  float(first1)
        second2 = 1 - 1  14
        second = float(df.round(2)[avg_loss][22]  float(second2))
        newavgloss = float(first) + float(second)

        RS3 = float(newavggain)  float(newavgloss) + 1
        RSINEW = 100 - 100  float(RS3)
        stopkokot = 0
        print(RSINEW)
        print(trade_ids)
        #RSINEW = int(input(Enter2))

        pole = [35, 40, 45, 50, 55]
        pole2 = [65, 60, 55, 50, 45]
        if len(tradeforUS)!=0
            print(kokot2)
            if typeoforder2 == 1
                print(kokot2)
                try
                    # if RSINEW  64
                    #   client.close_all_trades()
                    #  bolean2 = False
                    # bolean = True

                    if RSINEW  pole[dick2]
                        print(kokot2)
                        client.close_trade(int(tradeforUS[0]))
                        tradeforUS.pop(0)
                        dick2 += 1
                        bolean4 = False
                        bolean = True

                    else
                        bolean4 = False
                        bolean = True

                except
                    print(DIck)
                    bolean4 = False
                    bolean = True




            if typeoforder2 == 0
                try
                    # if RSINEW  34
                    #   client.close_all_trades()
                    #  bolean2 = False
                    # bolean = True

                    if RSINEW  pole2[dick2]
                        client.close_trade(int(tradeforUS[0]))
                        tradeforUS.pop(0)
                        dick2 += 1
                        bolean4 = False
                        bolean = True
                    else
                        bolean4 = False
                        bolean = True
                except
                    print(DIck)
                    bolean4 = False
                    bolean = True

        bolean=True
        bolean4=False




        #if len(client.get_trades()) == 0
         #   bolean2 = False
          #  bolean = True

        #if len(tradeforDE) != 0
         #   bolean = False

        #if len(tradeforDE) == 0
         #   bolean = True
        print(tradeforDE)



client.logout()