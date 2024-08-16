# 0x18. Webstack Monitoring

## Description
This project is about setting up webstack monitoring using Datadog, a cloud-based monitoring and analytics platform. The objective is to measure and visualize the performance of our servers and applications to ensure they are operating as expected. We will be focusing on both application and server monitoring.

## Learning Objectives
By the end of this project, you should be able to:

- Understand why monitoring is essential in software systems.
- Identify the two main areas of monitoring: Application Monitoring and Server Monitoring.
- Know the purpose of access logs and error logs in web servers like Nginx.

## Tasks

### 0. Sign up for Datadog and Install Datadog Agent
- Sign up for a Datadog account using the US1 region.
- Install the `datadog-agent` on the `web-01` server.
- Create and copy the Datadog API key and Application key to your Intranet user profile.
- Verify that your server `web-01` is visible in Datadog under the hostname `XX-web-01`.
  
### Requirements
- All files are interpreted on Ubuntu 16.04 LTS.
- Bash scripts should be executable and must pass Shellcheck (version 0.3.7) without errors.
- The first line of all Bash scripts should be `#!/usr/bin/env bash`.
- Scripts should include a comment explaining what they do.

## References
- [What is server monitoring](https://www.techtarget.com/searchdatacenter/definition/server-monitoring)
- [What is application monitoring](https://www.appdynamics.com/product/application-performance-monitoring/)
- [System monitoring by Google](https://landing.google.com/sre/sre-book/chapters/monitoring-distributed-systems/)
- [Nginx logging and monitoring](https://docs.nginx.com/nginx/admin-guide/monitoring/logging/)

## Author
project was developed by Chancy Tsonga [effort inc] . All rights reserved.

