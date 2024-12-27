**Course Title:** Implementing and Managing Microsoft Virtualization Platforms for Hyper-V

**Overall Structure:** (Same as before, but with added file location details)

*   **Duration:** 5 Days (40 Hours Total)
*   **Lecture/Lab Split:** 50/50 (Approximately 20 hours each)
*   **Module Structure:** 3-5 Lessons per Module, each with Demo and Review Questions
*   **Lab Structure:** One Lab per Module, based on demos and lessons
*   **Target Audience:** IT Professionals, System Administrators
*   **Environment:**
    *   **VM:** Windows Server 2022 VM named `MIA-SQL`
    *   **Course Files:** `C:\Classfiles`
    *   **Lab Files:** `C:\Classfiles\Labfiles\ModuleX` (X = Module Number)
    *   **Demo Files:** `C:\Classfiles\demofiles\ModuleX` (X = Module Number)

**Daily Schedule (Approximate):**

*   **Morning Session:** Lecture & Demos (3 hours)
*   **Lunch Break:** (1 hour)
*   **Afternoon Session:** Lab Work & Review (4 hours)

**Course Outline (Revised with File Paths)**

**Day 1: Introduction to Virtualization and Hyper-V**

*   **Module 1: Introduction to Virtualization Concepts (4 hours)**
    *   **Lesson 1.1: What is Virtualization?**
        *   Lecture: Types of Virtualization, Benefits, Use Cases.
        *   Demo: Comparison of a traditional setup with a virtual setup. (Demo files: `C:\Classfiles\demofiles\Module1\Demo1.1.pptx` )
        *   Review Questions: Basic virtualization principles.
    *   **Lesson 1.2: Introduction to Hyper-V**
        *   Lecture:  Hyper-V architecture, features, editions, and components.
        *   Demo:  Different versions of Hyper-V (GUI, Core, Server Manager) on `MIA-SQL`.
        *   Review Questions: Hyper-V components, supported guest OSes.
    *   **Lesson 1.3: Planning Your Hyper-V Deployment**
        *   Lecture:  Hardware requirements, storage options, networking considerations.
         *   Demo: Using Hyper-V Compatibility checker to ensure server compatibility on `MIA-SQL`. (Demo files: `C:\Classfiles\demofiles\Module1\Demo1.3.ps1` )
        *   Review Questions: Minimum HW requirements, planning the Virtual Switch design.
    *   **Lab 1: Basic Hyper-V Setup**
        *   Task: Enable Hyper-V on `MIA-SQL` (GUI or Powershell). (Lab files: `C:\Classfiles\Labfiles\Module1\Lab1.1.ps1`)
        *   Task: Verify Hyper-V Manager is started on `MIA-SQL`.
        *   Task: Take screenshots of the process and place in a report within C:\Classfiles\Labfiles\Module1.

*   **Module 2: Initial Hyper-V Configuration (4 Hours)**
    *   **Lesson 2.1: Setting up Networking**
        *   Lecture: Types of Virtual Switches (External, Internal, Private), Network Adapters.
        *    Demo: Creating and managing virtual switches using the Hyper-V Manager on `MIA-SQL`.
        *   Review Questions: What are the different types of virtual switches, when to use them.
    *   **Lesson 2.2: Configuring Storage**
        *   Lecture: Virtual disk types (VHD, VHDX), Storage options, Storage Pools and Spaces.
        *    Demo: Creating VHD and VHDX files on `MIA-SQL`.
        *   Review Questions: Different types of virtual disk, Dynamic vs Fixed disks.
    *   **Lesson 2.3: Initial Settings**
        *   Lecture: Hyper-V server configuration, Remote Management, Performance tuning overview.
        *   Demo: Configuring remote management on `MIA-SQL`.
        *   Review Questions: How to connect to a Hyper-V server remotely.
    *   **Lab 2: Configuring Virtual Networking and Storage**
        *   Task: Create a External, Internal, and Private virtual switch on `MIA-SQL`. (Lab files: `C:\Classfiles\Labfiles\Module2\Lab2.1.ps1`)
        *   Task: Create a new Dynamic VHDX file on `MIA-SQL`. (Lab files: `C:\Classfiles\Labfiles\Module2\Lab2.2.ps1`)

