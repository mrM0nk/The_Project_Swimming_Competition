USE [master]
GO

IF EXISTS (SELECT NAME 
           FROM master.dbo.sysdatabases 
           WHERE NAME = N'SwimmingCompetitionStaging')
DROP DATABASE [SwimmingCompetitionStaging]
GO

CREATE DATABASE SwimmingCompetitionStaging
GO

ALTER DATABASE SwimmingCompetitionStaging SET RECOVERY SIMPLE 
GO
