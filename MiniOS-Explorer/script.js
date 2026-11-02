const fileDetails = {
    main: {
        name: "main.py",
        icon: "PY",

        summary:
            "The main entry  point of MiniOS. It starts the interactive command loop.",

        purpose:
            "This file receives user commands and connects the shell with the  other project modules.",

        tasks: [
            "Starts the MiniOS command-line interface.",
            "Reads the user's input.",
            "Routes supported commands to the relevant modules.",
            "Displays result or helpful messages.",
            "Provides a central command loop so the user can perform multiple operations in one session.",
            "Connects different parts of the simulator through imports and function calls."
        ],

        connection:
            "main.py recieves the user's file-related command and calls the relevant function from file_manager.py. The file manager then performs the request operation and returnsor displays the result, depending on how its function are written.",

        importance:
            "This file acts as the central control point of MiniOS. It connects the command-line interface with different modules and allows users to access the simulator's features."
    },

    file: {
        name: "file_manager.py",
        icon: "PY",

        summary:
            "file_manager.py is responsible for file-related operationin the MiniOS simulator. It demonstrate how a program can create, access, update and remove files through a set of functions.",

        purpose:
            "Its purpose is to keep file-handling logic seperate from the main command interface. This makes the program easier to understand, test, maintain and extend with additional file feature.",

        tasks: [
            "Creates a new file when a suppported create command is used.",
            "Writes user-provided content into files.",
            "Reads and displays the content of an existing file.",
            "Deletes a file when the relevant operation is requested.",
            "Checks whether a file already exists before performing certain operations, if implemented.",
            "Provides feedback when a file cannotbe found or an operation fails.",
            "Keeps file-operation code seperate from command parsing in main.py.",
            "Checks file permissions before allowing read, write or delete operations."
        ],

        connection:
            "main.py recieves the user's file-related command and calls the relevant function from file_manager.py. The file manager then performs the requested operation and return or displays the result, dependig how its functions are written.",

        importance:
            "This module helps demonstarte basic file-system operations. It also makes it easier to add features such as file listing, renaming, folders or permissionsint he future."
    },

    process: {
        name: "process_manager.py",
        icon: "py",

        summary:
            "process_manager.py simulates basic process management. A processis a programor task that is being executed. In an operating system, process management helps keep track of tasks and their execution starts",

        purpose:
            "The purpose of this module is to demonstrate how MiniOS can create and track simulated processes. It helps explain concepts such as process identifiers, process lists and starting or stopping tasks without claiming to manage actual windows processes.",

        tasks: [
            "Starts a simulated process when the appropriate command is entered.",
            "Assigns a unique Process ID (PID) to each process.",
            "Stores process names, burst times and priorities.",
            "Displays the processes currently tracked by MiniOS.",
            "Stops a simulated process when requested.",
            "Maintains process information for CPU scheduling demonstrations."
        ],

        connection:
            "main.py sends process related commands to process_manager.py. A CPU scheduling module may use process information to demonstrate scheduling, but that connection exists only if the current source code implements it.",

        importance:
            "Process managementis is a core operating-system concept. This module helps learners unedrstand how tasks can be identified, tracked and controlled in a simplified enviourment."
    },

    memory: {
        name: "memory_manager.py",
        icon: "PY",

        summary:
            "memory_manager.py simulates memory allocation and usage tracking with a total capacity of 1024 units. It demonstrates how an operating system manages memory resources.",

        purpose:
            "This module demonstrate how a program can keep track of simulated memory capacity, allocated memory and remaining memory. It is an educational model and does not directly allocate or control the computer's physical RAM.",

        tasks: [
            "Displays memory information maintained by the simulator.",
            "Allocates a specified amount of simulated memory when requested.",
            "Tracks allocated memory against a process name.",
            "Frees previously allocated memory when the relevant command is used.",
            "Updates the tracked memory usage after allocation or release.",
            "Helps illustrate the difference between used and available memory.",
            "Can demontrate allocation errors, such as requesting more memory than is available, if implemented."
        ],

        connection:
            "main.py handles the user's memory command and calls memory_manager.py, The module updates its simulated memory records and reports the result. Integration with process_manager.py depends on whether the code associates memory allocations with tracked processes.",

        importance:
            "This module introduces the basic idea of memory allocation and resource tracking. It can be extended to demonstrate memory limits, allocation tables or simple memory-management stratagies.",
    },

    cpu: {
        name: "cpu_schedulor.py",
        icon: "PY",

        summary:
            "cpu_schedulor.py demonstrates three CPU scheduling algorithms: First Come First Served (FCFS), Round Robin and Priority Scheduling.",

        purpose:
            "A CPU scheduling module can help compare how different scheduling stratigies select processes. Its actual purpose and capabilities should be confirmed by examining the functions and algorithms present in the current source file.",

        tasks: [
            "Implements First Come First Served (FCFS) scheduling.",
            "Provides a Round Robin scheduling function.",
            "Provides a Priority Scheduling function.",
            "Demonstrates how different scheduling algorithms arrange processes.",
            "Helps explain how CPU time can be distributed among processes."
        ],

        connection:
            "A scheduling module can work with process information from process_manager.py and can be called through main.py. These connections must ne verified from the actual imports and function calls; the filename alone does not confirm that scheduling is implemented.",

        importance:
            "CPU scheduling is important for understanding how operating system share processor time among tasks. A working simulator can help learners compare scheduling approaches."
    },

    user: {
        name: "user_manager.py",
        icon: "PY",

        summary:
            "user_manager.py is intended to contain use-management functionality for MiniOS. User management can involve maintaining account information, checking login details and disguisting between different users or rules.",

        purpose:
            "The purpose of this module is to keep user-related logic seperate from the main command interface. Its exact features depend on the functions, data structure and checks implemented in the source code",

        tasks: [
            "May provide functions for creating or maintaining user accounts.",
            "May check login credentials when authentication is implemented.",
            "May distinguish user roles or permissions if the project supports them.",
            "May store account information in memory or in a file, depending on the implementation.",
            "Can be extended with access-control checks for selected commands",
            "Requires source-code review to confirm how passwords and account data are handled."
        ],

        connection:
            "main.py could call  user_manger.py when the user requests an account-related operation. Other modules would need appropriate checks to enforce permissions, simply having a user manager does not automatically secure every command.",

        importance:
            "This module can introduce concepts such as user accounts, authentication and access control. Real security requires careful credential handling and permission checks throughout the application."
    },

    disk: {
        name: "disk_manager.py",
        icon: "PY",

        summary:
            "disk_manager.py simulates disk-space management with a total capacity of 10240 units. It tracks storage allocation and saves allocation records in disk_storage.json.",

        purpose:
            "The module can demonstrate how storage capacity and usage are tracked. Depending on its implementation, it may maintain a simulated storage model rather than manage physical disk or partitions.",

        tasks: [
            "May track the total storage capacity defined for the simulator.",
            "May record how much simulated storage is used and remains available.",
            "Can demonstrate storage allocation and release if those operations are implemented.",
            "May report storage statistics to the user.",
            "Can be extended to track file sizes or storage blocks.",
            "Should be checked to confirm whether it uses actual file sizes, simulated values or another data structure."
        ],

        connection:
            "main.py may route storage-related commands to disk_manager.py. The module could also share information with file_manager.py, but that integration must be confirmed in the source code.",

        importance:
            "This module can help explain the difference between memory and long-term storage. It also provides a starting point for learning about capacity tracking and storage allocation."
    },

    monitor: {
        name: "system_monitor.py",
        icon: "Py",

        summary:
            "system_monitor.py is intended to display information about the state and resources of the MiniOS simulator. A system monitor helps users observe what is heppening instead of relaying only on individual command result.",

        purpose:
            "Its purpose is to bring relevant status information together in a readable form. The exact statistics it can display depend on which modules it reads and what data the current implementation makes available.",

        tasks: [
            "May display an overview of the simulator's current state.",
            "Can show tracked process information if connected to process_manager.py.",
            "Can display simulated mamory usage if connected to memory_manager.py",
            "Can display storage statistics if connected to disk_manager.py.",
            "May calculate or present summary statistics from available data.",
            "Can be extended into a status screen or monitoring dashboard.",
            "Should be checked to a confirm which statistics are actually collected and displayed."
        ],

        connection:
            "A system monitor can obtain information from the process, memory and disk modules and present it to the user. These connections require actual imports, function calls or shared data in the project.",

        importance:
            "System monitoring helps users understand resource usage and system state. In an educational simulator, it can bring several operating-system concepts together in one view."
    }
};