**Day 2: Virtual Machine Creation and Management**

*   **Module 3: Creating Virtual Machines (4 hours)**
    *   **Lesson 3.1: Creating a New Virtual Machine (GUI)**
        *   Lecture: Using Hyper-V Manager GUI, Choosing Memory and CPU.
        *   Demo: Step-by-step walkthrough of VM creation using Hyper-V Manager on `MIA-SQL`.
        *   Review Questions: What are the options for a new VM, what is Generation 1 and 2 VMs, and what are the differences.
    *   **Lesson 3.2: Creating a New Virtual Machine (PowerShell)**
        *   Lecture: Using Powershell to create VMs, setting VM parameters.
        *   Demo: Creating VMs via Powershell script on `MIA-SQL`. (Demo files: `C:\Classfiles\demofiles\Module3\Demo3.2.ps1` )
        *   Review Questions: Advantages of using Powershell.
    *   **Lesson 3.3: Importing and Exporting VMs**
        *   Lecture: Methods for importing and exporting VMs, live migration vs cold migration.
        *    Demo: Export a VM and import it using `MIA-SQL`.
        *   Review Questions: Different migration types.
    *   **Lab 3: Create Virtual Machines**
         *   Task: Create a new VM using GUI on `MIA-SQL`, install an operating system. (Lab files: `C:\Classfiles\Labfiles\Module3\Lab3.1.txt`)
         *   Task: Create a new VM using PowerShell on `MIA-SQL`, and install an OS. (Lab files: `C:\Classfiles\Labfiles\Module3\Lab3.2.ps1`)
         *   Task: Export the VM from `MIA-SQL` and import it to a different location.

*   **Module 4: Managing Virtual Machines (4 Hours)**
    *   **Lesson 4.1: Managing VM Settings**
        *   Lecture: Modifying VM hardware resources (memory, CPU, disks).
         *   Demo: Adjusting VM memory, CPU, and virtual disk allocations on `MIA-SQL`.
        *   Review Questions: When to add or remove memory or CPU.
    *   **Lesson 4.2: Managing Snapshots**
        *   Lecture: Creating and managing checkpoints, benefits and limitations.
         *   Demo: Creating, applying, and deleting VM checkpoints on `MIA-SQL`.
        *   Review Questions: What is the use of Snapshots, best practices.
    *   **Lesson 4.3: VM Connect & Console**
        *   Lecture: How to Connect to a VM, options for connecting.
         *   Demo: Connecting to a VM via the GUI, Powershell, and using other methods on `MIA-SQL`.
        *   Review Questions: Remote connection options.
    *   **Lab 4: Managing VMs**
        *   Task: Create several snapshots using `MIA-SQL`, then restore to a point in time. (Lab files: `C:\Classfiles\Labfiles\Module4\Lab4.1.txt`)
        *   Task: Using the GUI on `MIA-SQL`, adjust a VMs RAM and CPU, then using Powershell. (Lab files: `C:\Classfiles\Labfiles\Module4\Lab4.2.ps1`)
        *   Task: Connect to several VMs using different methods on `MIA-SQL`.

**Day 3: Advanced Hyper-V Features**

*   **Module 5: Advanced Networking (4 hours)**
    *   **Lesson 5.1: VLANs and Virtual Networks**
        *   Lecture: Using VLANs with virtual networks, creating VLAN IDs.
        *   Demo: Creating VLANs and tagging virtual networks with VLAN IDs on `MIA-SQL`.
        *   Review Questions: Best practices when using VLANs.
    *   **Lesson 5.2: NIC Teaming and Load Balancing**
        *   Lecture: Combining NICs into a team for redundancy and increased bandwidth.
         *   Demo: Setting up a NIC team and how to integrate it into the Virtual Switch on `MIA-SQL`.
        *   Review Questions: Benefits of using a NIC team.
    *   **Lesson 5.3: Virtual Network Adapters**
         *   Lecture: Configuring virtual network adapters, options for different types of VMs.
          *   Demo: Adding a new network adapter, connecting it to a Virtual Switch, removing an adapter on `MIA-SQL`.
        *   Review Questions: How to configure a Legacy network adapter.
    *   **Lab 5: Advanced Networking Lab**
        *   Task: Create a team and connect it to the virtual switch, configure VLAN IDs on `MIA-SQL`. (Lab files: `C:\Classfiles\Labfiles\Module5\Lab5.1.ps1`)
        *   Task: Add, remove, and configure virtual network adapters on several VMs using `MIA-SQL`. (Lab files: `C:\Classfiles\Labfiles\Module5\Lab5.2.txt`)

