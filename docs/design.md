# Проєктування бази даних

## Mодель бізнес-об'єктів


@startuml

top to bottom direction

entity Person #88cc88
entity Person.id #b3ffb3
entity Person.first_name #b3ffb3
entity Person.last_name #b3ffb3
entity Person.email #b3ffb3
entity Person.phone #b3ffb3
entity Person.secret #b3ffb3
entity Person.age #b3ffb3

Person.id -d-* Person
Person.first_name -d-* Person
Person.last_name -d-* Person
Person.email -d-* Person
Person.phone -d-* Person
Person.secret -d-* Person
Person.age -d-* Person

entity Response #e85b71
entity Response.id #ffb6c1
entity Response.body #ffb6c1
entity Response.person_id #ffb6c1
entity Response.question_id #ffb6c1
entity Response.ref_id #ffb6c1

Response.id -d-* Response
Response.body -d-* Response
Response.person_id -d-* Response
Response.question_id -d-* Response
Response.ref_id -d-* Response

entity Choice #9c27b0
entity Choice.id #ba68c8
entity Choice.content #ba68c8

Choice.id --* Choice
Choice.content --l-* Choice

entity Selection #d32f2f
Selection "0,* " <-u-> "1,1" Choice
Selection "0,* " <-d-> "1,1" Response

entity Inquiry #ab47bc
entity Inquiry.id #e1bee7
entity Inquiry.details #e1bee7
entity Inquiry.quiz_id #e1bee7
entity Inquiry.title #e1bee7

Inquiry.id -d-* Inquiry
Inquiry.details -d-* Inquiry
Inquiry.quiz_id -d-* Inquiry
Inquiry.title -d-* Inquiry

Inquiry "1,1" <- "0,*" Response 
Choice "0,*" -u-> "1,1" Inquiry

entity Category #00796b
entity Category.id #80cbc4
entity Category.notes #80cbc4
entity Category.question_id #80cbc4

Category.id -d-* Category
Category.notes -d-* Category
Category.question_id -d-* Category

entity Outcome #4caf50
entity Outcome.id #4caf50
entity Outcome.explanation #4caf50
entity Outcome.label #4caf50
entity Outcome.response_id #4caf50

Outcome.id -d-* Outcome
Outcome.explanation -d-* Outcome
Outcome.label -d-* Outcome
Outcome.response_id -d-* Outcome

entity Comment #ff9800
entity Comment.id #ffe0b2
entity Comment.subject #ffe0b2
entity Comment.content #ffe0b2
entity Comment.timestamp #ffe0b2
entity Comment.person_id #ffe0b2
entity Comment.quiz_id #ffe0b2

Comment.id -d-* Comment
Comment.subject -d-* Comment
Comment.content -d-* Comment
Comment.timestamp -d-* Comment
Comment.person_id -d-* Comment
Comment.quiz_id -d-* Comment

entity Test #26c6da
entity Test.id #b2ebf2
entity Test.creator_id #b2ebf2
entity Test.info #b2ebf2
entity Test.active #b2ebf2
entity Test.start_date #b2ebf2
entity Test.end_date #b2ebf2
entity Test.name #b2ebf2

Test.id -d-* Test
Test.creator_id -d-* Test
Test.info -d-* Test
Test.active -d-* Test
Test.start_date -d-* Test
Test.end_date -d-* Test
Test.name -d-* Test

entity Group #3f51b5
entity Group.id #c5cae9
entity Group.name #c5cae9
entity Group.description #c5cae9

Group.id -d-* Group
Group.name -d-* Group
Group.description -d-* Group

entity Access #aed581
entity Access.id #dcedc8
entity Access.title #dcedc8
entity Access.details #dcedc8

Access.id -d-* Access
Access.title -d-* Access
Access.details -d-* Access

entity Log #fbc02d
entity Log.id #fff176
entity Log.date #fff176
entity Log.status #fff176
entity Log.description #fff176

Log.id -d-* Log
Log.date -d-* Log
Log.status -d-* Log
Log.description -d-* Log

entity Participant #ce93d8
entity Participant.id #e1bee7
entity Participant.role #e1bee7

Participant.id -d-* Participant
Participant.role -d-* Participant

Test "1,1" <-- "0,*" Inquiry

