# Проєктування бази даних

## Mодель бізнес-об'єктів

## ER-модель
<center style="
    border-radius:4px;
    border: 1px solid #cfd7e6;
    box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
    padding: 1em;">

@startuml

    package UserControl {
        entity User
        {
            id: INT
            firstname: MEDIUMTEXT
            lastname: MEDIUMTEXT
            nickname: MEDIUMTEXT
            email: MEDIUMTEXT
            password: MEDIUMTEXT
        }
    }
    package PermissionControl {
    entity Grant    
        {
            id: INT
            appointed: DATE
        }

        entity Role
        {
            id: INT
            name: TINYTEXT
        }
    
        entity Permission
        {
            id: INT
            name: TINYTEXT
        }
    }

    package SurveyControl {
        entity Survey
        {
        id: INT
        title: MEDIUMTEXT
        description: LONGTEXT
        created: DATE
        }

        entity Answer
        {
            id: INT
            text: MEDIUMTEXT
        }
 
        entity Question
        {
            id: INT
            text: MEDIUMTEXT
            type: TINYTEXT
        }
    
        entity Action
        {
            id: INT
            date: DATE
        }
    
        entity State
        {
            id: INT
            name: TINYTEXT
        }
    }
    User "0,*"--"1,1" Role
    Grant "0,*"--"1,1" Role
    User "1,1"--"0,*" Answer
    User "1,1"--"0,*" Survey
    Survey "1,1"*--"0,*" Question
    Role "1,1"--"0,*" Action
    Survey "1,1"--"0,*" Action
    Answer "0,*"--*"1,1" Question
    Grant "0,*"--"1,1" Permission
    Action "0,*"--"1,1" State

@enduml

</center>

## Реляційна схема

## Реляційна схема
