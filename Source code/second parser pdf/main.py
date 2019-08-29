from competition import *
from file_pdf import *


def get_discipline(string):
    distance, style = string.split('м ')
    return distance, style.strip()  # {"discipline": {"distance": distance, "style": style}}


def get_chief_judge(string):  # получает главного судью соревнований
    judge = string.split(' ', 5)[-1].strip()
    return judge


def get_chief_secretary(string):  # получает главного секреторя соревновани
    secretary = string.split(' ', 5)[-1].strip()
    return secretary


def get_namber_stage(string):  # получает номер этапа
    arr = ['этапы', 'I-й', 'II-й', 'III-й', 'IV-й', 'V-й', 'VI-й', 'VII-й', 'VIII-й', 'IX-й', 'X-й', 'XI-й', 'XII-й']
    return arr.index(string)


def pars_header(content):
    name = content[0][4].replace('\n', '').strip()
    third_row = content[2][4].split()
    date = third_row[0]
    city ="{} {}".format(third_row[2], third_row[3][:-1])
    stage = get_namber_stage(content[1][4].split()[0])
    pool_name = third_row[4] + " " + third_row[5]
    str_size = third_row[-1].strip('(')
    str_size = str_size.strip(')')
    pool_size = int(str_size[: -1])
    pool = Pool(pool_name=pool_name, pool_city=city, pool_size=pool_size)
    event = Event(name=name, stage=stage)
    return event, pool, date


def get_date(content):  # получает дату event
    return content[2][4].split()[0]


def get_group_name(content):
    name = content.split(':')[1]
    name = name.split()
    return ' '.join(name[1:])


def clean(string):
    if string[0] in ("0123456789-– "):
        string = string[1:]
        return clean(string)
    else:
        return string


def get_time(string):
    if any(map(str.isdigit, string)):
        string = string.replace('.', ':')
        string = string.replace(',', '.')
        if string.index('.') == 2:
            string = "00:00:" + string
        elif string.index('.') == 4:
            string = "00:0" + string
        elif string.index('.') == 5:
            string = "00:" + string
        return string, None
    else:
        return None, string


def get_result(string, gender):
    string = string.replace('\n', ' ')
    firstname, other = clean(string).split(' ', 1)
    lastname, other = other.lstrip().split(' ', 1)
    year_of_birth, other = other.lstrip().split(' ', 1)
    try:
        club, other = other.lstrip().split(',', 1)
    except:
        club, sep, other = other.lstrip().partition('г.')
        other = sep + other
    city, time, rang, _ = other.lstrip().split('  ', 3)
    time_res, disqualification = get_time(time)
    result = Result(lastname, firstname, year_of_birth, gender, club_name=club, club_city=city, result_time=time_res,
                    dsq=disqualification, start_rank=rang)
    return result


def get_record(string, gender):
    _, other = string.split(':', 1)
    time, other = other.lstrip().split(' ', 1)
    time, _ = get_time(time)
    listname, other = other.lstrip().split(' ', 1)
    firstname, other = other.lstrip().split(' ', 1)
    year_of_birth, other = other.lstrip().split(' ', 1)
    try:
        club, other = other.lstrip().split(',', 1)
    except:
        club, sep, other = other.lstrip().partition('г.')
        other = sep + other
    other = other.lstrip().split()
    date, _ = other[-1].lstrip().split('г', 1)
    city = ' '.join(other[0: -1])
    record = Record(first_name=firstname, last_name=listname, birth_year=int(year_of_birth), gender=gender,
                    club_name=club, club_city=city, record_time=time, record_date=date)
    return record


def get_additional_comp(string, date, pool_city):
    distance, other = string.split('м', 1)
    style, category = other.split(':', 1)
    gender = get_gender(string)
    comp = Competition(comp_date=date, comp_city=pool_city, distance=distance, style=style, group_name=category,
                       group_gender=gender)
    return comp


def get_gender(string):
    if "Девочки" in string or "Девушки" in string or "Женщины" in string or "Юниорки" in string:
        gender = "w"
    else:
        gender = "m"
    return gender


def parser(file_name):
    pdf = Pdf(file_name)
    content = pdf.get_content()
    distance, style = None, None
    event, pool, date = pars_header(content[0])
    flag_new_event, additional_heats = False, False
    for namb, page in enumerate(content):  # идем по страницам
        # for i in page:
            # print(i)
        if flag_new_event:  # новый event, pool и date
            try:  # если нет даты, то конец документа
                new_date = get_date(page)
            except:
                break
            if new_date != date:
                event, pool, date = pars_header(page)
                flag_new_event = False  # перешли к следующему event
            else:
                continue
        for i, element in enumerate(page):  # идем по элементам страницы
            if i in (0, 1, 3, 4, 5) or element[-1] == 1:  # эти элементы пропускаем
                continue
            if element[4].count('–') > 6 or 'Фамилия' in element[4]:
                continue
            if 'Рекорд' in element[4] and element[2] > 400:  # элемент с рекордом
                event.competition[-1].record = get_record(element[4], gender)
                continue
            if element[0] > 38 and element[0] < 39:  # судья и секретарь
                if 'судья' in element[4]:   # получаем главного судью соревнований
                    judge = get_chief_judge(element[4])
                    for comp in event.competition:  # обновляем атр
                        comp.comp_chief_judge = judge
                elif 'секретарь' in element[4]:   # получаем главного секреторя соревнований
                    secretary = get_chief_secretary(element[4])
                    for comp in event.competition:
                        comp.comp_chief_secretary = secretary
                    event.save_json(pool=pool)
                    flag_new_event, additional_heats = True, False  # переходим к следующему event
                else:
                    continue
            if additional_heats and element[0] > 100 and element[0] < 300:  # получаем доп.competition
                new_comp = get_additional_comp(element[4], date, pool.pool_city,)
                event.competition.append(new_comp)
                continue
            elif additional_heats and element[0] > 40 and element[0] <100:  # получаем результат доп.competition
                result = get_result(element[4], gender)
                event.competition[-1].add_result(result)
                continue
            elif element[0] > 200 and 'группа' not in element[4]:  # дистанция, стиль, дополнительные заплывы)
                if 'заплывы' in element[4]:  # дополнительные заплывы
                    additional_heats = True
                    continue
                elif '0м' in element[4]:  # distance, style
                    distance, style = get_discipline(element[4])
            elif element[0] > 185 and element[0] < 230:  # находит строку group
                group = element[4]
                gender = get_gender(group)
                group_name = get_group_name(group)
                new_comp = Competition(comp_date=date, comp_city=pool.pool_city, distance=distance, style=style,
                                       group_name=group_name, group_gender=gender)
                event.competition.append(new_comp)
            elif (element[0] > 32.2 and element[0] < 34) or (element[0] > 35 and element[0] < 36):  # результаты
                result = get_result(element[4], gender)
                event.competition[-1].add_result(result)
            elif element[0] > 43.4 and element[0] < 43.7 and '\n' not in element[4]:  # результаты
                result = get_result(element[4], gender)
                event.competition[-1].add_result(result)


if __name__ == "__main__":
    parser("2.pdf")