const fileButtons = document.querySelectorAll(".file-button");

const detailIcon = document.getElementById("detailIcon");
const detailName = document.getElementById("detailName");
const detailSummary = document.getElementById("detailSummary");
const detailPurpose = document.getElementById("detailPurpose");
const detailTask = document.getElementById("detailTask");
const detailConnection = document.getElementById("detailConnection");
const detailImportance = document.getElementById("detailImportance");

fileButtons.forEach(function (button) {
    button.addEventListener("click", function () {

        const selectedFile = button.dataset.file;
        const details = fileDetails[selectedFile];

        if (!details) {
            return;
        }

        fileButtons.forEach(function (item) {
            item.classList.remove("active");
        });

        button.classList.add("active");

        detailIcon.textContent = details.icon;
        detailName.textContent = details.name;
        detailSummary.textContent = details.summary;
        detailPurpose.textContent = details.purpose;
        detailConnection.textContent = details.connection;
        detailImportance.textContent = details.importance;

        detailTask.replaceChildren();

        details.tasks.forEach(function (task) {
            const listItem = document.createElement("li");
            listItem.textContent = task;
            detailTask.appendChild(listItem);
        });
    });
});

const commandForm = document.getElementById("commandForm");
const commandInput = document.getElementById("commandInput");
const terminalOutput = document.getElementById("terminalOutput");

commandForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    const command = commandInput.value.trim();

    if (!command) {
        return;
    }

    const commandLine = document.createElement("p");
    commandLine.textContent = `MiniOS > ${command}`;
    terminalOutput.appendChild(commandLine);

    commandInput.value = "";

    try {
        const response = await fetch("/api/command", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ command: command })
        });

        const data = await response.json();

        const resultLine = document.createElement("pre");
        resultLine.textContent = data.output || "No output recieved.";
        terminalOutput.appendChild(resultLine);
    } catch (error) {
        const errorLine = document.createElement("p");
        errorLine.textContent = "Error: Could not connect to MiniOS backend.";
        terminalOutput.appendChild(errorLine);
    }

    terminalOutput.scrollTop = terminalOutput.scrollHeight;
    commandInput.focus();
});