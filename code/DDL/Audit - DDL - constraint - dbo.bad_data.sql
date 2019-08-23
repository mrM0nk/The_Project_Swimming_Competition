USE [Audit]
GO

/*
IF EXISTS(SELECT 1 
          FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS 
          WHERE CONSTRAINT_NAME = 'BK_bad_data_process_load_status_id_error_datetime')
    ALTER TABLE dbo.bad_data
    DROP CONSTRAINT BK_bad_data_process_load_status_id_error_datetime
GO

ALTER TABLE dbo.bad_data
    ADD CONSTRAINT BK_bad_data_process_load_status_id_error_datetime UNIQUE
(
    process_load_status_id,
    error_datetime
)
GO
*/

IF OBJECT_ID('DF_bad_data_modified_date', 'D') IS NOT NULL
    ALTER TABLE dbo.bad_data 
    DROP CONSTRAINT DF_bad_data_modified_date
GO

ALTER TABLE dbo.bad_data
    ADD CONSTRAINT DF_bad_data_modified_date 
    DEFAULT (GETDATE()) FOR modified_date
GO


IF EXISTS(SELECT 1
          FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
          WHERE CONSTRAINT_NAME = 'FK_process_load_status_bad_data')
    ALTER TABLE dbo.bad_data
    DROP CONSTRAINT FK_process_load_status_bad_data
GO

ALTER TABLE dbo.bad_data
    ADD CONSTRAINT FK_process_load_status_bad_data 
    FOREIGN KEY (process_load_status_id) 
    REFERENCES dbo.process_load_status (process_load_status_id)
GO