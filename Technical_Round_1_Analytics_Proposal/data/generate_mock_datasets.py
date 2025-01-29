import pandas as pd
import random
from faker import Faker
import numpy as np
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Seed for reproducibility
random.seed(42)
np.random.seed(42)

# Update dataset sizes to 1000 rows for each table
n_groups = 200  # More groups to distribute 1000 rows better
n_members = 1000
n_messages = 1000

# Generate Group Info mock data (up to 50 groups)
group_info_data = {
    "group_id": list(range(1, n_groups + 1)),  # REQUIRED, INTEGER
    "title": [fake.word() + " Group" for _ in range(n_groups)],  # REQUIRED, STRING
    "description": [fake.sentence() if random.random() > 0.2 else None for _ in range(n_groups)],  # NULLABLE, STRING
    "group_type": [random.choice(["public", "private"]) for _ in range(n_groups)],  # REQUIRED, STRING
    "member_count": [random.randint(50, 1000) if random.random() > 0.1 else None for _ in range(n_groups)],  # NULLABLE, INTEGER
    "admin_count": [random.randint(1, 15) if random.random() > 0.1 else None for _ in range(n_groups)],  # NULLABLE, INTEGER
    "number_of_bots": [random.randint(0, 50) if random.random() > 0.1 else None for _ in range(n_groups)],  # NULLABLE, INTEGER
    "pinned_messages": [fake.sentence() if random.random() > 0.5 else None for _ in range(n_groups)],  # NULLABLE, STRING
    "pinned_messages_timestamp": [fake.date_time_between(start_date='-1y', end_date='now') if random.random() > 0.5 else None for _ in range(n_groups)],  # NULLABLE, TIMESTAMP
    "visibility": [random.choice(["public", "restricted"]) if random.random() > 0.1 else None for _ in range(n_groups)],  # NULLABLE, STRING
}

group_info_df = pd.DataFrame(group_info_data)

# Generate Member Info mock data (up to 1000 members)
member_info_data = {
    "user_id": list(range(1, n_members + 1)),
    "username": [fake.user_name() for _ in range(n_members)],
    "first_name": [fake.first_name() for _ in range(n_members)],
    "last_name": [fake.last_name() for _ in range(n_members)],
    "is_bot": [random.choice([True, False]) for _ in range(n_members)],
    "role": [random.choice(["admin", "member", "moderator"]) for _ in range(n_members)],
    "join_date": [fake.date_time_this_year().isoformat() for _ in range(n_members)],
    "group_id": [random.randint(1, n_groups) for _ in range(n_members)],
}
member_info_df = pd.DataFrame(member_info_data)

# Generate Message Info mock data (up to 1000 messages)
message_info_data = {
    "message_id": list(range(1, n_messages + 1)),
    "sender_id": [random.randint(1, n_members) for _ in range(n_messages)],
    "timestamp": [fake.date_time_this_year().isoformat() for _ in range(n_messages)],
    "message_type": [random.choice(["text", "media", "link", "sticker"]) for _ in range(n_messages)],
    "text": [fake.sentence() for _ in range(n_messages)],
    "media_links": [fake.url() if random.random() > 0.7 else None for _ in range(n_messages)],
    "hashtags": [[fake.word() for _ in range(random.randint(0, 3))] for _ in range(n_messages)],
    "urls": [[fake.url() for _ in range(random.randint(0, 2))] for _ in range(n_messages)],
    "replies": [random.randint(0, 50) for _ in range(n_messages)],
    "views": [random.randint(0, 5000) for _ in range(n_messages)],
    "forwards": [random.randint(0, 200) for _ in range(n_messages)],
    "sender_name": [fake.name() for _ in range(n_messages)],
    "sender_username": [fake.user_name() for _ in range(n_messages)],
    "group_id": [random.randint(1, n_groups) for _ in range(n_messages)],
}
message_info_df = pd.DataFrame(message_info_data)

# Save the datasets to CSV files
group_info_df.to_csv('D:\Data_Analyst\Project_Assignment\Technical_Round_1_Analytics_Proposal\data\group_info.csv', index=False)
member_info_df.to_csv('D:\Data_Analyst\Project_Assignment\Technical_Round_1_Analytics_Proposal\data\member_info.csv', index=False)
message_info_df.to_csv('D:\Data_Analyst\Project_Assignment\Technical_Round_1_Analytics_Proposal\data\message_info.csv', index=False)

# Confirm datasets are saved
"group_info.csv, member_info.csv, and message_info.csv created with 1000 rows each."
