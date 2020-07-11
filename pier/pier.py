import requests
import docker
import json

client = docker.from_env()

for container in client.containers.list():
  container_stats = json.dumps(container.stats(stream=False), indent=4)
  container_stats_json = json.loads(container_stats)
  container_name = container_stats_json["name"]
  container_id = container_stats_json["id"]
  print("Name: " + container_name)
  print("ID: " + container_id)


for image in client.images.list():
    print(image.id, image.labels, image.tags)
    client.images.remove(image.id)
