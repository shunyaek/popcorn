import requests
import docker
import json

client = docker.from_env()

containers_list = client.containers.list()

for i in range(0, len(containers_list)):
    container_stats = json.dumps(containers_list[i].stats(stream=False), indent=4)
    container_stats_json = json.loads(container_stats)

    container_name = container_stats_json["name"]
    container_id = container_stats_json["id"]

    print(container_name)
    print(container_id)