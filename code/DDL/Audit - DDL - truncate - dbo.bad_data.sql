USE [Audit]
GO


IF OBJECT_ID('dbo.bad_data', 'U') IS NOT NULL
    TRUNCATE TABLE dbo.bad_data
GO