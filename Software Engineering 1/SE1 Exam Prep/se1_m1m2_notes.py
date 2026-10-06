import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = HERE.parent

sys.path.insert(0, str(ROOT / "Network and Communications 2" / "DEVASC M3-M4 Exam Prep"))
from notes_lib import Notes


def m1(n):
    n.h1("Part 1: Module 1, Software Engineering")

    n.h2("Chapter 1: Software And Software Engineering")

    n.h3("What Is A Software?")
    n.bullets([
        "It is a set of instructions or codes or computer program that when executed provides desired features, "
        "function and performance.",
        "They are data structures that enable the programs to adequately manipulate information (such as "
        "databases).",
        "It is a collection of computer programs, procedures and documentation that perform tasks on a computer "
        "system.",
    ])

    n.h3("The Five Software Questions")
    n.p("Listed on the overview slide as **Software Guidelines**:")
    n.numbered([
        "Why does it take long to finish a software?",
        "Why are development costs so high?",
        "Why can't we find all errors prior to release?",
        "Why spend much time and effort to maintain an existing software?",
        "Why do difficulties continue in measuring progress as software is developed and maintained?",
    ])
    n.memory("**Tired Cats Eat Messy Meals** = Time, Cost, Errors, Maintenance, Measuring progress.\n"
             "All five questions are complaints about software: it is slow, costly, buggy, hard to maintain, and "
             "hard to measure.")

    n.h3("The Seven Software Categories")
    n.table(
        ["Category", "Definition"],
        [
            ["**System Software**", "A collection of programs written to service other programs."],
            ["**Application Software**", "Usually stand-alone programs that solve specific business needs."],
            ["**Engineering/Scientific Software**", "A broad array of \"number crunching\" programs."],
            ["**Embedded Software**", "Resides within a product or system, used to implement control features "
             "for the user and the system itself."],
            ["**Product-line Software**", "Designed to provide specific capabilities for use by many customers."],
            ["**Web/Mobile Application**", "Network-centric applications that encompass browser-based apps "
             "and/or mobile apps."],
            ["**Artificial Intelligence Software**", "Makes use of non-numerical algorithms to solve complex "
             "problems not amenable to computation or forward analysis."],
        ],
        [2.3, 4.2],
    )
    n.memory("**Sam Always Eats Eggs, Pizza, Waffles, Apples** = System, Application, Engineering/Scientific, "
             "Embedded, Product-line, Web/Mobile, AI.")

    n.h3("Legacy Software")
    n.bullets([
        "These are older programs that were developed decades ago.",
        "They are continually modified today to meet changes in business requirements and computing platforms.",
        "They can be costly to maintain and risky to evolve.",
    ])

    n.h3("\"Infants\" Software")
    n.table(
        ["Type", "Definition"],
        [
            ["**WebApps**", "Sophisticated computing tools that not only provide stand-alone function to users, "
             "but can also integrate databases and corporate applications."],
            ["**Mobile Applications**", "Encompasses a user interface that takes advantage of the unique "
             "interaction mechanisms provided by the mobile platform."],
            ["**Cloud Computing**", "Encompasses an infrastructure or \"ecosystem\" that enables any user from "
             "anywhere or anytime to use a computing device to share or use computing resources on a broad scale."],
            ["**Product Line Software**", "A set of software-intensive systems that share a common, managed set "
             "of features satisfying the specific needs of a particular market segment."],
        ],
        [2.0, 4.5],
    )
    n.memory("**We Make Cool Products** = WebApps, Mobile apps, Cloud computing, Product line software.\n"
             "These are called \"infants\" because they are the newer software categories, next to legacy software.")

    n.h3("Software Realities")
    n.bullets([
        "Software has become deeply embedded in virtually every aspect of our lives.",
        "The IT requirements demanded by individuals or businesses grow in an increasingly complex terms.",
        "Individuals, businesses and even governments increasingly rely on software for processes and "
        "decision making.",
        "The perceived values of specific software application grows as its user base grows.",
    ])
    n.memory("**Every Computer Relies on Value** = Embedded everywhere, Complexity grows, Relies on it for "
             "decisions, Value grows with user base.")

    n.h3("Software Engineering")
    n.p("**Engineering** is a discipline or profession of acquiring and applying technical, scientific or "
        "mathematical knowledge to design and implement structures, systems and processes to realize a desired "
        "objective. **Software Engineering** is a process or collection of methods and an array of tools that "
        "allow professionals to build high quality computer software.")
    n.p("It is a systematic, disciplined and quantifiable approach to development, operation and maintenance of "
        "software. Adaptability and agility are both required. The slide text says Software Engineering **is a "
        "layered technology and its foundation is the process layer**. It is a glue that holds the technology "
        "layers together and enables rational and timely development of computer software.")

    n.h3("The Four Software Engineering Layers")
    n.p("The diagram, top to bottom: **Tools, Methods, Process, Quality Focus.**")
    n.memory("**Toddlers Make Pretty Quilts** = top to bottom, Tools, Methods, Process, Quality Focus.\n"
             "Quality Focus sits at the very bottom of the stack, so it is the **bedrock** everything else rests on.")
    n.watch("The slide **text** (p12) says Software Engineering's **foundation is the process layer**. But the "
            "**diagram** (p13) stacks Quality Focus at the very bottom, under Process. If a question asks which "
            "layer is the **bedrock**, the diagram answer is **Quality Focus**; if it asks which layer is called "
            "the **foundation** in the slide text, the answer is **Process**. Both appear on the slides, so read "
            "the question's wording carefully.")

    n.h3("The Software Process")
    n.table(
        ["Term", "Definition"],
        [
            ["**Process**", "A collection of activities, actions and tasks that are performed when some work "
             "product is to be created."],
            ["**Activity**", "Strives to achieve a broad objective."],
            ["**Action**", "A set of tasks that produce a major work product."],
            ["**Task**", "Focuses on small, but well defined objectives to produce a tangible outcome."],
        ],
        [1.5, 5.0],
    )
    n.memory("**Please Arrange Action Tasks** = Process, Activity, Action, Task, biggest to smallest.")

    n.h3("The Process Framework (Five Framework Activities)")
    n.table(
        ["Activity", "What It Means"],
        [
            ["**Communication**", "Communicate and collaborate with the user to understand objectives."],
            ["**Planning**", "Mapping the software project to create guidelines."],
            ["**Modeling**", "A \"sketch\" of the project in order to understand the big picture. In other "
             "words, blueprints or software requirements design."],
            ["**Construction**", "Building of the software project."],
            ["**Deployment**", "Software is delivered to the customer who evaluates and provides feedback."],
        ],
        [1.8, 4.7],
    )
    n.memory("**Chatty People Make Cool Deliveries** = Communication, Planning, Modeling, Construction, "
             "Deployment.")

    n.h3("Software Engineering Practice (Four Practice Steps)")
    n.table(
        ["Step", "What It Involves"],
        [
            ["**Understand the Problem**", "Communication and Analysis (Research)."],
            ["**Plan a Solution**", "Modeling and Software Design (Designing)."],
            ["**Carry out the Plan**", "Code generation (Programming)."],
            ["**Examine the result for accuracy**", "Testing and Quality Assurance (Deliberate)."],
        ],
        [2.5, 4.0],
    )
    n.memory("**Understand, Plan, Carry, Examine.** This is the same shape as the scientific method: research, "
             "design, build, test.")

    n.h3("The Seven Software Engineering Principles")
    n.table(
        ["Principle", "What It Means"],
        [
            ["**The Reason it all Exists**", "Provide value to its users."],
            ["**KISS (Keep It Simple, STUPID!)**", "All design should be as simple as possible, but no simpler."],
            ["**Maintain the Vision**", "It is essential for the success of the software project."],
            ["**What you produce, others Consume**", "Always specify, design and implement knowing someone else "
             "will have to understand what you do."],
            ["**Be open to the Future**", "Never design yourself in the corner."],
            ["**Plan Ahead for Reuse**", "Reduces the cost and increases value of both reusable components and "
             "the system where it is incorporated."],
            ["**Think!**", "Practice a complete and clear thought before taking action for better results."],
        ],
        [2.6, 3.9],
    )
    n.memory("**Real Kids Make Pretty Open Plans, Think!** = Reason it Exists, KISS, Maintain vision, Produce for "
             "others to Consume, Open to the future, Plan ahead for reuse, Think.")

    n.pagebreak()
    n.h2("Chapter 2: Systems And Information Systems")

    n.h3("Systems")
    n.bullets([
        "It is a set of processes or integrated parts with entities each performing specific functions.",
        "It is a set of interacting or interdependent entities, real or abstract, forming an integrated whole.",
        "The concept of an \"integrated whole\" can also be stated in terms of a system embodying a set of "
        "relationships which are differentiated from relationships of the set to other elements, and from "
        "relationships between an element of the set and elements not a part of the relational regime.",
    ])

    n.h3("System Types: Open Vs Closed")
    n.table(
        ["Type", "Definition"],
        [
            ["**Open Systems**", "Also called probabilistic systems. Outputs or results can't be determined "
             "precisely but can only be guessed. One can't predict such occurrences until the actual event "
             "arrives."],
            ["**Closed Systems**", "Can be predicted with certainty. The measurement of the given input will "
             "actually let the output be predictable as it appears to be."],
        ],
        [1.7, 4.8],
    )
    n.watch("**Open systems = probabilistic**, their output can only be guessed, not calculated exactly. "
            "**Closed systems** are the predictable ones. It is easy to mix these up because \"open\" sounds "
            "like it should be more knowable.")

    n.h3("Information System")
    n.bullets([
        "It is a set of interrelated components that collect, store, process and help analyze, support "
        "decision-making and perform control functions in an organization.",
        "It handles the flow and maintenance of information that supports a business or some other operation.",
        "It is the system of people, data records and activities that process the data and information in a "
        "given organization, including manual processes or automated processes.",
    ])

    n.h3("The IS Activities")
    n.p("Diagram: **Input -> Process -> Output**, with a **Feedback** loop back to Input.")
    n.table(
        ["Activity", "What It Means"],
        [
            ["**Input**", "Starts off with acquisition of raw data and is then introduced to the system."],
            ["**Process**", "Involves data processing, classifying, and arranging, calculating data."],
            ["**Output**", "The processed data becomes information."],
            ["**Feedback**", "The evaluation."],
        ],
        [1.6, 4.9],
    )
    n.memory("**I Produce Output, Feedback** = Input, Process, Output, Feedback, in that loop order.")

    n.h3("IS Resource Approach")
    n.p("Diagram: **DATA** in the middle, surrounded by **Create** (data going in), **Destroy** (data going "
        "out), **Process**, **Retrieve**, and **Update**.")
    n.memory("This is the classic **CRUD** idea (Create, Retrieve, Update, Destroy) plus **Process** in the "
            "center of the data lifecycle.")

    n.h3("Information Management")
    n.bullets([
        "The system is managing information in its own way.",
        "Focusing on information, any kind of data presented in a form which is understandable or meaningful "
        "and helps make decisions.",
        "Today, Information Technology Enabled Services (ITES) consider information as a \"utility\", just "
        "like electricity or telephone, and the key factor is business strategy.",
    ])

    n.h3("Six Good Information Characteristics")
    n.bullets([
        "Accuracy",
        "Timeliness",
        "Less Uncertainty",
        "An element of surprise value",
        "Should aid in decision-making",
        "Should update knowledge",
    ])
    n.memory("**Any Timely Lead Adds Decisions, Updates** = Accuracy, Timeliness, Less uncertainty, Element of "
             "surprise, Aid decision-making, Update knowledge.")

    n.h3("IS Business Perspective")
    n.p("Diagram: a circle with **Information System** in the centre, surrounded by **Organizational structure "
        "and system, Environmental Factors, Management Policy, and Technology Development**.")
    n.memory("**Our Era Means Tech** = Organizational structure, Environmental factors, Management policy, "
             "Technology development, all circling the IS.")

    n.h3("IS Key Components")
    n.p("Diagram: **DATA, PEOPLE, TECHNOLOGY, EQUIPMENT, PROGRAMS, PROCEDURES.**")
    n.memory("**Data People Trust Equipment, Programs, Procedures** = Data, People, Technology, Equipment, "
             "Programs, Procedures.")

    n.h3("IS Major Components")
    n.table(
        ["Component", "Definition"],
        [
            ["**Data**", "Consists of raw facts and is an important component of an IS. It has two sources: "
             "external and internal."],
            ["**Database**", "Is a collection of all relevant and related organized data in an integrated file."],
            ["**Process**", "An important component of IS that generates the most useful information for "
             "decision-making."],
            ["**Information**", "Consists of analyzed facts that was processed from a data source and is an "
             "output of an IS."],
        ],
        [1.6, 4.9],
    )
    n.memory("**Data Drives Processed Information** = Data, Database, Process, Information.")

    n.h3("The Seven Types Of Information Systems")
    n.table(
        ["Type", "Who Uses It / Purpose", "Example"],
        [
            ["**Transaction Processing System (TPS)**", "Used primarily for record keeping required in any "
             "organization to conduct business. Used for periodic report generation in a scheduled manner, and "
             "for reports on demand as well as exception reports.", "Sales order entry, payroll, shipping "
             "records."],
            ["**Decision Support System (DSS)**", "Serves the management of an organization with sophisticated "
             "data analysis tools that support and assist all aspects of problem-specific decision-making. Used "
             "when the problem is complex and information is difficult to obtain and use.", "Developed with "
             "decision-makers; may use external data such as current stock prices."],
            ["**Executive Information System (EIS)**", "Used by senior managers, so it must be easy to use "
             "without assistance. Can do trend analysis, exception reporting, and drill-down. Has online "
             "analysis tools accessing a broad range of internal and external data.", "Results shown in "
             "graphical form tailored to the executive's needs."],
            ["**Management Information System (MIS)**", "Provides management routine summary of basic "
             "operations; consolidates data on sales, production, etc. Provides routine information to managers "
             "and decision makers to increase operational efficiency.", "May support marketing, production, "
             "finance."],
            ["**Workflow System**", "A rule-based management system that directs, coordinates and monitors the "
             "execution of an interrelated set of tasks arranged to form a business process. May be Internet-"
             "based, combined with e-mail, or based on server architecture using a database or file server.", "See "
             "the three workflow types below."],
            ["**Enterprise Resource Planning (ERP)**", "A business process management software that allows an "
             "organization to use a system of integrated programs capable of managing a company's vital business "
             "operations.", "For an entire multi-site, global organization."],
            ["**Expert Systems**", "Has the ability to make suggestions and act like an expert in a particular "
             "field of an organization.", "Has an extensive knowledge base."],
        ],
        [1.9, 3.4, 1.8],
    )
    n.memory("Group the seven by job: **record-keepers** (TPS), **decision helpers** (DSS, EIS, MIS), "
             "**coordinators** (Workflow), and **integrators** (ERP, Expert Systems).")
    n.watch("**DSS helps decide, but does not make the decision itself.** It is developed with the decision-"
            "makers and assists the decision-making process only.")
    n.watch("**EIS is also called the Executive Support System.** If a question gives that name instead of the "
            "acronym, it is still the EIS.")

    n.h3("Three Types Of Workflow Systems")
    n.bullets([
        "**Administrative Workflow Systems** - focus on the tracking of expense reports, travel requests, "
        "messages.",
        "**Ad-hoc Workflow System** - deals with the shaping of product, sales proposals and strategic plans.",
        "**Production Workflow Systems** - are concerned with mortgage loans and insurance claims.",
    ])

    n.pagebreak()
    n.h2("Chapter 3: System Development Life Cycle (SDLC)")

    n.h3("What Is SDLC?")
    n.bullets([
        "Also referred to as the application development life-cycle, is a process for planning, creating, "
        "testing, and deploying an information system.",
        "The systems development life cycle concept applies to a range of hardware and software "
        "configurations, as a system can be composed of hardware only, software only, or a combination of "
        "both.",
        "SDLC is used during the development of an IT project and describes the different stages involved in "
        "the project from the drawing board, through the completion of the project.",
        "SDLC describes the stages involved in an information system development project, from an initial "
        "feasibility study through maintenance of the completed application. It can apply to technical and "
        "non-technical systems involving hardware and software.",
        "In SDLC, documentation is crucial, regardless of the type of model chosen for any application, and is "
        "usually done in parallel with the development process.",
    ])

    n.h3("The Seven SDLC Phases")
    n.p("Cycle on the slide: **Planning -> Analysis -> Design -> Development -> Testing -> Implementation -> "
        "Maintenance -> back to Planning.**")
    n.table(
        ["Phase", "What Happens", "Key Detail"],
        [
            ["1. **Planning**", "Identifies whether or not there is a need for a new system. A preliminary plan "
             "(feasibility study) for a company's business initiative to acquire resources to build, modify or "
             "improve a service.", "Finds the scope of the problem and determines solutions considering "
             "resources, costs, time, benefits."],
            ["2. **System Analysis**", "The business works on the source of the problem or the need for change. "
             "Possible solutions are submitted and analyzed to identify the best fit for the project's goals. "
             "Teams consider the functional requirements of the project.", "Tools: **CASE** (Computer Aided "
             "Systems/Software Engineering), requirements gathering, structured analysis."],
            ["3. **System Design**", "Describes in detail the necessary specifications, features and operations "
             "that will satisfy the functional requirements of the proposed system. End users discuss and "
             "determine their specific business information needs.", "Considers essential components (hardware "
             "and/or software), networking capabilities, processing, and procedures."],
            ["4. **System Development**", "The real work begins: a programmer, network engineer and/or database "
             "developer are brought on to do the major work on the project.", "Uses a flow chart to organize the "
             "process; signifies the start of production; training can be a big benefit here."],
            ["5. **System Testing**", "Systems integration and system testing of programs and procedures, "
             "normally carried out by a QA professional to determine if the design meets the initial goals.", "May "
             "be repeated to check for errors, bugs and interoperability; includes verification and validation."],
            ["6. **System Implementation**", "The slide says this is when the majority of the code for the "
             "program is written. Also involves the actual installation of the newly developed system, moving "
             "data and components from the old system via a **direct cutover**.", "Cutover typically happens "
             "during off-peak hours to minimize risk."],
            ["7. **System Maintenance**", "Involves maintenance, regular operations and required updates.", "End "
             "users can fine-tune the system; new updates usually require looking back at the first phase, "
             "beginning the cycle again."],
        ],
        [1.4, 3.3, 2.4],
    )
    n.memory("**Please Always Design Decent, Test, Implement, Maintain** = Planning, Analysis, Design, "
             "Development, Testing, Implementation, Maintenance.")
    n.watch("The slide for **phase 6, System Implementation** (p12) says \"the majority of the code for the "
            "program is written\" here, and also describes installing the system via a **direct cutover during "
            "off-peak hours**. This looks like it contradicts **phase 4, System Development** (p10), which is "
            "described as where \"the real work begins\" writing code. Quote the slide as written: writing most "
            "of the code is mentioned under **Implementation**, even though development work also happens "
            "earlier in **System Development**.")

    n.h3("System Development Life Cycle Vs Software Development Life Cycle")
    n.table(
        ["System Development Life Cycle", "Software Development Life Cycle"],
        [
            ["Involves end-to-end People, process, Software/Technology deployment. This includes Change "
             "Management, training, Organizational updates.", "Only looks at software components development "
             "planning, technical architecture, software quality testing and deployment of working software."],
            ["It is a much broader term which is a superset to the above and is a larger part of the "
             "development phase which includes many other approaches and end phases.", "The meaning of the "
             "process gets limited to a certain boundary beyond which it ceases to provide relevance."],
            ["It is about implementing hardware and software in a phased manner systematically. Here both the "
             "hardware and the software are considered as a system.", "It is about building a software "
             "(\"only\") in a phased approach systematically. Hence, it's just part of the other SDLC, in "
             "particular during the Development Phase."],
        ],
        [3.25, 3.25],
    )
    n.watch("**System SDLC is the superset.** It covers people, process, and technology end to end (hardware "
            "AND software, as a system). **Software SDLC is the narrower one**: it is only part of the "
            "Development Phase of the System SDLC, and only covers building the software itself.")


