USE SwimmingCompetitionStaging
GO

/*
IF EXISTS(SELECT 1 
          FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS 
          WHERE CONSTRAINT_NAME = 'AK_stg_discipline_style_distance')
    ALTER TABLE dbo.stg_discipline 
    DROP CONSTRAINT AK_stg_discipline_style_distance
GO

ALTER TABLE dbo.stg_discipline
    ADD CONSTRAINT AK_stg_discipline_style_distance UNIQUE
(
    style,
    distance
)
GO
*/


IF OBJECT_ID('DF_stg_discipline_distance', 'D') IS NOT NULL
    ALTER TABLE dbo.stg_discipline 
    DROP CONSTRAINT DF_stg_discipline_distance
GO

ALTER TABLE dbo.stg_discipline
    ADD CONSTRAINT DF_stg_discipline_distance 
    DEFAULT (-1) FOR distance
GO


IF OBJECT_ID('DF_stg_discipline_modified_date', 'D') IS NOT NULL
    ALTER TABLE dbo.stg_discipline 
    DROP CONSTRAINT DF_stg_discipline_modified_date
GO

ALTER TABLE dbo.stg_discipline
    ADD CONSTRAINT DF_stg_discipline_modified_date 
    DEFAULT (GETDATE()) FOR modified_date
GO