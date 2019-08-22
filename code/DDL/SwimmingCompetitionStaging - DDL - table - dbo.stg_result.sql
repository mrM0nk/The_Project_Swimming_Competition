USE SwimmingCompetitionStaging
GO

IF OBJECT_ID('dbo.stg_result', 'U') IS NOT NULL
    DROP TABLE dbo.stg_result
GO

CREATE TABLE dbo.stg_result
(
    result_id       INT           NOT NULL  IDENTITY,
    competition_id  INT           NOT NULL,
    first_name      NVARCHAR(50)  NOT NULL,
    last_name       NVARCHAR(50)  NOT NULL,
    birth_year      SMALLINT      NOT NULL,
    gender          CHAR(1)       NOT NULL,
    club_name       NVARCHAR(50),
    club_city       NVARCHAR(30),
    club_country    NVARCHAR(40),
    rank_start      NVARCHAR(20),
    result_time     TIME(2),
    dsq             VARCHAR(3),
    reason          NVARCHAR(20),
    duration        NVARCHAR(50),
    record_date     DATE,
    modified_date   DATETIME      NOT NULL,

    CONSTRAINT PK_stg_result PRIMARY KEY (
        result_id
    )
)
GO