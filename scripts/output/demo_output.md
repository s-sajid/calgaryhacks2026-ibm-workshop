# Hackathon Project Report

## Analyzer Output

### Overview
**AssigmentHub** is an Android application designed to help university professors manage assignments more efficiently. The project includes features for adding, viewing, and tracking student submissions of assignments, aiming to streamline the grading process and improve communication between teachers and students.

The repository contains a solid foundation with essential files such as `AndroidManifest.xml`, layout definitions (`*.kt`), ViewModel classes, and Gradle configuration files. This setup indicates that core functionality is already in place, providing a good starting point for further development.

### Existing Strengths
- **Well-Documented**: The project includes clear README, license information, and usage instructions.
- **Modern Tooling**: Uses modern Android development practices (e.g., Lint compliance) and integrates AWS Amplify for backend authentication and data storage.
- **Modular Structure**: Organized into distinct packages (`android`, `data.repositories`, `ui`, etc.), which enhances maintainability.
- **Feature Completeness**: Implements essential features like adding assignments, tracking student submissions, and authenticating users (teacher login).
- **UI Enhancements**: Utilizes Material Design components for a polished user interface, with animations for smoother transitions.

### Weaknesses
- **Missing Features**: No UI for viewing completed assignments or handling overdue submissions.
- **Limited Error Handling**: The `HomeActivity.kt` lacks comprehensive error handling and recovery mechanisms.
- **Authentication Complexity**: While AWS Amplify handles authentication, deeper integration (e.g., role-based access control) is not yet implemented.
- **Testing Coverage**: No indication of automated tests being present in the repository, which could be a risk for future changes.
- **Documentation Gaps**: Some sections like `DetailAssignmentActivity.kt` and `AddStudentActivity.kt` lack comments explaining their behavior or purpose.

## Planner Output

**Top Features to Build**
- **View Completed Assignments**: Implement a feature allowing professors to view all completed assignments, including submission status and grades.
- **Overdue Submissions Alert**: Add functionality to notify professors about overdue submissions, enhancing communication with students.
- **Error Handling Enhancements**: Improve error handling in key components such as `HomeActivity.kt` to ensure a smoother user experience.
- **Role-Based Access Control (RBAC)**: Integrate RBAC for different levels of access based on professor roles or departments.
- **Automated Testing Framework**: Set up unit and integration tests to cover critical paths, ensuring code stability.

**24-Hour Execution Plan**
1. **Morning (2 Hours)**
   - Review existing repository structure and documentation.
   - Identify key areas needing improvement (e.g., error handling, testing).

2. **Afternoon (4 Hours)**
   - Implement View Completed Assignments feature:
     - Modify database schema to track assignment completion status.
     - Add UI components for listing completed assignments with filters for due dates and grades.

3. **Evening (4 Hours)**
   - Implement Overdue Submissions Alert:
     - Use AWS Amplify's notification system or Android’s Notification API.
     - Set up real-time updates for overdue submissions via a simple notification banner in the app.

4. **Night (2 Hours)**
   - Enhance Error Handling:
     - Add try-catch blocks and error messages where necessary, especially in critical UI components like `HomeActivity.kt`.
   - Start Integration of RBAC:
     - Plan initial roles for professors and set up basic access control using AWS Amplify.

5. **Final Hour**
   - Set up Automated Testing Framework:
     - Implement a simple test suite using JUnit or AndroidJUnit.
   - Refactor Code and Fix Bugs:
     - Ensure all new features are integrated smoothly without introducing regressions.

**Demo Pitch**
- *Title*: AssignmentHub: Streamlining Professors' Workflow
- **Introduction**: Introduce AssignmentHub as an innovative Android application designed to enhance the efficiency of university professors in managing assignments.
- **Key Features**:
  - View Completed Assignments: Allows professors to easily track and manage all completed work, ensuring no submissions are overlooked.
  - Overdue Submissions Alert: Keeps professors informed about overdue tasks, reducing administrative burdens and improving student communication.
  - Enhanced Error Handling: Provides a more robust user experience by gracefully handling errors and exceptions.
  - Role-Based Access Control (RBAC): Offers granular control over access permissions based on professor roles or departments.
- **Benefits**:
  - Saves Time: Automates the tracking of completed assignments, freeing up time for grading and other tasks.
  - Improves Communication: Notifies students about overdue submissions promptly.
  - Increases Efficiency: Reduces administrative overhead through better organization and error management.
- **Conclusion**: AssignmentHub is poised to transform how professors manage their workload, making their job more efficient and less stressful. Join us in revolutionizing academic administration!

**First 3 Tasks**
1. **Review Repository Structure and Documentation**
   - Analyze existing repository structure to understand the current state of the application.
   - Review documentation and README files for insights on project goals and functionalities.

2. **Implement View Completed Assignments Feature**
   - Modify database schema to track assignment completion status.
   - Develop UI components that list completed assignments, allowing professors to filter by due dates and grades.

3. **Enhance Error Handling in `HomeActivity.kt`**
   - Add try-catch blocks and comprehensive error messages throughout the application, focusing on critical paths like `HomeActivity.kt`.
   - Test error handling scenarios to ensure they provide meaningful feedback to users.

## Judge Output

### Scores (1-10)

**Topic Alignment**: 8  
**Innovation**: 7  
**Solution Effectiveness**: 8  
**Technical Challenge**: 6  
**UI/Design**: 7  

### Strengths

- **Well-Documented**: The project includes clear README, license information, and usage instructions.
- **Modern Tooling**: Uses modern Android development practices (e.g., Lint compliance) and integrates AWS Amplify for backend authentication and data storage.
- **Modular Structure**: Organized into distinct packages (`android`, `data.repositories`, `ui`, etc.), which enhances maintainability.
- **Feature Completeness**: Implements essential features like adding assignments, tracking student submissions, and authenticating users (teacher login).
- **UI Enhancements**: Utilizes Material Design components for a polished user interface, with animations for smoother transitions.

### Weaknesses

- **Missing Features**: No UI for viewing completed assignments or handling overdue submissions.
- **Limited Error Handling**: The `HomeActivity.kt` lacks comprehensive error handling and recovery mechanisms.
- **Authentication Complexity**: While AWS Amplify handles authentication, deeper integration (e.g., role-based access control) is not yet implemented.
- **Testing Coverage**: No indication of automated tests being present in the repository, which could be a risk for future changes.
- **Documentation Gaps**: Some sections like `DetailAssignmentActivity.kt` and `AddStudentActivity.kt` lack comments explaining their behavior or purpose.

### Overall Verdict

The project demonstrates solid foundational work with good documentation and modern development practices. However, it lacks features that are crucial for a complete solution, such as viewing completed assignments and overdue submissions handling. Additionally, the absence of comprehensive error handling and testing could lead to issues in real-world usage. With enhancements in these areas, particularly focusing on UI improvements and robust backend support, this project has the potential to significantly impact how professors manage their workload.
