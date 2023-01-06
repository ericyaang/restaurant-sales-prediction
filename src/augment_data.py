import pandas as pd
from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO


def get_weather_data(url):
    resp = urlopen(url)
    myzip = ZipFile(BytesIO(resp.read()))
    files = myzip.infolist()
    _list = []
    for file in files:
        if file.filename.startswith("produkt_"):
            for line in myzip.open(file).readlines():
                _list.append(line.decode("utf-8").replace(" ", "").strip().split(";"))

    _df = pd.DataFrame(_list[1:], columns=_list[0])
    _df = _df[["MESS_DATUM", "NM", "RSK", "PM", "UPM", "SDK", "TMK", "FM"]]
    _df = _df.rename(
        columns={
            "MESS_DATUM": "date",
            "NM": "cloud_cover",
            "RSK": "precipitation",
            "PM": "pressure_msl",
            "UPM": "relative_humidity",
            "SDK": "sunshine",
            "TMK": "temperature",
            "FM": "wind_speed",
        }
    )
    _df["date"] = pd.to_datetime(_df["date"], format="%Y%m%d")
    return _df


weather_old = get_weather_data(
    "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/daily/kl/historical/tageswerte_KL_01975_19360101_20211231_hist.zip"
)
weather_recent = get_weather_data(
    "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/daily/kl/recent/tageswerte_KL_01975_akt.zip"
)

weather_data = pd.concat(
    [
        weather_old,
        weather_recent,
    ],
    axis=0,
    ignore_index=True,
).drop_duplicates(subset="Date", keep="last")

# run
weather_data = weather_data.set_index("date").loc[initial_date:final_date]
