from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

v1 = client.CoreV1Api()
print("Listing pods with their IPs:")
ret = v1.list_pod_for_all_namespaces(watch=False)
podstatus={}
for i in ret.items:
    #if i.status.phase != 'Running':
    #    podstatus[i.metadata.name]=i.status.phase
#    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
#    print(i.status.phase)
#    print(i.status.container_statuses)
    for ii in i.status.container_statuses:
     #   print(ii.state.running)
        if ii.state.running is None:
#            print(ii.state.running,i.status.pod_ip, i.metadata.namespace, i.metadata.name)
            podstatus[i.metadata.name] = ii.state
#print(len(podstatus))
if len(podstatus) > 0:
 #   print("Check the status of deployment ",podstatus)
    raise Exception("Check the status of deployment ",podstatus)


