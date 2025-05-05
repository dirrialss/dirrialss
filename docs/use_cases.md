# Розроблення функціональних вимог до системи

## Модель прецедентів

В цьому файлі необхідно перелічити всі документи, розроблені в проекті та дати посилання на них.

*Модель прецедентів повинна містити загальні оглядові діаграми та специфікації прецедентів.*



Вбудовування зображень діаграм здійснюється з використанням сервісу [plantuml.com](https://plantuml.com/). 

В markdown-файлі використовується опис діаграми

[![UseCase діаграма для користувача](https://img.plantuml.biz/plantuml/svg/XPGzJiD048NxIBd3qa4H3e0GuhUZG4XqD8ip14kEBUrk14WK8HHG80g4WaG3Y0iOauZVX2lCteZnEWwxJWoHNCH-xystCsClIyM5QZM3QcL67K0Js5xGWeRWnzLAjS8z5Gc6TpZKRNpJfxgZpp31M9-dJndzPdSaYFbjQFXIWLWztcXoFzWDyPP4RUph6sDgZsmT4tB9y1LZXZqSuZTTNtIzK8ahblxL5wbiZd792h5snJK1NC6AvqMjK56zHp8b8qooCupnWmgUuK1tJ9PZi9CseuOVKi8J9hgBxvaxcGmmEjkunQKyZ4Hz6oIa2DTax-603fFa4D-c2qFyr9UZ0v7KpjYe--ht40_OfuGONtxRnSoDWUuwG1YRECljzEQ0Xmt8ySmmleXjK4RbwejuMo1a5F9WdIi-cJNKfvJqF5gExXXtp6VR7SWetFT5SyLJVfIs_pxjdXbYd-1wUNvFT_LLHcaRxAHr2C1UXMjyCnIVPQlW6F95dhRah5PRchOufLfhHqer4qChLKxbT73OuacjLdnDs0A38mLXNMOE0vKhQV_ivvd2GifqxaOK0oVanJd_PJ0jjKT9OZ_qWbOTnZpEmVzrB5CXym7x0G00)](https://editor.plantuml.com/uml/XPGzJiD048NxIBd3qa4H3e0GuhUZG4XqD8ip14kEBUrk14WK8HHG80g4WaG3Y0iOauZVX2lCteZnEWwxJWoHNCH-xystCsClIyM5QZM3QcL67K0Js5xGWeRWnzLAjS8z5Gc6TpZKRNpJfxgZpp31M9-dJndzPdSaYFbjQFXIWLWztcXoFzWDyPP4RUph6sDgZsmT4tB9y1LZXZqSuZTTNtIzK8ahblxL5wbiZd792h5snJK1NC6AvqMjK56zHp8b8qooCupnWmgUuK1tJ9PZi9CseuOVKi8J9hgBxvaxcGmmEjkunQKyZ4Hz6oIa2DTax-603fFa4D-c2qFyr9UZ0v7KpjYe--ht40_OfuGONtxRnSoDWUuwG1YRECljzEQ0Xmt8ySmmleXjK4RbwejuMo1a5F9WdIi-cJNKfvJqF5gExXXtp6VR7SWetFT5SyLJVfIs_pxjdXbYd-1wUNvFT_LLHcaRxAHr2C1UXMjyCnIVPQlW6F95dhRah5PRchOufLfhHqer4qChLKxbT73OuacjLdnDs0A38mLXNMOE0vKhQV_ivvd2GifqxaOK0oVanJd_PJ0jjKT9OZ_qWbOTnZpEmVzrB5CXym7x0G00)



```md

<center style="
    border-radius:4px;
    border: 1px solid #cfd7e6;
    box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
    padding: 1em;"
>

@startuml

    right header
        <font size=24 color=black>Package: <b>UCD_3.0
    end header

    title
        <font size=18 color=black>UC_8. Редагувати конфігурацію порталу
        <font size=16 color=black>Діаграма прецедентів
    end title


    actor "Користувач" as User #eeeeaa
    
    package UCD_1{
        usecase "<b>UC_1</b>\nПереглянути список \nзвітів" as UC_1 #aaeeaa
    }
    
    usecase "<b>UC_1.1</b>\nЗастосувати фільтр" as UC_1.1
    usecase "<b>UC_1.2</b>\nПереглянути метадані \nзвіту" as UC_1.2  
    usecase "<b>UC_1.2.1</b>\nДати оцінку звіту" as UC_1.2.1  
    usecase "<b>UC_1.2.2</b>\nПереглянути інформацію \nпро авторів звіту" as UC_1.2.2
    
    package UCD_1 {
        usecase "<b>UC_4</b>\nВикликати звіт" as UC_4 #aaeeaa
    }
    
    usecase "<b>UC_1.1.1</b>\n Використати \nпошукові теги" as UC_1.1.1  
    usecase "<b>UC_1.1.2</b>\n Використати \nрядок пошуку" as UC_1.1.2
    usecase "<b>UC_1.1.3</b>\n Використати \nавторів" as UC_1.1.3  
    
    
    
    User -> UC_1
    UC_1.1 .u.> UC_1 :extends
    UC_1.2 .u.> UC_1 :extends
    UC_4 .d.> UC_1.2 :extends
    UC_1.2 .> UC_1.2 :extends
    UC_1.2.1 .u.> UC_1.2 :extends
    UC_1.2.2 .u.> UC_1.2 :extends
    UC_1 ..> UC_1.2.2 :extends
    
    
    UC_1.1.1 -u-|> UC_1.1
    UC_1.1.2 -u-|> UC_1.1
    UC_1.1.3 -u-|> UC_1.1
    
    right footer
        Аналітичний портал. Модель прецедентів.
        НТУУ КПІ ім.І.Сікорського
        Киів-2020
    end footer

@enduml

**Діаграма прецедентів**

</center>
```

яка буде відображена наступним чином

<center style="
    border-radius:4px;
    border: 1px solid #cfd7e6;
    box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
    padding: 1em;"
    >

```plantuml
@startuml

    right header
        <font size=24 color=black>Package: <b>UCD_3.0
    end header

    title
        <font size=18 color=black>UC_8. Редагувати конфігурацію порталу
        <font size=16 color=black>Діаграма прецедентів
    end title


    actor "Користувач" as User #eeeeaa
    
    package UCD_1{
        usecase "<b>UC_1</b>\nПереглянути список \nзвітів" as UC_1 #aaeeaa
    }
    
    usecase "<b>UC_1.1</b>\nЗастосувати фільтр" as UC_1.1
    usecase "<b>UC_1.2</b>\nПереглянути метадані \nзвіту" as UC_1.2  
    usecase "<b>UC_1.2.1</b>\nДати оцінку звіту" as UC_1.2.1  
    usecase "<b>UC_1.2.2</b>\nПереглянути інформацію \nпро авторів звіту" as UC_1.2.2
    
    package UCD_1 {
        usecase "<b>UC_4</b>\nВикликати звіт" as UC_4 #aaeeaa
    }
    
    usecase "<b>UC_1.1.1</b>\n Використати \nпошукові теги" as UC_1.1.1  
    usecase "<b>UC_1.1.2</b>\n Використати \nрядок пошуку" as UC_1.1.2
    usecase "<b>UC_1.1.3</b>\n Використати \nавторів" as UC_1.1.3  
    
    
    
    User -> UC_1
    UC_1.1 .u.> UC_1 :extends
    UC_1.2 .u.> UC_1 :extends
    UC_4 .d.> UC_1.2 :extends
    UC_1.2 .> UC_1.2 :extends
    UC_1.2.1 .u.> UC_1.2 :extends
    UC_1.2.2 .u.> UC_1.2 :extends
    UC_1 ..> UC_1.2.2 :extends
    
    
    UC_1.1.1 -u-|> UC_1.1
    UC_1.1.2 -u-|> UC_1.1
    UC_1.1.3 -u-|> UC_1.1
    
    right footer
        Аналітичний портал. Модель прецедентів.
        НТУУ КПІ ім.І.Сікорського
        Киів-2020
    end footer

@enduml
```


**Діаграма прецедентів**

</center>

