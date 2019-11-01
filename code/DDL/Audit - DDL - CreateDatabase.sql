USE [master]
GO

IF EXISTS (SELECT NAME 
           FROM master.dbo.sysdatabases 
           WHERE NAME = N'Audit')
DROP DATABASE [Audit]
GO

CREATE DATABASE [Audit]
GO

ALTER DATABASE [Audit] SET RECOVERY SIMPLE 
GO
