Feature: login with Medsembly
		As a user i want to signin in medsembly so that i go to dashboard
		
Scenario: sign in to medsembly by valid user details
		  Given the user on medsembly signin page
		  When user enter jamit@mailinator.com as email in signin page
		  And user enter spider@123 as password in signin page
		  And user click on signin button 
		  Then ensure that user should be on dashboard page with welcome message Successfully signed in as jamit@mailinator.com.
		  When user click on user profile pic to select logout 
		  And user click on logout button in navbar dropdown
		  And user click on sign out button to confirm logout from the Medsembly
		  Then ensure that user should be redirect to signin page of Medsembly and recive message You have signed out.	
		  
Scenario: sign in to medsembly by wrong email address
		  Given the user on medsembly signin page
		  When user enter xxx@mailinator.com as email in signin page
		  And user enter spider@123 as password in signin page
		  And user click on signin button 				
		  Then ensure that user should get error message The e-mail address and/or password you specified are not correct.	
		  
Scenario: sign in to medsembly by wrong password 
		  Given the user on medsembly signin page
		  When user enter jamit@mailinator.com as email in signin page
		  And user enter 123456789 as password in signin page
		  And user click on signin button 				
		  Then ensure that user should get error message The e-mail address and/or password you specified are not correct.				
		  
