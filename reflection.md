1. Which issues were easiest and hardest to fix?<br>
 The easiest fixes were style-related issues, such as adding docstrings and renaming functions to follow snake_case conventions. The hardest was handling exceptions correctly, since it required understanding which exceptions might actually occur and deciding how to log or handle them properly.


3. Did the static analysis tools report any false positives?<br>
 Yes. Pylint warned about an unused import (logging), but I later used it for proper error handling, making the warning irrelevant after refactoring.


4. How would you integrate static analysis tools into your workflow?<br>
 I would integrate these tools in a GitHub Actions CI pipeline so that every pull request is automatically scanned by Bandit, Flake8, and Pylint. Locally, I would run them before committing code to maintain consistent style and prevent vulnerabilities.


6. What improvements did you notice after applying the fixes?<br>
 After the fixes, the code became much more readable, maintainable, and secure. The exception handling is now explicit, file operations are safer, and the removal of eval() eliminated a potential security risk.
