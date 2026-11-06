# deva.cyber.py
Repository dedicated to Cybersecurity research, Digital Forensics, and Ethical Hacking tools. Features practical scripts including cryptographic file integrity checkers, secure automation workflows, and defensive logic implementations built with Python.



File Integrity Checker Architecture
```mermaid
Overview
This Python-based File Integrity Checker monitors a target file for unauthorized modifications by using SHA-256 cryptographic hashing. The application generates an initial baseline hash, waits for potential file changes, recalculates the file hash, and compares both values to verify integrity.

Architecture Diagram
flowchart TD

    A[User Provides Target File Path]
    B{File Exists?}
    C[Generate Baseline SHA-256 Hash]
    D[Store Baseline Hash]
    E[Wait for User Modification]
    F[Recalculate Current SHA-256 Hash]
    G{Compare Hashes}
    H[Integrity Verified ✅<br/>Green Signal]
    I[Security Alert 🚨<br/>File Modified]
    J[Display Error<br/>File Not Found]

    A --> B

    B -->|Yes| C
    B -->|No| J

    C --> D
    D --> E
    E --> F
    F --> G

    G -->|Match| H
    G -->|Mismatch| I
Component Responsibilities
User Input
Accepts the target file path from the user.
Initiates the integrity monitoring process.
File Existence Validation
Verifies whether the specified file is available.
Prevents unnecessary hash calculations on invalid paths.
Baseline Hash Generator
Computes the initial SHA-256 hash of the target file.
Establishes the trusted integrity reference.
Baseline Hash Storage
Stores the original hash value in memory or a local file.
Provides a reference for future comparisons.
Modification Waiting Phase
Represents the period during which the user may edit or modify the file.
Simulates real-world file monitoring behavior.
Current Hash Generator
Recalculates the SHA-256 hash after the file may have changed.
Produces the current integrity state of the file.
Integrity Verification Logic
Compares the baseline and current hash values.
Determines whether the file remains unchanged.
Security Alert
Triggered when the hashes do not match.
Indicates potential tampering or unauthorized modification.
Integrity Verified
Triggered when the hashes match.
Confirms that file contents remain unchanged.
Processing Flow
User specifies a target file.
System checks whether the file exists.
If the file exists, a baseline SHA-256 hash is generated.
The baseline hash is stored as a trusted reference.
The system waits for potential file modifications.
A new SHA-256 hash is calculated.
Both hashes are compared.
Matching hashes produce an integrity success notification.
Mismatched hashes generate a security alert. ```

