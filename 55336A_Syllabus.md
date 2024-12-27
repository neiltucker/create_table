## Course Syllabus

### Course Title
**Implementing and Managing Microsoft Virtualization Platforms for Hyper-V**

### Course #: 55336A

### Number of Days
5 Days (40 Hours Total)

### Format
Instructor-led / Workshop

### Course Overview
This comprehensive five-day course provides IT professionals and system administrators with the skills necessary to deploy, manage, and maintain Microsoft Hyper-V virtualization platforms. Through a mix of lectures, demos, and hands-on labs, students will gain proficiency in virtualization concepts, Hyper-V deployment, virtual machine management, advanced networking and storage configurations, and automation using PowerShell. This course is designed for environments running Windows Server.

### Course Audience
- IT Professionals
- System Administrators

### Course Value
This course enables IT professionals to:
- Deploy and configure Hyper-V environments effectively.
- Manage virtual machines and optimize performance.
- Implement advanced networking and storage solutions.
- Automate Hyper-V management using PowerShell.
- Ensure high availability and disaster recovery for virtual environments.

### At Course Completion
After completing this course, students will be able to:
- Understand and implement virtualization concepts using Hyper-V.
- Deploy and configure Hyper-V environments.
- Create and manage virtual machines effectively.
- Configure advanced networking and storage settings.
- Automate administrative tasks using PowerShell.
- Implement backup, disaster recovery, and troubleshooting solutions for Hyper-V environments.

### Prerequisites
- A basic knowledge of Windows Server environments.
- Familiarity with command-line tools (PowerShell).
- Understanding of networking and storage concepts.
- Experience with basic system administration tasks.

### Course Outline

#### Day 1: Introduction to Virtualization and Hyper-V
**Module 1: Introduction to Virtualization Concepts**
- Lesson 1.1: What is Virtualization?
  - Lecture: Types of virtualization, benefits, use cases.
  - Demo: Comparison of traditional and virtualized setups (Demo files: `C:\Classfiles\demofiles\Module1\Demo1.1.pptx`).
- Lesson 1.2: Introduction to Hyper-V
  - Lecture: Hyper-V architecture, features, editions, and components.
  - Demo: Overview of Hyper-V Manager on `MIA-SQL`.
- Lesson 1.3: Planning Your Hyper-V Deployment
  - Lecture: Hardware requirements, storage options, networking considerations.
  - Demo: Using the Hyper-V compatibility checker (Demo files: `C:\Classfiles\demofiles\Module1\Demo1.3.ps1`).
- **Lab 1: Basic Hyper-V Setup**
  - Enable and verify Hyper-V on `MIA-SQL` (Lab files: `C:\Classfiles\Labfiles\Module1\Lab1.1.ps1`).

**Module 2: Initial Hyper-V Configuration**
- Lesson 2.1: Setting up Networking
  - Lecture: Virtual switches (External, Internal, Private).
  - Demo: Creating and managing virtual switches using Hyper-V Manager on `MIA-SQL`.
- Lesson 2.2: Configuring Storage
  - Lecture: Virtual disk types (VHD, VHDX), storage pools and spaces.
  - Demo: Creating VHD and VHDX files on `MIA-SQL`.
- Lesson 2.3: Initial Settings
  - Lecture: Hyper-V server configuration, remote management, performance tuning overview.
  - Demo: Configuring remote management on `MIA-SQL`.
- **Lab 2: Configuring Virtual Networking and Storage**
  - Create virtual switches and dynamic VHDX files on `MIA-SQL` (Lab files: `C:\Classfiles\Labfiles\Module2\Lab2.1.ps1`).

#### Day 2: Virtual Machine Creation and Management
**Module 3: Creating Virtual Machines**
- Lesson 3.1: Creating a New Virtual Machine (GUI)
  - Lecture: Configuring memory, CPU, and storage.
  - Demo: Step-by-step walkthrough on `MIA-SQL`.
