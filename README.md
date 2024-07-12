# security-k8s-scan-pipeline
Security scanning of Kubernetes

## Introduction

This repository contains the code necessary to run trivy container scan in a infraestructure.
Have the code to deploy trivy operator into a Kubernetes cluster and to deploy trivy-defectdojo-reporter.

## Trivy container

With the trivy container we use the scanner to obtain the vulnerabilities at misconfiguration and compliance level, these reports which are not fully compatible with defect dojo are stored as zuul artifacts.

## Trivy operator

With the official trivy operator which gives us more information about the vulnerabilities that can be found within our cluster, the advantage of using the operator on the container is that we get immediate information once any component is deployed in kubernetes whether it is an application or not, this will generate a report that in turn thanks to another tool will be sent immediately to defect dojo for traceability.

## Trivy defect dojo reporter

The reporter operator is used to be able to send the reports directly to defect dojo and in this same one to have the traceability of the vulnerabilities obtained immediately, the reports that we send are those of vulnerabilityreports, rbacassessmentreports, infraassessmentreports, configauditreports, exposedsecretreports. These reports have been previously generated thanks to the trivy operator.