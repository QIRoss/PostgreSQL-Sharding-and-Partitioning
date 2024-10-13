CREATE EXTENSION IF NOT EXISTS citus;

CREATE TABLE user_activity_sharded_partitioned (
    user_id BIGINT,
    activity TEXT,
    activity_date DATE
) PARTITION BY RANGE (activity_date);

SELECT create_distributed_table('user_activity_sharded_partitioned', 'user_id');

CREATE TABLE user_activity_2024_01 PARTITION OF user_activity_sharded_partitioned
    FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');

CREATE TABLE user_activity_2024_02 PARTITION OF user_activity_sharded_partitioned
    FOR VALUES FROM ('2024-02-01') TO ('2024-03-01');

CREATE TABLE user_activity_2024_03 PARTITION OF user_activity_sharded_partitioned
    FOR VALUES FROM ('2024-03-01') TO ('2024-04-01');