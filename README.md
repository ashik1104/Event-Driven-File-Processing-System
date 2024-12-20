# **Event-Driven File Processing System**

## **Summary**  
Developed an event-driven architecture for automated file processing, enabling dynamic handling of incoming files in a monitored directory. This system supports real-time execution, file archiving, and automatic cleanup, reducing manual file management tasks.

---

## **Key Features**  

- **File Monitoring:** Continuously monitored a source directory for incoming files using event-driven logic.  
- **Dynamic Code Execution:** Identified and executed Python files in real time, ensuring proper cleanup post-execution.  
- **File Processing & Archiving:** Split text files into smaller files, packaged them into zip archives, and transferred them to a designated destination folder.  
- **Error Handling:** Implemented robust exception handling with detailed traceback logging for debugging and issue resolution.  

---

## **Technologies Used**  

- **Programming Language:** Python  
- **Libraries/Modules:** `os`, `shutil`, `glob`, `traceback`  
- **Design Pattern:** Event-Driven Architecture  

---

## **Impact**  

- Automated file processing pipeline with minimal manual intervention.  
- Enhanced system reliability by ensuring proper file cleanup after every task.  
- Improved code execution safety using detailed error logging and recovery mechanisms.  

---

