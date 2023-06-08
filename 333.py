import requests
a = input('Введите ИНН: ')
b = input('Введите ИНН: ')
qq1 = []
qq2 = []
qq1.append(a)
qq2.append(b)
s1 = []
s2 = []
# 6623134596
# 6623141177
def qq33():
    for k in range(len(qq1)):
        query16 = {
            "inn": qq1[k]
        }
        response16 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/details', json=query16)
        response16 = response16.json()
        for i in response16['message']['founders']:
            if 'innfl' in i:
                s1.append(i['innfl'])
            elif 'inn' in i:
                query17 = {
                    "inn": i['inn']
                }
                response17 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/details', json=query17)
                response17 = response17.json()

                for t in response17['message']['founders']:
                    if 'innfl' in t:
                        if t['innfl'] not in s1:
                            s1.append(t['innfl'])

                for t in response17['message']['foundersH']:
                    if 'innfl' in t:
                        if t['innfl'] not in s1:
                            s1.append(t['innfl'])

                for t in response17['message']['directors']:
                    if t['innfl'] not in s1:
                        s1.append(t['innfl'])

                for t in response17['message']['directorsH']:
                    if t['innfl'] not in s1:
                        s1.append(t['innfl'])

        for i in response16['message']['foundersH']:
            if 'innfl' in i:
                if i['innfl'] not in s1:
                    s1.append(i['innfl'])

                query18 = {
                         "inn": i['inn']
                     }
                response18 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/details', json=query18)
                response18 = response18.json()
                for t in response18['message']['founders']:
                    if 'innfl' in t:
                        if t['innfl'] not in s1:
                            s1.append(t['innfl'])

                for t in response18['message']['foundersH']:
                    if 'innfl' in t:
                        if t['innfl'] not in s1:
                            s1.append(t['innfl'])

                for t in response18['message']['directors']:
                    if t['innfl'] not in s1:
                        s1.append(t['innfl'])

                for t in response18['message']['directorsH']:
                    if t['innfl'] not in s1:
                        s1.append(t['innfl'])

        for i in response16['message']['directors']:
            if i['innfl'] not in s1:
                s1.append(i['innfl'])

        for i in response16['message']['directorsH']:
            if i['innfl'] not in s1:
                s1.append(i['innfl'])

def ww33():
    for k in range(len(qq2)):
        query19 = {
            "inn": qq2[k]
        }
        response19 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/details', json=query19)
        response19 = response19.json()
        for i in response19['message']['founders']:
            if 'innfl' in i:
                if i['innfl'] not in s2:
                    s2.append(i['innfl'])
            elif 'inn' in i:
                query20 = {
                    "inn": i['inn']
                }
                response20 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/details', json=query20)
                response20 = response20.json()
                for t in response20['message']['founders']:
                    if 'innfl' in t:
                        if t['innfl'] not in s2:
                            s2.append(t['innfl'])
                for t in response20['message']['foundersH']:
                    if 'innfl' in t:
                        if t['innfl'] not in s2:
                            s2.append(t['innfl'])

                for t in response20['message']['directors']:
                    if t['innfl'] not in s2:
                        s2.append(t['innfl'])
                for t in response20['message']['directorsH']:
                    if t['innfl'] not in s2:
                        s2.append(t['innfl'])

        for i in response20['message']['foundersH']:
            if 'innfl' in i:
                if i['innfl'] not in s2:
                    s2.append(i['innfl'])
            elif 'inn' in i:
                query21 = {
                    "inn": i['inn']
                }
                response21 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/details', json=query21)
                response21 = response21.json()
                for t in response21['message']['founders']:
                    if 'innfl' in t:
                        if t['innfl'] not in s2:
                            s2.append(t['innfl'])
                for t in response21['message']['foundersH']:
                    if 'innfl' in t:
                        if t['innfl'] not in s2:
                            s2.append(t['innfl'])
                for t in response21['message']['directors']:
                    if t['innfl'] not in s2:
                        s2.append(t['innfl'])
                for t in response21['message']['directorsH']:
                    if t['innfl'] not in s2:
                        s2.append(t['innfl'])

        for i in response19['message']['directors']:
            if i['innfl'] not in s2:
                s2.append(i['innfl'])

        for i in response19['message']['directorsH']:
            if i['innfl'] not in s2:
                s2.append(i['innfl'])


def ee33():
    for o in s1:
        query22 = {
            "inn": o
        }
        response22 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/person', json=query22)
        response22 = response22.json()
        for i in response22['message']['data']:
            if len(i['inn']) == 12:
                if i['inn'] not in s1:
                    s1.append(i['inn'])
            else:
                if i['inn'] not in qq1:
                    qq1.append(i['inn'])
    print(qq1)
