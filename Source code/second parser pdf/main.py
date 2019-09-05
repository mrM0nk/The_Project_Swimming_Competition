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


def get_date(content):  # получает дату event
    return content[4][4].split()[0]


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
        if ',' in string:
            string = string.replace('.', ':', 1)
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
    other = clean(string)
    lastname, other = other.lstrip().split(maxsplit=1)
    if other.split()[0].isdigit():
        firstname = None
    elif other.split()[2].isdigit():
        second_lastname, firstname, other = other.split(maxsplit=2)
        lastname = lastname + " " + second_lastname
    else:
        firstname, other = other.split(maxsplit=1)
    year_of_birth, other = other.lstrip().split(' ', maxsplit=1)
    year_of_birth = year_of_birth.strip('г.')
    if 'г.' in other:
        club, sep, other = other.lstrip().partition('г.')
        club = club.rstrip()
        club = club.rstrip(',')
        other = sep + other
    elif ',' in other:
        club, other = other.lstrip().split(',', 1)
    try:
        city, time, rang, _ = other.lstrip().split('  ', 3)
    except:
        city, time, other = other.lstrip().split('  ', 2)
        rang = ' '.join(other.split()[: -2])
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
        year_of_birth = int(year_of_birth)
    except:
        return Record()
    try:
        club, other = other.lstrip().split(',', 1)
    except:
        club, sep, other = other.lstrip().partition('г.')
        other = sep + other
    other = other.lstrip().split()
    date, _ = other[-1].lstrip().split('г', 1)
    city = ' '.join(other[0: -1])
    record = Record(first_name=firstname, last_name=listname, birth_year=year_of_birth, gender=gender,
                    club_name=club, club_city=city, record_time=time, record_date=date)
    return record


def get_additional_comp(string, date, stage, pool_city):
    distance, other = string.split('м', 1)
    try:
        style, category = other.split(':', 1)
    except:
        style, category = other.split('–', 1)
    gender = get_gender(string)
    comp = Competition(comp_date=date, comp_city=pool_city, distance=distance, style=style, group_name=category,
                       stage=stage, group_gender=gender)
    return comp


def get_gender(string):
    if "Девочки" in string or "Девушки" in string or "Женщины" in string or "Юниорки" in string:
        gender = "w"
    else:
        gender = "m"
    return gender


def determine_type(content):  # определяет тип фала pdf
    if 'ПРОТОКОЛ СОРЕВНОВАНИЙ' in content[0][6][4]:
        return True
    else:
        return False

def run_second_parser(content, **kwargs):

    def pars_header(page, **kwargs):
        stage = get_namber_stage(page[3][4].split()[0])
        third_row = page[4][4].split()
        date = third_row[0]
        city = "{} {}".format(third_row[1], third_row[2].rstrip(','))
        pool_name = ' '.join(third_row[3: -1])
        pool_size = third_row[-1].lstrip('(').rstrip(')').rstrip('м')
        pool = Pool(pool_name=pool_name, pool_city=city, pool_size=pool_size, pool_country=kwargs['country'])
        event = Event(name=kwargs['event_name'], save_format=kwargs['save_one_swim'], save_dir=kwargs['save_dir'])
        return event, pool, date, stage

    distance, style = None, None
    event, pool, date, stage = pars_header(page=content[0], **kwargs)
    flag_new_event, additional_heats = False, False
    for namb, page in enumerate(content):  # идем по страницам
        if flag_new_event:  # новый event, pool и date
            try:  # если нет даты, то конец документа
                new_date = get_date(page)
                if new_date != date:
                    event, pool, date, stage = pars_header(page, **kwargs)
                    flag_new_event = False  # перешли к следующему event
                else:
                    continue
            except:
                continue
        for i, element in enumerate(page):  # идем по элементам страницы
            if i in (0, 1, 2, 3, 4, 5, 6, 7) or element[-1] == 1 or len(element[4].strip()) < 3:  # эти элементы пропускаем
                continue
            if element[4].count('–') > 6 or 'Фамилия' in element[4]:
                continue
            if 'Рекорд' in element[4]:  # элемент с рекордом
                if element[4].count('-') + element[4].count('–') < 5 and element[2] > 400:
                    event.competition[-1].record = get_record(element[4], gender)
                continue
            if element[0] > 25 and 'судья' in element[4]:  # судья и секретарь
                judge, secretary, j = False, False, i
                if element[2] > 500:
                    judge = ' '.join(element[4].split()[-3:])
                while not all((judge, secretary)):
                    if page[j][0] > 300 and not judge:
                        judge = page[j][4].strip()
                    elif 'секретарь' in page[j][4]:
                        secretary = ' '.join(page[j][4].split()[-3:])
                    j += 1
                for comp in event.competition:  # обновляем атрибуты
                    comp.comp_chief_judge = judge
                    comp.comp_chief_secretary = secretary
                event.save_json(pool=pool)
                flag_new_event, additional_heats = True, False  # переходим к следующему event
                break
            if additional_heats and element[0] > 100 and element[0] < 300:  # получаем доп.competition
                new_comp = get_additional_comp(element[4], date, stage, pool.pool_city,)
                event.competition.append(new_comp)
                continue
            elif additional_heats and element[0] > 40 and element[0] <100:  # получаем результат доп.competition
                result = get_result(element[4], gender)
                event.competition[-1].add_result(result)
                continue
            elif element[0] > 185 and 'группа' not in element[4]:  # дистанция, стиль, дополнительные заплывы)
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
                                       stage=stage, group_name=group_name, group_gender=gender)
                event.competition.append(new_comp)
            elif (element[0] > 23 and element[0] < 34.5) or (element[0] > 35 and element[0] < 36):  # результаты
                result = get_result(element[4], gender)
                event.competition[-1].add_result(result)
            elif element[0] > 43.4 and element[0] < 43.7 and '\n' not in element[4]:  # результаты
                result = get_result(element[4], gender)
                event.competition[-1].add_result(result)