def m2(n):
    n.h1("Part 2: Module 2, Project Management")

    n.h2("Chapter 1: Project Management")

    n.h3("What Is A Project?")
    n.p("A project is a **temporary endeavor** designed to produce a unique product or service with a defined "
        "beginning and end (usually time-constrained, and often constrained by funding or staffing) undertaken "
        "to meet unique goals and objectives, to bring about beneficial change or added value. It is an "
        "activity to meet the creation of a unique product or service, and thus activities that are undertaken "
        "to accomplish **routine activities cannot be considered projects**.")

    n.h3("Project Application")
    n.bullets([
        "Schools and Universities",
        "Civil and Industry (Private)",
        "Military and State (Government)",
        "Computer Software (IT-based)",
    ])
    n.memory("**Schools, Construction, Military, Computers** = Schools/Universities, Civil/Industry (Private), "
             "Military/State (Government), Computer Software (IT-based).")

    n.h3("Project Management")
    n.p("Project management is the **practice** of initiating, planning, executing, controlling, and closing "
        "the work of a team to achieve specific goals and meet specific success criteria at the specified time. "
        "The primary challenge is to achieve all of the project goals within the given constraints. This is "
        "usually described in **project documentation**, created at the beginning of the development process.")

    n.h3("Project Manager")
    n.p("A professional in the field of project management, in-charge of people and responsibilities such as "
        "planning, execution, controlling, and closing of any project. A project manager needs to understand the "
        "order of execution of a project to schedule it correctly, as well as the time necessary to accomplish "
        "each individual task. They are the people **accountable for accomplishing the stated project "
        "objectives**.")
    n.p("Quote from the slide: **\"Project Management is not a tool or a person, it's a practice.\"**")

    n.h3("Origins Of Project Management")
    n.p("As a discipline, project management developed from several fields of application including civil "
        "construction, engineering, and heavy defense activity.")
    n.table(
        ["Forefather / Era", "Contribution"],
        [
            ["**Henry Gantt**", "Called the **father of planning and control techniques**, famous for his use "
             "of the **Gantt Chart**."],
            ["**Henri Fayol**", "Creator of the **five management functions** that form the foundation of the "
             "body of knowledge associated with project and program management."],
            ["**The 1950s**", "Marked the beginning of the modern project management era, where core "
             "engineering fields came together to work as one. Project management became recognized as a "
             "distinct discipline arising from the management discipline with engineering mode."],
            ["**CPM and PERT**", "Two mathematical project-scheduling models developed in that era: the "
             "**Critical Path Method (CPM)** and the **Program/Project Evaluation and Review Technique (PERT).**"],
        ],
        [1.6, 4.9],
    )
    n.watch("**Gantt = father of planning (and control techniques), remembered for the Gantt Chart. Fayol = the "
            "five management functions.** They are the two separate forefathers; do not swap their "
            "contributions.")

    n.h3("Gantt Chart Vs PERT Chart")
    n.table(
        ["", "Gantt Chart", "PERT Chart"],
        [
            ["What it is", "A chart created using Microsoft Project.", "A project management tool used to "
             "schedule, organize, and coordinate tasks within a project."],
            ["What it shows", "Red marks indicate the **critical path**, or the longest stretch of the "
             "project. Columns: ID, Task Name, Predecessors, Duration.", "A network diagram of tasks and their "
             "dependencies, used to analyze the tasks involved in completing a project."],
            ["Main purpose", "Visualize schedule and the critical path.", "Identify the **minimum time needed** "
             "to complete the total project, especially the time needed to complete each task."],
        ],
        [1.4, 2.9, 2.2],
    )

    n.h3("The PERT Example From The Slide")
    n.p("Nodes: **10, 20, 30, 40, 50.** Activities:")
    n.bullets([
        "A: 10 -> 30, t = 3 months",
        "B: 10 -> 20, t = 4 months",
        "C: 20 -> 50, t = 3 months",
        "D: 30 -> 40, t = 1 month",
        "E: 30 -> 50, t = 3 months",
        "F: 40 -> 50, t = 3 months",
    ])
    n.p("The longest path is **10-30-40-50 = 7 months**, which ties with **10-20-50 = 7 months**. Both paths "
        "take 7 months, so either can be the critical path in this example.")

    n.h3("Project Management Application")
    n.p("Project management methods can be applied to any project. It is often customized to a specific type of "
        "project based on size, nature and industry. For example, the construction industry, which focuses on "
        "the delivery of things like buildings, roads, and bridges, has developed its own specialized form of "
        "project management that it refers to as **construction project management**, in which project "
        "managers can become trained and/or certified.")

    n.h3("The Four P's Approach")
    n.table(
        ["P", "Meaning"],
        [
            ["**Plan**", "The planning and forecasting activities."],
            ["**Process**", "The overall approach to all activities and project governance."],
            ["**People**", "Including dynamics of how they collaborate and communicate."],
            ["**Power**", "Lines of authority, decision-makers, organograms, policies for implementation and the "
             "like."],
        ],
        [1.5, 5.0],
    )
    n.memory("The name is already the mnemonic: **Plan, Process, People, Power**, all four P's.")

    n.h3("The Ten Project Management Areas")
    n.bullets([
        "Integration", "Scope", "Time", "Cost", "Quality", "Procurement", "Human resources", "Communications",
        "Risk management", "Stakeholder management",
    ])
    n.memory("**I Scoped This Cost Quickly, Procured Human Capital, Communicated Risks, Satisfied Stakeholders** "
             "= Integration, Scope, Time, Cost, Quality, Procurement, Human resources, Communications, Risk "
             "management, Stakeholder management.")

    n.h3("The Five Project Management Phases")
    n.p("Flow on the slide: **Initiation -> Planning and Design -> Executing <-> Monitoring and Controlling -> "
        "Closing.**")
    n.memory("**Is Pizza Eaten Mid-Course?** = Initiation, Planning and design, Execution, Monitoring and "
             "controlling, Closing. Execution and Monitoring/Controlling loop back and forth (\"mid-course\") "
             "before Closing.")
    n.table(
        ["Phase", "Description", "Process-Group Items From The Diagram"],
        [
            ["1. **Initiation**", "Determines the nature and scope of the project. If this stage is not "
             "performed well, it is unlikely the project will succeed in meeting the business' needs. Needs an "
             "understanding of the business environment and all necessary controls incorporated.", "Initiating "
             "Process Group -> Scope: Develop Charter; Scope: Develop Preliminary Scope Statement."],
            ["2. **Planning and Design**", "After initialization, the project is planned to an appropriate "
             "level of detail. The main purpose is to plan time, cost and resources adequately, to estimate the "
             "work needed, and to effectively manage risk during execution.", "(No diagram items given beyond "
             "the phase flow.)"],
            ["3. **Execution**", "One must know what are the planned terms to be executed. Ensures the project "
             "management plan's deliverables are executed accordingly, with proper allocation, co-ordination and "
             "management of human and other resources. Output: the project deliverables.", "Planning Process "
             "Group -> Integration: Project Management Plan Execution; Quality: Quality Assurance; "
             "Communication: Information Distribution; Communication: Team Development; Procurement: Plan "
             "Contracting -> Source Selection -> Contract Administration. Loops with the Controlling Process "
             "Group."],
            ["4. **Monitoring and Controlling**", "Processes performed to observe project execution so potential "
             "problems can be identified in a timely manner and corrective action taken when necessary. Key "
             "benefit: performance is observed and measured regularly to identify variances from the plan.", "Communications: "
             "Performance Reporting; Integration: Integrated Change Control; Scope: Scope Verification; Scope: "
             "Scope Change Control; Time: Schedule Control; Cost: Cost Control; Procurement: Quality Control; "
             "Procurement: Risk Monitoring and Control. Feeds the Closeout Process Group."],
            ["5. **Closing**", "Includes the formal acceptance and ending of the project. Administrative "
             "activities include archiving files and documentation.", "Controlling Process Group -> Procurement: "
             "Contract Closure; Communication: Close Project. Consists of **Contract closure** (settle and close "
             "each contract) and **Project close** (finalize all activities to formally close the project or "
             "phase)."],
        ],
        [1.3, 2.9, 2.3],
    )

    n.h3("Project Documentation")
    n.p("Documenting everything within a project is key to being successful. To maintain budget, scope, "
        "effectiveness and pace, a project must have physical documents pertaining to each specific task. With "
        "correct documentation, it is easy to see whether or not a project's requirement has been met, and it "
        "provides information regarding what has already been completed.")
    n.p("Documentation throughout a project provides a documented trail for anyone who needs to go back and "
        "reference past work. In most cases, documentation is the most successful way to monitor and control "
        "the specific phases of a project. If performed correctly, it can be the **backbone to a project's "
        "success**.")

    n.h3("Five Project Characteristics")
    n.bullets([
        "Projects should always have a specific start and end dates.",
        "They are performed and completed by a group of people working as one.",
        "The output should deliver a working/unique product or service.",
        "They are temporary in nature.",
        "They are progressively elaborated.",
    ])
    n.memory("**Smart Groups Usually Try Everything** = Start/end dates, Group of people, Unique output, "
             "Temporary, Elaborated progressively.")

    n.h3("The Eight Umbrella Activities")
    n.table(
        ["Activity", "What It Means"],
        [
            ["**Project Tracking and Control**", "Assess the progress of the project plan."],
            ["**Risk Management**", "Assess risks that may affect the product outcome."],
            ["**Quality Assurance**", "Conduct activities to ensure product quality."],
            ["**Technical Review**", "Assess the work product to identify errors beforehand."],
            ["**Measurement**", "Defines and collects process to deliver and meet the needs of the "
             "stakeholders."],
            ["**Configuration Management**", "Manages the effects of changes in the software process."],
            ["**Reusability Management**", "Defines criteria to establish mechanisms for reusable components."],
            ["**Work Product Preparation and Production**", "Encompasses activities required to create work "
             "products such as models or documentation."],
        ],
        [2.6, 3.9],
    )
    n.memory("**Tracking Risks Quietly, Technical Measures Control Reuse, Work** = Tracking and Control, Risk "
             "management, Quality assurance, Technical review, Measurement, Configuration management, "
             "Reusability management, Work product preparation.")

    n.pagebreak()
    n.h2("Chapter 2: Analysis And Computer Science Research Trends")

    n.h3("Analysis Vs Synthesis")
    n.p("**Analysis** is defined as \"the procedure by which we break down an intellectual or substantial whole "
        "into parts,\" while **synthesis** means \"the procedure by which we combine separate elements or "
        "components in order to form a coherent whole.\" System analysis researchers apply methodology to the "
        "systems involved, forming an overall picture.")

    n.h3("System Analysis")
    n.p("It is the process of studying a procedure or business in order to identify its goals and purposes and "
        "create systems and procedures that will achieve them in an efficient way. It is also a problem-solving "
        "technique that breaks down a system into its component pieces for the purpose of studying how well "
        "those component parts work and interact to accomplish their purpose.")

    n.h3("The Analysis Phase")
    n.p("The analysis phase involves gathering requirements for the system. At this stage, business needs are "
        "studied with the intention of making business processes more efficient. The system analysis phase "
        "focuses on what the system will do, in an effort that views all stakeholders as viable sources of "
        "information. A significant amount of time is spent talking with stakeholders and reviewing their "
        "input.")

    n.h3("The Five Analysis Phase Procedures")
    n.table(
        ["Procedure", "What It Means"],
        [
            ["1. **Scope Definition**", "Clearly defined objectives and requirements necessary to meet a "
             "project's requirements as defined by its stakeholders."],
            ["2. **Problem Analysis**", "The process of understanding problems and needs and arriving at "
             "solutions that meet them."],
            ["3. **Requirements Analysis**", "Determining the conditions that need to be met."],
            ["4. **Logical Design**", "Looking at the logical relationship among the objects."],
            ["5. **Decision Analysis**", "Making a final decision."],
        ],
        [2.0, 4.5],
    )
    n.memory("**Some People Really Love Deciding** = Scope definition, Problem analysis, Requirements analysis, "
             "Logical design, Decision analysis.")

    n.h3("Computer Science Research Trends")
    n.p("Computer science graduates have some of the highest starting salaries out there and are in such high "
        "demand that they can afford to be picky about the type of job and industry they opt for. If you are "
        "interested in pursuing a career in computer science, it's important to stay up to date with the "
        "latest trends in computer science research, to make an informed choice about where to head next.")

    n.h3("The Five CS Research Trends (2019 to 2020)")
    n.table(
        ["Trend", "Description"],
        [
            ["**Artificial Intelligence and Robotics**", "One of the most controversial and intriguing areas of "
             "CS research. Still in its early stages, but tech giants like Facebook, Google and IBM are "
             "investing huge amounts of money and resources into AI research. No shortage of opportunities for "
             "real-world applications and breakthroughs."],
            ["**Big Data Analytics**", "A surge in demand for experts in this field, with doubled efforts by "
             "brands and agencies to boost salaries and attract data science talents. From banking to "
             "healthcare, big data analytics is everywhere as companies try to make better use of enormous "
             "datasets."],
            ["**Computer-assisted Education**", "The use of computers and software to assist education and/or "
             "training. Brings many benefits, such as personalized instruction for students with learning "
             "disabilities, letting them learn at their own pace. Still growing but promising, allowing "
             "active, independent, play-based learning."],
            ["**Bioinformatics**", "An application of big data, or the use of programming and software "
             "development to build enormous datasets of biological information, carrying enormous potential. "
             "Linking big pharmaceutical companies with software companies, it offers good job prospects for "
             "CS researchers interested in biology, medical technology, and pharmaceuticals."],
            ["**Cyber Security**", "We live in a hyper-connected world where everything, from banking to "
             "dating to governmental infrastructure, is done online. Data protection is no longer optional, for "
             "either individuals or nations, making this a growing strand of CS research."],
        ],
        [2.1, 4.4],
    )
    n.memory("**Amazing Big Computers Battle Cyberthreats** = AI and robotics, Big data analytics, "
             "Computer-assisted education, Bioinformatics, Cyber security.")

    n.h3("Top Research Titles By Trend (2019, Low Detail)")
    n.p("These titles are listed on the slides for reference only; the exam is unlikely to ask for their "
        "content, just that they exist under each trend.")
    n.table(
        ["Research Area", "Titles Listed"],
        [
            ["AI and Robotics", "The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks; "
             "Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations; "
             "Meta-Learning Update Rules for Unsupervised Representation Learning."],
            ["Big Data Analytics", "An integrated parallel big data decision support tool using the "
             "W-CLUS-MCDA; Effect of E-customization Capability on Financial Performance of Commercial Banks in "
             "Kenya; Interaction of East Bay Area Voters with California Death Penalty Ballot Initiatives; "
             "Command Decision: Ethical Leadership In The Information Environment."],
            ["Computer-Assisted Education", "Qualitative case studies of innovative pedagogical practices using "
             "ICT; What strategies are effective for formative assessment in an e-learning environment?; "
             "Web-based Assessment and Test Analyses (WATA) system; Computer-Assisted Learning in Orthodontic "
             "Education."],
            ["Bioinformatics", "A Survey for Escherichia coli Virulence Factors in Asymptomatic Free-Ranging "
             "Parrots; Immunoreactivity of the 14F7 Mab Raised against N-Glycolyl GM3 Ganglioside in Epithelial "
             "Malignant Tumors from Digestive System; Investigating the effects of external fields polarization "
             "on the coupling of pure magnetic waves in the human body in very low frequencies."],
            ["Cyber Security", "Intelligence Gathering And Social Media-Based Sentiment Correlation; High "
             "Accuracy Phishing Detection Based on Convolutional Neural Networks; Understanding Security "
             "Policies in the Cyber Warfare Domain Through System Dynamics."],
        ],
        [1.7, 4.8],
    )


