USE SwimmingCompetitionStaging
GO

/*
IF EXISTS(SELECT 1 
          FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS 
          WHERE CONSTRAINT_NAME = 'AK_stg_result_competition_id_first_name_last_name_birth_year_gender')
    ALTER TABLE dbo.stg_result
    DROP CONSTRAINT AK_stg_result_competition_id_first_name_last_name_birth_year_gender
GO

ALTER TABLE dbo.stg_result
    ADD CONSTRAINT AK_stg_result_competition_id_first_name_last_name_birth_year_gender UNIQUE
(
    competition_id,
    first_name,
    last_name,
    bitrh_year,
    gender
)
GO
*/

IF OBJECT_ID('DF_stg_result_competition_id', 'D') IS NOT NULL
    ALTER TABLE dbo.stg_result 
    DROP CONSTRAINT DF_stg_result_competition_id
GO

ALTER TABLE dbo.stg_result
    ADD CONSTRAINT DF_stg_result_competition_id
    DEFAULT (0) FOR competition_id
GO


IF OBJECT_ID('DF_stg_result_first_name', 'D') IS NOT NULL
    ALTER TABLE dbo.stg_result 
    DROP CONSTRAINT DF_stg_result_first_name
GO

ALTER TABLE dbo.stg_result
    ADD CONSTRAINT DF_stg_result_first_name
    DEFAULT ('-') FOR first_name
GO


IF OBJECT_ID('DF_stg_result_last_name', 'D') IS NOT NULL
    ALTER TABLE dbo.stg_result 
    DROP CONSTRAINT DF_stg_result_last_name
GO

ALTER TABLE dbo.stg_result
    ADD CONSTRAINT DF_stg_result_last_name
    DEFAULT ('-') FOR last_name
GO


IF OBJECT_ID('DF_stg_result_birth_year', 'D') IS NOT NULL
    ALTER TABLE dbo.stg_result 
    DROP CONSTRAINT DF_stg_result_birth_year
GO

ALTER TABLE dbo.stg_result
    ADD CONSTRAINT DF_stg_result_birth_year
    DEFAULT (0) FOR birth_year
GO


IF OBJECT_ID('DF_stg_result_gender', 'D') IS NOT NULL
    ALTER TABLE dbo.stg_result 
    DROP CONSTRAINT DF_stg_result_gender
GO

ALTER TABLE dbo.stg_result
    ADD CONSTRAINT DF_stg_result_gender
    DEFAULT ('-') FOR gender
GO


IF OBJECT_ID('DF_stg_result_modified_date', 'D') IS NOT NULL
    ALTER TABLE dbo.stg_result 
    DROP CONSTRAINT DF_stg_result_modified_date
GO

ALTER TABLE dbo.stg_result
    ADD CONSTRAINT DF_stg_result_modified_date 
    DEFAULT (GETDATE()) FOR modified_date
GO


IF EXISTS(SELECT 1
          FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
          WHERE CONSTRAINT_NAME = 'FK_stg_result_stg_competition')
    ALTER TABLE dbo.stg_result
    DROP CONSTRAINT FK_stg_result_stg_competition
GO

ALTER TABLE dbo.stg_result
    ADD CONSTRAINT FK_stg_result_stg_competition 
    FOREIGN KEY (competition_id) 
    REFERENCES dbo.stg_competition (competition_id)
GO