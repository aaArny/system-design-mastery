# Week 1 — Foundations

## What's running

- Load balancer (Nginx) routing round-robin across 2 backend services
- service-a, service-b — identical Flask apps, differentiated by env var
- [add monitoring stack here once you build it on Day 3]

## Capacity math

**Q1: If each service handles 100 req/s, what's the total capacity with 2 services?**
2 server that means server A + server B then 200req/s is the capacity

**Q2: If each response is 1KB, what's the daily bandwidth?**
200kb/s for a server -> 12000kb/min -> 720000kb/hour -> 17280000kb/day -> 17280mb/day(took 1k bytes to divide instead of 1024)

**Q3: If you add a 3rd service, what changes?**
If a new server/service is added, the handling capacity is increased, however , as only one of the server is handling the distribution of tasks then the limiting factor of the system is the throughput of the load balancing server

## Architecture diagram

![architecture](loadBalancer.png)

## Key learnings

- Servers are independent body, they are nothing but a path which a users uses to communicate with any hosted application, we ran a single app on 2 instances of server and hosted them on our local machine, 1 image/container -> 2 instances differntiated by the environment variable inserted at the run time of the container
- When a user request anything, the request is handled by a load balancer which splits the trafic to the server based on various algorithim. round robin is the most common, give each server the same chance/weight. The trade off is that the LB is not aware if the server went down or not
- Advantages of a load balancer are they keep the flow/conection to the application active eventually re-routes around failure, at the cost of a timeout for whoever's request hit the dead backend first
- One thing i noticed, when i stopped the service a to see the load balancer in effect, the refresh of the local host was slow for the first time, this timeout occured due to LB not knowing that the service-a was shut down, thus it waited for the timeout to occur before redirecting to the service b. This happned because the LB was not aware of the health status and still tried resulting in a slower load time for the user. If the port aborted suddenly and not cleanly like docker stop then the port initself would have rejected the call and thus this timeout would not have occured.
