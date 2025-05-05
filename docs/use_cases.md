# Розроблення функціональних вимог до системи
У цьому розділі містяться діаграми прецедентів, зокрема загальна та конкретизовані, і діаграми активностей. 

## Короткий зміст
1. [Діаграма use case для користувача](#UserUseCase)


## Діаграми прецедентів бізнес акторів
Діаграма прецедентів (або діаграма варіантів використання) (англ. Use case diagram) — в UML, діаграма, на якій зображено відношення між акторами та прецедентами в системі.

Діаграма прецедентів показує різні варіанти використання та різні типи користувачів системи і часто супроводжується іншими типами діаграм. Варіанти використання представлені колами або еліпсами. Актори (дійові особи) часто зображуються у вигляді паличок.

<span id="UserUseCase"></span>
### Діаграма use case для всіх бізнес акторів
<center style="
    border-radius:4px;
    border: 1px solid #cfd7e6;
    box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
    padding: 1em;"
>

@startuml

    actor Expert
    actor Client

    usecase "UserManageAccount\nВзаємодія з\nобліковим записом" as UInteraction
    usecase "SurveyInteraction\nВзаємодія з опитуванням" as EInteraction
    usecase "SurveyCreate\nСтворити\nопитування" as SCreate
    usecase "SurveyDelete\nВидалити\nопитування" as SDelete
    usecase "SurveyManageResults\nВзаємодія\nз результатами" as SResults
    usecase "SurveyShareAccess\nПоділитись\nопитуванням" as SShare
    usecase "SurveyUpdate\nОновлення опитування" as SUpdate

    Expert -d-|> Client
    Expert -> EInteraction
    Client -u-> SResults
    Client -r-> SCreate
    Client -d-> UInteraction
    Client -d-> SDelete
    Client -d-> SUpdate
    Client -l-> SShare

@enduml

</center>




**Діаграма прецедентів**

</center>

