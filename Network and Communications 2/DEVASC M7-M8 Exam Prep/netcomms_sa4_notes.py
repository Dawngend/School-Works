"""NetComms 2 (CS0016) Summative 4 reviewer: DEVASC Module 7 and Module 8. Built from the two slide PDFs."""


from netcomms_sa4_bank import bank_section

def sa4(n):
    n.h1("What Is Inside")
    n.p("This reviewer covers the fourth summative assessment: **Module 7 Infrastructure and Automation** and "
        "**Module 8 Cisco Platforms and Development**. Your prof uses **multiple choice only**, so every section "
        "below is written to help you pick the right choice: definitions, counts, which-tool-does-what, and the "
        "code and command lines the slides show. The blue boxes are memory aids I made; they are not from the slides. "
        "**Read the Question Bank part first**: it holds the literal exam-style questions and answers Dawn found, and "
        "it ranks above everything else in this document. Where the slides and the bank disagree, trust the bank.")
    n.table(
        ["Module", "Topics"],
        [
            ["**7 Infrastructure and Automation**", "7.1 Automating Infrastructure, 7.2 DevOps and SRE, 7.3 Basic Automation Scripting, 7.4 Automation Tools (Ansible, Puppet, Chef), 7.5 Infrastructure as Code, 7.6 Automating Testing (pyATS, Genie), 7.7 Network Simulation (VIRL)"],
            ["**8 Cisco Platforms and Development**", "8.1 Cisco API Platform, 8.2 SDKs, 8.3 Model-Driven Programmability (YANG, NETCONF, RESTCONF), 8.4 Network Management (IOS XE, DNA Center, ACI, Meraki, NX-OS, NSO, SD-WAN), 8.5 Compute (UCS, Intersight), 8.6 Collaboration (Unified CM, Finesse, Webex), 8.7 Security (AMP, Firepower, ISE, Threat Grid, Umbrella)"],
        ],
        [2.2, 4.3],
    )

    n.h1("Fast Memory Map")
    n.table(
        ["If The Question Says", "Think"],
        [
            ["Agentless, SSH, YAML playbooks, inventory", "**Ansible**"],
            ["Server plus agent, certificates, manifests, `.pp` files", "**Puppet**"],
            ["Cookbooks, recipes, Knife, run_list", "**Chef**"],
            ["Same result every time you run it", "**Idempotency**"],
            ["Operations by pull request", "**GitOps**"],
            ["Two identical production environments", "**Blue/green** (traffic cut over); **canary** goes user by user"],
            ["Python network test system, testbed YAML", "**pyATS** (library: **Genie**)"],
            ["`.virl` file", "**VIRL** network simulation"],
            ["Data modeling language for NETCONF", "**YANG**"],
            ["XML over SSH, edit-config", "**NETCONF**"],
            ["HTTP, GET/POST/PUT/DELETE on YANG data", "**RESTCONF**"],
            ["`netconf-yang`, `restconf`, `ip http secure-server`", "**IOS XE** enable commands"],
            ["Controller with Design, Policy, Provision, Assurance, Platform", "**Cisco DNA Center**"],
            ["Nexus 9000, APIC, managed objects, Cobra", "**Cisco ACI**"],
            ["Cloud-managed, Dashboard API, API key from My Profile", "**Meraki**"],
            ["vManage, vSmart, vBond, vEdge", "**Cisco SD-WAN**"],
            ["Service Profiles, Fabric Interconnects, UCS Manager", "**UCS**"],
            ["SaaS compute management", "**Intersight**"],
            ["SOAP admin API for Unified CM", "**AXL**"],
            ["REST API for end users on Unified CM", "**UDS**"],
            ["Browser-based contact center agent desktop", "**Finesse**"],
            ["DNS-layer security", "**Umbrella**"],
            ["Rule-based network access, identity", "**ISE**"],
        ],
        [3.6, 2.9],
    )
    n.pagebreak()
    bank_section(n)
    n.pagebreak()

    # ------------------------------------------------------------------ MODULE 7
    n.h1("Module 7: Infrastructure and Automation")

    n.h2("7.1 Automating Infrastructure With Cisco")
    n.p("**Automation** is using code to configure, deploy, and manage applications together with the compute, "
        "storage, and network infrastructure and services they run on. Cisco platforms either work with common tools "
        "(**Ansible, Puppet, Chef**) or give **direct API access** to the programmable infrastructure.")
    n.h3("Walk, Run, Fly")
    n.table(
        ["Stage", "What You Do"],
        [
            ["**Walk**", "**Read-only** automation. Gather the network configuration, audit it, then put it back into compliance."],
            ["**Run**", "Activate policies and provide **self-service** across multiple domains. Automate onboarding workflows and day-to-day configuration."],
            ["**Fly**", "Deploy applications and network configurations through **CI/CD**. Monitor and proactively manage users and devices, with telemetry insights."],
        ],
        [1.2, 5.3],
    )
    n.p("This progression is how the **DevNet Automation Exchange** categorizes automation.")
    n.memory("Walk = **W**atch (read only). Run = **R**equest (self-service). Fly = **F**ast pipelines (CI/CD).")
    n.h3("Why Automate")
    n.bullets([
        "**Speed and agility:** explore, experiment with, and exploit opportunities ahead of competitors. Developers must speed up coding, testing, and staging, and DevOps makes developers deploy and manage in production too.",
        "**Manual operations** add cost, take time, are hard to scale, and are prone to human error. Documentation written for humans is often incomplete and ambiguous, hard to test, and quickly outdated.",
        "**Dependency risks:** the software ecosystem is decentralized. Component developers may abandon obsolete features, and dependency-ridden setups get locked into fragile, increasingly insecure stacks.",
    ])
    n.h3("Benefits Of Full-Stack Automation")
    n.table(
        ["Benefit", "Meaning"],
        [
            ["**Self-service**", "Users requisition infrastructure on demand"],
            ["**Scale on demand**", "Apps and platforms scale up and down with traffic and workload"],
            ["**Observability**", "Users can infer the internal state of a complex system from its outputs"],
            ["**Automated problem mitigation**", "Apps and platforms are engineered to minimize the effect of issues, self-heal, and monitor events"],
        ],
        [2.2, 4.3],
    )
    n.memory("Four benefits: **S**elf-service, **S**cale, **O**bservability, **A**uto-mitigation. \"**S**ome **S**ailors **O**bserve **A**lbatrosses.\"")
    n.h3("Software-Defined Infrastructure And Microservices")
    n.bullets([
        "**Software-defined infrastructure = cloud computing.** Developers and operators use software to requisition, configure, deploy, and manage bare-metal and virtualized compute, storage, and network resources.",
        "Cloud benefits: self-service (platforms on demand), close specification, consistency and repeatability, platform abstraction. Challenges: design, architecture and security care; **access control is critical** because wrong permissions can do a lot of damage; self-served consumption is hard to manage and costs are hard to calculate.",
        "**Microservices:** distributed apps built from small, light components, often isolated in containers, connected by discovery and messaging services, backed by resilient scalable databases. Benefit: **scalability** (scaled and load-balanced across servers or regions, no single point of failure). Challenge: **increased complexity**, so **automation is a requirement**.",
    ])
    n.watch("Do not confuse the two lists. Microservice **benefit** = scalability and infrastructure automation tools. "
            "Microservice **challenge** = complexity, so automation becomes mandatory.")

    n.h2("7.2 DevOps And SRE")
    n.p("Full-stack automation needs a culture change: break down the divide between **Development (Dev)** and "
        "**Operations (Ops)**. In the early 2000s a movement began to treat them as one entity: make coders "
        "responsible for deployment and maintenance, and treat virtualized infrastructure as code.")
    n.table(
        ["Characteristic", "Dev", "Ops"],
        [
            ["Cares about", "Bespoke applications and how they work", "Applications and how they run, plus infrastructure, OS, network"],
            ["Business treats as", "**Profit center** (demands resources)", "**Cost center** (provides and accounts for resources)"],
            ["On-call rotation", "Occasionally (only when escalated)", "**Regularly** (point of spear)"],
            ["Performance measured", "Abstractly (including bad metrics)", "**Concretely** (SLA compliance, issues resolved)"],
            ["Skills", "**More deep than broad**: languages, APIs, architecture, tools", "**More broad than deep**: configuration, administration, OS, automation"],
            ["Agility", "Move fast, innovate, break things, fix later", "Investments must be extensively justified, expectations managed"],
        ],
        [1.4, 2.5, 2.6],
    )
    n.memory("Dev = **D**eep, **D**emands resources (profit). Ops = **O**n-call, **O**ver a broad area, **O**wns the cost.")
    n.h3("Evolution Of DevOps")
    n.table(
        ["Year", "Event"],
        [
            ["**2003**", "Google institutionalizes **Site Reliability Engineering (SRE)**"],
            ["**2009**", "**Patrick Debois**: automating virtual and physical infrastructure with version control and Agile methods (**Agile Infrastructure**)"],
            ["**2009**", "**John Allspaw and Paul Hammond**: simple DevOps best practices based on Dev and Ops cooperatively enabling the business"],
        ],
        [1.0, 5.5],
    )
    n.memory("SRE came first (**2003**, Google). Debois and Allspaw/Hammond are both **2009**.")
    n.h3("Core Principles")
    n.bullets([
        "A focus on **automation**.",
        "The idea that **\"failure is normal\"**.",
        "Reframing **\"availability\"** in terms of what the business can tolerate.",
    ])
    n.table(
        ["Term", "Meaning"],
        [
            ["**SLO** (Service Level Objective)", "The agreed, measurable business value target, defined in terms of real metrics"],
            ["**SLI** (Service Level Indicator)", "The real metrics the SLO is defined with; they map to the practical reality of delivering a service"],
            ["**Error budget**", "A set amount of allowed failure for a period of time; failures to achieve the SLO are subtracted from it"],
        ],
        [2.4, 4.1],
    )
    n.p("The SLO/SLI idea removes the obligation to seek **perfection** (perfect delivery is statistically impossible), "
        "which permits cheaper, more rapid delivery of business value.")
    n.memory("SLO = the **O**bjective (goal). SLI = the **I**ndicator (the measured number). Budget = how much you may miss.")

    n.h2("7.3 Basic Automation Scripting")
    n.bullets([
        "Tools like Ansible, Puppet, and Chef bring ease of use, predictability, discipline, and scale, but they **do not solve every deployment problem**, so basic scripting skills still matter. Every automation tool has functions that run basic commands and scripts on targets and return results.",
        "**Bash** is a Unix shell, default on most Linux distributions and macOS. **Shell scripting is historically the bedrock of automation.** Using commands in a Bash script is much like using them from the command line, for example scripting the AWS CLI.",
        "More sophisticated languages (such as Python) improve on Bash as complexity and scale grow, especially with SDKs in cloud environments.",
    ])
    n.h3("Procedural Automation And Idempotency")
    n.p("An **imperative procedure** is an ordered sequence of commands aimed at a goal, and it can include flow control, "
        "conditions, functions, and classes. To make scripts efficient and reusable: standardize parameters, flags, and "
        "errors; build a code hierarchy; write **high-level scripts for whole deployments and lower-level scripts for "
        "phases**; and **separate deployment-specific data from the code**.")
    n.p("Careful scripts and declarative tools **examine the target first** and only do what is needed to reach the "
        "desired state. That quality is **idempotency**.")
    n.bullets([
        "Ensure the change has **not already been made**.",
        "Get to a **known-good state** before making changes, if possible.",
        "**Test** for idempotency.",
        "**All components** of a procedure must be idempotent.",
    ])
    n.h3("Running Scripts On Remote Machines")
    n.p("Slide options: store locally, copy with **scp**, log in with **ssh** and run; pipe with **cat | ssh**; use "
        "**SFTP**; store scripts on a webserver or Git repo and fetch with **wget** or **curl**; use full remote tools "
        "like **VNC** or **NoMachine**; or inject a configuration script through the cloud CLI or web UI that creates "
        "the platform.")
    n.h3("Cloud Automation And Cloud CLIs And SDKs")
    n.p("Cloud automation provisions virtualized hosts, configures virtual networks, requisitions services, and "
        "deploys applications. IaaS clouds provide CLIs and SDKs that connect to underlying interfaces, usually **REST-based**.")
    n.table(
        ["Platform", "Examples On The Slide"],
        [
            ["**Cisco UCS** (bare-metal cloud)", "Cisco Intersight RESTful API; SDKs for Python and Microsoft PowerShell; Ansible modules"],
            ["**VMware**", "Datacenter CLI, vSphere CLI, PowerCLI for Windows PowerShell, SDKs for vSphere Automation and vCloud Suite"],
            ["**OpenStack**", "OpenStack Client (OSC), Compute, Identity, Image, Object Storage and Block Storage APIs, Python SDK, toolkits"],
        ],
        [2.4, 4.1],
    )

    n.h2("7.4 Automation Tools")
    n.p("Automation tools beat ad-hoc Bash or Python scripts because they **simplify and standardize**, give "
        "out-of-the-box features, help reusability and security, do **discovery and inventory**, handle scale, and "
        "engage a community.")
    n.h3("Critical Concepts")
    n.bullets([
        "**Idempotent software** produces the same desirable result every time it runs. In deployment software this enables **convergence and composability**: build collections that create new kinds of infrastructure, and rerun whole build or deploy collections to safely repair, upgrade incrementally, change configuration, or scale.",
        "**Procedural vs declarative:** procedural code can reach idempotency, but many tools use a **declarative** approach. A declarative is a **static model**; middleware adds deployment details, examines present circumstances, and brings real infrastructure into line with the model by the least time-consuming path.",
        "**Statelessness:** automation works best when redeploying an app in place does not destroy the data users need. **Not stateless** = saves important information in local files or a local database. **Stateless** = persists state to a **separate database** or needs no memory of state between calls.",
    ])
    n.table(
        ["Term", "Meaning"],
        [
            ["**Provisioning**", "Obtaining compute, storage, and network infrastructure (real or virtual), enabling communications, putting it into service, ready for operators and developers"],
            ["**Configuration**", "Installing base applications and services and performing the tasks and tests to prepare a low-level platform for applications or a higher-level platform"],
            ["**Deployment**", "Building, arranging, integrating, and preparing multi-component applications or higher-level platforms, often across multiple nodes"],
            ["**Orchestration**", "Automation managing workload lifecycles and reacting dynamically to change; or workflows that link automation tasks to deliver business benefit such as self-service"],
        ],
        [1.6, 4.9],
    )
    n.memory("Order of effort: **P**ut it in place (Provision), **C**onfigure the base, **D**eploy the app, **O**rchestrate it all. \"**P**ink **C**ats **D**rink **O**rangeade.\"")
    n.h3("Popular Tools")
    n.bullets([
        "**Puppet was the first modern automation tool:** open source in **2005**, commercialized as **Puppet Enterprise** by Puppet Labs in **2011**.",
        "The most popular tools are **Ansible, Puppet, Chef**. All are relatively easy to learn, available in open source, and have plugins and adapters to control many resource types.",
        "Other tools: OpenStack **HEAT**, AWS **CloudFormation**, **SaltStack**, **Terraform**.",
    ])
    n.table(
        ["", "Ansible", "Puppet", "Chef"],
        [
            ["**Architecture**", "**Control node** on any Linux machine with Python 2 or 3, connects over **SSH**; no agent needed", "A **Puppet Server** plus a secure **Puppet Agent** on each host; modules for cloud APIs and hardware that cannot run an agent; proxy agent at scale", "**Chef Workstation**, **Chef Infra Client** (host agent), **Chef Infra Server**; most tasks can also go from Workstation straight to nodes"],
            ["**Code format**", "**YAML** (`.yml`) files, tasks run top-down", "**Manifests** (`.pp`), classes, modules", "**Recipes** (Ruby, `default.rb`) in **cookbooks**"],
            ["**Reusable unit**", "**Roles** referenced from higher-level **playbooks**", "**Modules** from Puppet Forge", "**Cookbooks** from Chef Supermarket"],
            ["**At scale**", "Red Hat **Ansible Tower** or the **AWX** project; **Ansible Vault** encrypts secrets", "Extra **compile masters** behind a load balancer; PE-PostgreSQL replaces PuppetDB in Puppet Enterprise", "Chef Infra Server in high availability with load-balanced front-end proxies"],
            ["**Cisco support**", "Modules for ACI (APIC), IOS-XR over CLI or NETCONF, UCS via Intersight", "Cisco IOS modules, UCS modules via UCS Manager", "Modified Chef Infra Agents in the NX-OS guest shell; Cisco Cookbook for NX-OS; UCS cookbook for IMC"],
        ],
        [1.1, 1.8, 1.8, 1.8],
    )
    n.memory("**A**nsible = **A**gentless (SSH). **P**uppet = **P**ulls from a server with an agent (every **15 minutes**). **C**hef = **C**ookbooks and **C**ook recipes with Knife.")

    n.h3("Ansible In Detail")
    n.bullets([
        "Free open source, plus a version with added features from IBM/Red Hat called **Ansible Tower**. Managed mostly from the **Bash command line**; code is written in any text editor.",
        "The control node can run shell commands on a remote server, talk to a router through its REST interface, inject Python scripts into targets and remove them after they run, and install Python on targets if needed. Plugins let it gather facts from devices that cannot run Python.",
        "Hundreds of pre-built **Python modules** wrap operating-system functions. Work is split into YAML files holding tasks.",
        "A **playbook** can be one monolithic document of named tasks. Complex jobs are modeled as **roles** (low-level task sequences) referenced from higher-level playbooks. This keeps clarity, reusability, and shareability.",
        "Project folders are a nested directory tree, easy to put under version control for **GitOps-style infrastructure as code**. Elements: **inventory files, variable files, library and utility files, main playbook files**.",
    ])
    n.h3("The Ansible Web Server Example")
    n.p("Goal: build a simple website on a target host over SSH. Prerequisites: a target running a compatible OS (such as "
        "Ubuntu 18.04), **SSH and keywise authentication** set up on it, and Ansible on your workstation. At the top "
        "of the project folder you need an **inventory file**, a top-level **`site.yml`**, and a **role** folder "
        "structure for the webserver role (built with **`ansible-galaxy`**).")
    n.box("Code: inventory file", "[webservers]\ntarget    # can also be IP address")
    n.p("`webservers` is a **group**. You can add hostnames to it or add more group blocks (for example `[dbservers]`) for complex deployments.")
    n.box("Code: site.yml (top-level playbook)", "---\n- hosts: webservers\n  become: true\n  roles:\n    - webservers")
    n.p("`site.yml` says **which hosts** to act on and **which roles** to apply. `become: true` means perform the roles "
        "**as root via sudo**.")
    n.box("Code: roles/webserver/tasks/main.yml", "---\n- name: Perform updates and install apache2\n  apt:\n    name: apache2\n    state: present\n    update_cache: yes\n- name: Insert new homepage index.html\n  copy:\n    src: index.html\n    dest: /var/www/html\n    owner: myname\n    mode: '0644'")
    n.bullets([
        "The role has **two tasks**: deploy **Apache2** (the `apt:` stanza names the package, its required state, and updates the cache), and **copy a new `index.html`** into the Apache2 HTML root, replacing the default page (the `copy` routine also changes owner and permissions).",
        "The `copy` command assumes the file is stored in the role's **`/files`** directory unless told otherwise.",
    ])
    n.box("Code: run the deployment", "ansible-playbook -i inventory -u myname -K site.yml")
    n.table(
        ["Part", "Meaning"],
        [
            ["`-i inventory`", "names the **inventory file**"],
            ["`-u myname`", "names your **sudo user**"],
            ["`-K`", "asks for your **sudo (BECOME) password** when execution begins"],
            ["`site.yml`", "the file that **governs the deployment**"],
        ],
        [2.0, 4.5],
    )
    n.memory("**I**nventory, **U**ser, **K**ey (password prompt), then the playbook: \"**I U K**, play!\"")
    n.p("**CI/CD walkthrough on the slides:** a developer commits a change on GitHub; tests in the repository run "
        "syntax and sanity checks and code-review rules on each pull request; the CI/CD system (the slide pipeline uses "
        "**Jenkins**) prepares an environment and runs predefined tests, then a second pipeline pushes to production.")
    n.p("**Labs in the module:** Use Ansible to Back Up and Configure a Device; Use Ansible to Automate Installing a Web Server.")

    n.h3("Puppet In Detail")
    n.bullets([
        "**Architecture:** a designated **server**, a secure client called the **Puppet Agent**, **modules** for cloud APIs and hardware that cannot run an agent, and (at scale) a **proxy agent** to offload work connecting to device CLIs.",
        "The Puppet Server needs powerful hardware (or a big VM) and a configured **NTP client**. Agents need **`puppet.conf`** to find the server. Code lives under **`/etc/puppetlabs/code/environments`**. Extra resources come from **Puppet Forge** with the `puppet module` command.",
        "**Certificate signing:** the first time the agent starts it asks the server to **sign its certificate**. On the server, the **`ca list`** command shows pending certificates; you then sign the certificate. After that the server gathers facts and clients **converge their state every 15 minutes**.",
        "**At scale:** a monolithic server is recommended by the open-source implementers; add **compile masters** (which compile catalogs for agents) behind a **load balancer**.",
        "Cisco resources: **Cisco IOS modules** and **Cisco UCS modules** (via UCS Manager).",
    ])
    n.h3("The Puppet Apache Example")
    n.bullets([
        "Become root on the server (`sudo su -`), go to the `/modules` folder in the `/production` environment, and create the module folders.",
        "Inside the `manifests` folder create **`init.pp`**, a **reserved filename for the initialization step of a module**.",
        "Then create **`site.pp`** in `/etc/puppetlabs/code/environments/production/manifests`, which **invokes the module and applies it to the target machine**.",
    ])
    n.box("Code: init.pp", "class apache2 {\n  package { 'apache2':\n    ensure => installed,\n  }\n  service { 'apache2':\n    ensure  => true,\n    enable  => true,\n    require => Package['apache2'],\n  }\n}")
    n.bullets([
        "**Step 1:** the **package** resource installs the named package with **`ensure => installed`**.",
        "**Step 2:** the **service** resource runs once its requirement is met, makes sure the service is available, and **enables it to restart automatically on reboot**.",
    ])
    n.box("Code: site.pp", "node 'puppetclient' {\n  include apache2\n}")
    n.p("**Two ways to deploy:** restart the Puppet Server so manifests are compiled and the agent applies them at the next update cycle; or, for **development and debugging**, invoke the Puppet Agent on the target so it immediately asks the server, downloads its catalog, and applies it.")

    n.h3("Chef In Detail")
    n.bullets([
        "Chef is a complete system for **infrastructure as code**. Products are partly licensed but free for personal use (Chef Infra Server is free for **fewer than 25 managed nodes**).",
        "**Chef Workstation** includes command-line tools, Test Kitchen, **ChefSpec**, and **InSpec**. It runs on Linux and Windows.",
        "**`chef-run`** makes basic configuration changes on hosts (the example installs the **ntp** package). **Chef Infra Client** can be bootstrapped by Workstation or preinstalled on nodes using the Chef installer **Omnitruck**.",
        "Before installing **Chef Infra Server**, install openssh-server with keywise access and **NTP**. The server stores configuration and hands it to clients **when polled**, so clients converge to a desired state. **Chef-Manage** adds the web interface.",
        "**Knife** manages cookbooks, recipes, nodes, and other assets and talks to the Infra Server. Set it up with **`config.rb`** in the `.chef` folder, then run **`knife ssl fetch`** to store the server certificate. **`knife bootstrap`** installs the client on a target node.",
    ])
    n.box("Code: Chef recipe (default.rb)", "apt_update do\n  action :update\nend\npackage 'apache2' do\n  action :install\nend\ncookbook_file \"/var/www/html/index.html\" do\n  source \"index.html\"\n  mode \"0644\"\nend")
    n.bullets([
        "The recipe does **three actions**: **`apt_update`** handles the apt package manager on Debian, **`package`** installs apache2 from public repositories, and **`cookbook_file`** copies `index.html` from `/files/default` to the target server.",
        "Cookbook files in the **`/files/default`** subdirectory are found by recipe name alone, with no path.",
        "The node's **`run_list`** is the ordered list of recipes for the node, for example `recipe[apache2]`. **`knife ssh`** logs into the node over SSH and runs **`chef-client`**.",
        "Cisco: modified Chef Infra Agents in the **NX-OS guest shell**, and a **Cisco Chef Cookbook** on Chef Supermarket.",
    ])

    n.h2("7.5 Infrastructure As Code")
    n.bullets([
        "**Immutability** = maintaining systems **entirely as code, performing no manual operations on them at all**.",
        "**GitOps** is modern infrastructure as code, also called **\"operations by pull request\"**. A typical repository has branches such as **Development, Testing/UAT, and Production**.",
    ])
    n.table(
        ["Strategy", "What It Is"],
        [
            ["**Blue/green deployment**", "Reduces or eliminates downtime. Keep **two identical production environments** (any two colors will do) and be able to redirect traffic quickly. Deploy the release to the **idle (green)** environment, test, redirect traffic. If problems appear, **switch back to blue**. If green is good, blue's resources are freed and roles swap for the next release."],
            ["**Red/black** (note on the slide)", "Some practitioners say in blue/green traffic moves **gradually** (it hits both systems for a while), while in red/black traffic is **cut over all at once**."],
            ["**Canary testing**", "Like rolling blue/green but more delicate. Migration happens **customer by customer or even user by user**, to reduce risk and improve feedback quality."],
        ],
        [1.8, 4.7],
    )
    n.memory("Blue/green = **swap the whole lane**. Canary = **one bird at a time** (a few users first, like the canary in the coal mine).")

    n.h2("7.6 Automating Testing")
    n.bullets([
        "Unit test tools such as **pytest** let developers test code automatically on every change. Unit-test frameworks make tests part of the codebase through commits, pull requests, and code-review gates. They are useful for **test-driven development (TDD)**.",
        "Testing a network is hard because behavior is **collective** across many devices; manual testing is difficult, time-consuming, error-prone, and risky.",
        "Cisco SDN work: **Application Centric Infrastructure (ACI)**, **Cisco DNA Center**, and REST APIs and SDKs for Ansible, Puppet, and Chef.",
    ])
    n.h3("pyATS And Genie")
    n.table(
        ["Item", "What It Is"],
        [
            ["**pyATS** (Python Automated Test System)", "Python-based network device **test and validation** solution; can be used in any Python code; modular with **AEtest** and **Easypy**; has a CLI to interrogate live networks and extract facts; can consume topologies from **JSON, YANG models** and other sources"],
            ["**Genie**", "The **higher-level library** of pyATS: APIs to interact with devices, plus a CLI for topology and device management; installing it adds features to pyATS"],
            ["**Testbed file**", "A **YAML** file (or built from YAML and Python) describing the devices; tells pyATS which library APIs to load and how to communicate with each device"],
            ["**pyATS script**", "A Python file where pyATS tests are declared; syntax inspired by pytest, with assertions and explicit results"],
        ],
        [2.2, 4.3],
    )
    n.bullets([
        "Install pyATS inside a Python **virtual environment (venv)**: a copy of your base environment kept separate from it, so you avoid permanently changing your system. venv is native to Python 3; Ubuntu 18.04 may need the **python3-venv** package.",
        "Steps from the slide: make sure **`python3-pip`** is installed and install **git**; create the venv; `cd` into the project folder and activate it; install pyATS from **PyPI**; verify with **`pyats --help`**; clone the DevNet pyATS sample scripts.",
        "\"Failed building wheel for...\" errors during install can be **safely ignored**; pip has a backup plan and the dependencies are installed anyway.",
    ])
    n.p("**Lab in the module:** Automated Testing Using pyATS and Genie (create a venv, use pyATS, create a testbed file, use Genie to compare configurations).")

    n.h2("7.7 Network Simulation")
    n.bullets([
        "Network simulation lets you test configurations, debug configuration code, and learn Cisco infrastructure and APIs **safely, conveniently, and cheaply**.",
        "**Cisco VIRL (Virtual Internet Routing Laboratory)** is a commercial product originally built for internal Cisco use. Now version 2, it runs on **bare metal or large VMs** on several hypervisors. The virtual equipment runs **the same code as real Cisco products**.",
        "VIRL gives a **local CLI** for system management, a **REST interface** for automation, and a **UI** (Design perspective: drag, drop, and connect network entities).",
        "Its native format is the **`.virl` file**, a human-readable **YAML** file describing routers, interface configs and connections, and credentials. It lets you define simulations **as code**, launch simulations through the VIRL REST API, convert to and from **pyATS and Genie testbed files**, and detect **configuration drift**.",
    ])
    n.memory("`.virl` = **VIRL** + **YAML**. Drift check = compare the simulation with the `.virl` file.")

    n.h2("Module 7 Labs On The Slides")
    n.bullets([
        "Install the CSR1000v VM (DEVASC-LAB VM and CSR1000v VM on VirtualBox, verify communications).",
        "Use Ansible to Back Up and Configure a Device.",
        "Use Ansible to Automate Installing a Web Server (backup, IPv6 addressing, install Apache, add options).",
        "Automated Testing Using pyATS and Genie.",
    ])
    n.pagebreak()

    n.h2("Module 7 Cram Sheet")
    n.table(
        ["Topic", "Remember"],
        [
            ["Walk, Run, Fly", "Read only, self-service, CI/CD"],
            ["Full-stack automation benefits", "Self-service, scale on demand, observability, automated problem mitigation"],
            ["Software-defined infrastructure", "Also known as cloud computing"],
            ["SRE", "Institutionalized by Google in 2003"],
            ["Debois, Allspaw and Hammond", "Both 2009"],
            ["SLO, SLI, error budget", "Objective, indicator, allowed failure"],
            ["Dev vs Ops", "Dev = profit center, deep skills; Ops = cost center, broad skills, on call"],
            ["Idempotency", "Same result every run; check first, change only what is needed"],
            ["Stateless app", "Persists state to a separate database"],
            ["Provisioning, configuration, deployment, orchestration", "Get infra, prepare platform, build app, coordinate workflows"],
            ["First modern automation tool", "Puppet, 2005 (Enterprise 2011)"],
            ["Ansible", "Agentless over SSH, YAML, inventory, playbooks, roles; `ansible-playbook -i inventory -u myname -K site.yml`"],
            ["Puppet", "Server and agent, certificates (`ca list`), `init.pp`, `site.pp`, converge every 15 min"],
            ["Chef", "Workstation, Infra Client, Infra Server; Knife; cookbook, recipe `default.rb`; `run_list`; fewer than 25 nodes free"],
            ["Immutability, GitOps", "No manual operations; operations by pull request"],
            ["Blue/green, canary", "Two identical environments; user by user"],
            ["pyATS, Genie, testbed", "Python test system; its library; YAML device file"],
            ["VIRL", "`.virl` YAML file; same code as real Cisco products"],
        ],
        [2.4, 4.1],
    )
    n.pagebreak()

    # ------------------------------------------------------------------ MODULE 8
    n.h1("Module 8: Cisco Platforms and Development")

    n.h2("8.1 The Cisco API Platform")
    n.p("DevNet creates **Dev Centers** for each technology group to keep technologies together. The Dev Centers are: "
        "**Cloud, Collaboration, Data center, Internet of Things (IoT) and edge computing, Networking, Security, "
        "Wireless and mobile, and Application developers.** (The summary slide also lists **Unified Communications Manager**.)")

    n.h2("8.2 Cisco SDKs")
    n.bullets([
        "A **Software Development Kit (SDK)** is a set of integrated software development tools for developing applications for a **specific device or system**. Most SDKs are a package with libraries, documents, and code examples. SDKs often help with **pagination or rate limiting** on a particular API.",
        "Cisco SDKs on the slide: Webex Teams Android SDK; Jabber Web SDK; Jabber Guest SDK for Web, iOS, Android; **Cisco DNA Center Multivendor SDK**; **UCS Python SDK**; **Cisco APIC Python SDK (Cobra SDK)**; **Cisco IMC Python SDK**; Cisco Instant Connect SDK; **Webex Teams Python SDK**.",
    ])

    n.h2("8.3 Model-Driven Programmability: YANG, NETCONF, RESTCONF")
    n.h3("Model-Driven Programmability")
    n.bullets([
        "Provides a **human-readable** configuration language that is model-based, structured, and computer-friendly.",
        "Supports multiple model types: **native, OpenConfig, and IETF**.",
        "Its specification is **decoupled from transport, protocol, and encoding**.",
        "Uses model-driven APIs for abstraction and simplification; leverages open source with wide support.",
    ])
    n.h3("YANG")
    n.p("**YANG** (Yet Another Next Generation) is a **data modeling language** used to model configuration and state "
        "data manipulated by **NETCONF**, NETCONF remote procedure calls, and NETCONF notifications. There are two "
        "types of YANG models, **open and native**. YANG lets different vendors describe their device type, "
        "configuration, and state so it maps to device operation programmatically.")
    n.table(
        ["YANG Node Type", "Meaning"],
        [
            ["**Leaf node**", "One value of a simple type"],
            ["**Leaf-list node**", "A list of leaf values"],
            ["**Container node**", "Groups related nodes"],
            ["**List node**", "A sequence of entries identified by a key"],
        ],
        [2.4, 4.1],
    )
    n.p("YANG terms on the slide: anyxml, augment, container, data model, data node, data tree, derived type, grouping, "
        "identifier, leaf, leaf-list, list, module, RPC, state data.")
    n.p("**pyang** is a tool installed with **pip** in a virtual environment that turns a YANG file into an easy-to-read **tree structure** (the slide shows `ietf-interfaces`).")
    n.memory("Four YANG nodes: **L**eaf, **L**eaf-list, **C**ontainer, **L**ist = \"**L**ittle **L**ions **C**hase **L**ambs.\"")
    n.watch("The slides quote **RFC7519** for both YANG and NETCONF. In the real world those RFCs are different (YANG is RFC 7950, NETCONF is RFC 6241, and RFC 7519 is JSON Web Tokens). "
            "If a question quotes the slide, the expected answer is what the slide says. This warning is mine, not from the slides.")
    n.h3("NETCONF")
    n.bullets([
        "**Network Configuration (NETCONF)** is a protocol from the IETF designed to **install, manipulate, and delete** the configuration of network devices. It is the **primary protocol used with YANG** data models today.",
        "It uses **XML-based data encoding** for both configuration data and protocol messages, and gives a small set of operations to manage configuration and retrieve state.",
    ])
    n.table(
        ["NETCONF Operations (Nine)", ""],
        [
            ["**get**", "**copy-config**"],
            ["**get-config**", "**delete-config**"],
            ["**edit-config**", "**lock** and **unlock**"],
            ["**close-session**", "**kill-session**"],
        ],
        [3.25, 3.25],
    )
    n.memory("Nine operations: **2 gets** (get, get-config), **3 changers** (edit, copy, delete config), **2 lockers** (lock, unlock), **2 enders** (close-session, kill-session).")
    n.h3("NETCONF Versus SNMP")
    n.table(
        ["NETCONF", "SNMP"],
        [
            ["Multiple data stores (**candidate, running, startup**)", "Uses a **pull model** to retrieve data"],
            ["Device-level and network-wide **transactions**", "Does **not support transactions**"],
            ["Configuration **testing and validation**", "**No discovery** process for finding the MIBs a device supports"],
            ["Extensible remote procedure calls", "Lacks **backup and restore** of element configuration"],
            ["Built-in **capability exchange**", "Limited industry support for configuration MIBs"],
        ],
        [3.25, 3.25],
    )
    n.h3("RESTCONF")
    n.bullets([
        "**RESTCONF** is defined in **RFC 8040**: a protocol for **REST-like access** to configuration information and control. It uses the datastore models and command verbs from NETCONF, **encapsulated in HTTP messages**.",
        "It uses structured data (**XML or JSON**) and YANG to give REST-like APIs. It is **not intended to replace NETCONF**; it is an HTTP interface that follows REST principles and fits the NETCONF datastore model.",
        "The base URL format is `https://<hostURL>/restconf<resource><container><leaf><options>`, and any portion after `restconf` can be omitted. The base URI is `/restconf/<resource-type>/<yang-module:resource>`.",
    ])
    n.table(
        ["Description", "NETCONF", "RESTCONF"],
        [
            ["Create a data resource", "`<edit-config>`", "**POST**"],
            ["Retrieve data and metadata", "`<get-config>`, `<get>`", "**GET**"],
            ["Create or replace a data resource", "`<edit-config>` (operation create/replace)", "**PUT**"],
            ["Delete a data resource", "`<edit-config>` (operation delete)", "**DELETE**"],
        ],
        [2.2, 2.6, 1.7],
    )
    n.memory("RESTCONF = the HTTP verbs you already know: **P**OST creates, **G**ET reads, **P**UT replaces, **D**ELETE deletes.")
    n.h3("RESTCONF Versus NETCONF")
    n.bullets([
        "**NETCONF** is more comprehensive, flexible, and complex. **RESTCONF** is easier for engineers with REST API experience.",
        "NETCONF supports **running and candidate** data stores; RESTCONF supports **only the running** data store, because edits of the candidate store are immediately committed.",
        "RESTCONF **does not support obtaining or releasing a data store lock**. If a data store has an active lock, the RESTCONF edit **fails**.",
        "A RESTCONF edit is a **transaction limited to one RESTCONF call**, and it does **not** support transactions across multiple devices.",
        "**Validation is implicit** in every RESTCONF edit: it either succeeds or fails.",
    ])
    n.watch("\"Only running\" and \"no locks\" are RESTCONF. \"Running and candidate, lock and unlock\" are NETCONF.")
    n.p("**Labs:** Explore YANG Models (GitHub and pyang); Use NETCONF to Access an IOS XE Device (ncclient); Use RESTCONF to Access an IOS XE Device (Postman and Python).")

    n.h2("8.4 Cisco Network Management")
    n.p("Network automation simplifies day-to-day work: **device provisioning, device software management, compliance "
        "checks, reporting, troubleshooting, data collection and telemetry**. Programmability helps reduce **operational "
        "expenses (OPEX)** and speeds service delivery by automating tasks normally done by hand in the **CLI**.")
    n.h3("Cisco IOS XE")
    n.bullets([
        "IOS XE offers standards-based, consistent, programmable interfaces and standard data models for configuration, deployment, and rollback. It is **based on Linux** and used on most high-end Cisco switches, routers, and gateways. IOS was the original operating system; **IOS XE is the next-generation programmable platform**.",
        "**NETCONF/YANG is supported as of IOS XE 16.3.1.** Cisco device YANG models are in the Cisco Device YANG models repository.",
        "IOS XE supports two datastores, **running and candidate**, plus locking and configuration **rollback**.",
        "NETCONF and RESTCONF connections should be authenticated with **AAA credentials**. RESTCONF runs over **HTTPS**.",
    ])
    n.table(
        ["To Enable", "Command (from configure terminal)"],
        [
            ["**NETCONF**", "`netconf-yang`"],
            ["**RESTCONF**", "`restconf`"],
            ["HTTPS for RESTCONF on **port 443**", "`ip http secure-server`"],
        ],
        [2.6, 3.9],
    )
    n.p("If `netconf-yang` returns **\"Unknown command\"**, double-check the device configuration. Browse or clone "
        "**github.com/YangModels/yang** for all Cisco YANG models; the **`vendor/cisco`** subdirectory holds the Cisco platform models.")
    n.h3("Cisco DNA Center")
    n.bullets([
        "A **foundational controller and analytics platform** for large and midsize organizations, with services and integration in the **north, east, south, and west** directions. A single dashboard for network management, automation, assurance, monitoring, analytics, and security.",
        "The GUI organizes services into **Design, Policy, Provision, Assurance, and Platform**.",
        "**RBAC:** the initial user, **admin**, has the **SUPER-ADMIN-ROLE**, with complete control and access to all sections.",
        "Hardware: the **DNA Center appliance** runs on dedicated Cisco rack servers in scalable configurations.",
        "The **Intent API** gives programmatic access to DNA Center services. Documentation is on DevNet under \"Cisco DNA Center - Intent API\" and, with a built-in **TryIt**, in the GUI under **Platform > Developer Toolkit**.",
        "**POST and PUT** Intent API calls need a **JSON** payload and are handled **asynchronously**: a successfully started request returns a structure with **`executionId`, `executionStatusUrl`, and a status message**, even though the work may not be finished.",
    ])
    n.memory("DNA Center GUI = **D**esign, **P**olicy, **P**rovision, **A**ssurance, **P**latform: \"**D**ogs **P**ush **P**ink **A**pple **P**ies.\"")
    n.h3("Cisco ACI And APIC")
    n.bullets([
        "**Cisco ACI** runs on **Nexus 9000** hardware and is Cisco's **SDN** solution. The centralized management is the **Application Policy Infrastructure Controller (APIC)**, a **cluster of controllers**, giving unified operation of physical and virtual infrastructure.",
        "The **entire** ACI infrastructure is open to programmatic access through the **ACI object model**, which represents the complete configuration and run-time state of every component.",
        "Nexus 9000 switches in **NX-OS mode** instead of ACI mode give device-level APIs and can be managed as Linux devices.",
        "Use cases: programmability as a single fabric, desired state defined and enforced, extension to **AWS or Azure** through the **Multi-Site Orchestrator (MSO)** and its API (the MSO API is different from the ACI APIC API).",
        "Tools: **ACI toolkit, Cobra (Python), ACIrb (Ruby), Puppet, Ansible**.",
        "**API Inspector** is a built-in APIC tool that shows (and lets you copy) the internal API messages the GUI sends when you perform a task, so you can replicate them to automate key operations.",
        "**Ansible ACI modules** (and MSO modules) let you manage fabrics as code. The slide task uses **`aci_tenant`** to **idempotently** ensure a tenant exists (creating it if not).",
        "The APIC **CLI, GUI, and SDK all use the same REST API**.",
    ])
    n.table(
        ["ACI Naming", "Meaning"],
        [
            ["**Managed Object (MO)**", "Object instances; every MO has a unique DN"],
            ["**Distinguished Name (DN)**", "Identifies a specific object globally; maps directly to URLs"],
            ["**Relative Name (RN)**", "Names the object **within its parent** (apart from its siblings)"],
        ],
        [2.4, 4.1],
    )
    n.box("ACI URL Format", "http(s)://  host:port  /api  /{mo|class}  /{dn|classname}  .{xml|json}  ?{options}")
    n.bullets([
        "The literal string **`api`** says the API is being invoked. The final **mandatory** part is the **encoding format: `.xml` or `.json`**. Filters go after `?`, joined with `&`.",
        "A common use case is **monitoring the ACI fabric**; automation can then apply policies and cut human error.",
    ])
    n.h3("Cobra SDK Workflow")
    n.p("**Cobra** is a Python library for the APIC REST API used to manipulate the MIT. The workflow, in order:")
    n.numbered([
        "Create a **session** object.",
        "**Log in** to the APIC.",
        "Create a **configuration object**.",
        "Create a **configuration request** object.",
        "Add the config object to the request.",
        "**Commit**.",
    ])
    n.memory("Cobra order: **S**ession, **L**ogin, **C**onfig object, **R**equest object, **A**dd, **C**ommit = \"**S**ome **L**azy **C**obras **R**est, **A**sleep, **C**oiled.\"")
    n.h3("Cisco Meraki")
    n.bullets([
        "A suite of **cloud-managed** network solutions with a **single source of management** for infrastructure, locations, and devices: wireless, switching, security, SD-WAN, mobile device management, and **smart cameras**.",
        "Meraki has **five APIs** for integration. The **Dashboard API** is a **RESTful API over HTTPS using JSON**.",
        "To use it: first **enable the API** under **Organization > Settings**, then generate an **API key** on the **My Profile** page. The key belongs to a Dashboard administrator account and must be **kept safe**, because it authenticates to **all** organizations with the API enabled.",
        "**Location Scanning API:** retail stores, conferences, user-engagement trends. **Bluetooth Scanning:** access points detect nearby **BLE** devices. **Smart Cameras** do object detection and tracking **at the edge**. Camera APIs: **MV Sense, Live Link API, Snapshot API**.",
    ])
    n.h3("Cisco NX-OS")
    n.bullets([
        "**Nexus Operating System (NX-OS)** is the data center operating system for **Nexus switches**.",
        "**Open NX-OS** uses the **native Linux networking stack**, not the custom userspace stack (NetStack) of earlier NX-OS. Switch interfaces (physical, port-channel, vPC, VLAN) map to the kernel as standard **Linux netdevs**.",
        "Containers: runs **Linux Containers (LXC)** and offers a **CentOS 7-based Guest Shell** (secure, isolated shell for custom functions).",
        "Telemetry apps: **Ganglia, Splunk, Nagios**.",
        "Programmatic interfaces: the **NX-API REST** service and **YANG** model-driven programmability. The **native NX-OS data model** is in the image, so no extra download is needed.",
        "YANG models are supported through **NETCONF and RESTCONF** on Open NX-OS; a **NETCONF agent** is the client-facing interface. These instructions apply to **Open NX-OS 9.2.1 and later**; earlier versions needed manual RPM installation.",
        "**OpenConfig** models for Open NX-OS are downloaded from **Cisco Artifactory**, copied to the switch, and installed with **bash-shell** (the **feature bash-shell** must be enabled).",
    ])
    n.h3("Cisco NSO")
    n.bullets([
        "**Network Services Orchestrator (NSO)** lets operators adopt service configuration dynamically. **Three components:** **device and service abstraction layers, a configuration database, and a model-driven programmable interface (YANG)**.",
        "Two functional layers: the **Device Manager** (integrates devices through a YANG and NETCONF view and builds a **transactional change sequence**, whether the device speaks SNMP or CLI) and the **Service Manager** (service-aware apps; handles the **full lifecycle** of service instances: create, modify, delete).",
        "The **Configuration Database (CDB)** stores NSO's own configuration, all service configuration, and a **copy of every managed device's configuration**. It provides a model for config data, an internal API for locating element configuration, and automatic **upgrade and downgrade** support. NFS and other network file systems are **unsuitable** for the CDB in production.",
    ])
    n.table(
        ["NSO YANG Sources (Three)", "Meaning"],
        [
            ["**NSO data-model**", "Defines the built-in functions of NSO"],
            ["**Data models**", "From devices: native NETCONF YANG, YANG generated from SNMP MIBs, or reverse-engineered from a CLI device"],
            ["**YANG service models**", "Developer-defined services such as a BGP peer, firewall setting, or MPLS VPN"],
        ],
        [2.4, 4.1],
    )
    n.bullets([
        "A **Service** has two parts: a **YANG service model** (the attributes) and a **device configuration mapping** (done with **service templates** or **programmatically in Java**). Validation that needs outside code (like database look-ups) uses **MAAPI**.",
        "**Northbound** interfaces (integrate NSO with apps and portals): **REST API, CLI, NETCONF, Web UI, SNMP, Java**. The legacy REST API was **deprecated in NSO 5.1** and scheduled for removal in 5.3.",
        "The **NSO CLI** comes in two flavors: **Juniper-style and Cisco XR-style**. The **Web UI** is a YANG model browser built with **pure client-side JavaScript**.",
        "**Southbound** interfaces (configure network elements): **NETCONF, SNMP, CLI, IOS, IOS XR**. NSO needs a YANG model, device address, management port, and credentials per device, and a **name** for each.",
        "Add a device by **discovery, manually, cloning, or templates**.",
    ])
    n.memory("NSO = **N**orth is for **N**eighbors (apps and portals), **S**outh is for **S**witches (devices). Add a device: **D**iscover, **M**anual, **C**lone, **T**emplate.")
    n.h3("Cisco SD-WAN")
    n.bullets([
        "Managed through the **vManage** dashboard. It provides **transport independence** (zero network downtime across multiple connections), **network services** (rich networking and security by clicks), and **endpoint flexibility** (branches, campuses, data centers, cloud).",
        "Key features: **cloud-first architecture, embedded security, predictable application experience**.",
    ])
    n.table(
        ["Component", "Role"],
        [
            ["**vManage NMS**", "Centralized **network management system**; configure overlay networks from a dashboard"],
            ["**vSmart Controller**", "Controls the **flow of data traffic**, working with vBond to **authenticate** SD-WAN devices as they join"],
            ["**vBond Orchestrator**", "**Orchestrates connectivity** between vEdge routers and vSmart controllers"],
            ["**vEdge Routers**", "Provisioned at the **site perimeter** (hardware, software, cloud, or virtual); secure the virtual overlay over a mix of WAN transports"],
        ],
        [2.0, 4.5],
    )
    n.p("The SD-WAN **REST API** controls, configures, and monitors devices in the overlay. Each feature or operation is a "
        "**resource**, and resources are grouped into **collections**: Administration, Certificate Management, "
        "Configuration, Device Inventory, Monitoring, Real-Time Monitoring, Troubleshooting Tools.")
    n.memory("**vManage** manages. **vSmart** is the smart controller. **vBond** bonds (orchestrates) edge to controller. **vEdge** sits at the edge.")

    n.h2("8.5 Cisco Compute Management")
    n.bullets([
        "**Cisco Unified Computing System (UCS)** with its software and SaaS adjuncts provides a full physical and logical plant for compute, networking, and storage. Tools: **UCS Manager, UCS Director, Intersight** (and SaaS global management). UCS is **hyperconverged** infrastructure and virtualizes physical infrastructure so it is software-definable.",
        "UCS is a data center server line of hardware, switching fabric, embedded management software, and virtualization support, managed as a single unit through **UCS Manager, UCS Central, and the Cisco Integrated Management Controller (CIMC/IMC)**.",
    ])
    n.h3("Cisco UCS Manager")
    n.bullets([
        "Runs on the **primary fabric interconnect** with a **Virtual IP address (VIP)** and failover to the subordinate fabric interconnect. It **mediates all communication** in the system, knows the current configuration, performs **automated device discovery** when a resource is installed, and adds it to the inventory.",
        "It is an **abstraction layer** between server component interfaces and the administrator, presented as a **web GUI, an SSH CLI, and an API**.",
        "**Service Profiles** assign identity to a server when associated with it. **Each server can have only one Service Profile association at a time**, and a profile can be moved from one server to another.",
        "Servers are **B-Series blades** (in a chassis) or **C-Series rack-mounted**, both connected to a redundant pair of switches called **Fabric Interconnects (FIs)**. There should be no single point of failure. Events and alerts are reported with industry protocols like **SNMP and Syslog**.",
    ])
    n.h3("UCS Management Information Model And Managed Objects")
    n.bullets([
        "All physical and logical components are in a hierarchical **Management Information Model (MIM)**, also called the **MIT** (a tree). Each node is a **Managed Object (MO)** or group of objects holding administrative and operational state. The top of the tree is **`sys`**.",
        "A UCS managed object is an **XML representation** of a physical or logical entity. An object is identified by its **Distinguished Name (DN)** or **Relative Name (RN)**. The DN is a series of RNs: **`dn = {rn}/{rn}/{rn}/{rn}`**. All managed objects belong to a **class**.",
    ])
    n.table(
        ["UCS XML API Group", "Methods"],
        [
            ["**Authentication**", "**aaaLogin** (log in, get cookie), **aaaRefresh** (refresh cookie), **aaaLogout** (exit, deactivate cookie)"],
            ["**Query** (read)", "**configResolveDn** (by DN), **configResolveDns** (set of DNs), **configResolveClass**, **configResolveClasses**, **configFindDnsByClassId**, **configResolveChildren**, **configResolveParent**, **configScope**"],
            ["**Configuration** (change)", "**configConfMo** (single managed object), **configConfMos** (multiple subtrees), **configConfMoGroup** (same change across multiple subtrees or MOs)"],
        ],
        [1.8, 4.7],
    )
    n.memory("Query methods start **configResolve...** (they **resolve** = read). Change methods start **configConf...** (they **conf**igure = write). Login, Refresh, Logout = **aaa**.")
    n.bullets([
        "**UCS API documentation** (the UCS Object Model documentation, with the UCS Platform Emulator or online) lists every object class and method. Per-object sections: **Overview** (abstract or concrete), **Naming Rules** (prefix), **Containers Hierarchies**, **Contained Hierarchies**, **Inheritance**, **Events/faults/FSMs**, **Properties Summary**, **Properties Detail**.",
    ])
    n.h3("UCS Tools")
    n.table(
        ["Tool", "Facts"],
        [
            ["**UCS PowerTool**", "A library of **PowerShell cmdlets** for managing UCS from Microsoft OSs through the UCS XML API; **nearly 6000 cmdlets**"],
            ["**UCS Python SDK**", "Python modules built to automate UCS Manager via the UCS XML API; hundreds of modules"],
            ["**UCS Ansible**", "For UCS Manager and CIMC; modules are called as **tasks in a playbook**"],
        ],
        [2.0, 4.5],
    )
    n.box("PowerTool Cmdlets On The Slides", "Connect-Ucs -Name <ip-address-ucs-manager>\nGet-UcsBlade | Select-Object Dn\nGet-UcsLanCloud | Add-UcsVlan -Name vlan100 -Id 100")
    n.p("`Connect-Ucs` **authenticates**, `Get-UcsBlade` lists blades and their DNs, and the last line **creates VLAN 100**.")
    n.h3("Cisco UCS Director")
    n.bullets([
        "A complete, highly secure, **end-to-end management, orchestration, and automation** solution for Cisco and non-Cisco data center components and converged infrastructure based on **UCS and Nexus**.",
        "Features: **central management, self-service catalog, adaptive provisioning, dynamic capacity management, multiple hypervisor support** (VMware ESX/ESXi, Microsoft Hyper-V, Red Hat), **compute, network, and storage management**, dashboards.",
        "Model-based orchestration: a task library with **over 1000 tasks** and out-of-the-box workflows, plus a workflow designer.",
        "**REST API:** needs a valid UCS Director user and an **API access key**, passed as the HTTP header **`X-Cloupia-Request-Key`**. API **version 1** URL: `http://SERVER/app/api/rest?formatType=json&opName=operationName&opData=operationData` (JSON or XML). API **version 2**: **XML only**, `http://server/cloupia/api-v2/group`, HTTP method **POST**. Enable the **developer menu** in the GUI for the **Report Metadata, REST API Browser, and REST Client**. **cURL** runs REST requests from the command line.",
    ])
    n.h3("Cisco Intersight")
    n.bullets([
        "A **Software as a Service (SaaS)** systems management platform for infrastructure at the **edge, remote locations, and the data center**. It builds on the UCS Unified Fabric and UCS management with a **Cisco-hosted** platform. New features are added **without impacting existing automation**.",
        "The Intersight API accepts and returns **JSON** over **HTTP over TLS** and exposes the Intersight **MIM/MIT**. Access it with a **web browser as a REST client** or with **API keys** for remote or service access.",
        "Integrations: **Ansible modules** (inventory collection and configuration management), a **Python SDK** and **PowerShell modules** generated from the **Intersight OpenAPI (Swagger) specification** hosted on intersight.com.",
    ])
    n.memory("UCS Manager = **on-premises** box manager. UCS Director = **orchestration** with a task library. Intersight = **SaaS** in the cloud.")

    n.h2("8.6 Cisco Collaboration Platforms")
    n.bullets([
        "**Cisco Unified Communications Manager (Unified CM, CUCM, CallManager):** an **IP-based** on-premise solution integrating **voice, video, and data** for call control and session management. Manages phone users, IP phones, directory numbers, and connecting calls. Used in hospitals, banks, universities, and government agencies. You define gateways, trunks, and remote destinations and configure hold, transfer, call forward, and conferencing.",
        "Other products: **Contact Center** (call center support), **Finesse** (agent and supervisor desktop), **Webex** (Meetings, Teams, Devices).",
    ])
    n.table(
        ["", "AXL", "UDS"],
        [
            ["**Full name**", "**Administrative XML Layer**", "**User Data Services**"],
            ["**Type**", "**XML/SOAP**-based", "**REST**-based"],
            ["**Purpose**", "**Administration and configuration** (create, read, update, delete gateways, users, devices, route patterns)", "**End users** configure settings; directory search and user preferences in a web app"],
            ["**Data format**", "XML with WSDL", "**XML**-formatted data; uses GET, POST, PUT, DELETE"],
        ],
        [1.2, 2.7, 2.6],
    )
    n.bullets([
        "**AXL method names begin with `list`, `add`, `update`, `get`, `remove`** (for example `listPhone` lists all phones, `addUser` creates a user). Direct SQL queries use **`ExecuteSQLquery`** and **`ExecuteSQLupdate`**.",
        "**Versioning:** AXL schema is **backwards compatible for up to two major releases** (schema 10.0(1) works for Unified CM 10.0(1) through 12.5(1)).",
        "**Change Notification** is an advanced AXL feature: repeat a SOAP request to see what changed since the last run, for specific categories (Phone, User) or all changes.",
        "**Serviceability** has similar SOAP APIs for phone registration status and IP address, a performance monitoring API, and an API to manage and get status of CUCM services.",
        "Advanced features named on the slide include AXL, UDS, Serviceability, PAWS, softphone compatibility, Extension Mobility, Jabber Voice and Video SDK, JTAPI or TAPI, Client Matter Codes, Forced Authentication Codes, hunt lists, and music/video on hold. Unified CM integrates with **Cisco IM&P, voicemail, and Contact Center**.",
    ])
    n.memory("**AXL** = **A**dministrators, **X**ML/SOAP. **UDS** = **U**sers, **D**ata over REST. Admins use the heavy SOAP tool; users get the light REST one.")
    n.h3("Cisco Finesse")
    n.bullets([
        "**Finesse** is Cisco's **browser-based contact center agent and supervisor desktop**, with **REST APIs and JavaScript APIs** to build custom agent desktops, integrate contact center functions into applications, and integrate applications into the Finesse desktop.",
        "A **contact center** (call center) is a centralized place handling customer service by calls, text, email, and chat. **Inbound** tasks: the customer starts contact. **Outbound** tasks: the agent contacts the customer.",
        "Contact center systems do **skill-based routing** with an **Automatic Call Distributor (ACD)** and manage agents and supervisors.",
        "Two deployments: **Standalone Finesse** with a **Contact Center Enterprise** system, and **Co-resident Finesse** with **Unified Contact Center Express**. Finesse talks to the contact center system through the **CTI protocol**.",
        "Finesse REST APIs are HTTP-based, so usable in thick and thin apps. **GET** requests are **synchronous**; the rest are **asynchronous**.",
    ])
    n.h3("Webex Teams")
    n.bullets([
        "**Webex Teams** is an online collaboration solution connecting people through **chat, voice, and video**, with secure virtual workspaces. Features: create spaces, create meetings, work inside and outside the company, place calls. It integrates with Webex devices and with third parties such as Microsoft, Google Cloud, and Salesforce.",
        "The **Webex Teams API** lets you interact with the whole platform, including creating conversational **bots** and embedded video calls.",
    ])
    n.table(
        ["Webex Teams API Resource", "Meaning"],
        [
            ["**Organizations**", "A set of people; can manage other organizations or be managed"],
            ["**Teams**", "Groups of people with rooms visible to all members"],
            ["**People**", "Registered users"],
            ["**Rooms**", "Virtual meeting places where people post messages and collaborate"],
            ["**Memberships**", "A person's relationship to a **room** (list, create, revoke; make a moderator)"],
            ["**Team Memberships**", "A person's relationship to a **team**"],
            ["**Messages**", "Communication in a room (list, create, delete)"],
        ],
        [2.4, 4.1],
    )
    n.memory("Order from big to small: **O**rganization, **T**eam, **R**oom, then **M**essage; **P**eople and **M**emberships connect people to rooms and teams.")
    n.p("**Lab:** Construct a Python Script to Manage Webex Teams (access token, then people, rooms, memberships, messages).")
    n.h3("Webex Devices")
    n.bullets([
        "Types: **Webex Board Series** (all-in-one team collaboration for meeting rooms), **Room Series** (integrated video conferencing for every room), **Desk Series** (high-quality video at your desk), and **Cisco Touch 10** (touchscreen for interacting with conferencing systems).",
        "Customized through the **xAPI**, which enables two-way communication with third-party apps and control systems. Access xAPI over **Telnet/SSH, HTTP, or RS-232 serial**. It supports **XML and JSON**, and **JavaScript macros** for on-device customization.",
        "**UI Extensions** are custom widgets, buttons, and virtual controllers (previously called **In-Room Controls**, now a subset of UI Extensions, built in the **UI Extensions Editor**). They add custom elements to the **Touch 10** display; the editor's simulator loads a virtual meeting room.",
        "From **version 9.2** of the Collaboration Endpoint software you can brand room devices. In the **Halfwake** state: add a **background image**, a **small logo in the bottom right corner**, and customize or remove the welcome message. In the **Awake** state: add a small logo at the bottom right, and a label or message at the bottom left (screen only).",
    ])

    n.h2("8.7 Cisco Security Platforms")
    n.p("Scripts can ingest data **faster than a human**, so automation helps identify threats and mitigate risk. The "
        "API-manageable portfolio on the slide: **AMP for Endpoints, Firepower Management Center (FMC), Firepower Threat "
        "Defense (FTD), Identity Services Engine (ISE), Threat Grid, Umbrella.**")
    n.table(
        ["Product", "Key Facts"],
        [
            ["**AMP for Endpoints**", "API access to automate security workflows; **sandboxing** to inspect suspicious files safely and in isolation. Subscription-based products with a **central web console**; deploy on phones, email, and web servers. Integrates with **Umbrella** and **Meraki MX**. Three capabilities: **Prevention** (stop known threats), **Detection** (continuously monitor and record file activity), **Response and automation** (speed investigations, auto-remediate on PCs, Macs, Linux, servers, Android, iOS)."],
            ["**Firepower: FMC and FTD**", "**FMC** is the central management console to configure **all aspects of FTD**, including access control rules and policy objects. The **FMC API and FTD APIs cannot co-exist**: choose either **FDM/FTD-API/CDO** or **FMC**. FMC runs on **VMware vSphere or AWS** and on physical FMC models. FTD with **Firepower Device Manager (FDM)** manages CA certificates, private keys, **IKE** key management, and **ACLs (extended and standard)**. FDM and FMC integrate with **ISE** (move users in or out of **quarantine** after a VPN session starts). **FMC API authentication:** an **access token** valid for **30 minutes** (then refresh), sent in the header **`X-auth-access-token: <token>`**."],
            ["**ISE (Identity Services Engine)**", "A **rule-based engine** for **policy-based network access** to users and devices. Node types: **Administration, Policy Service, Monitoring, pxGrid**. Integrates with RBAC, **Okta/SAML SSO, LDAP, Active Directory**. Capabilities: **asset visibility, policy compliance, secure wired access, segmentation**."],
            ["**Threat Grid**", "A **malware analysis platform** combining **static** and **dynamic** analysis with global threat intelligence. For SOC analysts, malware analysts, and forensic investigators. **Static** = identifying info about the file, headers, contents. **Dynamic** = runs the malware in a safe virtual environment called a **\"glovebox\"**. Content subscription: **500 to 10,000 samples per day**. Integrates with AMP, next-generation firewalls, and **Cisco ASA with FirePOWER Services**."],
            ["**Umbrella**", "Uses **DNS** to enforce security; blocks malicious **domains, URLs, IPs, and files**. APIs: **Enforcement, Network Devices, Investigate, Reporting**. Enforcement API acts on a domain request; **Investigate API** pulls threat intelligence. Integrates with **Meraki MR** for wireless protection. Capabilities: Wi-Fi protection for guests, selected application blocking, endpoint security off-network (not on VPN), **web filtering**."],
        ],
        [1.6, 4.9],
    )
    n.memory("AMP = **A**ntivirus-ish for endpoints (Prevent, Detect, Respond). FMC = the **M**anager of FTD. ISE = **I**dentity gate. Threat Grid = the **glovebox** lab. Umbrella = **DNS** shield.")
    n.watch("\"FMC and FTD APIs cannot directly co-exist\" means you pick one management path: FDM/FTD-API/CDO **or** FMC.")

    n.h2("Packet Tracer Activities Closing Module 8")
    n.bullets([
        "**Compare Using CLI and an SDN Controller to Manage a Network:** Explore the topology; use the CLI to gather information; configure an SDN controller; use it to **discover a topology**; use it to gather information; use it to **configure network settings**.",
        "**Implement REST APIs with an SDN Controller:** Launch the DEVASC VM; verify external connectivity to Packet Tracer; **request an authentication token with Postman**; send REST requests with Postman; send REST requests with VS Code; send REST requests inside Packet Tracer.",
    ])
    n.p("What the two labs showed: PT-Controller0 listens on **port 58000** (the controller's HTTP port); a **POST to `/api/v1/ticket`** "
        "with a username and password returns a **serviceTicket**; later GET calls send it in the **`X-Auth-Token`** header; "
        "`/api/v1/network-device` returns the network devices and `/api/v1/host` the hosts. In the controller GUI, discovery uses **CDP** "
        "with CLI credentials and the Network Settings policy can **push DNS, NTP, and Syslog** to devices.")
    n.pagebreak()

    n.h2("Module 8 Cram Sheet")
    n.table(
        ["Topic", "Remember"],
        [
            ["Dev Centers", "Cloud, Collaboration, Data center, IoT and edge, Networking, Security, Wireless and mobile, Application developers"],
            ["SDK", "Tools for developing apps for a specific device or system; helps with pagination and rate limiting"],
            ["YANG node types", "Leaf, leaf-list, container, list"],
            ["NETCONF", "XML, nine operations, running/candidate/startup, locks, transactions"],
            ["RESTCONF", "RFC 8040, HTTP, only running datastore, no locks, POST/GET/PUT/DELETE"],
            ["IOS XE commands", "`netconf-yang`, `restconf`, `ip http secure-server` (port 443); NETCONF/YANG from 16.3.1"],
            ["YANG models repo", "github.com/YangModels/yang, `vendor/cisco`"],
            ["DNA Center", "Design, Policy, Provision, Assurance, Platform; admin = SUPER-ADMIN-ROLE; Intent API; async POST/PUT with executionId"],
            ["ACI", "Nexus 9000, APIC cluster, MO/DN/RN, `/api/{mo|class}/{dn}.json|xml`, Cobra, API Inspector"],
            ["Cobra order", "Session, login, config object, request, add, commit"],
            ["Meraki", "Cloud-managed; Dashboard API (REST, HTTPS, JSON); enable under Organization > Settings; key from My Profile"],
            ["NX-OS", "Open NX-OS on Linux; LXC and CentOS 7 Guest Shell; NX-API REST; NETCONF and RESTCONF from 9.2.1"],
            ["NSO", "3 components; Device Manager and Service Manager; CDB; 3 YANG sources; service = model + mapping"],
            ["SD-WAN", "vManage, vSmart, vBond, vEdge"],
            ["UCS", "Manager (VIP on primary FI), Service Profile = one server at a time, B-Series blades, C-Series rack, FIs, MIT root `sys`"],
            ["UCS XML API", "aaaLogin/aaaRefresh/aaaLogout; configResolve... query; configConf... change"],
            ["UCS Director", "1000+ tasks; header `X-Cloupia-Request-Key`; API v2 is XML and POST only"],
            ["Intersight", "SaaS; JSON over HTTPS/TLS; API keys; OpenAPI spec"],
            ["AXL vs UDS", "AXL = SOAP admin; UDS = REST end users"],
            ["Finesse", "Agent/supervisor desktop; REST + JavaScript; CTI; GET synchronous, others asynchronous"],
            ["Webex Teams API", "Organizations, Teams, People, Rooms, Memberships, Team Memberships, Messages"],
            ["Webex devices", "Board, Room, Desk, Touch 10; xAPI over SSH/HTTP/RS-232; UI Extensions; macros"],
            ["Security", "AMP (prevent, detect, respond); FMC manages FTD; ISE nodes (Admin, Policy Service, Monitoring, pxGrid); Threat Grid glovebox; Umbrella DNS with 4 APIs"],
            ["FMC token", "30 minutes; `X-auth-access-token`"],
        ],
        [2.0, 4.5],
    )

    n.pagebreak()
    n.h1("Question Bank Extras")
    n.p("The same question bank, boiled down to the facts it asks, grouped by what the question is about. Use this "
        "part to review after you have read the literal items.")
    n.h2("Module 7 Extras")
    n.table(
        ["Question Style", "Answer"],
        [
            ["Most common cause of IT outages", "An engineer **misconfiguring** a device or network with **manual changes** (human error)"],
            ["Average outage cost for the largest enterprises", "**$300,000 per hour** (the source quotes Gartner: over $5,600 per minute)"],
            ["Developers vs operations, historically", "Developers **create** applications; operations **verify they work** for users and the business"],
            ["What is an unopinionated component", "One that does **not show extra preference for specific companion components or architectures** unless they are necessary"],
            ["Platform abstraction (containers)", "A **containerized app can run on a generically specified host environment**"],
            ["Two cloud challenges", "**Maintaining access control** and **managing costs**"],
            ["How is an error budget calculated", "The difference between the **SLO and 100 percent availability**"],
            ["What is an error budget for", "Measures **allowable errors**, a **gate on release speed**"],
            ["Purpose of an SLI", "A **benchmark metric** used to determine and describe **SLOs**"],
            ["How does DevOps treat failure", "**Failure is normal**; chaos engineering: minimize the **blast radius**, **self-heal**, monitor events"],
            ["Default shell on macOS and Linux", "**Bash**"],
            ["Automation type dangerous when the starting state is not fully known", "**Procedural** (imperative scripting)"],
            ["What is an imperative procedure", "An **ordered sequence of commands** used to reach a specific end state"],
            ["Declarative static model", "**Examines present circumstances and brings real infrastructure into alignment** with the desired state"],
            ["Idempotency is the quality of what", "**Software** (the quality of software)"],
            ["Ansible file with tasks in top-down order", "**.yml** (YAML)"],
            ["Ansible file that describes the managed devices", "The **inventory file**"],
            ["Ansible ping fails (two causes)", "The **destination host IP address is wrong** or the **SSH service did not start** on the host"],
            ["Playbook command to see interface names, IPs, and status on a Cisco router", "**show ip interface brief**"],
            ["Language Chef uses for recipes", "**Ruby**"],
            ["pyATS component that bundles and runs jobs", "**Easypy**"],
            ["Command to compare a new .virl backup with the old one", "**diff** (detects configuration drift)"],
            ["Tech that runs on bare metal or large VMs to simulate Cisco networks", "**VIRL**"],
            ["Canary deployment", "The **switchover of selected users** to a new release"],
            ["Create a Python virtual environment", "**python3 -m venv /path/to/new/virtual/environment** (for example `python3 -m venv devenv` creates a Python 3 venv named devenv)"],
            ["Cannot reach https://192.168.56.101 for the CSR1000v", "Run **show ip interface brief** in the CSR1000v VM to check its IP address"],
        ],
        [2.6, 3.9],
    )
    n.memory("Error budget = **100% minus the SLO**. SLO = the target, SLI = the number you measure, budget = the room left to fail.")
    n.h2("Module 8 Extras")
    n.table(
        ["Question Style", "Answer"],
        [
            ["Technology that lets Umbrella block a site", "**DNS**"],
            ["Language NETCONF uses for data and messages", "**XML**"],
            ["Default TCP port for NETCONF over SSH", "**830**"],
            ["Two RESTCONF media types for YANG constructs", "**application/yang-data+xml** and **application/yang-data+json**"],
            ["Data format that describes a list of interfaces in the exhibit", "**YANG**"],
            ["A characteristic of YANG", "It uses a **tree structure**"],
            ["Two types of YANG models", "**Native** and **open**"],
            ["Three primary NSO YANG sources", "**Data models from devices**, the **NSO data model**, and **YANG service models**"],
            ["Three main capabilities of AMP", "**Detection, responses and automation, prevention**"],
            ["AMP API rate limit header X-Rate-Limit-Limit", "The number of total allowed **requests** in the current period"],
            ["What Finesse REST APIs do (three)", "**Integrate** contact center functions into existing apps, **build a fully functioning agent desktop**, **build scripts to automate tasks**"],
            ["What Finesse JavaScript APIs do (two)", "**Embed existing web pages into a custom gadget** and **build a custom gadget** for the agent state workflow"],
            ["Cisco Finesse is", "A **browser-based contact center agent and supervisor desktop**"],
            ["Two benefits of the Webex Teams Python SDK", "**Error reporting** and **pagination** handling (also simpler authentication and file attachments)"],
            ["Default maximum items the Webex Teams API returns before pagination", "**100**"],
            ["Why Meraki returns 404 instead of 403 for a bad API key", "So the system does **not reveal that resources exist** to unauthorized users"],
            ["What ISE does when it identifies a user or device", "**Automatically and securely places** the device and user into the **right part of the network**"],
            ["UCS service profiles", "Assign a **unique identity** to the server associated with each profile"],
            ["AXL function for users", "**Provisions and manages objects** in the Unified Communication management administration (configuration database)"],
            ["Two UCS Director tasks", "**Deploy and add capacity to converged infrastructure** repeatably; **create, clone, and deploy service profiles and templates**"],
            ["Two Firepower traffic control actions", "Use **security intelligence data** (IPs, address blocks, domains, URLs) to filter traffic; **control which websites** users can reach"],
            ["SD-WAN dashboard name", "**vManage**"],
            ["SaaS platform offering API keys for remote or service access", "**Cisco Intersight**"],
            ["SDK that is a call widget embedded in an iframe on a web page", "**Jabber Guest SDK for Web**"],
            ["Where to open the FTD API Explorer", "At the **URL address of the device itself**"],
            ["SDK the APIC uses", "**Cobra SDK**"],
        ],
        [2.6, 3.9],
    )
    n.h2("Platform One-Liners")
    n.table(
        ["Platform", "One Line"],
        [
            ["**Cisco IOS**", "Network infrastructure OS with different specialty flavors"],
            ["**Cisco IOS XR**", "Focuses on **service provider** use cases"],
            ["**Cisco IOS XE**", "**Separates the data plane and control plane**; next-generation programmable platform"],
            ["**Cisco NX-OS**", "Works across **physical and virtual data center** deployments"],
            ["**Edge computing**", "Computing capability as **close to the actual data** as possible"],
            ["**Data model (networking)**", "A programmatic, standards-based way of writing configurations for any network device"],
            ["**Jabber Web SDK**", "For web applications on Cisco Unified Communications (voice, video, IM, presence)"],
            ["**DNA Center Multivendor SDK**", "Adds support for a **mix of Cisco and non-Cisco** devices"],
            ["**UCS Python SDK**", "Python module that automates all aspects of **UCS management**"],
            ["**IMC Python SDK**", "Automates **Cisco IMC** management servers (C-Series and E-Series)"],
            ["**Webex Teams Python SDK**", "Uses the **webexteamssdk** package; token set with the **WEBEX_TEAMS_ACCESS_TOKEN** environment variable or passed directly"],
        ],
        [2.0, 4.5],
    )
