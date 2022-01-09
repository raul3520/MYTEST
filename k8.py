from kubernetes import client, config

config.load_incluster_config()
v1 = client.CoreV1Api()
print("Listing pods with their IPs: and status")
ret = v1.list_pod_for_all_namespaces(watch=False)
podstatus={}
for i in ret.items:
    for ii in i.status.container_statuses:
        if ii.state.running is None:
            podstatus[i.metadata.name] = ii.state
if len(podstatus) > 0:
    raise Exception("Check the status of deployment ",podstatus)
