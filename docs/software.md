# Реалізація інформаційного та програмного забезпечення

В рамках проекту розробляється: 
- SQL-скрипт для створення на початкового наповнення бази даних
```sql
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `mydb` ;

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Role`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Role` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Role` (
  `id` INT NOT NULL,
  `name` VARCHAR(50) NOT NULL,
  `description` VARCHAR(100) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`User`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`User` ;

CREATE TABLE IF NOT EXISTS `mydb`.`User` (
  `id` INT NOT NULL,
  `picture` MEDIUMBLOB NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `email` VARCHAR(100) NOT NULL,
  `password` VARCHAR(100) NOT NULL,
  `name` VARCHAR(50) NOT NULL,
  `surname` VARCHAR(50) NOT NULL,
  `nickname` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`UserRole`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`UserRole` ;

CREATE TABLE IF NOT EXISTS `mydb`.`UserRole` (
  `User_id` INT NOT NULL,
  `Role_id` INT NOT NULL,
  INDEX `fk_UserRole_Role_idx` (`Role_id` ASC) VISIBLE,
  INDEX `fk_UserRole_User1_idx` (`User_id` ASC) VISIBLE,
  CONSTRAINT `fk_UserRole_Role`
    FOREIGN KEY (`Role_id`)
    REFERENCES `mydb`.`Role` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_UserRole_User1`
    FOREIGN KEY (`User_id`)
    REFERENCES `mydb`.`User` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Quiz`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Quiz` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Quiz` (
  `id` INT NOT NULL,
  `created_by` INT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `name` VARCHAR(100) NULL,
  `description` VARCHAR(255) NULL,
  `User_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Quiz_User1_idx` (`User_id` ASC) VISIBLE,
  CONSTRAINT `fk_Quiz_User1`
    FOREIGN KEY (`User_id`)
    REFERENCES `mydb`.`User` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`ExpertiseCategory`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`ExpertiseCategory` ;

CREATE TABLE IF NOT EXISTS `mydb`.`ExpertiseCategory` (
  `id` INT NOT NULL,
  `name` VARCHAR(50) NULL,
  `description` VARCHAR(100) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`UserExpertise`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`UserExpertise` ;

CREATE TABLE IF NOT EXISTS `mydb`.`UserExpertise` (
  `ExpertiseCategory_id` INT NOT NULL,
  `User_id` INT NOT NULL,
  INDEX `fk_UserExpertise_ExpertiseCategory1_idx` (`ExpertiseCategory_id` ASC) VISIBLE,
  INDEX `fk_UserExpertise_User1_idx` (`User_id` ASC) VISIBLE,
  CONSTRAINT `fk_UserExpertise_ExpertiseCategory1`
    FOREIGN KEY (`ExpertiseCategory_id`)
    REFERENCES `mydb`.`ExpertiseCategory` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_UserExpertise_User1`
    FOREIGN KEY (`User_id`)
    REFERENCES `mydb`.`User` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Question`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Question` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Question` (
  `id` INT NOT NULL,
  `Quiz_id` INT NOT NULL,
  `number` INT NULL,
  `description` VARCHAR(255) NULL,
  `type` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Question_Quiz1_idx` (`Quiz_id` ASC) VISIBLE,
  CONSTRAINT `fk_Question_Quiz1`
    FOREIGN KEY (`Quiz_id`)
    REFERENCES `mydb`.`Quiz` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`SurveySession`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`SurveySession` ;

CREATE TABLE IF NOT EXISTS `mydb`.`SurveySession` (
  `id` INT NOT NULL,
  `User_id` INT NOT NULL,
  `Quiz_id` INT NOT NULL,
  `started_at` DATETIME NULL,
  `completed_at` DATETIME NULL,
  `status` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_SurveySession_User1_idx` (`User_id` ASC) VISIBLE,
  INDEX `fk_SurveySession_Quiz1_idx` (`Quiz_id` ASC) VISIBLE,
  CONSTRAINT `fk_SurveySession_User1`
    FOREIGN KEY (`User_id`)
    REFERENCES `mydb`.`User` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_SurveySession_Quiz1`
    FOREIGN KEY (`Quiz_id`)
    REFERENCES `mydb`.`Quiz` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Option`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Option` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Option` (
  `id` INT NOT NULL,
  `Question_id` INT NOT NULL,
  `number` INT NULL,
  `description` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Option_Question1_idx` (`Question_id` ASC) VISIBLE,
  CONSTRAINT `fk_Option_Question1`
    FOREIGN KEY (`Question_id`)
    REFERENCES `mydb`.`Question` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Answer`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Answer` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Answer` (
  `id` INT NOT NULL,
  `SurveySession_id` INT NOT NULL,
  `Question_id` INT NOT NULL,
  `file` MEDIUMBLOB NULL,
  `text` VARCHAR(255) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Answer_Question1_idx` (`Question_id` ASC) VISIBLE,
  INDEX `fk_Answer_SurveySession1_idx` (`SurveySession_id` ASC) VISIBLE,
  CONSTRAINT `fk_Answer_Question1`
    FOREIGN KEY (`Question_id`)
    REFERENCES `mydb`.`Question` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Answer_SurveySession1`
    FOREIGN KEY (`SurveySession_id`)
    REFERENCES `mydb`.`SurveySession` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`SelectedOption`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`SelectedOption` ;

CREATE TABLE IF NOT EXISTS `mydb`.`SelectedOption` (
  `Answer_id` INT NOT NULL,
  `Option_id` INT NOT NULL,
  INDEX `fk_SelectedOption_Option1_idx` (`Option_id` ASC) VISIBLE,
  INDEX `fk_SelectedOption_Answer1_idx` (`Answer_id` ASC) VISIBLE,
  CONSTRAINT `fk_SelectedOption_Option1`
    FOREIGN KEY (`Option_id`)
    REFERENCES `mydb`.`Option` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_SelectedOption_Answer1`
    FOREIGN KEY (`Answer_id`)
    REFERENCES `mydb`.`Answer` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
 ```

# Insert script
```sql
-- Role
INSERT INTO Role (id, name, description) VALUES (1, 'Admin', 'Administrator role');

-- User
INSERT INTO User (id, picture, created_at, updated_at, email, password, name, surname, nickname)
VALUES (1, NULL, NOW(), NOW(), 'user@example.com', 'hashed_password', 'John', 'Doe', 'jdoe');

-- UserRole
INSERT INTO UserRole (User_id, Role_id) VALUES (1, 1);

-- ExpertiseCategory
INSERT INTO ExpertiseCategory (id, name, description) VALUES (1, 'Math', 'Mathematics Expert');

-- UserExpertise
INSERT INTO UserExpertise (ExpertiseCategory_id, User_id) VALUES (1, 1);

-- Quiz
INSERT INTO Quiz (id, created_by, created_at, updated_at, name, description, User_id)
VALUES (1, 1, NOW(), NOW(), 'General Quiz', 'Basic questions', 1);

-- Question
INSERT INTO Question (id, Quiz_id, number, description, type)
VALUES (1, 1, 1, 'What is 2+2?', 'single-choice');

-- Option
INSERT INTO Option (id, Question_id, number, description)
VALUES (1, 1, 1, 4); -- Note: description should be VARCHAR, not INT

-- SurveySession
INSERT INTO SurveySession (id, User_id, Quiz_id, started_at, completed_at, status)
VALUES (1, 1, 1, NOW(), NULL, 'in_progress');

-- Answer
INSERT INTO Answer (id, SurveySession_id, Question_id, file, text)
VALUES (1, 1, 1, NULL, '4');

-- SelectedOption
INSERT INTO SelectedOption (Answer_id, Option_id) VALUES (1, 1);

```
- RESTfull сервіс для управління даними

