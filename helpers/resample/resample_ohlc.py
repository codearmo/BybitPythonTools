import pandas as pd

VALID_RESAMPLE_INTERVALS = ["1min", "5min", "15min", "30min", "h", "D", "W"]


def resample_bybit_ohlc(df: pd.DataFrame, new_interval: str) -> pd.DataFrame:
    if new_interval not in VALID_RESAMPLE_INTERVALS:
        raise ValueError(
            f"'{new_interval}' is not a valid interval. Must be one of {VALID_RESAMPLE_INTERVALS}."
        )
    agg_dict = {
        "open": "first",  # take the first price for new open
        "high": "max",  # take the max price for new high
        "low": "min",  # take the min price for new low
        "close": "last",  # take the last price for new close
        "volume": "sum",  # take sum over interval for new volume
        "turnover": "sum",  # take sum over interval for new turnover
    }
    return df.resample(new_interval).agg(agg_dict)
