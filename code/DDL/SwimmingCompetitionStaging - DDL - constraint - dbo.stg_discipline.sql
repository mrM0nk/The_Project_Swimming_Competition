USE SwimmingCompetitionStaging
GO


IF OBJECT_ID('DF_stg_discipline_modified_date', 'D') IS NOT NULL
    ALTER TABLE dbo.stg_discipline 
    DROP CONSTRAINT DF_stg_discipline_modified_date
GO

ALTER TABLE dbo.stg_discipline
    ADD CONSTRAINT DF_stg_discipline_modified_date 
    DEFAULT (GETDATE()) FOR modified_date
GO