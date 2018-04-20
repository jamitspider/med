Feature: login with Medsembly
		As a user i want to signin in medsembly so that i go to dashboard
		
Scenario: signin to medsembly by valid user details
		  Given the user on medsembly signin page
		  When user enter jamit@mailinator.com as email in signin page
		  And user enter spider@123 as password in signin page
		  And user click on signin button 
		  Then ensure that user should be on dashboard page with welcome message Successfully signed in as jamit@mailinator.com.