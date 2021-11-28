import urllib.parse

safe_string = urllib.parse.quote_plus('')
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


def str_in_dict(input_question, input_dict):
    while True:
        input_string = input(input_question).lower().strip()

        if input_string in input_dict:
            break
        else:
            print("--------------------\nInvalid selection!\n--------------------")

    return input_string


def int_input(text):
    while True:
        try:
            input_int = int(input(text))
            break
        except ValueError:
            print("--------------------\nInvalid selection!\n--------------------")
    return input_int


def build_willhaben_url():
    while True:
        global uk
        mp_first_under = input("Do you want to choose a subcategory? Y - Yes or N - No\n").lower()

        if mp_first_under == "y":
            while True:
                mp_user_choice_uc = int_input("Choose a subcategory:\n"
                                              "0. Antiquitäten / Kunst\n"
                                              "1. Kameras / TV / Multimedia\n"
                                              "2. Baby / Kind\n"
                                              "3. KFZ-Zubehör / Motorradteile\n"
                                              "4. Beauty / Gesundheit / Wellness\n"
                                              "5. Mode / Accessoires\n"
                                              "6. Boote / Yachten / Jetskis\n"
                                              "7. Smartphones / Telefonie\n"
                                              "8. Bücher / Filme / Musik\n"
                                              "9. Spielen / Spielzeug\n"
                                              "10. Computer / Software\n"
                                              "11. Sport / Sportgeräte\n"
                                              "12. Dienstleistungen\n"
                                              "13. Tiere / Tierbedarf\n"
                                              "14. Freizeit / Instrumente / Kulinarik\n"
                                              "15. Uhren / Schmuck\n"
                                              "16. Games / Konsolen\n"
                                              "17. Wohnen / Haushalt / Gastronomie\n"
                                              "18. Haus / Garten / Werkstatt\n"
                                              "19. To give away Free\n")

                if mp_user_choice_uc in range(20):
                    uk = mp_user_choice_uc
                    break
                else:
                    print("--------------------\nInvalid selection!\n--------------------")

            break

        elif mp_first_under == "n":
            uk = ""
            break
        else:
            print("--------------------\nInvalid selection!\n--------------------")

    while True:
        keyword = urllib.parse.quote_plus(input("Select keyword:\n").strip())
        if not keyword:
            kw_rq = input("Do you want to grab products without a keyword? Y - No Keyword N - Choose Keyword\n").lower()
            if kw_rq == "y":
                break
            elif kw_rq != "y" and kw_rq != "n":
                print("--------------------\nInvalid selection!\n--------------------")
        else:
            break

    types = {"d": "&ISPRIVATE=1", "h": "&ISPRIVATE=0", "b": ""}
    typ = str_in_dict("By whom should products be grabbed?\nD - Private dealers\nH - Business Dealers\nB - Both\n",
                      types)

    if uk == 20:
        url = "https://www.willhaben.at/iad/kaufen-und-verkaufen/zu-verschenken/marktplatz"  f"?rows=100" + f"&keyword={keyword}"
    else:
        while True:
            minimum_price = int_input("Minimum price:\n")
            maximum_price = int_input("Maximum price:\n")
            if minimum_price > maximum_price:
                print(
                    "---------------------------------------------------\nMinimum price cannot be higher than maximum price!\n---------------------------------------------------")

            else:
                break

        if uk != "":
            url = url_base + menu["links"][str(uk)] + f"?PRICE_FROM={minimum_price}" + f"{types[typ]}" + f"&keyword={keyword}" + f"&PRICE_TO={maximum_price}" + f"&rows=25"
        else:
            url = url_base + f"?PRICE_FROM={minimum_price}" + f"{types[typ]}" + f"&keyword={keyword}" + f"&PRICE_TO={maximum_price}" + "&rows=25"

    return url


x = build_willhaben_url()
print(x)