def rr33():
    for o in s2:
        query23 = {
            "inn": o
        }
        response23 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/person', json=query23)
        response23 = response23.json()
        for i in response23['message']['data']:
            if len(i['inn']) == 12:
                if i['inn'] not in s2:
                    s2.append(i['inn'])
            else:
                if i['inn'] not in qq2:
                    qq2.append(i['inn'])
    print(qq2)

    

    
 def qq44():
        for k in range(len(qq1)):
            query24 = {
                "inn": qq1[k]
            }
            response24 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/details', json=query24)
            response24 = response24.json()
            for i in response24['message']['founders']:
                if 'innfl' in i:
                    s1.append(i['innfl'])
                elif 'inn' in i:
                    query25 = {
                        "inn": i['inn']
                    }
                    response25 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/details', json=query25)
                    response25 = response25.json()

                    for t in response25['message']['founders']:
                        if 'innfl' in t:
                            if t['innfl'] not in s1:
                                s1.append(t['innfl'])

                    for t in response25['message']['foundersH']:
                        if 'innfl' in t:
                            if t['innfl'] not in s1:
                                s1.append(t['innfl'])

                    for t in response25['message']['directors']:
                        if t['innfl'] not in s1:
                            s1.append(t['innfl'])

                    for t in response25['message']['directorsH']:
                        if t['innfl'] not in s1:
                            s1.append(t['innfl'])

            for i in response24['message']['foundersH']:
                if 'innfl' in i:
                    if i['innfl'] not in s1:
                        s1.append(i['innfl'])

                    query26 = {
                            "inn": i['inn']
                        }
                    response26 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/details', json=query26)
                    response26 = response26.json()
                    for t in response26['message']['founders']:
                        if 'innfl' in t:
                            if t['innfl'] not in s1:
                                s1.append(t['innfl'])

                    for t in response26['message']['foundersH']:
                        if 'innfl' in t:
                            if t['innfl'] not in s1:
                                s1.append(t['innfl'])

                    for t in response26['message']['directors']:
                        if t['innfl'] not in s1:
                            s1.append(t['innfl'])

                    for t in response26['message']['directorsH']:
                        if t['innfl'] not in s1:
                            s1.append(t['innfl'])

            for i in response24['message']['directors']:
                if i['innfl'] not in s1:
                    s1.append(i['innfl'])

            for i in response24['message']['directorsH']:
                if i['innfl'] not in s1:
                    s1.append(i['innfl'])

    def ww44():
        for k in range(len(qq2)):
            query27 = {
                "inn": qq2[k]
            }
            response27 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/details', json=query27)
            response27 = response27.json()
            for i in response27['message']['founders']:
                if 'innfl' in i:
                    if i['innfl'] not in s2:
                        s2.append(i['innfl'])
                elif 'inn' in i:
                    query278 = {
                        "inn": i['inn']
                    }
                    response28 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/details', json=query28)
                    response28 = response28.json()
                    for t in response28['message']['founders']:
                        if 'innfl' in t:
                            if t['innfl'] not in s2:
                                s2.append(t['innfl'])
                    for t in response28['message']['foundersH']:
                        if 'innfl' in t:
                            if t['innfl'] not in s2:
                                s2.append(t['innfl'])

                    for t in response28['message']['directors']:
                        if t['innfl'] not in s2:
                            s2.append(t['innfl'])
                    for t in response28['message']['directorsH']:
                        if t['innfl'] not in s2:
                            s2.append(t['innfl'])

            for i in response28['message']['foundersH']:
                if 'innfl' in i:
                    if i['innfl'] not in s2:
                        s2.append(i['innfl'])
                elif 'inn' in i:
                    query29 = {
                        "inn": i['inn']
                    }
                    response29 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/details', json=query29)
                    response29 = response37.json()
                    for t in response29['message']['founders']:
                        if 'innfl' in t:
                            if t['innfl'] not in s2:
                                s2.append(t['innfl'])
                    for t in response29['message']['foundersH']:
                        if 'innfl' in t:
                            if t['innfl'] not in s2:
                                s2.append(t['innfl'])
                    for t in response29['message']['directors']:
                        if t['innfl'] not in s2:
                            s2.append(t['innfl'])
                    for t in response29['message']['directorsH']:
                        if t['innfl'] not in s2:
                            s2.append(t['innfl'])

            for i in response27['message']['directors']:
                if i['innfl'] not in s2:
                    s2.append(i['innfl'])

            for i in response27['message']['directorsH']:
                if i['innfl'] not in s2:
                    s2.append(i['innfl'])


    def ee44():
        for o in s1:
            query30 = {
                "inn": o
            }
            response30 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/person', json=query30)
            response30 = response30.json()
            for i in response30['message']['data']:
                if len(i['inn']) == 12:
                    if i['inn'] not in s1:
                        s1.append(i['inn'])
                else:
                    if i['inn'] not in qq1:
                        qq1.append(i['inn'])
        print(qq1)
    def rr44():
        for o in s2:
            query31 = {
                "inn": o
            }
            response31 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/person', json=query31)
            response31 = response39.json()
            for i in response31['message']['data']:
                if len(i['inn']) == 12:
                    if i['inn'] not in s2:
                        s2.append(i['inn'])
                else:
                    if i['inn'] not in qq2:
                        qq2.append(i['inn'])
        print(qq2)   
    
    
    
    
    
    

