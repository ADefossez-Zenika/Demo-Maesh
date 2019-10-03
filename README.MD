# Maesh Demo

clone this repository, be sure to have helm installed and kubedns as a network provider.

```bash
Apply namespaces
Apply deployment
apply svc
```


kubectl port-forward svc/front -n=front 5000:80

kubectl port-forcat
k port-forward --namespace=maesh svc/jaeger-query 16686