USE SwimmingCompetitionStaging
GO

IF OBJECT_ID('dbo.stg_norm', 'U') IS NOT NULL
    DROP TABLE dbo.stg_norm
GO

CREATE TABLE dbo.stg_norm
(
    norm_id        INT           NOT NULL  IDENTITY,
    country        NVARCHAR(40)  NOT NULL,
    gender         CHAR(1)       NOT NULL,
    pool_size      SMALLINT      NOT NULL,
    style          NVARCHAR(30)  NOT NULL,
    distance       SMALLINT      NOT NULL,
    rank_name      NVARCHAR(20)  NOT NULL,
    [time]         TIME(2)       NOT NULL,
    modified_date  DATETIME      NOT NULL,

    CONSTRAINT PK_stg_norm PRIMARY KEY (
        norm_id
    )
)
GO