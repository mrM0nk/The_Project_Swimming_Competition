USE SwimmingCompetitionStaging
GO


IF OBJECT_ID('dbo.stg_result', 'U') IS NOT NULL
    TRUNCATE TABLE dbo.stg_result
GO