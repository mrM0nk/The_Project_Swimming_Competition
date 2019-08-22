USE SwimmingCompetitionStaging
GO

IF OBJECT_ID('dbo.stg_group', 'U') IS NOT NULL
    DROP TABLE dbo.stg_group
GO

CREATE TABLE dbo.stg_group
(
    group_id       INT           NOT NULL  IDENTITY,
    [name]         NVARCHAR(30)  NOT NULL,
    gender         CHAR(1)       NOT NULL,
    modified_date  DATETIME      NOT NULL,

    CONSTRAINT PK_stg_group PRIMARY KEY (
        group_id
	)
)
GO