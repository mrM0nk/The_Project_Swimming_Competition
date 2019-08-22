USE SwimmingCompetitionStaging
GO


IF OBJECT_ID('DF_stg_competition_event_id', 'D') IS NOT NULL
    ALTER TABLE dbo.stg_competition 
    DROP CONSTRAINT DF_stg_competition_event_id
GO

ALTER TABLE dbo.stg_competition
    ADD CONSTRAINT DF_stg_competition_event_id 
    DEFAULT (0) FOR event_id 
GO


IF OBJECT_ID('DF_stg_competition_pool_id', 'D') IS NOT NULL
    ALTER TABLE dbo.stg_competition 
    DROP CONSTRAINT DF_stg_competition_pool_id
GO

ALTER TABLE dbo.stg_competition
    ADD CONSTRAINT DF_stg_competition_pool_id 
    DEFAULT (0) FOR pool_id 
GO


IF OBJECT_ID('DF_stg_competition_discipline_id', 'D') IS NOT NULL
    ALTER TABLE dbo.stg_competition 
    DROP CONSTRAINT DF_stg_competition_discipline_id
GO

ALTER TABLE dbo.stg_competition
    ADD CONSTRAINT DF_stg_competition_discipline_id 
    DEFAULT (0) FOR discipline_id 
GO


IF OBJECT_ID('DF_stg_competition_group_id', 'D') IS NOT NULL
    ALTER TABLE dbo.stg_competition 
    DROP CONSTRAINT DF_stg_competition_group_id
GO

ALTER TABLE dbo.stg_competition
    ADD CONSTRAINT DF_stg_competition_group_id 
    DEFAULT (0) FOR group_id 
GO


IF OBJECT_ID('DF_stg_competition_city', 'D') IS NOT NULL
    ALTER TABLE dbo.stg_competition 
    DROP CONSTRAINT DF_stg_competition_city
GO

ALTER TABLE dbo.stg_competition
    ADD CONSTRAINT DF_stg_competition_city 
    DEFAULT ('-') FOR city
GO


IF OBJECT_ID('DF_stg_competition_country', 'D') IS NOT NULL
    ALTER TABLE dbo.stg_competition 
    DROP CONSTRAINT DF_stg_competition_country
GO

ALTER TABLE dbo.stg_competition
    ADD CONSTRAINT DF_stg_competition_country 
    DEFAULT ('-') FOR country
GO


IF OBJECT_ID('DF_stg_competition_modified_date', 'D') IS NOT NULL
    ALTER TABLE dbo.stg_competition 
    DROP CONSTRAINT DF_stg_competition_modified_date
GO

ALTER TABLE dbo.stg_competition
    ADD CONSTRAINT DF_stg_competition_modified_date 
    DEFAULT (GETDATE()) FOR modified_date
GO


IF EXISTS(SELECT 1
          FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
          WHERE CONSTRAINT_NAME = 'FK_stg_competition_stg_event')
    ALTER TABLE dbo.stg_competition
    DROP CONSTRAINT FK_stg_competition_stg_event
GO

ALTER TABLE dbo.stg_competition
    ADD CONSTRAINT FK_stg_competition_stg_event 
    FOREIGN KEY (event_id) 
    REFERENCES dbo.stg_event (event_id)
GO


IF EXISTS(SELECT 1
          FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
          WHERE CONSTRAINT_NAME = 'FK_stg_competition_stg_pool')
    ALTER TABLE dbo.stg_competition
    DROP CONSTRAINT FK_stg_competition_stg_pool
GO

ALTER TABLE dbo.stg_competition
    ADD CONSTRAINT FK_stg_competition_stg_pool 
    FOREIGN KEY (pool_id) 
    REFERENCES dbo.stg_pool (pool_id)
GO


IF EXISTS(SELECT 1
          FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
          WHERE CONSTRAINT_NAME = 'FK_stg_competition_stg_discipline')
    ALTER TABLE dbo.stg_competition
    DROP CONSTRAINT FK_stg_competition_stg_discipline
GO

ALTER TABLE dbo.stg_competition
    ADD CONSTRAINT FK_stg_competition_stg_discipline 
    FOREIGN KEY (discipline_id) 
    REFERENCES dbo.stg_discipline (discipline_id)
GO


IF EXISTS(SELECT 1
          FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
          WHERE CONSTRAINT_NAME = 'FK_stg_competition_stg_group')
    ALTER TABLE dbo.stg_competition
    DROP CONSTRAINT FK_stg_competition_stg_group
GO

ALTER TABLE dbo.stg_competition
    ADD CONSTRAINT FK_stg_competition_stg_group 
    FOREIGN KEY (group_id) 
    REFERENCES dbo.stg_group (group_id)
GO