*   **Module 6: Advanced Storage (4 Hours)**
    *   **Lesson 6.1: Shared VHDXs**
        *   Lecture: Benefits of using shared VHDX, configuration requirements.
         *   Demo: Creating and using shared VHDX files for clustering on `MIA-SQL`.
        *   Review Questions: What are shared VHDX.
    *   **Lesson 6.2: Storage QoS**
         *   Lecture: Setting up storage Quality of Service policies, minimum and maximum IOPS.
          *   Demo: Configuring Storage QoS for VMs on `MIA-SQL`.
        *   Review Questions: What are Storage QoS.
    *   **Lesson 6.3: Storage Migration**
        *   Lecture: Different methods for migrating virtual machine storage.
         *   Demo: Migrate a VMs virtual disk to a different volume on `MIA-SQL`.
        *   Review Questions: Options when migrating a VMs storage.
    *   **Lab 6: Advanced Storage Lab**
        *   Task: Create a Shared VHDX on `MIA-SQL`, add the virtual disk to a VM, access it from the guest OS. (Lab files: `C:\Classfiles\Labfiles\Module6\Lab6.1.txt`)
        *   Task: Configure Storage QoS policy for VMs using `MIA-SQL`, test and monitor IOPS. (Lab files: `C:\Classfiles\Labfiles\Module6\Lab6.2.ps1`)
        *   Task: Migrate the virtual disks of 1 or more VMs to another disk volume on `MIA-SQL`. (Lab files: `C:\Classfiles\Labfiles\Module6\Lab6.3.txt`)

**Day 4: Hyper-V Management and Automation**

*   **Module 7: Hyper-V Management Tools (4 Hours)**
    *   **Lesson 7.1: Hyper-V Manager**
        *   Lecture: In-depth features of the Hyper-V Manager GUI, remote access options.
         *   Demo: Using the Hyper-V Manager to monitor VMs, configure settings on `MIA-SQL`.
        *   Review Questions: Reviewing the various features available in the Manager.
    *   **Lesson 7.2: Failover Cluster Manager**
        *   Lecture: Managing Hyper-V clusters with Failover Cluster Manager.
        *   Demo: Using the Failover Cluster Manager on `MIA-SQL`.
        *   Review Questions: Overview of Failover cluster manager.
    *   **Lesson 7.3: System Center Virtual Machine Manager**
        *   Lecture: Overview of SCVMM for enterprise management.
        *   Demo: Overview of the SCVMM Console on `MIA-SQL`.
        *   Review Questions: Benefits of using SCVMM.
    *   **Lab 7: Hyper-V Management**
        *   Task: Using Hyper-V Manager on `MIA-SQL`, create several VMs, configure their settings, monitor resource usage.
        *   Task: Connect remotely to a Hyper-V server on `MIA-SQL`.
        *   Task: Using Failover Cluster Manager to manage clustered VMs on `MIA-SQL`.

