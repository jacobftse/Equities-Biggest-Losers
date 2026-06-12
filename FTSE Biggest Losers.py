import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import lxml 

# FTSE 100 tickers (Yahoo format)

import pandas as pd
import requests

import pandas as pd
import requests
from io import StringIO

url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

print(response)

html = StringIO(response.text)
df = pd.read_html(html)[0]

tickers = df["Symbol"].tolist()
sp500 = [t.replace(".", "-") for t in tickers]

print(sp500)





ftse_350_tickers = [
"3IN.L","FOUR.L","AAS.L","ABDN.L","ASL.L","AEP.L","ALFA.L","ATT.L","AO.L","APN.L",
"ASHM.L","AIE.L","AML.L","ATYM.L","AGT.L","AVON.L","BME.L","BGFD.L","USA.L","BBY.L",
"BCG.L","BAG.L","AJB.L","BWY.L","BHMG.L","BYG.L","BPCR.L","BRGE.L","BRSC.L","BRWM.L",
"BSIF.L","BOY.L","BREE.L","BPT.L","BUT.L","BYIT.L","CCR.L","CLDN.L","CGT.L","CWR.L",
"CHG.L","CSN.L","CHRY.L","CTY.L","CKN.L","CBG.L","CMCX.L","COA.L","CCC.L","COST.L",
"CWK.L","CURY.L","CVSG.L","DLN.L","DSCV.L","DOM.L","DRX.L","DOCS.L","DNLM.L","EZJ.L",
"EDIN.L","EWI.L","ELM.L","ENOG.L","ESCT.L","EWG.L","FCSS.L","FEML.L","FEV.L","FSV.L",
"FGT.L","FGP.L","FGEN.L","FSG.L","FRAS.L","FCH.L","GFRD.L","GAMA.L","GBG.L","GCP.L",
"GEN.L","GNS.L","GSCT.L","GDWN.L","GFTU.L","GRI.L","GPE.L","UKW.L","GNC.L","GRG.L",
"HMSO.L","HBR.L","HVPE.L","HWG.L","HAS.L","HTWS.L","HFEL.L","HSL.L","HRI.L","HGT.L",
"HICL.L","HIK.L","HILS.L","HFG.L","HOC.L","BOWL.L","HTG.L","IBST.L","ICGT.L","IEM.L",
"INCH.L","IHP.L","IPF.L","INPP.L","IWG.L","IAD.L","INVP.L","IPO.L","ITH.L","ITV.L",
"JMAT.L","JSG.L","JAM.L","JCH.L","JEMI.L","JMGI.L","JEDT.L","JEGI.L","JGGI.L","JIGI.L",
"JFJ.L","JTC.L","JUP.L","KNOS.L","KLR.L","KIE.L","LRE.L","LWDB.L","EMG.L","MSLH.L",
"MEGP.L","MRC.L","MRCH.L","MTRO.L","MAB.L","MTO.L","GROW.L","MNKS.L","MONY.L","MOON.L",
"MGAM.L","MGNS.L","MUT.L","MYI.L","NBPE.L","NCC.L","N91.L","NAS.L","OCI.L","OCDO.L",
"OSB.L","OXB.L","OXIG.L","ONT.L","PHI.L","PAGE.L","PAF.L","PINT.L","PIN.L","PAG.L",
"PEY.L","PPET.L","PNN.L","PNL.L","PETS.L","PTEC.L","PLUS.L","PCGH.L","POLN.L","PPH.L",
"PFD.L","PHP.L","PRN.L","QQ.L","QLT.L","RNK.L","RPI.L","RAT.L","RSW.L","RHIM.L",
"RCP.L","ROR.L","RS1.L","RTW.L","RICA.L","SAFE.L","SAGA.L","SVS.L","MNTN.L","ATR.L",
"SDP.L","SOI.L","SAIN.L","SEIT.L","SNR.L","SEQI.L","SRP.L","SHC.L","SHAW.L","SRE.L",
"SCT.L","SPI.L","SSPG.L","SUPR.L","SYNC.L","THRL.L","TATE.L","TW.L","TBCG.L","TEP.L",
"TMPL.L","TEM.L","TRIG.L","THG.L","TCAP.L","TRN.L","TPK.L","TRY.L","TRST.L","TFIF.L",
"UTG.L","UEM.L","VSVS.L","VCT.L","VEIL.L","VOF.L","VTY.L","FAN.L","WOSG.L","JDW.L",
"SMWH.L","WIX.L","WIZZ.L","WKP.L","WWH.L","WPP.L","XPP.L","XPS.L","ZIG.L",
"III.L","ADM.L","AAF.L","ALW.L","AAL.L","ANTO.L","ABF.L","AZN.L","AUTO.L","AV.L",
"BAB.L","BA.L","BARC.L","BTRW.L","BEZ.L","BKG.L","BP.L","BATS.L","BLND.L","BT.A.L",
"BNZL.L","BRBY.L","CNA.L","CCEP.L","CCH.L","CPG.L","CTEC.L","CRDA.L","DCC.L","DGE.L",
"DPLM.L","EDV.L","ENT.L","EXPN.L","FCIT.L","FRES.L","GAW.L","GLEN.L","GSK.L","HLN.L",
"HLMA.L","HSX.L","HWDN.L","HSBA.L","ICG.L","IGG.L","IHG.L","IMI.L","IMB.L","INF.L",
"IAG.L","ITRK.L","JD.L","BGEO.L","KGF.L","LAND.L","LGEN.L","LLOY.L","LMP.L","LSEG.L",
"MNG.L","MKS.L","MRO.L","MTLN.L","MNDI.L","NG.L","NWG.L","NXT.L","PSON.L","PSH.L",
"PSN.L","PCT.L","PRU.L","RKT.L","REL.L","RTO.L","RMV.L","RIO.L","RR.L","SGE.L",
"SBRY.L","SDR.L","SMT.L","SGRO.L","SVT.L","SHEL.L","SMIN.L","SN.L","SPX.L","SSE.L",
"STAN.L","SDLF.L","STJ.L","TSCO.L","BBOX.L","ULVR.L","UU.L","VOD.L","WEIR.L","WTB.L"
]

# Date range
end_date = datetime.today()
start_date = end_date - timedelta(days=5*365)

# Download adjusted close prices
data = yf.download(
    ftse_350_tickers,
    start=start_date,
    end=end_date,
    auto_adjust=False,
    progress=False
)

# DEBUG: Uncomment to inspect structure
# print(data.columns)

returns = {}

for ticker in ftse_350_tickers:
    try:
        prices = data["Adj Close"][ticker].dropna()
        if len(prices) < 2:
            continue

        pct_return = (prices.iloc[-1] / prices.iloc[0] - 1) * 100
        returns[ticker.replace(".L", "")] = pct_return
    except KeyError:
        print(f"Missing data for {ticker}")

# Create DataFrame
returns_df = pd.DataFrame.from_dict(
    returns,
    orient="index",
    columns=["5-Year Return (%)"]
).sort_values("5-Year Return (%)")

# Select biggest losers
losers = returns_df.head(15)

# Plot
plt.figure(figsize=(15, 6))
plt.barh(losers.index, losers["5-Year Return (%)"])
plt.xlabel("5-Year Return (%)")
plt.title("UK Equities – Biggest Losers (Last 5 Years)")
plt.grid(axis="x", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()
