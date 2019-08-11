from competition import *
from file_pdf import *


def get_pool(string):
    string = string.split(',')[1]
    start, end = string.index(' ('), string.index('м)')
    return Pool(title=string[1: start + 1], size=string[start + 1: end])

def get_discipline(string):
    distance, style = string.split('м ')
    return distance, style  # {"discipline": {"distance": distance, "style": style}}


def get_result(string, gender):

    def clean(string):
        if string[0] in ("0123456789-– "):
            string = string[1:]
            return clean(string)
        else:
            return string

    def get_time(string):
        if string in ("дискв", "неявка"):
            return None, string
        else:
            string = string.replace('.', ':')
            string = string.replace(',', '.')
            return string, None

    string = clean(string).split("  ")
    lastname, fistname = string[0].split()
    year_of_birth = string[1].strip()
    club_and_city = string[2].split(",")
    if len(club_and_city) == 1:
        club_and_city = club_and_city[0].split(" ", 1)
    club = club_and_city[0]
    city = club_and_city[1].split()[-1]
    time_res, disqualification = get_time(string[3])
    rang = string[4]
    result = Result(lastname, fistname, year_of_birth, gender, club=club, city=city, time=time_res,
                    disqualification=disqualification, rang=rang)
    return result



def parser(file_name):
    pdf = Pdf(file_name)
    content, event = pdf.get_content()
    print(event.get_attributes())
    new_competition, new_pool, distance, style, gender = None, None, None, None, None
    for namb, page in enumerate(content):
        if namb > 2:
            break
        for i, element in enumerate(page):
            if i in (0, 1, 3, 4, 5):
                continue
            elif i == 2:
                new_pool = get_pool(element[4])
            elif i == 6 and element[0] > 200:
                distance, style = get_discipline(element[4])
            elif element[0] > 185 and element[0] < 230:
                if new_competition is not None:
                    new_competition.save_json()
                    # for i in new_competition.get_attributes():
                    #     print(i)
                category = element[4]
                if "Девочки" in category or "Девушки" in category or "Женщины" in category or "Юниорки" in category:
                    gender = "famale"
                else:
                    gender = "male"
                new_competition = Competition(event, new_pool, category, style, distance)
            elif (element[0] > 32.2 and element[0] < 34) or (element[0] > 35 and element[0] < 36):  # результаты
                result = get_result(element[4], gender)
                new_competition.add_result(result)
            elif element[0] > 43.4 and element[0] < 43.7 and '\n' not in element[4]:  # результаты
                result = get_result(element[4], gender)
                new_competition.add_result(result)
        if namb == 9:
            break


if __name__ == "__main__":
    parser("1.pdf")