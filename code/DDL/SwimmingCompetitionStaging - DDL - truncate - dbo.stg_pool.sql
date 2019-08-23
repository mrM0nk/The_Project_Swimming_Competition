USE SwimmingCompetitionStaging
GO


IF OBJECT_ID('dbo.stg_pool', 'U') IS NOT NULL
    TRUNCATE TABLE dbo.stg_pool
GO