def qq55():
    for k in range(len(qq1)):
        query32 = {
            "inn": qq1[k]
        }
        response32 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/details', json=query32)
        response32 = response32.json()
        for i in response32['message']['founders']:
            if 'innfl' in i:
                s1.append(i['innfl'])
            elif 'inn' in i:
                query33 = {
                    "inn": i['inn']
                }
                response33 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/details', json=query33)
                response33 = response33.json()

                for t in response33['message']['founders']:
                    if 'innfl' in t:
                        if t['innfl'] not in s1:
                            s1.append(t['innfl'])

                for t in response33['message']['foundersH']:
                    if 'innfl' in t:
                        if t['innfl'] not in s1:
                            s1.append(t['innfl'])

                for t in response33['message']['directors']:
                    if t['innfl'] not in s1:
                        s1.append(t['innfl'])

                for t in response33['message']['directorsH']:
                    if t['innfl'] not in s1:
                        s1.append(t['innfl'])

        for i in response32['message']['foundersH']:
            if 'innfl' in i:
                if i['innfl'] not in s1:
                    s1.append(i['innfl'])

                query34 = {
                         "inn": i['inn']
                     }
                response34 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/details', json=query34)
                response34 = response34.json()
                for t in response34['message']['founders']:
                    if 'innfl' in t:
                        if t['innfl'] not in s1:
                            s1.append(t['innfl'])

                for t in response34['message']['foundersH']:
                    if 'innfl' in t:
                        if t['innfl'] not in s1:
                            s1.append(t['innfl'])

                for t in response34['message']['directors']:
                    if t['innfl'] not in s1:
                        s1.append(t['innfl'])

                for t in response34['message']['directorsH']:
                    if t['innfl'] not in s1:
                        s1.append(t['innfl'])

        for i in response32['message']['directors']:
            if i['innfl'] not in s1:
                s1.append(i['innfl'])

        for i in response32['message']['directorsH']:
            if i['innfl'] not in s1:
                s1.append(i['innfl'])

def ww55():
    for k in range(len(qq2)):
        query35 = {
            "inn": qq2[k]
        }
        response35 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/details', json=query35)
        response35 = response35.json()
        for i in response35['message']['founders']:
            if 'innfl' in i:
                if i['innfl'] not in s2:
                    s2.append(i['innfl'])
            elif 'inn' in i:
                query36 = {
                    "inn": i['inn']
                }
                response36 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/details', json=query36)
                response36 = response36.json()
                for t in response36['message']['founders']:
                    if 'innfl' in t:
                        if t['innfl'] not in s2:
                            s2.append(t['innfl'])
                for t in response36['message']['foundersH']:
                    if 'innfl' in t:
                        if t['innfl'] not in s2:
                            s2.append(t['innfl'])

                for t in response36['message']['directors']:
                    if t['innfl'] not in s2:
                        s2.append(t['innfl'])
                for t in response36['message']['directorsH']:
                    if t['innfl'] not in s2:
                        s2.append(t['innfl'])

        for i in response36['message']['foundersH']:
            if 'innfl' in i:
                if i['innfl'] not in s2:
                    s2.append(i['innfl'])
            elif 'inn' in i:
                query37 = {
                    "inn": i['inn']
                }
                response37 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/details', json=query37)
                response37 = response37.json()
                for t in response37['message']['founders']:
                    if 'innfl' in t:
                        if t['innfl'] not in s2:
                            s2.append(t['innfl'])
                for t in response37['message']['foundersH']:
                    if 'innfl' in t:
                        if t['innfl'] not in s2:
                            s2.append(t['innfl'])
                for t in response37['message']['directors']:
                    if t['innfl'] not in s2:
                        s2.append(t['innfl'])
                for t in response37['message']['directorsH']:
                    if t['innfl'] not in s2:
                        s2.append(t['innfl'])

        for i in response35['message']['directors']:
            if i['innfl'] not in s2:
                s2.append(i['innfl'])

        for i in response35['message']['directorsH']:
            if i['innfl'] not in s2:
                s2.append(i['innfl'])


def ee55():
    for o in s1:
        query38 = {
            "inn": o
        }
        response38 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/person', json=query38)
        response38 = response38.json()
        for i in response38['message']['data']:
            if len(i['inn']) == 12:
                if i['inn'] not in s1:
                    s1.append(i['inn'])
            else:
                if i['inn'] not in qq1:
                    qq1.append(i['inn'])
    print(qq1)
def rr55():
    for o in s2:
        query39 = {
            "inn": o
        }
        response39 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/person', json=query39)
        response39 = response39.json()
        for i in response39['message']['data']:
            if len(i['inn']) == 12:
                if i['inn'] not in s2:
                    s2.append(i['inn'])
            else:
                if i['inn'] not in qq2:
                    qq2.append(i['inn'])
    print(qq2)








