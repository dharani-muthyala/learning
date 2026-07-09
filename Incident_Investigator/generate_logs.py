import random
from datetime import datetime, timedelta

errors = [
    "S3 Timeout",
    "Database Connection Lost",
    "Authentication Failed",
    "Lambda Timeout",
    "Redis Cache Miss",
    "API Gateway 502",
]

apis = [
    "/upload",
    "/login",
    "/profile",
    "/documents",
    "/search",
]

start = datetime.now()

with open("logs.txt", "w") as f:

    for i in range(5000):

        t = start + timedelta(seconds=i)

        if random.random() < 0.2:

            log = f"{t} ERROR {random.choice(apis)} {random.choice(errors)}\n"

        else:

            log = f"{t} INFO {random.choice(apis)} Success\n"

        f.write(log)

print("Generated 5000 logs")