Person "1, 1" <-- "0, *" Response : person_id
Person "1, 1" -- "0, *" Comment : person_id
Person "1, 1" -- "0, *" Test : creator_id
Person "1, 1" --> "0, *" Group
Person "1, 1" -- "0 .. *" Access
Inquiry "0, *" --> "1,1" Category 
Inquiry "1, 1" -- "0 .. *" Response : question_id
Response "0 .. *" -- "1, 1" Outcome : response_id

Test "1, 1" -- "0 .. *" Comment  
Group "1, 1" -- "0 .. *" Access : RolePermission

Log "0,*" --> "1,1" Person: initiator
Log "1,1" --> "1,1" Test
Participant "0,*" --> "1,1" Log
Participant "0,*" --> "1,1" Person

@enduml





## ER-модель
**ER-модель** описує сутності системи та визначає зв'язки між ними. [[детальніше]](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model)
[![ER-модель](https://img.plantuml.biz/plantuml/svg/jLN9JiCm4BrRyZ_uLa12AeXU448KAAA2ifJ25OLaG1PPZ1SWBD_0aV_W0k8hmX_XE6cKnIb8Y6FcsM_UpFDCDeHqk5I1Zn5644egOpAEV22F616oG3soIeO74xAsThItlfx6GYS07JphZxTs--EvNdS-ZNeWN4wPf55O0fUwAVfSuZuLmDkv8N2etxXF27E4k8kuPu7iSeJYTY2axhKTOTILYgV0QB0zF1rjxXzkfd6NWoF1EtUaXhRxay5aE1gaW6AU3QXNM-gcqf_dfR9tyh8Nk3xJ1CfCWti6N581MphdLSJZ_pIeIFQJRZSNCrlxiQ8FlvOxzTMkTxdNco-RSX4tHFt5hsC5mcHiLNkZQx6rOhPS6RDoZIjPD5J1XPu6GrNLSSX-Kf7f_BsIObnQSvueVWln2GWnCtNRMsXhZDalDZlSA60-M25zHofHRrXPR3yKTxCMYSZAi0jjxvs4UscnxvBwzRrGwHpuuEf2AguvHg5rQY9cpsyuEoHvJTuwNo_9U_APV61aDkRJq-9Yz5Zi4upCLcb4wsUBGSQekK3ivweaPdHNyvaI69dl0iiQcKRpiScHh15rhie3grBL88ogZp4_bPdUJ3UDOvG_YobhnHUCSdzQK8ms8FJCd_0R)](https://editor.plantuml.com/uml/jLN9JiCm4BrRyZ_uLa12AeXU448KAAA2ifJ25OLaG1PPZ1SWBD_0aV_W0k8hmX_XE6cKnIb8Y6FcsM_UpFDCDeHqk5I1Zn5644egOpAEV22F616oG3soIeO74xAsThItlfx6GYS07JphZxTs--EvNdS-ZNeWN4wPf55O0fUwAVfSuZuLmDkv8N2etxXF27E4k8kuPu7iSeJYTY2axhKTOTILYgV0QB0zF1rjxXzkfd6NWoF1EtUaXhRxay5aE1gaW6AU3QXNM-gcqf_dfR9tyh8Nk3xJ1CfCWti6N581MphdLSJZ_pIeIFQJRZSNCrlxiQ8FlvOxzTMkTxdNco-RSX4tHFt5hsC5mcHiLNkZQx6rOhPS6RDoZIjPD5J1XPu6GrNLSSX-Kf7f_BsIObnQSvueVWln2GWnCtNRMsXhZDalDZlSA60-M25zHofHRrXPR3yKTxCMYSZAi0jjxvs4UscnxvBwzRrGwHpuuEf2AguvHg5rQY9cpsyuEoHvJTuwNo_9U_APV61aDkRJq-9Yz5Zi4upCLcb4wsUBGSQekK3ivweaPdHNyvaI69dl0iiQcKRpiScHh15rhie3grBL88ogZp4_bPdUJ3UDOvG_YobhnHUCSdzQK8ms8FJCd_0R)


## Реляційна схема

<center style="
    border-radius:4px;
    border: 1px solid #cfd7e6;
    box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
    padding: 1em;"
>

![Реляційна схема](img/relational_scheme.png)

</center>

