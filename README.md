# Database Sharding and Partitioning

Studies based in day 31-32 of 100 Days System Design for DevOps and Cloud Engineers.

https://deoshankar.medium.com/100-days-system-design-for-devops-and-cloud-engineers-18af7a80bc6f

Days 31–40: Scalability and Performance Optimization

Day 33–34: Study database sharding and partitioning at scale; implement for a high-volume application.

## Project Overview

This project consist in partitioning and sharding practices using postgres inside Docker.

### Understanding Partitioning vs. Sharding

* Partitioning: Splits a single table into smaller pieces (partitions) based on a column value. All partitions are stored in the same database. Types include range, list, and hash partitioning.

* Sharding: Distributes data across multiple databases (or nodes), each handling a portion of the dataset. This is suitable for horizontal scaling when a single database server can't handle the load.

We're using Citus Extension to Shard the data across multiple nodes in Citus cluster. Partioning done in```init_sharded_partitioned.sql```.

### How to Run:

#### Virtual Env
```
python3 -m venv venv
source venv/bin/activate
```

#### Docker
```
docker-compose up
```

#### Populate
```
python3 populate.py
```

#### Query and Test Performance

Regular Database:
```
docker exec -it postgres_regular psql -U user -d high_volume_regular_db
SELECT COUNT(*) FROM user_activity_regular;
EXPLAIN ANALYZE SELECT * FROM user_activity_regular WHERE user_id = 12345;
```
Check the execution time.

Sharded and Partitioned Database:
```
docker exec -it postgres_sharded_partitioned psql -U user -d high_volume_sharded_partitioned_db
SELECT COUNT(*) FROM user_activity_sharded_partitioned;
EXPLAIN ANALYZE SELECT * FROM user_activity_sharded_partitioned WHERE user_id = 12345;
```
Compare the execution times.

## Author
This project was implemented by [Lucas de Queiroz dos Reis][2]. It is based on the Day 23–24: Automate multi-environment setups using Terraform and Ansible dynamic inventories from the [100 Days System Design for DevOps and Cloud Engineers][1].

[1]: https://deoshankar.medium.com/100-days-system-design-for-devops-and-cloud-engineers-18af7a80bc6f "Medium - Deo Shankar 100 Days"
[2]: https://www.linkedin.com/in/lucas-de-queiroz/ "LinkedIn - Lucas de Queiroz"