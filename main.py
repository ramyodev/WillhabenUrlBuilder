import urllib.parse

url_base = "https://www.willhaben.at/iad/kaufen-und-verkaufen/marktplatz"
menu = {"1": "/kaufen-und-verkaufen",
        "links": {"1": "/antiquitaeten-kunst-6941", "2": "/kameras-tv-multimedia-6808", "3": "/baby-kind-3928",
                  "4": "/kfz-zubehoer-motorradteile-6142", "5": "/beauty-gesundheit-wellness-3076",
                  "6": "/mode-accessoires-3275", "7": "/boote-yachten-jetskis-5007823",
                  "8": "/smartphones-telefonie-2691",
                  "9": "/buecher-filme-musik-387", "10": "/spielen-spielzeug-5136", "11": "/computer-software-5824",
                  "12": "/sport-sportgeraete-4390", "13": "/dienstleistungen-537", "14": "/tiere-tierbedarf-4915",
                  "15": "/freizeit-instrumente-kulinarik-6462", "16": "/uhren-schmuck-2409",
                  "17": "/games-konsolen-2785", "18": "/wohnen-haushalt-gastronomie-5387",
                  "19": "/haus-garten-werkstatt-3541", "20": "/zu-verschenken/"}}
seller_types = {"d": "&ISPRIVATE=1", "h": "&ISPRIVATE=0", "b": ""}


def build_willhaben_url(keyword: str, category_id: int, seller_type: str, minimum_price: int = 0,
                        maximum_price: int = 10000, rows: str = 25) -> str:
    """

    :param keyword: (must not be url encoded)
    :param category_id: get id dict from lib.main.menu
    :param seller_type:
    :param minimum_price: min price to filter by, default is 0
    :param maximum_price: max price to filter by, default is 10000
    :param rows: only user predefined rows, default is 25
    :return: willhaben url
    """
    if category_id and str(category_id) in menu["links"]:
        url = url_base + menu["links"][str(category_id)]
    else:
        url = url_base

    url += "?PRICE_FROM=" + str(minimum_price)
    url += seller_types[seller_type]
    url += "&sellerType=" + seller_type
    url += "&keyword=" + urllib.parse.quote_plus(keyword)
    url += "&PRICE_TO=" + str(maximum_price)
    url += "&rows=" + str(rows)

    return url


x = build_willhaben_url("nvidia", 1, "d", 0, 10000, 25)
print(x)
