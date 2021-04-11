# EonNextAutomationFramework
Test Framework developed using Python nehave framework

After cloning the git repo, please install the packages in requirements.txt to your local PC

Use the below commands to run the test:

Open the terminal & navigate to the root directory
Run the below command to execute the test
behave -f allure_behave.formatter:AllureFormatter -o allure/results ./features

Run the below command to launch the test results from allure
allure serve <Path of the results directory inside the test framework>
example: allure serve /Users/kiran/PycharmProjects/BDD/allure/results
