ProTeam={
    'веб-дизайн':{
        'Сосюра':{
            'посада':"веб-дизайнер",
            'коефіцієнт активності':"9",
            'портфоліо':['сайт для онлайн магазину одягу', 'сайт для онлайн магазину косметики', 'сайт для онлайн магазину зоотоварів']
        },
        'Шевченко':{
            'посада':"головний менеджер",
            'коефіцієнт активності':"8"
        },
        'Симоненко':{
            'посада':"фронтенд",
            'коефіцієнт активності':"10",
            'портфоліо':['сайт для ресторану', 'сайт для готелю']
        },
        'Франко':{
            'посада':'управляючий',
            'коефіцієнт активності':"9"
        }
    },
    'розробка ігор':{
        'Зінченко':{
            "посада":'тестувальник',
            'коефіцієнт активності':'9',
            "портфоліо":{"перевірка роботи гри FIFA","перевірка роботи гри GTA"}
        },
        'Мудрик':{
            "посада":'головний менеджер',
            'коефіцієнт активності':'8'
        },
        'Миколенко':{
            'посада':"розробник ігор",
            'коефіцієнт активності':"6",
            'портфоліо':['FIFA','GTA']
        },
        'Матвієнко':{
            'посада':'управляючий',
            'коефіцієнт активності':'7'
        }
    },
    'зроблення баз, систем різного типу':{
        'Жадан':{
            'посада':'головний розробник',
            'коефіцієнт активності':'8',
            'портфоліо':['онлайн щоденник для школи', 'база про працівників для компанії']
        },
        'Пивоваров':{
            'посада':'менеджер',
            'коефіцієнт активності':'10'
        },
        'Меловін':{
            'посада':'управляючий',
            'коефіцієнт активності':'9'
        }
    }
}

print('Виберіть дію:')
print('1 - список відділів')
print('2 - інформація про компанію ProTeam')
print('3 - вийти')

question=int(input('Ваша дія:'))

