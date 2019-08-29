USE SwimmingCompetitionStaging
GO


IF OBJECT_ID('dbo.stg_competition', 'U') IS NOT NULL
    TRUNCATE TABLE dbo.stg_competition
GO