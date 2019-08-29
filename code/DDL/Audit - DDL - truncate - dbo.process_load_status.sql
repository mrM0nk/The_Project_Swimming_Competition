USE [Audit]
GO


IF OBJECT_ID('dbo.process_load_status', 'U') IS NOT NULL
    TRUNCATE TABLE dbo.process_load_status
GO