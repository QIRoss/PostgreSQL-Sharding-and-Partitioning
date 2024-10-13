import psycopg2
import random
from datetime import datetime, timedelta

conn_sharded_partitioned = psycopg2.connect(
    host="localhost",
    port="5433",
    dbname="high_volume_sharded_partitioned_db",
    user="user",
    password="password"
)

conn_regular = psycopg2.connect(
    host="localhost",
    port="5434",
    dbname="high_volume_regular_db",
    user="user",
    password="password"
)

def generate_random_activity_data():
    activities = ['login', 'logout', 'purchase', 'view_item']
    user_id = random.randint(1, 1000000)
    activity = random.choice(activities)
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 3, 1)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    activity_date = start_date + timedelta(days=random_days)
    return user_id, activity, activity_date

cur_sharded_partitioned = conn_sharded_partitioned.cursor()
cur_regular = conn_regular.cursor()

for _ in range(100000):
    user_id, activity, activity_date = generate_random_activity_data()

    cur_sharded_partitioned.execute(
        "INSERT INTO user_activity_sharded_partitioned (user_id, activity, activity_date) VALUES (%s, %s, %s)",
        (user_id, activity, activity_date)
    )

    cur_regular.execute(
        "INSERT INTO user_activity_regular (user_id, activity, activity_date) VALUES (%s, %s, %s)",
        (user_id, activity, activity_date)
    )

conn_sharded_partitioned.commit()
conn_regular.commit()

cur_sharded_partitioned.close()
cur_regular.close()
conn_sharded_partitioned.close()
conn_regular.close()
