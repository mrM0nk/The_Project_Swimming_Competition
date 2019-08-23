USE SwimmingCompetitionStaging
GO


IF OBJECT_ID('dbo.stg_event', 'U') IS NOT NULL
    TRUNCATE TABLE dbo.stg_event
GO