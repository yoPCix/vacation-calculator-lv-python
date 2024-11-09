from datetime import date

Holidays = set([
    date(2019, 1, 1),
    date(2019, 4, 19),
    date(2019, 4, 21),
    date(2019, 4, 22),
    date(2019, 5, 1),
    date(2019, 5, 4),
    date(2019, 5, 6),
    date(2019, 6, 23),
    date(2019, 6, 24),
    date(2019, 11, 18),
    date(2019, 12, 24),
    date(2019, 12, 25),
    date(2019, 12, 26),
    date(2019, 12, 31),
    date(2020, 1, 1),
    date(2020, 4, 10),
    date(2020, 4, 12),
    date(2020, 4, 13),
    date(2020, 5, 1),
    date(2020, 5, 4),
    date(2020, 6, 23),
    date(2020, 6, 24),
    date(2020, 11, 18),
    date(2020, 12, 24),
    date(2020, 12, 25),
    date(2020, 12, 26),
    date(2020, 12, 31),
    date(2021, 1, 1),
    date(2021, 4, 2),
    date(2021, 4, 4),
    date(2021, 4, 5),
    date(2021, 5, 1),
    date(2021, 5, 4),
    date(2021, 6, 23),
    date(2021, 6, 24),
    date(2021, 11, 18),
    date(2021, 12, 24),
    date(2021, 12, 25),
    date(2021, 12, 26),
    date(2021, 12, 31),
    date(2022, 1, 1),
    date(2022, 4, 15),
    date(2022, 4, 17),
    date(2022, 4, 18),
    date(2022, 5, 1),
    date(2022, 5, 4),
    date(2022, 5, 8),
    date(2022, 6, 5),
    date(2022, 6, 23),
    date(2022, 6, 24),
    date(2022, 11, 18),
    date(2022, 12, 24),
    date(2022, 12, 25),
    date(2022, 12, 26),
    date(2022, 12, 31),
    date(2023, 1, 1),
    date(2023, 4, 7),
    date(2023, 4, 9),
    date(2023, 4, 10),
    date(2023, 5, 1),
    date(2023, 5, 4),
    date(2023, 5, 8),
    date(2023, 6, 5),
    date(2023, 6, 23),
    date(2023, 6, 24),
    date(2023, 11, 18),
    date(2023, 12, 24),
    date(2023, 12, 25),
    date(2023, 12, 26),
    date(2023, 12, 31),
    date(2024, 1, 1),
    date(2024, 3, 29),
    date(2024, 3, 31),
    date(2024, 4, 1),
    date(2024, 5, 1),
    date(2024, 5, 4),
    date(2024, 5, 6),
    date(2024, 5, 12),
    date(2024, 5, 19),
    date(2024, 6, 23),
    date(2024, 6, 24),
    date(2024, 11, 18),
    date(2024, 12, 24),
    date(2024, 12, 25),
    date(2024, 12, 26),
    date(2024, 12, 31),
    date(2025, 1, 1),
    date(2025, 4, 18),
    date(2025, 4, 20),
    date(2025, 4, 21),
    date(2025, 5, 1),
    date(2025, 5, 4),
    date(2025, 5, 5),
    date(2025, 5, 11),
    date(2025, 6, 8),
    date(2025, 6, 23),
    date(2025, 6, 24),
    date(2025, 11, 18),
    date(2025, 12, 24),
    date(2025, 12, 25),
    date(2025, 12, 26),
    date(2025, 12, 31),
    date(2026, 1, 1),
])


HoursPerMonth = {
    201901: 176,
    201902: 160,
    201903: 168,
    201904: 158,
    201905: 167,
    201906: 152,
    201907: 184,
    201908: 176,
    201909: 168,
    201910: 184,
    201911: 160,
    201912: 142,
    202001: 176,
    202002: 160,
    202003: 176,
    202004: 158,
    202005: 152,
    202006: 159,
    202007: 184,
    202008: 168,
    202009: 176,
    202010: 176,
    202011: 159,
    202012: 158,
    202101: 160,
    202102: 160,
    202103: 184,
    202104: 158,
    202105: 159,
    202106: 159,
    202107: 176,
    202108: 176,
    202109: 176,
    202110: 168,
    202111: 167,
    202112: 166,
    202201: 168,
    202202: 160,
    202203: 184,
    202204: 151,
    202205: 167,
    202206: 159,
    202207: 168,
    202208: 184,
    202209: 176,
    202210: 168,
    202211: 167,
    202212: 166,
    202301: 176,
    202302: 160,
    202303: 184,
    202304: 143,
    202305: 167,
    202306: 167,
    202307: 160,
    202308: 184,
    202309: 168,
    202310: 176,
    202311: 167,
    202312: 152,
    202401: 176,
    202402: 168,
    202403: 159,
    202404: 167,
    202405: 167,
    202406: 152,
    202407: 184,
    202408: 176,
    202409: 168,
    202410: 184,
    202411: 160,
    202412: 142,
    202501: 176,
    202502: 160,
    202503: 168,
    202504: 158,
    202505: 160,
    202506: 152,
    202507: 184,
    202508: 168,
    202509: 176,
    202510: 184,
    202511: 151,
    202512: 150,
    202601: 168
}