# Maesh Demo

## Install It

clone this repository, be sure to have helm installed and kubedns as a network provider.

in the pv.yaml file, make sure to change the path to actual existing paths on your laptop

then, apply:

```bash
kubectl appli -f ns.yaml
kubectl apply -f pv.yaml
kubectl appli -f deployment.yaml
kubectl appli -f svc
```

your application should be deploying.

## Play with it

Create a bunch of port-forward :

Jaeger:

```bash
kubectl kubectl port-forward svc/jaeger-query -n=maesh 5001:16686
```

Front:

```bash
kubectl port-forward svc/front -n=front 5000:80
```

Grafana is exposed as a nodePort:

```bash
kubectl get service grafana --namespace=maesh --output jsonpath="{.spec.ports[0].nodePort}"
````

Then launch your web browser on <http://localhost:5000> and refresh the page to create some traffic. You should notice that this page responds in +/- 0.1 to 2 seconds. That's because backend simulate network latency before returning content to the front.

On another tab, you can open  <http://localhost:5001> and <http://localhost:GRAFANAPORT> 

