=========
shaperest
=========

Shaperest (rhymes with Mt. Everest) is a RESTful service agnostic, layer-7
traffic shaper. It is implemented purely in python and will be open-source.

Development Plan
================

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
====================================

An incomplete list of alternatives to this project follows:

- `Layer7 technologies <http://www.layer7tech.com>`_ provides a REST proxy that
  appears to have traffic shaping capabilities

Targetted Services and Status
=============================

Nicira NVP
~~~~~~~~~~

`NVP <http://www.vmware.com/products/datacenter-virtualization/nicira.html>`_
is the primary target for shaperest and will be the first service to be
supported.

Status
------
- All traffic is currently being forwarded to a single NVP controller but auth
  is not working with it yet.
- Multiple controllers can be supported by placing a shaperest in front of each
  controller or in front of a load balancing server.