while question!=3:

    if question==1:
        print('Наші відділи:')
        for viddil in ProTeam:
            print(viddil)
        print('Виберіть дію:')
        print('1 - докладніша інформація про один з відділів')
        print('2 - інформація про компанію ProTeam')
        print('3 - вийти')
        print('4 - меню')
        q1=int(input('Ваша дія:'))

        if q1==1:
            print("Про який з відділів ви б хотіли дізнатися докладніше?")
            i=1
            for viddil in ProTeam:
                print(i,'-', viddil)
                i+=1
            print('4 - Вийти')
            print('5 - меню')
            q2=int(input('Вибраний відділ:'))

            if q2==1:
                print('Список працівників:')
                x=1
                for worker in ProTeam['веб-дизайн']:
                    print(x, worker)
                    x+=1
                    for skill in ProTeam['веб-дизайн'][worker]:
                        print(' ', skill, ":", ProTeam['веб-дизайн'][worker][skill])    
                print('Виберіть дію:')
                print("1 - додати працівника")
                print('2 - видалити працівника')
                print('3 - меню')
                print('4 - вийти')
                q3=int(input('Ваша дія:'))

                if q3==1:
                    name=input('Прізвище працівника:')
                    rang=input('Посада:')
                    activity=input('коефіцієнт активності:')
                    prt=input('Портфоліо (якщо немає: - ):')

                    if portfolio=='-':
                        ProTeam['веб-дизайн'][name]={'посада':rang, 'коефіцієнт активності':activity}
                    
                    else:
                        ProTeam['веб-дизайн'][name]={'посада':rang, 'коефіцієнт активності':activity, 'Портфоліо':prt}

                    print('Новий список працівників:')
                    x=1
                    for worker in ProTeam['веб-дизайн']:
                        print(x, worker)
                        x+=1
                        for skill in ProTeam['веб-дизайн'][worker]:
                            print(' ', skill, ":", ProTeam['веб-дизайн'][worker][skill])

                elif q3==2:
                    surname=input('Вкажіть прізвище працівника, якого бажаєте видалити з бази:')
                    del ProTeam['веб-дизайн'][surname ]

                    print('Новий список працівників:')
                    x=1
                    for worker in ProTeam['веб-дизайн']:
                        print(x, worker)
                        x+=1
                        for skill in ProTeam['веб-дизайн'][worker]:
                            print(' ', skill, ":", ProTeam['веб-дизайн'][worker][skill]) 

                elif q3==3:
                    print('Виберіть дію:')
                    print('1 - список відділів')
                    print('2 - інформація про компанію ProTeam')
                    print('3 - вийти')
                    question=int(input('Ваша дія:'))

                elif q3==4:
                    break

                else:
                    print('Ви вказали щось неправильно')
                    print('Виберіть дію:')
                    print("1 - додати працівника")
                    print('2 - видалити працівника')
                    print('3 - меню')
                    print('4 - вийти')
                    q3=int(input('Ваша дія:'))

            elif q2==2:
                print('Список працівників:')
                x=1
                for worker in ProTeam['розробка ігор']:
                    print(x, worker)
                    x+=1
                    for skill in ProTeam['розробка ігор'][worker]:
                        print(' ', skill, ":", ProTeam['розробка ігор'][worker][skill])

                print('Виберіть дію:')
                print("1 - додати працівника")
                print('2 - видалити працівника')
                print('3 - меню')
                print('4 - вийти')
                q3=int(input('Ваша дія:'))

                if q3==1:
                    name=input('Прізвище працівника:')
                    rang=input('Посада:')
                    activity=input('коефіцієнт активності:')
                    prt=input('Портфоліо (якщо немає: - ):')

                    if portfolio=='-':
                        ProTeam['розробка ігор'][name]={'посада':rang, 'коефіцієнт активності':activity}
                    
                    else:
                        ProTeam['розробка ігор'][name]={'посада':rang, 'коефіцієнт активності':activity, 'Портфоліо':prt}

                    print('Новий список працівників:')
                    x=1
                    for worker in ProTeam['розробка ігор']:
                        print(x, worker)
                        x+=1
                        for skill in ProTeam['розробка ігор'][worker]:
                            print(' ', skill, ":", ProTeam['розробка ігор'][worker][skill])

                elif q3==2:
                    surname=input('Вкажіть прізвище працівника, якого бажаєте видалити з бази:')
                    del ProTeam['розробка ігор'][surname ]

                    print('Новий список працівників:')
                    x=1
                    for worker in ProTeam['розробка ігор']:
                        print(x, worker)
                        x+=1
                        for skill in ProTeam['розробка ігор'][worker]:
                            print(' ', skill, ":", ProTeam['розробка ігор'][worker][skill]) 

                elif q3==3:
                    print('Виберіть дію:')
                    print('1 - список відділів')
                    print('2 - інформація про компанію ProTeam')
                    print('3 - вийти')
                    question=int(input('Ваша дія:'))

                elif q3==4:
                    break

                else:
                    print('Ви вказали щось неправильно')
                    print('Виберіть дію:')
                    print("1 - додати працівника")
                    print('2 - видалити працівника')
                    print('3 - меню')
                    print('4 - вийти')
                    q3=int(input('Ваша дія:'))

            elif q2==3:
                print('Список працівників:')
                x=1
                for worker in ProTeam['зроблення баз, систем різного типу']:
                    print(x, worker)
                    x+=1
                    for skill in ProTeam['зроблення баз, систем різного типу'][worker]:
                        print(' ', skill, ":", ProTeam['зроблення баз, систем різного типу'][worker][skill]) 

                print('Виберіть дію:')
                print("1 - додати працівника")
                print('2 - видалити працівника')
                print('3 - меню')
                print('4 - вийти')
                q3=int(input('Ваша дія:'))

                if q3==1:
                    name=input('Прізвище працівника:')
                    rang=input('Посада:')
                    activity=input('коефіцієнт активності:')
                    prt=input('Портфоліо (якщо немає: - ):')

                    if portfolio=='-':
                        ProTeam['зроблення баз, систем різного типу'][name]={'посада':rang, 'коефіцієнт активності':activity}
                    
                    else:
                        ProTeam['зроблення баз, систем різного типу'][name]={'посада':rang, 'коефіцієнт активності':activity, 'Портфоліо':prt}

                    print('Новий список працівників:')
                    x=1
                    for worker in ProTeam['зроблення баз, систем різного типу']:
                        print(x, worker)
                        x+=1
                        for skill in ProTeam['зроблення баз, систем різного типу'][worker]:
                            print(' ', skill, ":", ProTeam['зроблення баз, систем різного типу'][worker][skill])
                    
                elif q3==2:
                    surname=input('Вкажіть прізвище працівника, якого бажаєте видалити з бази:')
                    del ProTeam['зроблення баз, систем різного типу'][surname ]

                    print('Новий список працівників:')
                    x=1
                    for worker in ProTeam['зроблення баз, систем різного типу']:
                        print(x, worker)
                        x+=1
                        for skill in ProTeam['зроблення баз, систем різного типу'][worker]:
                            print(' ', skill, ":", ProTeam['зроблення баз, систем різного типу'][worker][skill]) 

                elif q3==3:
                    print('Виберіть дію:')
                    print('1 - список відділів')
                    print('2 - інформація про компанію ProTeam')
                    print('3 - вийти')
                    question=int(input('Ваша дія:'))

                elif q3==4:
                    break

                else:
                    print('Ви вказали щось неправильно')
                    print('Виберіть дію:')
                    print("1 - додати працівника")
                    print('2 - видалити працівника')
                    print('3 - меню')
                    print('4 - вийти')
                    q3=int(input('Ваша дія:'))

            else:
                print('Ви вказали щось неправильно')
                print("Про який з відділів ви б хотіли дізнатися докладніше?")
                i=1
                for viddil in ProTeam:
                    print(i,'-', viddil)
                    i+=1
                print('4 - Вийти')
                print('5 - меню')
                q2=int(input('Вибраний відділ:'))

        elif q1==2:
            print(' ProTeam: ІТ Компанія для Геймерів та Бізнесу')
            print('Опис:')
            print(' ProTeam — це творча та різнобічна ІТ-команда, яка об’єднує геймерів, програмістів та дизайнерів. Наша мета — створювати захоплюючі ігри для геймерів та ефективні рішення для бізнесу.')
            print('Послуги:')
            print(' Розробка ігор:')
            print('     -Створення відеоігор для різних платформ (PC, консолі, мобільні пристрої).')
            print('     -Геймдизайн та розробка геймплею.')
            print('     -Оптимізація для високої продуктивності та графічної якості.')
            print(' Веб-дизайн:')
            print('     -Створення веб-сайтів для геймерських спільнот, ігрових студій та бізнесу.')
            print('     -Дизайн інтерфейсів для ігрових сайтів та платформ.')
            print(' Бази даних та системи:')
            print('     -Розробка баз даних для управління геймерськими профілями, досягненнями та інвентарем.')
            print('     -Створення корпоративних систем для бізнесу.')
            print(' Наш підхід:')
            print('Ми віримо, що кожен проект — це унікальна можливість для творчості та інновацій. ProTeam завжди відкрита до нових ідей та готова втілити їх у життя. Наша команда — це справжні геймери, які розуміють, як зробити ігри захоплюючими та незабутніми.')
            
            print('Виберіть дію:')
            print('1 - докладніша інформація про 1 з відділів')
            print('2 - вийти')
            print('3 - меню')
            q4=int(input('Ваша дія:'))

            if q4==1:
                print("Про який з відділів ви б хотіли дізнатися докладніше?")
                i=1
                for viddil in ProTeam:
                    print(i,'-', viddil)
                    i+=1
                print('4 - Вийти')
                print('5 - меню')
                q2=int(input('Вибраний відділ:'))

                if q2==1:
                    print('Список працівників:')
                    x=1
                    for worker in ProTeam['веб-дизайн']:
                        print(x, worker)
                        x+=1
                        for skill in ProTeam['веб-дизайн'][worker]:
                            print(' ', skill, ":", ProTeam['веб-дизайн'][worker][skill])    
                    print('Виберіть дію:')
                    print("1 - додати працівника")
                    print('2 - видалити працівника')
                    print('3 - меню')
                    print('4 - вийти')
                    q3=int(input('Ваша дія:'))

                    if q3==1:
                        name=input('Прізвище працівника:')
                        rang=input('Посада:')
                        activity=input('коефіцієнт активності:')
                        prt=input('Портфоліо (якщо немає: - ):')

                        if portfolio=='-':
                            ProTeam['веб-дизайн'][name]={'посада':rang, 'коефіцієнт активності':activity}
                        
                        else:
                            ProTeam['веб-дизайн'][name]={'посада':rang, 'коефіцієнт активності':activity, 'Портфоліо':prt}

                        print('Новий список працівників:')
                        x=1
                        for worker in ProTeam['веб-дизайн']:
                            print(x, worker)
                            x+=1
                            for skill in ProTeam['веб-дизайн'][worker]:
                                print(' ', skill, ":", ProTeam['веб-дизайн'][worker][skill])

                    elif q3==2:
                        surname=input('Вкажіть прізвище працівника, якого бажаєте видалити з бази:')
                        del ProTeam['веб-дизайн'][surname ]

                        print('Новий список працівників:')
                        x=1
                        for worker in ProTeam['веб-дизайн']:
                            print(x, worker)
                            x+=1
                            for skill in ProTeam['веб-дизайн'][worker]:
                                print(' ', skill, ":", ProTeam['веб-дизайн'][worker][skill]) 

                    elif q3==3:
                        print('Виберіть дію:')
                        print('1 - список відділів')
                        print('2 - інформація про компанію ProTeam')
                        print('3 - вийти')
                        question=int(input('Ваша дія:'))

                    elif q3==4:
                        break

                    else:
                        print('Ви вказали щось неправильно')
                        print('Виберіть дію:')
                        print("1 - додати працівника")
                        print('2 - видалити працівника')
                        print('3 - меню')
                        print('4 - вийти')
                        q3=int(input('Ваша дія:'))

                elif q2==2:
                    print('Список працівників:')
                    x=1
                    for worker in ProTeam['розробка ігор']:
                        print(x, worker)
                        x+=1
                        for skill in ProTeam['розробка ігор'][worker]:
                            print(' ', skill, ":", ProTeam['розробка ігор'][worker][skill])
                    print('Виберіть дію:')
                    print("1 - додати працівника")
                    print('2 - видалити працівника')
                    print('3 - меню')
                    print('4 - вийти')
                    q3=int(input('Ваша дія:'))

                    if q3==1:
                        name=input('Прізвище працівника:')
                        rang=input('Посада:')
                        activity=input('коефіцієнт активності:')
                        prt=input('Портфоліо (якщо немає: - ):')

                        if portfolio=='-':
                            ProTeam['розробка ігор'][name]={'посада':rang, 'коефіцієнт активності':activity}
                        
                        else:
                            ProTeam['розробка ігор'][name]={'посада':rang, 'коефіцієнт активності':activity, 'Портфоліо':prt}

                        print('Новий список працівників:')
                        x=1
                        for worker in ProTeam['розробка ігор']:
                            print(x, worker)
                            x+=1
                            for skill in ProTeam['розробка ігор'][worker]:
                                print(' ', skill, ":", ProTeam['розробка ігор'][worker][skill])

                    elif q3==2:
                        surname=input('Вкажіть прізвище працівника, якого бажаєте видалити з бази:')
                        del ProTeam['розробка ігор'][surname ]

                        print('Новий список працівників:')
                        x=1
                        for worker in ProTeam['розробка ігор']:
                            print(x, worker)
                            x+=1
                            for skill in ProTeam['розробка ігор'][worker]:
                                print(' ', skill, ":", ProTeam['розробка ігор'][worker][skill]) 

                    elif q3==3:
                        print('Виберіть дію:')
                        print('1 - список відділів')
                        print('2 - інформація про компанію ProTeam')
                        print('3 - вийти')
                        question=int(input('Ваша дія:'))

                    elif q3==4:
                        break

                    else:
                        print('Ви вказали щось неправильно')
                        print('Виберіть дію:')
                        print("1 - додати працівника")
                        print('2 - видалити працівника')
                        print('3 - меню')
                        print('4 - вийти')
                        q3=int(input('Ваша дія:'))

                elif q2==3:
                    print('Список працівників:')
                    x=1
                    for worker in ProTeam['зроблення баз, систем різного типу']:
                        print(x, worker)
                        x+=1
                        for skill in ProTeam['зроблення баз, систем різного типу'][worker]:
                            print(' ', skill, ":", ProTeam['зроблення баз, систем різного типу'][worker][skill]) 
                            
                    print('Виберіть дію:')
                    print("1 - додати працівника")
                    print('2 - видалити працівника')
                    print('3 - меню')
                    print('4 - вийти')
                    q3=int(input('Ваша дія:'))

                    if q3==1:
                        name=input('Прізвище працівника:')
                        rang=input('Посада:')
                        activity=input('коефіцієнт активності:')
                        prt=input('Портфоліо (якщо немає: - ):')

                        if portfolio=='-':
                            ProTeam['зроблення баз, систем різного типу'][name]={'посада':rang, 'коефіцієнт активності':activity}
                        
                        else:
                            ProTeam['зроблення баз, систем різного типу'][name]={'посада':rang, 'коефіцієнт активності':activity, 'Портфоліо':prt}

                        print('Новий список працівників:')
                        x=1
                        for worker in ProTeam['зроблення баз, систем різного типу']:
                            print(x, worker)
                            x+=1
                            for skill in ProTeam['зроблення баз, систем різного типу'][worker]:
                                print(' ', skill, ":", ProTeam['зроблення баз, систем різного типу'][worker][skill])
                        
                    elif q3==2:
                        surname=input('Вкажіть прізвище працівника, якого бажаєте видалити з бази:')
                        del ProTeam['зроблення баз, систем різного типу'][surname ]

                        print('Новий список працівників:')
                        x=1
                        for worker in ProTeam['зроблення баз, систем різного типу']:
                            print(x, worker)
                            x+=1
                            for skill in ProTeam['зроблення баз, систем різного типу'][worker]:
                                print(' ', skill, ":", ProTeam['зроблення баз, систем різного типу'][worker][skill]) 

                    elif q3==3:
                        print('Виберіть дію:')
                        print('1 - список відділів')
                        print('2 - інформація про компанію ProTeam')
                        print('3 - вийти')
                        question=int(input('Ваша дія:'))

                    elif q3==4:
                        break

                    else:
                        print('Ви вказали щось неправильно')
                        print('Виберіть дію:')
                        print("1 - додати працівника")
                        print('2 - видалити працівника')
                        print('3 - меню')
                        print('4 - вийти')
                        q3=int(input('Ваша дія:'))
            
                elif q2==4:
                    break

                elif q2==5:
                    print('Виберіть дію:')
                    print('1 - список відділів')
                    print('2 - інформація про компанію ProTeam')
                    print('3 - вийти')
                    question=int(input('Ваша дія:'))

                else:
                    print('Ви вказали щось неправильно')
                    print("Про який з відділів ви б хотіли дізнатися докладніше?")
                    i=1
                    for viddil in ProTeam:
                        print(i,'-', viddil)
                        i+=1
                    print('4 - Вийти')
                    print('5 - меню')
                    q2=int(input('Вибраний відділ:'))

            elif q1==3:
                break
            
            elif q1==4:
                print('Виберіть дію:')
                print('1 - список відділів')
                print('2 - інформація про компанію ProTeam')
                print('3 - вийти')
                question=int(input('Ваша дія:'))

            else:
                print('Ви вказали щось неправильно')
                print('Виберіть дію:')
                print('1 - докладніша інформація про один з відділів')
                print('2 - інформація про компанію ProTeam')
                print('3 - вийти')
                print('4 - меню')
                q1=int(input('Ваша дія:'))

    elif question==2:
        print(' ProTeam: ІТ Компанія для Геймерів та Бізнесу')
        print('Опис:')
        print(' ProTeam — це творча та різнобічна ІТ-команда, яка об’єднує геймерів, програмістів та дизайнерів. Наша мета — створювати захоплюючі ігри для геймерів та ефективні рішення для бізнесу.')
        print('Послуги:')
        print(' Розробка ігор:')
        print('     -Створення відеоігор для різних платформ (PC, консолі, мобільні пристрої).')
        print('     -Геймдизайн та розробка геймплею.')
        print('     -Оптимізація для високої продуктивності та графічної якості.')
        print(' Веб-дизайн:')
        print('     -Створення веб-сайтів для геймерських спільнот, ігрових студій та бізнесу.')
        print('     -Дизайн інтерфейсів для ігрових сайтів та платформ.')
        print(' Бази даних та системи:')
        print('     -Розробка баз даних для управління геймерськими профілями, досягненнями та інвентарем.')
        print('     -Створення корпоративних систем для бізнесу.')
        print(' Наш підхід:')
        print('Ми віримо, що кожен проект — це унікальна можливість для творчості та інновацій. ProTeam завжди відкрита до нових ідей та готова втілити їх у життя. Наша команда — це справжні геймери, які розуміють, як зробити ігри захоплюючими та незабутніми.')
        
        print('Виберіть дію:')
        print('1 - докладніша інформація про 1 з відділів')
        print('2 - вийти')
        print('3 - меню')
        q4=int(input('Ваша дія:'))

        if q4==1:
            print("Про який з відділів ви б хотіли дізнатися докладніше?")
            i=1
            for viddil in ProTeam:
                print(i,'-', viddil)
                i+=1
            print('4 - Вийти')
            print('5 - меню')
            q2=int(input('Вибраний відділ:'))

            if q2==1:
                print('Список працівників:')
                x=1
                for worker in ProTeam['веб-дизайн']:
                    print(x, worker)
                    x+=1
                    for skill in ProTeam['веб-дизайн'][worker]:
                        print(' ', skill, ":", ProTeam['веб-дизайн'][worker][skill])    
                print('Виберіть дію:')
                print("1 - додати працівника")
                print('2 - видалити працівника')
                print('3 - меню')
                print('4 - вийти')
                q3=int(input('Ваша дія:'))

                if q3==1:
                    name=input('Прізвище працівника:')
                    rang=input('Посада:')
                    activity=input('коефіцієнт активності:')
                    prt=input('Портфоліо (якщо немає: - ):')

                    if portfolio=='-':
                        ProTeam['веб-дизайн'][name]={'посада':rang, 'коефіцієнт активності':activity}
                    
                    else:
                        ProTeam['веб-дизайн'][name]={'посада':rang, 'коефіцієнт активності':activity, 'Портфоліо':prt}

                    print('Новий список працівників:')
                    x=1
                    for worker in ProTeam['веб-дизайн']:
                        print(x, worker)
                        x+=1
                        for skill in ProTeam['веб-дизайн'][worker]:
                            print(' ', skill, ":", ProTeam['веб-дизайн'][worker][skill])

                elif q3==2:
                    surname=input('Вкажіть прізвище працівника, якого бажаєте видалити з бази:')
                    del ProTeam['веб-дизайн'][surname ]

                    print('Новий список працівників:')
                    x=1
                    for worker in ProTeam['веб-дизайн']:
                        print(x, worker)
                        x+=1
                        for skill in ProTeam['веб-дизайн'][worker]:
                            print(' ', skill, ":", ProTeam['веб-дизайн'][worker][skill]) 

                elif q3==3:
                    print('Виберіть дію:')
                    print('1 - список відділів')
                    print('2 - інформація про компанію ProTeam')
                    print('3 - вийти')
                    question=int(input('Ваша дія:'))

                elif q3==4:
                    break

                else:
                    print('Ви вказали щось неправильно')
                    print('Виберіть дію:')
                    print("1 - додати працівника")
                    print('2 - видалити працівника')
                    print('3 - меню')
                    print('4 - вийти')
                    q3=int(input('Ваша дія:'))

            elif q2==2:
                print('Список працівників:')
                x=1
                for worker in ProTeam['розробка ігор']:
                    print(x, worker)
                    x+=1
                    for skill in ProTeam['розробка ігор'][worker]:
                        print(' ', skill, ":", ProTeam['розробка ігор'][worker][skill])
                print('Виберіть дію:')
                print("1 - додати працівника")
                print('2 - видалити працівника')
                print('3 - меню')
                print('4 - вийти')
                q3=int(input('Ваша дія:'))

                if q3==1:
                    name=input('Прізвище працівника:')
                    rang=input('Посада:')
                    activity=input('коефіцієнт активності:')
                    prt=input('Портфоліо (якщо немає: - ):')

                    if portfolio=='-':
                        ProTeam['розробка ігор'][name]={'посада':rang, 'коефіцієнт активності':activity}
                    
                    else:
                        ProTeam['розробка ігор'][name]={'посада':rang, 'коефіцієнт активності':activity, 'Портфоліо':prt}

                    print('Новий список працівників:')
                    x=1
                    for worker in ProTeam['розробка ігор']:
                        print(x, worker)
                        x+=1
                        for skill in ProTeam['розробка ігор'][worker]:
                            print(' ', skill, ":", ProTeam['розробка ігор'][worker][skill])

                elif q3==2:
                    surname=input('Вкажіть прізвище працівника, якого бажаєте видалити з бази:')
                    del ProTeam['розробка ігор'][surname ]

                    print('Новий список працівників:')
                    x=1
                    for worker in ProTeam['розробка ігор']:
                        print(x, worker)
                        x+=1
                        for skill in ProTeam['розробка ігор'][worker]:
                            print(' ', skill, ":", ProTeam['розробка ігор'][worker][skill]) 

                elif q3==3:
                    print('Виберіть дію:')
                    print('1 - список відділів')
                    print('2 - інформація про компанію ProTeam')
                    print('3 - вийти')
                    question=int(input('Ваша дія:'))

                elif q3==4:
                    break

                else:
                    print('Ви вказали щось неправильно')
                    print('Виберіть дію:')
                    print("1 - додати працівника")
                    print('2 - видалити працівника')
                    print('3 - меню')
                    print('4 - вийти')
                    q3=int(input('Ваша дія:'))

            elif q2==3:
                print('Список працівників:')
                x=1
                for worker in ProTeam['зроблення баз, систем різного типу']:
                    print(x, worker)
                    x+=1
                    for skill in ProTeam['зроблення баз, систем різного типу'][worker]:
                        print(' ', skill, ":", ProTeam['зроблення баз, систем різного типу'][worker][skill]) 
                        
                print('Виберіть дію:')
                print("1 - додати працівника")
                print('2 - видалити працівника')
                print('3 - меню')
                print('4 - вийти')
                q3=int(input('Ваша дія:'))

                if q3==1:
                    name=input('Прізвище працівника:')
                    rang=input('Посада:')
                    activity=input('коефіцієнт активності:')
                    prt=input('Портфоліо (якщо немає: - ):')

                    if portfolio=='-':
                        ProTeam['зроблення баз, систем різного типу'][name]={'посада':rang, 'коефіцієнт активності':activity}
                    
                    else:
                        ProTeam['зроблення баз, систем різного типу'][name]={'посада':rang, 'коефіцієнт активності':activity, 'Портфоліо':prt}

                    print('Новий список працівників:')
                    x=1
                    for worker in ProTeam['зроблення баз, систем різного типу']:
                        print(x, worker)
                        x+=1
                        for skill in ProTeam['зроблення баз, систем різного типу'][worker]:
                            print(' ', skill, ":", ProTeam['зроблення баз, систем різного типу'][worker][skill])
                    
                elif q3==2:
                    surname=input('Вкажіть прізвище працівника, якого бажаєте видалити з бази:')
                    del ProTeam['зроблення баз, систем різного типу'][surname ]

                    print('Новий список працівників:')
                    x=1
                    for worker in ProTeam['зроблення баз, систем різного типу']:
                        print(x, worker)
                        x+=1
                        for skill in ProTeam['зроблення баз, систем різного типу'][worker]:
                            print(' ', skill, ":", ProTeam['зроблення баз, систем різного типу'][worker][skill]) 

                elif q3==3:
                    print('Виберіть дію:')
                    print('1 - список відділів')
                    print('2 - інформація про компанію ProTeam')
                    print('3 - вийти')
                    question=int(input('Ваша дія:'))

                elif q3==4:
                    break

                else:
                    print('Ви вказали щось неправильно')
                    print('Виберіть дію:')
                    print("1 - додати працівника")
                    print('2 - видалити працівника')
                    print('3 - меню')
                    print('4 - вийти')
                    q3=int(input('Ваша дія:'))
                
            elif q2==4:
                break

            elif q2==5:
                print('Виберіть дію:')
                print('1 - список відділів')
                print('2 - інформація про компанію ProTeam')
                print('3 - вийти')
                question=int(input('Ваша дія:'))

            else:
                print('Ви вказали щось неправильно')
                print("Про який з відділів ви б хотіли дізнатися докладніше?")
                i=1
                for viddil in ProTeam:
                    print(i,'-', viddil)
                    i+=1
                print('4 - Вийти')
                print('5 - меню')
                q2=int(input('Вибраний відділ:'))

        elif q4==2:
            break
        
        elif q4==3:
            print('Виберіть дію:')
            print('1 - список відділів')
            print('2 - інформація про компанію ProTeam')
            print('3 - вийти')
            question=int(input('Ваша дія:'))

        else:
            print('Ви вказали щось неправильно')
            print('Виберіть дію:')
            print('1-докладніша інформація про 1 з відділів')
            print('2-вийти')
            q4=int(input('Ваша дія:'))
    
    elif question==3:
        break

    else:
        print('Ви вказали щось неправильно')
        print('Виберіть дію:')
        print('1-список відділів')
        print('2-інформація про компанію ProTeam')
        print('3-вийти')
        question=int(input('Ваша дія:'))
        
    print('Виберіть дію:')
    print('1-список відділів')
    print('2-інформація про компанію ProTeam')
    print('3-вийти')

    question=int(input('Ваша дія:'))

print('Дякую ❤')
print('До побачення!')