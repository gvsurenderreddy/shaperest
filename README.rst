shaperest
=========

Shaperest (rhymes with Mt. Everest) is a RESTful service agnostic, layer-7
traffic shaper. It is implemented purely in python and will be open-source.

Shaperest intends to be developed in phases:

1. A simple proxy server that will log and analyze traffic flows.
2. A traffic shaping service that will introduce delays between requests to
   stabilize target services.

    - The service will first start as it was in phase 1, a simple proxy server,
      but will then switch into shaping mode as it detects errors from the
      hosted service (500 errors).
3. A pluggable cache

    - The cache plugin is service-aware and will be able to provide appropriate
      caching based on read/write analysis of requests.

Alternatives and Commercial Products
------------------------------------

An incomplete list of alternatives to this project follows:

- `Layer7 technologies <http://www.layer7tech.com>`_ provides a REST proxy that
  appears to have traffic shaping capabilities
