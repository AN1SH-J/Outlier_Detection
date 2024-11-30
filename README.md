# Outlier_Detection

This script focuses on identifying the outliers from a given dataset of stock prices.

**CONTENTS:**
- Guide to run the application
- SRE/DevOps best practices
- References

**Guide to run the application:**
------------------------------
* _Install python in your system
* Install libraries like pandas, numpy using **pip** command
* Run the code as "python main.py"_

**SRE/DevOps best practices to be introduced:**
-------------------------------------------

1. Introducing observability tools like Datadog

* Adding logging steps for successful file processing and the necessary error logs being tracked helps in segregation and easier troubleshooting
* Enables adding alerts or monitors in place based on the requirements that prevent missing unprocessed/errorenous/bad files getting into the system

2. Shift-Left security practices

* Introduction of tools like Synk can enable in better security and reliability checks before the code is pushed into production to the end users
* This prevents use of depracted libraries or functions, danger prone gaps in external tools/libraries
* This is even more benefecial in an environent that had multiple collaborators and deployments

3. Secrets management

* Embedding the secrets like API keys for datadog and cloud access IDs etc. as a key-value pair to a tool like Vault can avoid exposure of sensitive data

4. Product focused reliabilty (assuming it is used for end-users)

* Adding file process "retry" option to cover for network and other technical glitches at client/server side
* Tracking using logs the time taken for file processing to ensure the UX is not hindered by abnormal duration to process the files
* Definition of 'success' is also something to be discussed from the product perspective for better delivery of the application/product


**References:**
-------------

- Mathematical functions and libraries : https://www.geeksforgeeks.org/mastering-python-libraries-for-effective-data-processing/
- OS functions : https://docs.python.org/3/library/os.html
- 

