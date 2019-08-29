USE SwimmingCompetitionStaging
GO


IF OBJECT_ID('dbo.stg_norm', 'U') IS NOT NULL
    TRUNCATE TABLE dbo.stg_norm
GO