USE [Audit]
GO


IF OBJECT_ID('dbo.process_load_status', 'U') IS NOT NULL
    DROP TABLE dbo.process_load_status
GO

CREATE TABLE dbo.process_load_status
(
    process_load_status_id  INT            NOT NULL  IDENTITY,
    process_name            NVARCHAR(255)  NOT NULL,
    start_process           DATETIME       NOT NULL,
    end_process             DATETIME,
    insert_count            INT,
    delete_count            INT,
    update_count            INT,
    modified_date           DATETIME       NOT NULL,

    CONSTRAINT PK_process_load_status PRIMARY KEY (
        process_load_status_id
    )
)
GO