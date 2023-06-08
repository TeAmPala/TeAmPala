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
def qq():
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

def ww():
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


def ee():
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
def rr():
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




