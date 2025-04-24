# Проєктування бази даних

## Mодель бізнес-об'єктів

## ER-модель
**ER-модель** описує сутності системи та визначає зв'язки між ними. [[детальніше]](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model)
<!--
@startuml
left to right direction
  entity "User" {
    + id: UUID
    + first_name: VARCHAR
    + last_name: VARCHAR
    + email: VARCHAR
    + password: VARCHAR
    + phone_number: VARCHAR
    + age: SMALLINT
    + status: VARCHAR
  }
  
  entity "Role" {
    + id: UUID
    + name: VARCHAR
    + description: TEXT
  }
  
  entity "User_Role" {
    + user_id: UUID
    + role_id: UUID
  }
  
  entity "Survey" {
    + id: UUID
    + title: VARCHAR
    + description: TEXT
    + creation_date: DATETIME
    + close_date: DATETIME
    + is_active: BOOLEAN
    + owner_id: UUID
    + status: VARCHAR
  }
  
  entity "Question" {
    + id: UUID
    + survey_id: UUID
    + header: VARCHAR
    + description: TEXT
    + order_number: INT
    + required: BOOLEAN
  }
  
  entity "Variant" {
    + id: UUID
    + text: TEXT
    + question_id: UUID
    + order_number: INT
  }
  
  entity "Answer" {
    + id: UUID
    + content: TEXT
    + user_id: UUID
    + question_id: UUID
    + answer_date: DATETIME
    + variant_id: UUID
  }
  
  entity "Statistics" {
    + id: UUID
    + survey_id: UUID
    + creation_date: DATETIME
    + data: JSON
  }
  
  entity "SurveyShare" {
    + id: UUID
    + survey_id: UUID
    + email: VARCHAR
    + access_token: VARCHAR
    + share_date: DATETIME
    + expiry_date: DATETIME
  }
  
  entity "ExportData" {
    + id: UUID
    + survey_id: UUID
    + export_date: DATETIME
    + format: VARCHAR
    + file_path: VARCHAR
    + user_id: UUID
  }
  
  entity "ExpertInvitation" {
    + id: UUID
    + survey_id: UUID
    + email: VARCHAR
    + invitation_date: DATETIME
    + status: VARCHAR
    + token: VARCHAR
  }
  
  entity "AnalyticalReport" {
    + id: UUID
    + survey_id: UUID
    + title: VARCHAR
    + description: TEXT
    + creation_date: DATETIME
    + data: JSON
    + creator_id: UUID
  }
  
  entity "SurveyTemplate" {
    + id: UUID
    + name: VARCHAR
    + description: TEXT
    + creation_date: DATETIME
    + creator_id: UUID
  }
  
  entity "MultimediaContent" {
    + id: UUID
    + question_id: UUID
    + type: VARCHAR
    + content_path: VARCHAR
    + description: TEXT
  }
  
  entity "SecurityLog" {
    + id: UUID
    + user_id: UUID
    + action: VARCHAR
    + timestamp: DATETIME
    + ip_address: VARCHAR
    + status: VARCHAR
  }
  
 
  
  User ||--o{ User_Role
  Role ||--o{ User_Role
  
  User ||--o{ Survey : creates/owns
  User ||--o{ Answer : provides
  User ||--o{ ExportData : exports
  User ||--o{ AnalyticalReport : creates
  User ||--o{ SurveyTemplate : creates
  User ||--o{ SecurityLog : generates
  
  Survey ||--o{ Question : contains
  Survey ||--o{ Statistics : has
  Survey ||--o{ ExpertInvitation : has
  Survey ||--o{ SurveyShare : access to
  Survey ||--o{ ExportData : exported as
  Survey ||--o{ AnalyticalReport : analyzed in
  Survey }o--|| SurveyTemplate : based on
  
  Question ||--o{ Variant : has options
  Question ||--o{ Answer : has answers
  Question ||--o{ MultimediaContent : includes
  
  Answer }o--o| Variant : selected option

@enduml
-->
![ER-модель](img/ER-model.png)
## Реляційна схема

