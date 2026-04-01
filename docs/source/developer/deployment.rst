
.. include:: ../affdo_docs_common.rst

Deployment & Infrastructure
============================

This section documents the AFFDOWS web service infrastructure for developers and maintainers.

Custom Domain Setup
-------------------

The AFFDOWS web service is accessible via a branded custom domain:

- **Public URL**: ``https://affdo.attmosdiscovery.com``
- **Server**: ``dust.sdsc.edu`` (SDSC, San Diego Supercomputer Center)
- **Redirect**: ``https://dust.sdsc.edu`` redirects (301) to the branded domain

Architecture
^^^^^^^^^^^^

.. code-block:: text

   User browser
       │
       ▼
   affdo.attmosdiscovery.com  (DNS CNAME → dust.sdsc.edu)
       │
       ▼
   nginx (port 443, SSL termination)
       ├── /api/*  →  Flask API (localhost:8080)
       └── /*      →  Streamlit app (localhost:8501)

DNS Configuration
^^^^^^^^^^^^^^^^^

The domain ``attmosdiscovery.com`` is managed via Google Cloud DNS (nameservers: ``ns-cloud-c*.googledomains.com``).

A single CNAME record maps the subdomain to the SDSC server:

.. code-block:: text

   affdo.attmosdiscovery.com.  CNAME  dust.sdsc.edu.

SSL Certificates
^^^^^^^^^^^^^^^^

SSL certificates are managed by `Let's Encrypt <https://letsencrypt.org/>`_ via Certbot with automatic renewal.

Two certificates are maintained on dust:

1. ``affdo.attmosdiscovery.com`` — serves the branded domain
2. ``dust.sdsc.edu`` — serves the redirect

Certificate files are stored at ``/etc/letsencrypt/live/<domain>/``.

To manually renew:

.. code-block:: bash

   sudo certbot renew

Nginx Configuration
^^^^^^^^^^^^^^^^^^^

Two nginx configuration files exist in ``/etc/nginx/conf.d/``:

- ``affdo.attmosdiscovery.com.conf`` — proxies to Streamlit and Flask API
- ``dust.sdsc.edu.conf`` — redirects all traffic to the branded domain

A backup of the original ``dust.sdsc.edu`` proxy configuration is preserved at
``/etc/nginx/conf.d/dust.sdsc.edu.conf.bak``.

To test and reload after changes:

.. code-block:: bash

   sudo nginx -t && sudo nginx -s reload

Environment Variables
^^^^^^^^^^^^^^^^^^^^^

The following environment variables control the URL configuration:

.. list-table::
   :header-rows: 1
   :widths: 30 40 30

   * - Variable
     - Description
     - Default
   * - ``AFFDOWS_URL``
     - Public-facing URL used in user emails
     - ``https://www.attmosdiscovery.com/tools``
   * - ``AFFDOWS_API_BASE``
     - API base URL used by Streamlit to call Flask
     - ``https://affdo.attmosdiscovery.com``

On the dust server, ``AFFDOWS_API_BASE`` should be set to ``http://localhost:8080`` to avoid
routing API calls through the external domain.

Service Management
------------------

The AFFDOWS web service consists of two processes running on dust:

1. **Flask API** (``affdows-api.py``): Handles job submission, status, and management
2. **Streamlit app** (``affdows-app.py``): User-facing web interface

Starting the Services
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   cd /server-home1/madu/Work/AFFDO

   # Start Flask API
   nohup python3 -u affdows-api.py > affdows-api.log 2>&1 & disown

   # Start Streamlit
   nohup streamlit run affdows-app.py \
       --server.address 0.0.0.0 --server.port 8501 \
       > affdows-app.log 2>&1 & disown

Stopping the Services
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   pkill -f "affdows"

Rollback Procedure
------------------

To revert the custom domain setup and restore direct access via ``dust.sdsc.edu``:

.. code-block:: bash

   # 1. Restore original dust.sdsc.edu nginx config
   sudo cp /etc/nginx/conf.d/dust.sdsc.edu.conf.bak /etc/nginx/conf.d/dust.sdsc.edu.conf

   # 2. Remove branded domain config
   sudo rm /etc/nginx/conf.d/affdo.attmosdiscovery.com.conf

   # 3. Reload nginx
   sudo nginx -s reload

   # 4. Remove DNS CNAME record from Google Cloud DNS

*Last updated on* |UPDATE_DATE|.
