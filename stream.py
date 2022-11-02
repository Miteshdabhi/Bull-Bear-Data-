import yfinance as yf
import pandas_ta as ta
import pandas as pd
import numpy as np
import streamlit as st
import pandas as pd
import numpy as np
my_bar = st.progress(0)
st.header("Stock bullish")
timeframe = st.selectbox(
    'Timeframe of Stock',
    ('5m', '15m', '30m' , '1h'))
st.write('You selected:', timeframe)

tickerl = st.radio(
    "Select Stock List",
    ('Bank_Nifty', 'Nifty', 'All_Future'))


#stocks = ("ALKEM.NS APOLLOHOSP.NS	AARTIIND.NS	ABFRL.NS	ACC.NS	ADANIENT.NS	ADANIPORTS.NS	ALKEM.NS	AMARAJABAT.NS	APLLTD.NS	APOLLOHOSP.NS	APOLLOTYRE.NS	ASHOKLEY.NS	ASIANPAINT.NS	AUBANK.NS	AUROPHARMA.NS	AXISBANK.NS	BAJAJ-AUTO.NS	BAJAJFINSV.NS	BAJFINANCE.NS	BALKRISIND.NS	BANDHANBNK.NS	BANKBARODA.NS	BATAINDIA.NS	BEL.NS	BERGEPAINT.NS	BHARATFORG.NS	BHARTIARTL.NS	BHEL.NS	BIOCON.NS	BOSCHLTD.NS	BPCL.NS	BRITANNIA.NS	CANBK.NS	CHOLAFIN.NS	CIPLA.NS	COALINDIA.NS	COFORGE.NS	COLPAL.NS	CONCOR.NS	COROMANDEL.NS	CUB.NS	CUMMINSIND.NS	DABUR.NS	DEEPAKNTR.NS	DIVISLAB.NS	DLF.NS	DRREDDY.NS	EICHERMOT.NS	ESCORTS.NS	EXIDEIND.NS	FEDERALBNK.NS	GAIL.NS	GLENMARK.NS	GMRINFRA.NS	GODREJCP.NS	GODREJPROP.NS	GRANULES.NS	GRASIM.NS	GUJGASLTD.NS	HAVELLS.NS	HCLTECH.NS	HdfC.NS	HdfCAMC.NS	HdfCBANK.NS	HdfCLIFE.NS	HEROMOTOCO.NS	HINDALCO.NS	HINDPETRO.NS	HINDUNILVR.NS	IBULHSGFIN.NS	ICICIBANK.NS	ICICIGI.NS	ICICIPRULI.NS	IDEA.NS	IdfCFIRSTB.NS	IGL.NS	INDHOTEL.NS	INDIGO.NS	INDUSINDBK.NS	INDUSTOWER.NS	INFY.NS	IOC.NS	IRCTC.NS	ITC.NS	JINDALSTEL.NS	JSWSTEEL.NS	JUBLFOOD.NS	KOTAKBANK.NS	L&TFH.NS	LALPATHLAB.NS	LICHSGFIN.NS	LT.NS	LTI.NS	LTTS.NS	LUPIN.NS	M&M.NS	M&MFIN.NS	MANAPPURAM.NS	MARICO.NS	MARUTI.NS	MCDOWELL-N.NS	METROPOLIS.NS	MFSL.NS	MGL.NS	MINDTREE.NS	MPHASIS.NS	MRF.NS	MUTHOOTFIN.NS	NAM-INDIA.NS	NATIONALUM.NS	NAUKRI.NS	NAVINFLUOR.NS	NESTLEIND.NS	NMDC.NS	NTPC.NS	ONGC.NS	PAGEIND.NS	PEL.NS	PETRONET.NS	PFC.NS	PFIZER.NS	PIDILITIND.NS	PIIND.NS	PNB.NS	POWERGRID.NS	PVR.NS	RAMCOCEM.NS	RBLBANK.NS	RECLTD.NS	RELIANCE.NS	SAIL.NS	SBILIFE.NS	SBIN.NS	SHREECEM.NS	SIEMENS.NS	SRF.NS	SRTRANSFIN.NS	SUNPHARMA.NS	SUNTV.NS	TATACHEM.NS	TATACONSUM.NS	TATAMOTORS.NS	TATAPOWER.NS	TATASTEEL.NS	TCS.NS	TECHM.NS	TITAN.NS	TORNTPHARM.NS	TORNTPOWER.NS	TRENT.NS	TVSMOTOR.NS	UBL.NS	ULTRACEMCO.NS	UPL.NS	VEDL.NS	VOLTAS.NS	WIPRO.NS	ZEEL.NS	ASTRAL.NS	STAR.NS	CANFINHOME.NS	DIXON.NS	HAL.NS	IEX.NS	INDIAMART.NS	IPCALAB.NS	MCX.NS	OFSS.NS	POLYCAB.NS	SYNGENE.NS")
def stock():
        
    All_Future = ("ALKEM.NS APOLLOHOSP.NS		ABFRL.NS	ACC.NS	ADANIENT.NS	ADANIPORTS.NS	ALKEM.NS	AMARAJABAT.NS	APLLTD.NS	APOLLOHOSP.NS	APOLLOTYRE.NS	ASHOKLEY.NS	ASIANPAINT.NS	AUBANK.NS	AUROPHARMA.NS	AXISBANK.NS	BAJAJ-AUTO.NS	BAJAJFINSV.NS	BAJFINANCE.NS	BALKRISIND.NS	BANDHANBNK.NS	BANKBARODA.NS	BATAINDIA.NS	BEL.NS	BERGEPAINT.NS	BHARATFORG.NS	BHARTIARTL.NS	BHEL.NS	BIOCON.NS	BOSCHLTD.NS	BPCL.NS	BRITANNIA.NS	CANBK.NS	CHOLAFIN.NS	CIPLA.NS	COALINDIA.NS	COFORGE.NS	COLPAL.NS 	CONCOR.NS	COROMANDEL.NS	CUB.NS	CUMMINSIND.NS	DABUR.NS	DEEPAKNTR.NS	DIVISLAB.NS	DLF.NS	DRREDDY.NS	EICHERMOT.NS	ESCORTS.NS	EXIDEIND.NS	FEDERALBNK.NS	GAIL.NS	GLENMARK.NS	GMRINFRA.NS	GODREJCP.NS	GODREJPROP.NS	GRANULES.NS	GRASIM.NS	GUJGASLTD.NS	HAVELLS.NS	HCLTECH.NS	HdfC.NS	HdfCAMC.NS	HdfCBANK.NS	HdfCLIFE.NS	HEROMOTOCO.NS	HINDALCO.NS	HINDPETRO.NS	HINDUNILVR.NS	IBULHSGFIN.NS	ICICIBANK.NS	ICICIGI.NS	ICICIPRULI.NS	IDEA.NS	IdfCFIRSTB.NS	IGL.NS	INDHOTEL.NS	INDIGO.NS	INDUSINDBK.NS	INDUSTOWER.NS	INFY.NS	IOC.NS	IRCTC.NS	ITC.NS	JINDALSTEL.NS	JSWSTEEL.NS	JUBLFOOD.NS	KOTAKBANK.NS	L&TFH.NS 	LALPATHLAB.NS	LICHSGFIN.NS	LT.NS	LTI.NS	LTTS.NS	LUPIN.NS	M&M.NS	M&MFIN.NS	MANAPPURAM.NS	MARICO.NS	MARUTI.NS	MCDOWELL-N.NS	METROPOLIS.NS	MFSL.NS	MGL.NS	MINDTREE.NS	MPHASIS.NS	MRF.NS	MUTHOOTFIN.NS	NAM-INDIA.NS	NATIONALUM.NS	NAUKRI.NS	NAVINFLUOR.NS	NESTLEIND.NS	NMDC.NS	NTPC.NS	ONGC.NS	PAGEIND.NS	PEL.NS	PETRONET.NS	PFC.NS	PFIZER.NS	PIDILITIND.NS	PIIND.NS	PNB.NS	POWERGRID.NS	PVR.NS	RAMCOCEM.NS	RBLBANK.NS	RECLTD.NS	RELIANCE.NS	SAIL.NS	SBILIFE.NS	SBIN.NS	SHREECEM.NS	SIEMENS.NS	SRF.NS	SRTRANSFIN.NS	SUNPHARMA.NS	SUNTV.NS	TATACHEM.NS	TATACONSUM.NS	TATAMOTORS.NS	TATAPOWER.NS	TATASTEEL.NS	TCS.NS	TECHM.NS	TITAN.NS	TORNTPHARM.NS")
    Nifty = ("ADANIENT.NS	ADANIPORTS.NS	APOLLOHOSP.NS	ASIANPAINT.NS	AXISBANK.NS	BAJAJ-AUTO.NS	BAJFINANCE.NS	BAJAJFINSV.NS	BPCL.NS	BHARTIARTL.NS	BRITANNIA.NS	CIPLA.NS	COALINDIA.NS	DIVISLAB.NS	DRREDDY.NS	EICHERMOT.NS	GRASIM.NS	HCLTECH.NS	HDFCBANK.NS	HDFCLIFE.NS	HEROMOTOCO.NS	HINDALCO.NS	HINDUNILVR.NS	HDFC.NS	ICICIBANK.NS	ITC.NS	INDUSINDBK.NS	INFY.NS	JSWSTEEL.NS	KOTAKBANK.NS	LT.NS	M&M.NS	MARUTI.NS	NTPC.NS	NESTLEIND.NS	ONGC.NS	POWERGRID.NS	RELIANCE.NS	SBILIFE.NS	SBIN.NS	SUNPHARMA.NS	TCS.NS	TATACONSUM.NS	TATAMOTORS.NS	TATASTEEL.NS	TECHM.NS	TITAN.NS	UPL.NS	ULTRACEMCO.NS	WIPRO.NS")
    Bank_Nifty = ("AUBANK.NS	AXISBANK.NS	BANDHANBNK.NS	BANKBARODA.NS	FEDERALBNK.NS	HDFCBANK.NS	ICICIBANK.NS	IDFCFIRSTB.NS	INDUSINDBK.NS	KOTAKBANK.NS	PNB.NS	SBIN.NS")
    if tickerl=="All_Future":
        data = yf.download(All_Future,period="5d",interval=timeframe).dropna()
    elif tickerl=="Nifty":
        data = yf.download(Nifty,period="5d",interval=timeframe).dropna()
    else:
        data = yf.download(Bank_Nifty,period="5d",interval=timeframe).dropna()

    
    
    
    #data = yf.download(All_Future,period="5d",interval=timeframe).dropna()
    bdf = pd.DataFrame()
    sdf = pd.DataFrame()
    numa = 1
    for b in list(data.columns.levels[1]):
        a = pd.DataFrame()
        
        a["Stockname"] = b
        a["Close"] =  data['Close'][b]
        a["High"] = data["High"][b]
        a["Low"] = data["Low"][b]
        a["Volume"] = data["Volume"][b]
        a["Open"] = data["Open"][b]
        a["Close"] = data["Close"][b]
        hh = a["High"]
        ll = a["Low"]
        vv = a["Volume"]
        oo = a["Open"]
        cc = a["Close"]
        a["Stockname"] = b
        adx = ta.adx(high=a["High"],low=a["Low"],close=a["Close"],length=14)
        a["rsi"] = ta.rsi(high=a["High"],low=a["Low"],close=a["Close"],length=14)
        bb = ta.bbands(cc,length=20,std=1)
        a["vwap"] = ta.vwap(high=hh,low=ll,close=cc,volume=vv)

        a["adx"] = 0
        a["adx"] = adx["ADX_14"]
        a["+di"] = adx["DMP_14"]
        a["-di"] = adx["DMN_14"]
        a["bb-u"] = bb["BBU_20_1.0"]
        a["bb-m"] = bb["BBM_20_1.0"]
        a["bb-l"] = bb["BBL_20_1.0"]
        #a = a[-2:-1]

        a["bbsignal"] = np.where(((a["Open"] < a["bb-u"]) & (a["Close"] > a["bb-u"]) & (a["Close"] > a["vwap"]) & (a["+di"] > 25) & (a["rsi"] > 55)& (a["adx"] > 23)) ,"Buy","") 
        a["bbsell"] = np.where(((a["Open"] > a["bb-l"]) & (a["Close"] < a["bb-l"]) & (a["Close"] < a["vwap"]) & (a["-di"] > 25) & (a["rsi"] < 45)& (a["adx"] > 23)) ,"Sell","")
        buy_sig = a[a["bbsignal"]=="Buy"]
        sell_sig = a[a["bbsell"]=="Sell"]
        bappend = pd.DataFrame(buy_sig)
        bdf = bdf.append(bappend)
        sappend = pd.DataFrame(sell_sig)
        sdf = sdf.append(sappend)
        numa = numa + (100/len(data.columns.levels[1]))
        if numa > 100:
            numa = 100
        else:
            numa = numa
        my_bar.progress(int(numa))
    bdf = bdf.reset_index()
    bdf['Date'] = pd.to_datetime(bdf['Datetime']).dt.date
    bdf['Time'] = pd.to_datetime(bdf['Datetime']).dt.time
    #bdf = bdf[bdf["Date"]==max(bdf["Date"])]
    
    
    st.header("Stock Bullish")
    st.dataframe(bdf)
    st.header("Stock Bearish")
    st.dataframe(sdf)
if st.button('Run FIle'):
    stock()

    

#st.table(data)


