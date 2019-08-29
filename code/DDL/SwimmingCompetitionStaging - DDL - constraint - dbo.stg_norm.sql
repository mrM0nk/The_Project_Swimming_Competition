USE SwimmingCompetitionStaging
GO

/*
IF EXISTS(SELECT 1 
          FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS 
          WHERE CONSTRAINT_NAME = 'AK_stg_norm_country_gender_pool_size_style_distance_rank_name')
    ALTER TABLE dbo.stg_norm
    DROP CONSTRAINT AK_stg_norm_country_gender_pool_size_style_distance_rank_name
GO

ALTER TABLE dbo.stg_norm
    ADD CONSTRAINT AK_stg_norm_country_gender_pool_size_style_distance_rank_name UNIQUE
(
    country,
    gender,
    pool_size,
    style,
    distance,
    rank_name
)
GO
*/

IF OBJECT_ID('DF_stg_norm_country', 'D') IS NOT NULL
    ALTER TABLE dbo.stg_norm 
    DROP CONSTRAINT DF_stg_norm_country
GO

ALTER TABLE dbo.stg_norm
    ADD CONSTRAINT DF_stg_norm_country
    DEFAULT ('-') FOR country
GO


IF OBJECT_ID('DF_stg_norm_gender', 'D') IS NOT NULL
    ALTER TABLE dbo.stg_norm 
    DROP CONSTRAINT DF_stg_norm_gender
GO

ALTER TABLE dbo.stg_norm
    ADD CONSTRAINT DF_stg_norm_gender
    DEFAULT ('-') FOR gender
GO


IF OBJECT_ID('DF_stg_norm_pool_size', 'D') IS NOT NULL
    ALTER TABLE dbo.stg_norm 
    DROP CONSTRAINT DF_stg_norm_pool_size
GO

ALTER TABLE dbo.stg_norm
    ADD CONSTRAINT DF_stg_norm_pool_size
    DEFAULT (0) FOR pool_size
GO


IF OBJECT_ID('DF_stg_norm_style', 'D') IS NOT NULL
    ALTER TABLE dbo.stg_norm 
    DROP CONSTRAINT DF_stg_norm_style
GO

ALTER TABLE dbo.stg_norm
    ADD CONSTRAINT DF_stg_norm_style
    DEFAULT ('-') FOR style
GO


IF OBJECT_ID('DF_stg_norm_distance', 'D') IS NOT NULL
    ALTER TABLE dbo.stg_norm 
    DROP CONSTRAINT DF_stg_norm_distance
GO

ALTER TABLE dbo.stg_norm
    ADD CONSTRAINT DF_stg_norm_distance
    DEFAULT (0) FOR distance
GO


IF OBJECT_ID('DF_stg_norm_rank_name', 'D') IS NOT NULL
    ALTER TABLE dbo.stg_norm 
    DROP CONSTRAINT DF_stg_norm_rank_name
GO

ALTER TABLE dbo.stg_norm
    ADD CONSTRAINT DF_stg_norm_rank_name
    DEFAULT ('-') FOR rank_name
GO


IF OBJECT_ID('DF_stg_norm_time', 'D') IS NOT NULL
    ALTER TABLE dbo.stg_norm 
    DROP CONSTRAINT DF_stg_norm_time
GO

ALTER TABLE dbo.stg_norm
    ADD CONSTRAINT DF_stg_norm_time
    DEFAULT ('00:00:00.00') FOR [time]
GO


IF OBJECT_ID('DF_stg_norm_modified_date', 'D') IS NOT NULL
    ALTER TABLE dbo.stg_norm 
    DROP CONSTRAINT DF_stg_norm_modified_date
GO

ALTER TABLE dbo.stg_norm
    ADD CONSTRAINT DF_stg_norm_modified_date 
    DEFAULT (GETDATE()) FOR modified_date
GO