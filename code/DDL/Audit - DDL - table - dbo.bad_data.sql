USE [Audit]
GO


IF OBJECT_ID('dbo.bad_data', 'U') IS NOT NULL
    DROP TABLE dbo.bad_data
GO

CREATE TABLE dbo.bad_data
(
    bad_data_id             INT            NOT NULL  IDENTITY,
    process_load_status_id  INT            NOT NULL,
    error_datetime          DATETIME2(6)   NOT NULL,
    source_name             NVARCHAR(255)  NOT NULL,
    [row]                   INT            NOT NULL,
    [column]                INT            NOT NULL,
    [data]                  NVARCHAR(MAX),
    [error_number]          INT,
    error_description       NVARCHAR(MAX),
    modified_date           DATETIME       NOT NULL,

    CONSTRAINT PK_bad_data PRIMARY KEY (
        bad_data_id
    )
)
GO