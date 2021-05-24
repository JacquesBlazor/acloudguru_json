import json
with open('all_acoundguru_course_entries.json', 'r', encoding='utf-8-sig') as f:
	readjson = json.load(f)
# readjson.sort(key=lambda x: x['details'])

aws = []
for i in readjson:
	for j, k in i.items():
		if j=='details' and k.startswith('AWS'):
			aws.append(i['title'])

aws.sort()
for i in aws:
	print(i)

'''
A Practical Guide to Amazon EKS
AIOps Essentials (Autoscaling Kubernetes with Prometheus Metrics)
AWS Advanced Networking Specialty (LA)
AWS Alexa Skill Builder Essentials
AWS Business Essentials
AWS Certification Preparation Guide
AWS Certified Advanced Networking - Specialty 2020
AWS Certified Alexa Skill Builder – Specialty 2020
AWS Certified Big Data - Specialty
AWS Certified Cloud Practitioner 2020
AWS Certified Data Analytics - Specialty
AWS Certified Database - Specialty (DBS-C01)
AWS Certified DevOps Engineer - Professional 2020
AWS Certified DevOps Professional Exam Prep Course
AWS Certified Developer - Associate 2020
AWS Certified Machine Learning - Specialty (LA)
AWS Certified Machine Learning - Specialty 2020
AWS Certified Security - Specialty 2020
AWS Certified Solutions Architect - Professional 2020
AWS Certified Solutions Architect Associate SAA-C02
AWS Certified SysOps Administrator - Associate 2020
AWS Certified SysOps Administrator Associate - SOA-C01 (LA)
AWS Cloud Practitioner - CLF-C01 (LA)
AWS Cloud Services and Infrastructure - Cost Optimization Deep Dive
AWS Concepts
AWS Developer Tools Deep Dive
AWS Essentials
AWS GovCloud: Beyond the Buzzwords
AWS IAM (Identity and Access Management) - Deep Dive
AWS Identity and Access Management (IAM) Concepts
AWS Operating Optimal Hybrid Environments
AWS Security Essentials
Advanced Networking with Kubernetes on AWS
Amazon Connect Essentials
Amazon Detective Deep Dive
Amazon DynamoDB Deep Dive
Amazon S3 Basics
Application Services for Associate AWS Solutions Architects
Applying Infrastructure as Code and Serverless Technologies to AWS Deployments
Automating AWS with Lambda, Python, and Boto3
Building a Full-Stack Serverless Application on AWS
Choosing the Right Database Service on AWS
Cloud Migration Fundamentals
CloudFormation Deep Dive
Configuring and Monitoring Governance of AWS Deployments
Deploying to AWS with Terraform and Ansible
Deployment Pipelines in AWS
Designing High Availability, Fault Tolerance, and DR with AWS Services
Designing Resilient Architectures for Associate AWS Solutions Architects
DevOps Concepts
DevOps Essentials
EKS Basics
Go Serverless with a Graph Database
Hands-On with AWS Systems Manager
HashiCorp Certified Terraform Associate
High Availability and Scalability for Associate AWS Solutions Architects
How to Properly Secure an S3 Bucket
Introduction to AWS
Introduction to AWS (Legacy)
Introduction to AWS AppSync
Introduction to AWS CloudFormation
Introduction to Amazon CodeGuru
Introduction to Amazon RDS
Introduction to Cloud Computing
Introduction to Cloud Migration Using Amazon Web Services
Introduction to Identity and Access Management (IAM)
Introduction to Optimizing Data Storage in AWS
Introduction to VMware Cloud on AWS
Introduction to VMware CloudHealth
Kubernetes Security
Kubernetes Security (Advanced Concepts)
Learn AWS by Doing
Logging and Security for Associate AWS Solutions Architects
Manage and Deploy Code with AWS Developer Tools (Legacy)
Managing AWS with Ansible
Mastering AWS CloudFormation
Mastering the AWS Well-Architected Framework
Networking and Compute for Associate AWS Solutions Architects
Practical Event-Driven Security with AWS
Python 3 Scripting for System Administrators
S3 Masterclass
Serverless Concepts
Storage, Databases, and Migration for Associate AWS Solutions Architects
Using Devops Automation for AWS Deployments
VMware Cloud on AWS Management Exam (5VO-31.19)
'''


azure = []
for i in readjson:
	for j, k in i.items():
		if j=='details' and k.startswith('Azure'):
			azure.append(i['title'])

azure.sort()
for i in azure:
	print(i)

