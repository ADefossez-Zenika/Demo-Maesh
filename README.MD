# Maesh Demo

## Install It

clone this repository, be sure to have helm installed and coredns as a network provider.

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

Install Maesh via the helm install command provided by the documentation.

Create a port-forward :

```bash
kubectl port-forward svc/front -n=front 5000:80
```

Then launch your web browser on <http://localhost:5000> and refresh the page to create some traffic. You should notice that this page responds in +/- 0.5 to 2.5 seconds. That's because backend simulate network latency before returning content to the front.

### Grafana

You can see the Grafana dashboard embeded with maesh. This one comes with a loadbalancer service, to find on wich port of your laptop grafana is listening, launch:

```bash
kubectl get service grafana --namespace=maesh --output jsonpath={.spec.ports[0].nodePort}
````

or

```bash
kubectl get service grafana --namespace=maesh --output jsonpath={.spec.ports} FIXME
````

### Jaeger

```bash
kubectl port-forward --namespace=maesh svc/jaeger-query 16686
```

open your browser to <http://localhost:16686>
