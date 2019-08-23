USE [Audit]
GO


IF EXISTS(SELECT 1 
          FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS 
          WHERE CONSTRAINT_NAME = 'BK_process_load_status_process_name_start_process')
    ALTER TABLE dbo.process_load_status
    DROP CONSTRAINT BK_process_load_status_process_name_start_process
GO

ALTER TABLE dbo.process_load_status
    ADD CONSTRAINT BK_process_load_status_process_name_start_process UNIQUE
(
    process_name,
    start_process
)
GO


IF OBJECT_ID('DF_process_load_status_modified_date', 'D') IS NOT NULL
    ALTER TABLE dbo.process_load_status 
    DROP CONSTRAINT DF_process_load_status_modified_date
GO

ALTER TABLE dbo.process_load_status
    ADD CONSTRAINT DF_process_load_status_modified_date 
    DEFAULT (GETDATE()) FOR modified_date
GO