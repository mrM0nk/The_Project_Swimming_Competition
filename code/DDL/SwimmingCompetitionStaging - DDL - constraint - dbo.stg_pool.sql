USE SwimmingCompetitionStaging
GO

/*
IF EXISTS(SELECT 1 
          FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS 
          WHERE CONSTRAINT_NAME = 'AK_stg_pool_name_city')
    ALTER TABLE dbo.stg_pool 
    DROP CONSTRAINT AK_stg_pool_name_city
GO

ALTER TABLE dbo.stg_pool
    ADD CONSTRAINT AK_stg_pool_name_city UNIQUE
(
    [name],
    city
)
GO
*/

IF OBJECT_ID('DF_stg_pool_name', 'D') IS NOT NULL
    ALTER TABLE dbo.stg_pool 
    DROP CONSTRAINT DF_stg_pool_name
GO

ALTER TABLE dbo.stg_pool
    ADD CONSTRAINT DF_stg_pool_name 
    DEFAULT ('-') FOR [name]
GO


IF OBJECT_ID('DF_stg_pool_city', 'D') IS NOT NULL
    ALTER TABLE dbo.stg_pool 
    DROP CONSTRAINT DF_stg_pool_city
GO

ALTER TABLE dbo.stg_pool
    ADD CONSTRAINT DF_stg_pool_city 
    DEFAULT ('-') FOR city
GO


IF OBJECT_ID('DF_stg_pool_pool_size', 'D') IS NOT NULL
    ALTER TABLE dbo.stg_pool 
    DROP CONSTRAINT DF_stg_pool_pool_size
GO

ALTER TABLE dbo.stg_pool
    ADD CONSTRAINT DF_stg_pool_pool_size 
    DEFAULT (0) FOR pool_size
GO


IF OBJECT_ID('DF_stg_pool_modified_date', 'D') IS NOT NULL
    ALTER TABLE dbo.stg_pool 
    DROP CONSTRAINT DF_stg_pool_modified_date
GO

ALTER TABLE dbo.stg_pool
    ADD CONSTRAINT DF_stg_pool_modified_date 
    DEFAULT (GETDATE()) FOR modified_date
GO