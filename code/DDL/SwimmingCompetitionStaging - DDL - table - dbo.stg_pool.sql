USE SwimmingCompetitionStaging
GO


IF OBJECT_ID('dbo.stg_pool', 'U') IS NOT NULL
    DROP TABLE dbo.stg_pool
GO

CREATE TABLE dbo.stg_pool
(
    pool_id        INT           NOT NULL  IDENTITY,
    [name]         NVARCHAR(50)  NOT NULL,
    city           NVARCHAR(30)  NOT NULL,
    country        NVARCHAR(40),
    pool_size      SMALLINT      NOT NULL,
    modified_date  DATETIME      NOT NULL,

    CONSTRAINT PK_stg_pool PRIMARY KEY (
        pool_id
    )
)
GO