shaperest
=========

Shaperest (rhymes with Mt. Everest) is a general-purpose traffic shaping proxy
service for new and preexisting RESTful services. 

Shaperest intends to be developed in phases:

1. A simple proxy server that will log and analyze traffic flows.
2. A traffic shaping service that will introduce delays between requests to
   stabilize target services.
3. A pluggable cache
   i. The cache plugin is service-aware and will be able to provide appropriate
      caching based on read/write analysis of requests.