*   **Module 8: Automation with PowerShell (4 hours)**
    *   **Lesson 8.1: Basic Hyper-V Cmdlets**
        *   Lecture: Introduction to Hyper-V PowerShell cmdlets, creating, editing, deleting VMs.
          *   Demo: Common PowerShell cmdlets for managing Hyper-V on `MIA-SQL`.
        *   Review Questions: Useful PowerShell cmdlets.
    *   **Lesson 8.2: Creating and Managing VMs with PowerShell**
        *   Lecture: Using scripts for bulk VM operations, automating VM creation and deployment.
           *   Demo: Automating VM creation with a PowerShell Script on `MIA-SQL`. (Demo files: `C:\Classfiles\demofiles\Module8\Demo8.2.ps1` )
        *   Review Questions: Advantages of using scripts.
    *   **Lesson 8.3: Monitoring and Reporting with PowerShell**
        *   Lecture: Creating custom reports using PowerShell to extract information about Hyper-V.
           *   Demo: Using Powershell to create monitoring dashboards on `MIA-SQL`. (Demo files: `C:\Classfiles\demofiles\Module8\Demo8.3.ps1` )
        *   Review Questions: PowerShell capabilities.
    *   **Lab 8: Hyper-V Automation with PowerShell**
        *   Task: Create a PowerShell script on `MIA-SQL` that creates 5 new VMs with a set configuration. (Lab files: `C:\Classfiles\Labfiles\Module8\Lab8.1.ps1`)
        *   Task: Create a PowerShell script on `MIA-SQL` that will generate a report on the status of all VMs. (Lab files: `C:\Classfiles\Labfiles\Module8\Lab8.2.ps1`)

**Day 5: Hyper-V Maintenance, Backup, and Recovery**

*   **Module 9: Hyper-V Backup and Disaster Recovery (4 Hours)**
    *   **Lesson 9.1: Backup Options for Hyper-V**
        *   Lecture: Methods for backing up VMs, backup tools.
          *   Demo: Using Windows Server Backup for VM Backup on `MIA-SQL`.
        *   Review Questions: Different backup strategies.
    *   **Lesson 9.2: Hyper-V Replica**
        *   Lecture: Configuring and using Hyper-V Replica for disaster recovery.
        *    Demo: Setting up Hyper-V replica between 2 Hyper-V servers using `MIA-SQL`.
        *   Review Questions: When to use replication.
    *   **Lesson 9.3: Restoring a VM**
        *   Lecture: Restoring VMs from a Backup or replicated server.
           *   Demo: Restoring from a backup and restoring from a replicated server using `MIA-SQL`.
        *   Review Questions: Backup strategies, RTO & RPO objectives.
    *   **Lab 9: Backup and Recovery Lab**
        *   Task: Configure a backup job for a single VM using `MIA-SQL`, then restore the VM. (Lab files: `C:\Classfiles\Labfiles\Module9\Lab9.1.txt`)
        *  Task: Set up Hyper-V replication between 2 Hyper-V servers using `MIA-SQL`, trigger failover. (Lab files: `C:\Classfiles\Labfiles\Module9\Lab9.2.txt`)

*   **Module 10: Hyper-V Maintenance and Troubleshooting (4 Hours)**
    *   **Lesson 10.1: Patching and Updates**
        *   Lecture: Updating the Hyper-V Server and Guest OSes, Best Practices.
         *   Demo: Update the Hyper-V server, update a guest VM using `MIA-SQL`.
        *   Review Questions: How to patch a Hyper-V host and guest.
    *   **Lesson 10.2: Monitoring Performance**
        *   Lecture: Using Performance Monitor for Hyper-V, identifying performance bottlenecks.
         *   Demo: Using Performance Monitor to analyze Hyper-V Performance using `MIA-SQL`.
        *   Review Questions: Using Performance counter.
    *   **Lesson 10.3: Common Troubleshooting Scenarios**
        *   Lecture: Troubleshooting common problems in Hyper-V environments.
          *   Demo: Troubleshooting VM connectivity problems using `MIA-SQL`.
        *   Review Questions: Tools and methods of troubleshooting.
    *   **Lab 10: Hyper-V Troubleshooting**
        *   Task: Patch a Hyper-V server on `MIA-SQL`, monitor performance counters using Performance Monitor. (Lab files: `C:\Classfiles\Labfiles\Module10\Lab10.1.txt`)
        *   Task: Create a VM Network connection issue on `MIA-SQL`, then troubleshoot and fix the issue. (Lab files: `C:\Classfiles\Labfiles\Module10\Lab10.2.txt`)