def build():
    n = Notes(
        "SE1 Midterm Reviewer: Modules 1 and 2",
        "CS0025 Software Engineering 1. Built from CS0024-M1S0-1, M1S1, M1S2, M1S3, CS0025-M2S0, M2S1, and M2S2. "
        "The blue boxes are memory aids I made; they are not from the slides. The red boxes flag places where the "
        "slides are easy to mix up.",
    )
    n.h1("What Is Inside")
    n.bullets([
        "**Part 1, Module 1:** Chapter 1 software and software engineering fundamentals; Chapter 2 systems and "
        "information systems; Chapter 3 the System Development Life Cycle.",
        "**Part 2, Module 2:** Chapter 1 project management, Gantt and PERT, and the project management phases; "
        "Chapter 2 analysis, system analysis, and computer science research trends.",
        "A one-page cram sheet at the end. Read it last, right before the exam.",
    ])
    n.h2("Fast Memory Map")
    n.table(
        ["Topic", "Hook"],
        [
            ["Software categories (7)", "Sam Always Eats Eggs, Pizza, Waffles, Apples"],
            ["SE layers (4)", "Toddlers Make Pretty Quilts (Tools, Methods, Process, Quality Focus)"],
            ["SE principles (7)", "Real Kids Make Pretty Open Plans, Think!"],
            ["IS types (7)", "Record-keepers (TPS), Decision helpers (DSS, EIS, MIS), Coordinators (Workflow), "
             "Integrators (ERP, Expert)"],
            ["SDLC phases (7)", "Please Always Design Decent, Test, Implement, Maintain"],
            ["Gantt vs Fayol", "Gantt = planning (chart); Fayol = five functions"],
            ["Four P's", "Plan, Process, People, Power"],
            ["PM areas (10)", "I Scoped This Cost Quickly, Procured Human Capital, Communicated Risks, "
             "Satisfied Stakeholders"],
            ["PM phases (5)", "Is Pizza Eaten Mid-Course?"],
            ["Umbrella activities (8)", "Tracking Risks Quietly, Technical Measures Control Reuse, Work"],
            ["Analysis procedures (5)", "Some People Really Love Deciding"],
            ["CS research trends (5)", "Amazing Big Computers Battle Cyberthreats"],
        ],
        [2.0, 4.5],
    )

    n.pagebreak()
    m1(n)
    n.pagebreak()
    m2(n)

    n.pagebreak()
    n.h1("One-Page Cram Sheet")
    n.table(
        ["Topic", "Remember"],
        [
            ["5 software questions", "Time, Cost, Errors before release, Maintenance, Measuring progress"],
            ["7 software categories", "System, Application, Engineering/Scientific, Embedded, Product-line, "
             "Web/Mobile, AI"],
            ["SE layers, top to bottom", "Tools, Methods, Process, Quality Focus (Quality Focus = bedrock, "
             "Process = text's \"foundation\")"],
            ["Process framework (5)", "Communication, Planning, Modeling, Construction, Deployment"],
            ["7 SE principles", "Reason it exists, KISS, Maintain vision, Produce for others, Open to future, "
             "Plan for reuse, Think"],
            ["Open vs Closed systems", "Open = probabilistic (guess only); Closed = predictable"],
            ["IS activities", "Input, Process, Output, Feedback"],
            ["6 good info traits", "Accuracy, Timeliness, Less uncertainty, Surprise value, Aid decisions, "
             "Update knowledge"],
            ["7 IS types", "TPS, DSS, EIS (= Executive Support System), MIS, Workflow, ERP, Expert Systems"],
            ["DSS trap", "DSS helps decide, does NOT make the decision"],
            ["7 SDLC phases", "Planning, Analysis, Design, Development, Testing, Implementation, Maintenance"],
            ["Implementation trap", "Slide says most code is written AND system cutover both happen in "
             "Implementation (p12), even though Development (p10) is where \"the real work begins\""],
            ["System vs Software SDLC", "System SDLC = superset, people+process+tech; Software SDLC = only "
             "software, part of the Development Phase"],
            ["Gantt vs Fayol", "Gantt = father of planning and control (Gantt Chart); Fayol = five management "
             "functions"],
            ["PERT example", "Longest path 10-30-40-50 = 7 months, ties with 10-20-50 = 7 months"],
            ["Four P's", "Plan, Process, People, Power"],
            ["10 PM areas", "Integration, Scope, Time, Cost, Quality, Procurement, HR, Communications, Risk, "
             "Stakeholder"],
            ["5 PM phases", "Initiation, Planning and Design, Execution, Monitoring and Controlling, Closing"],
            ["5 project characteristics", "Start/end dates, group effort, unique output, temporary, "
             "progressively elaborated"],
            ["8 umbrella activities", "Tracking and Control, Risk Mgmt, QA, Technical Review, Measurement, "
             "Configuration Mgmt, Reusability Mgmt, Work Product Preparation"],
            ["Analysis vs Synthesis", "Analysis breaks a whole into parts; Synthesis combines parts into a "
             "whole"],
            ["5 analysis procedures", "Scope Definition, Problem analysis, Requirements analysis, Logical "
             "design, Decision analysis"],
            ["5 CS research trends", "AI and robotics, Big data analytics, Computer-assisted education, "
             "Bioinformatics, Cyber security"],
        ],
        [1.9, 4.6],
    )

    path = str(OUT / "PAMESA - SE1 M1-M2 Reviewer.docx")
    n.save(path)
    return path


if __name__ == "__main__":
    build()
    print("done")
