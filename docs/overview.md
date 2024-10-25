# Overview

## Introdution

When we talk about Kubernetes and cloud operations, we're discussing two scenarios with potential vulnerabilities. It's not like other situations where you can have a single focus; here, you need to be constantly vigilant about what's happening. As a platform for deploying applications, Kubernetes becomes a critical system.Modern cloud infrastructure security is a complex and critical aspect of maintaining robust and resilient cloud services. Moreover, as organizations increasingly rely on cloud environments for their operations, the security of these infrastructures becomes paramount

The Container-as-a-Service layer in SCS, is susceptible to various security threats. To address these concerns, continuous and automated security is essential when we working with applications.

For this reason, the generated reports are also used to track all these issues, and continuous monitoring is applied to ensure the resolution of the vulnerabilities found.

## Kubernetes Security Concerns

Cloud infrastructure security involves protecting data, applications, and services from unauthorized access and threats security challenges, in Kubernetes, you must covering both infrastructure and application-related issues:

### Infrastructure Security Challenges in Kubernetes:

1. **Misconfigured Cluster Components**: Kubernetes clusters consist of various components like the API server, etcd, kubelet, and controller manager. Misconfigurations in these components can lead to unauthorized access, data leakage, and service disruptions.
2. **Inadequate Network Policies**: Without proper network policies, unauthorized services might communicate with each other, leading to potential lateral movement of threats across the cluster.
3. **Unsecured API Server**: The Kubernetes API server is the central control point for the entire cluster. Weak authentication and authorization mechanisms can expose the cluster to unauthorized access and potential exploits.
4. **Insufficient TLS Encryption**: Communication between Kubernetes components, including the API server, etcd, and nodes, should be encrypted using TLS. Lack of proper encryption can lead to man-in-the-middle attacks and data interception.
5. **Vulnerable etcd Configuration**: etcd stores all the cluster data, including secrets and configurations. If not properly secured, an attacker could gain access to sensitive information, potentially compromising the entire cluster.
6. **Improper Use of Privileged Containers**: Running containers with elevated privileges or allowing access to the host filesystem can lead to a compromise of the host system or other containers.
7. **Insecure Container Images**: Using container images from untrusted sources or without scanning them for vulnerabilities can introduce security risks into the cluster.

### Application Security Challenges in Kubernetes:

1. **Insecure Container Images**: Similar to infrastructure, deploying applications with unverified or outdated container images can introduce known vulnerabilities, increasing the attack surface.
2. **Excessive Container Privileges**: Applications running with more privileges than necessary can lead to potential security breaches if the application is compromised.
3. **Lack of Resource Quotas and Limits**: Without setting resource quotas and limits, a compromised application could exhaust cluster resources, leading to Denial of Service (DoS) attacks.
4. **Improper Secret Management**: Storing application secrets (e.g., API keys, credentials) in unsecured locations or without proper encryption can expose them to unauthorized access.
5. **Vulnerable Dependencies**: Applications often rely on third-party libraries and dependencies. Without regular updates and vulnerability scanning, these dependencies can introduce security risks.
6. **Unsecured Service Exposures**: Exposing application services without proper security measures (like ingress controllers with TLS, firewalls, etc.) can make them vulnerable to external attacks.
7. **Lack of Security Context and Policies**: Applications should be deployed with defined security contexts and policies to ensure they run with the least privilege necessary. Without these, applications are more susceptible to attacks.

In summary, securing Kubernetes requires a comprehensive approach that addresses both the infrastructure and the applications deployed on it. This includes proper configuration, encryption, privilege management, and regular security audits to identify and mitigate potential vulnerabilities.

## Infrastructure and application scanning

Here’s an overview in English of what Trivy does when scanning images, infrastructure, and using the Trivy operator for internal scanning:

### Scanning Images with Trivy:

When Trivy scans container images, it performs a deep inspection of the image layers. Internally, Trivy pulls the image from a container registry and unpacks it to examine the filesystem and all the packages installed within the image. It looks for known vulnerabilities by comparing the image's software packages against a database of known CVEs (Common Vulnerabilities and Exposures). Trivy supports various package managers (e.g., apt, yum, pip, npm) and can detect vulnerabilities in operating system packages as well as application dependencies. Trivy also checks for misconfigurations, such as insecure file permissions or exposed secrets, that could pose security risks.

### Scanning Infrastructure with Trivy:

For infrastructure-as-code (IaC) scanning, Trivy inspects configuration files like Terraform, Kubernetes manifests, Dockerfiles, and other IaC templates. Internally, it parses these files and checks them against a set of security rules and best practices. Trivy identifies misconfigurations that could lead to security issues, such as overly permissive access controls, unencrypted data storage, and insecure network configurations. The scanning process is rule-based, and the results highlight potential risks before the infrastructure is deployed, allowing teams to address them early in the development process.

### Trivy Operator for Internal Scanning:

The Trivy operator is designed to work within a Kubernetes cluster, performing continuous security scans of running workloads. Internally, the operator automatically scans Kubernetes resources, including pods, images, and configurations, as they are deployed or updated in the cluster. It integrates directly with Kubernetes, using Kubernetes events and controllers to trigger scans. The operator then reports on vulnerabilities, misconfigurations, and compliance issues directly within the cluster environment. The results can be surfaced via Kubernetes CRDs (Custom Resource Definitions) and integrated with other tools or CI/CD pipelines for further action.

## Quickstart Guide

See [the quickstart page](./quickstart.md).

## Tools

See [the tools page](./tools.md).

## Source

[github.com/SovereignCloudStack/security-k8s-scan-pipeline](https://github.com/SovereignCloudStack/security-k8s-scan-pipeline).