- Lesson 3.2: Creating a New Virtual Machine (PowerShell)
  - Lecture: Using PowerShell to automate VM creation.
  - Demo: VM creation script (Demo files: `C:\Classfiles\demofiles\Module3\Demo3.2.ps1`).
- Lesson 3.3: Importing and Exporting VMs
  - Lecture: Live migration vs cold migration.
  - Demo: Exporting and importing VMs on `MIA-SQL`.
- **Lab 3: Create Virtual Machines**
  - Create VMs using GUI and PowerShell (Lab files: `C:\Classfiles\Labfiles\Module3\Lab3.2.ps1`).

**Module 4: Managing Virtual Machines**
- Lesson 4.1: Managing VM Settings
  - Lecture: Modifying hardware resources.
  - Demo: Adjusting memory, CPU, and disk on `MIA-SQL`.
- Lesson 4.2: Managing Snapshots
  - Lecture: Creating and managing checkpoints.
  - Demo: Managing snapshots on `MIA-SQL`.
- **Lab 4: Managing VMs**
  - Adjust VM settings, create and restore snapshots on `MIA-SQL` (Lab files: `C:\Classfiles\Labfiles\Module4\Lab4.2.ps1`).

#### Day 3: Advanced Hyper-V Features
**Module 5: Advanced Networking**
- Lesson 5.1: VLANs and Virtual Networks
  - Lecture: Configuring VLAN IDs.
  - Demo: VLAN setup on `MIA-SQL`.
- Lesson 5.2: NIC Teaming and Load Balancing
  - Lecture: Benefits of NIC teaming.
  - Demo: Creating a NIC team on `MIA-SQL`.
- **Lab 5: Advanced Networking**
  - Configure VLANs and NIC teams (Lab files: `C:\Classfiles\Labfiles\Module5\Lab5.1.ps1`).

**Module 6: Advanced Storage**
- Lesson 6.1: Shared VHDX
  - Lecture: Benefits and configuration.
  - Demo: Configuring shared VHDX files on `MIA-SQL`.
- **Lab 6: Advanced Storage**
  - Configure shared VHDX and storage QoS (Lab files: `C:\Classfiles\Labfiles\Module6\Lab6.1.txt`).

#### Day 4: Hyper-V Management and Automation
**Module 7: Hyper-V Management Tools**
- Lesson 7.1: Hyper-V Manager
  - Lecture: GUI features and remote access.
  - Demo: Monitoring VMs on `MIA-SQL`.
- **Lab 7: Hyper-V Management**
  - Create and manage VMs using Hyper-V Manager (Lab files: `C:\Classfiles\Labfiles\Module7\Lab7.1.txt`).

**Module 8: Automation with PowerShell**
- Lesson 8.1: Basic Hyper-V Cmdlets
  - Lecture: Automating VM management.
  - Demo: PowerShell scripts for VM operations (Demo files: `C:\Classfiles\demofiles\Module8\Demo8.1.ps1`).
- **Lab 8: Automation with PowerShell**
  - Automate VM creation and reporting (Lab files: `C:\Classfiles\Labfiles\Module8\Lab8.1.ps1`).

#### Day 5: Hyper-V Maintenance, Backup, and Recovery
**Module 9: Hyper-V Backup and Disaster Recovery**
- Lesson 9.1: Backup Options
  - Lecture: Methods and tools for VM backup.
  - Demo: Backup and restore on `MIA-SQL`.
- **Lab 9: Backup and Recovery**
  - Configure and test VM backup and recovery (Lab files: `C:\Classfiles\Labfiles\Module9\Lab9.1.txt`).

**Module 10: Hyper-V Maintenance and Troubleshooting**
- Lesson 10.1: Patching and Updates
  - Lecture: Updating hosts and VMs.
  - Demo: Patch management on `MIA-SQL`.
- **Lab 10: Troubleshooting**
  - Simulate and resolve common issues (Lab files: `C:\Classfiles\Labfiles\Module10\Lab10.1.txt`).

