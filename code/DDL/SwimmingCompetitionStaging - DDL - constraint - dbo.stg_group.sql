USE SwimmingCompetitionStaging
GO

/*
IF EXISTS(SELECT 1 
          FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS 
          WHERE CONSTRAINT_NAME = 'AK_stg_group_name_gender')
    ALTER TABLE dbo.stg_group 
    DROP CONSTRAINT AK_stg_group_name_gender
GO

ALTER TABLE dbo.stg_group
    ADD CONSTRAINT AK_stg_group_name_gender UNIQUE
(
    [name],
    gender
)
GO
*/

IF OBJECT_ID('DF_stg_group_modified_date', 'D') IS NOT NULL
    ALTER TABLE dbo.stg_group 
    DROP CONSTRAINT DF_stg_group_modified_date
GO

ALTER TABLE dbo.stg_group
    ADD CONSTRAINT DF_stg_group_modified_date 
    DEFAULT (GETDATE()) FOR modified_date
GO