'''
A Cloud Guru's Elastic Certified Analyst Exam Preparation Course
AKS Basics
AKS Deep Dive
AZ-103 Microsoft Azure Administrator 2019 (Preview)
AZ-104 Microsoft Azure Administrator Certification Prep
AZ-204: Developing Solutions for Microsoft Azure
AZ-303 Part 1 - Implement and Monitor Azure Infrastructure
AZ-303 Part 2 - Implement Management and Security Solutions in Azure
AZ-303 Part 3 - Implement Solutions for Apps in Azure
AZ-303 Part 4 - Implement and Manage Data Platforms in Azure
AZ-303 Part 5 - Preparing for the Microsoft Azure Architect Technologies Exam
AZ-304: Microsoft Azure Architect Design
AZ-500: Microsoft Azure Security Technologies (LA)
AZ-900 Microsoft Azure Fundamentals
Azure AI Components and Services
Azure AI Implementation and Monitoring
Azure AI Solution Requirements
Azure AI Workflow and Pipelines
Azure AI-100 Exam Preparation
Azure Architecture Design Concepts
Azure CLI Essentials
Azure Concepts
Azure Cosmos DB Deep Dive
Azure Database Administrator Associate
Azure IoT Solution Infrastructure (AZ-220: Course 1)
Azure PowerShell Essentials
Azure Storage Deep Dive
Build and Deploy Azure Templates
Build and Deploy Pipelines with Microsoft Azure
Cloud Security Fundamentals
Cost Control on Azure
Cross-Platform PowerShell in Azure
DP-100 Part 1 - Preparation
DP-100 Part 2 - Modeling
Deployment Pipelines using GitHub Actions
Designing an Azure DevOps Strategy
DevSecOps Essentials
Getting Started with Azure Machine Learning Studio
Hands-On Introduction to Azure Files
Identity and Access Management for Azure
Implementing Application Infrastructure in Azure
Implementing Azure DevOps Development Processes
Implementing Continuous Delivery in Azure
Implementing Continuous Feedback in Azure
Implementing Continuous Integration in Azure
Implementing Dependency Management in Azure
Intro to Azure for AWS Admins
Intro to Serverless on Azure
Introduction to Azure
Introduction to Azure
Introduction to Azure DevOps
Introduction to Azure Resource Manager
Introduction to Azure Security
Introduction to Azure VMware Cloud Solution
Introduction to Hybrid Environments on Azure
Learn Microsoft Azure by Doing
Managing Microsoft Azure Applications and Infrastructure with Terraform
Microsoft Azure Architect Design - Exam AZ-301 (LA)
Microsoft Azure Architect Technologies - Exam AZ-300
Microsoft Azure Exam DP-200 - Implementing an Azure Data Solution
Microsoft Azure Exam DP-201 - Designing an Azure Data Solution
Microsoft Azure Fundamentals - AZ-900 Exam Prep (LA)
Microsoft Azure Security Essentials
Microsoft Certified Azure Developer - Exam AZ-203 Prep
Microsoft SQL Server on Linux in Azure
Migrating Servers to Azure
PL-900 Microsoft Power Platform Fundamentals
PowerShell Core for Linux Admins
Preparing for the AZ-400 Azure DevOps Exam
Provisioning and Managing Devices in Azure IoT (AZ-220: Course 2)
Running Linux Servers on Azure
Running OpenShift on Microsoft Azure
SQL Deep Dive
Serverless Computing with Azure Functions
Using Azure for Disaster Recovery Quick Start
Using Microsoft Azure Database Services
'''

GCP = []
for i in readjson:
	for j, k in i.items():
		if j=='details' and k.startswith('GCP'):
			GCP.append(i['title'])


GCP.sort()
for i in GCP:
	print(i)

'''
Choosing the Right Database Service on GCP
Cost Control on GCP
Crash Course on Google Cloud Platform
Deploying Resources to GCP with Terraform
GKE Basics
Google Certified Associate Cloud Engineer 2020
Google Certified Professional Cloud Architect 2020
Google Certified Professional Cloud Developer
Google Certified Professional Cloud Network Engineer
Google Certified Professional Cloud Network Engineer Exam Prep (LA Part 5)
Google Certified Professional Data Engineer
Google Cloud AI Services Deep Dive
Google Cloud Apigee Certified API Engineer
Google Cloud CI/CD Pipelines (GCP DevOps Engineer Track Part 3)
Google Cloud Certified Professional Cloud Architect (LA)
Google Cloud Certified Professional Cloud Developer
Google Cloud Certified Professional Cloud Security Engineer
Google Cloud Certified Professional Data Engineer (LA)
Google Cloud Concepts
Google Cloud DevOps and SREs (GCP DevOps Engineer Track Part 2)
Google Cloud Essentials
Google Cloud Functions Deep Dive
Google Cloud Hybrid Networking - GCP Network Engineer Track Part 3
Google Cloud Identity and Access Management (IAM) Deep Dive
Google Cloud Network Concepts - GCP Network Engineer Track Part 1
Google Cloud Network Design and Monitoring - GCP Network Engineer Track Part 4
Google Cloud Network Management - GCP Network Engineer Track Part 2
Google Cloud Run Deep Dive
Google Cloud SQL Deep Dive
Google Cloud Security Essentials
Google Kubernetes Engine (GKE): Beginner to Pro
Google Kubernetes Engine Deep Dive
Google Professional Cloud DevOps Engineer Certification Course (GCP DevOps Engineer Track Part 5)
Google Professional Cloud DevOps Engineer Certification Path Introduction (GCP DevOps Engineer Track Part 1)
Hands-On IoT on GCP
Infrastructure as Code on GCP with Deployment Manager
Intro to GCP for AWS Admins
Introduction to Google Cloud
Introduction to Google Cloud VMware Cloud Engine
Introduction to Migrating Databases and Virtual Machines to Google Cloud Platform
Introduction to Serverless on Google Cloud
Learn Google Cloud by Doing
Monitoring, Managing, and Maximizing Google Cloud Operations (GCP DevOps Engineer Track Part 4)
'''