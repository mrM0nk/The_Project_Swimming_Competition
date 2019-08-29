USE SwimmingCompetitionStaging
GO


IF OBJECT_ID('dbo.stg_competition', 'U') IS NOT NULL
    DROP TABLE dbo.stg_competition
GO

CREATE TABLE dbo.stg_competition
(
    competition_id   INT           NOT NULL  IDENTITY,
    event_id         INT           NOT NULL,
    pool_id          INT           NOT NULL,
    discipline_id    INT           NOT NULL,
    group_id         INT           NOT NULL,
    [date]           DATE          NOT NULL,
    city             NVARCHAR(30)  NOT NULL,
    country          NVARCHAR(40)  NOT NULL,
    chief_judge      NVARCHAR(50),
    chief_secretary  NVARCHAR(50),
    modified_date    DATETIME      NOT NULL,

    CONSTRAINT PK_stg_competition PRIMARY KEY (
        competition_id
    )
)
GO