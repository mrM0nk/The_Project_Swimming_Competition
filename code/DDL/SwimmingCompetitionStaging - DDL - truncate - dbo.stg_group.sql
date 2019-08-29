USE SwimmingCompetitionStaging
GO


IF OBJECT_ID('dbo.stg_group', 'U') IS NOT NULL
    TRUNCATE TABLE dbo.stg_group
GO