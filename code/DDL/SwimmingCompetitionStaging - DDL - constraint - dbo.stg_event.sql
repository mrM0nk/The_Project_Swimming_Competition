USE SwimmingCompetitionStaging
GO

/*
IF EXISTS(SELECT 1 
          FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS 
          WHERE CONSTRAINT_NAME = 'AK_stg_event_name')
    ALTER TABLE dbo.stg_event 
    DROP CONSTRAINT AK_stg_event_name
GO

ALTER TABLE dbo.stg_event
    ADD CONSTRAINT AK_stg_event_name UNIQUE
(
    [name]
)
GO
*/


IF OBJECT_ID('DF_stg_event_modified_date', 'D') IS NOT NULL
    ALTER TABLE dbo.stg_event 
    DROP CONSTRAINT DF_stg_event_modified_date
GO

ALTER TABLE dbo.stg_event
    ADD CONSTRAINT DF_stg_event_modified_date 
    DEFAULT (GETDATE()) FOR modified_date
GO