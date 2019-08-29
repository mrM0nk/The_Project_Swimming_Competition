USE SwimmingCompetitionStaging
GO


IF OBJECT_ID('dbo.stg_discipline', 'U') IS NOT NULL
    TRUNCATE TABLE dbo.stg_discipline
GO