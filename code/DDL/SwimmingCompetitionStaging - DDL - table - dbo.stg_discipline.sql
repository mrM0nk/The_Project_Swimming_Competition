USE SwimmingCompetitionStaging
GO

IF OBJECT_ID('dbo.stg_discipline', 'U') IS NOT NULL
    DROP TABLE dbo.stg_discipline
GO

CREATE TABLE dbo.stg_discipline
(
    discipline_id  INT           NOT NULL  IDENTITY,
    style          NVARCHAR(30)  NOT NULL,
    distance       SMALLINT      NOT NULL,
    modified_date  DATETIME      NOT NULL,

    CONSTRAINT PK_stg_discipline PRIMARY KEY (
        discipline_id
    )
)
GO