def run_first_parser(content, **kwargs):

    def pars_header(content, **kwargs):
        third_row = content[2][4].split()
        date = third_row[0]
        city = "{} {}".format(third_row[2], third_row[3][:-1])
        stage = get_namber_stage(content[1][4].split()[0])
        pool_name = third_row[4] + " " + third_row[5]
        str_size = third_row[-1].strip('(')
        str_size = str_size.strip(')')
        pool_size = int(str_size[: -1])
        pool = Pool(pool_name=pool_name, pool_city=city, pool_size=pool_size, pool_country=kwargs['country'])
        event = Event(name=kwargs['event_name'], save_format=kwargs['save_one_swim'], save_dir=kwargs['save_dir'])
        return event, pool, date, stage

    distance, style = None, None
    event, pool, date, stage = pars_header(content=content[0], **kwargs)
    flag_new_event, additional_heats = False, False
    for namb, page in enumerate(content):  # идем по страницам
        if flag_new_event:  # новый event, pool и date
            try:  # если нет даты, то конец документа
                new_date = page[2][4].split()[0]
            except:
                break
            if new_date != date:
                event, pool, date, stage = pars_header(page,  **kwargs)
                flag_new_event = False  # перешли к следующему event
            else:
                continue
        for i, element in enumerate(page):  # идем по элементам страницы
            if i in (0, 1, 3, 4, 5) or element[-1] == 1:  # эти элементы пропускаем
                continue
            if element[4].count('–') > 6 or 'Фамилия' in element[4]:
                continue
            if 'Рекорд ' in element[4] and element[2] > 400:  # элемент с рекордом
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
                new_comp = get_additional_comp(element[4], date, stage, pool.pool_city,)
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
                                       stage=stage, group_name=group_name, group_gender=gender)
                event.competition.append(new_comp)
            elif (element[0] > 32.2 and element[0] < 34) or (element[0] > 35 and element[0] < 36):  # результаты
                result = get_result(element[4], gender)
                event.competition[-1].add_result(result)
            elif element[0] > 43.4 and element[0] < 43.7 and '\n' not in element[4]:  # результаты
                result = get_result(element[4], gender)
                event.competition[-1].add_result(result)


if __name__ == "__main__":
    with open("config.json") as config_file:
        configs = json.loads(config_file.read())
    for config in configs['arr_pdf']:
        pdf = Pdf(config['file_name'])
        content = pdf.get_content()
        if determine_type(content):
            run_second_parser(content, **config)
        else:
            run_first_parser(content, **config)
