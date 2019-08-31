USE SwimmingCompetitionStaging
GO


IF OBJECT_ID('dbo.stg_event', 'U') IS NOT NULL
    DROP TABLE dbo.stg_event
GO

CREATE TABLE dbo.stg_event
(
    event_id       INT            NOT NULL  IDENTITY,
    [name]         NVARCHAR(255)  NOT NULL,
    [description]  NVARCHAR(MAX),
    modified_date  DATETIME       NOT NULL,

    CONSTRAINT PK_stg_event PRIMARY KEY (
        event_id
    )
)
GO