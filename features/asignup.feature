Feature: Signup with Medsembly
		As a user i want to Signup in medsembly so that i can login to medsembly
		
Scenario:	Signup with valid user detail
			Given the user on medsembly signup page
			When user enter jamit@mailinator.com as email in signup form
			And user enter spider@123 as password in signup form
			And user enter spider@123 as confirm password in signup form
			And user click on signup button for signup
			Then ensure that user should get notification for Verify Your E-mail Address
			Given user go to mailinator.com to verify mail
			When user open mail for confirm mail id
			And user click on confirm link 
			Then ensure that user should redirect to Confirm E-mail Address page to verify email
			When user click on confirm button to verify mail
			Then ensure that after verification user goes to Sign In page 
			
Scenario:	Try to Signup with already register email
			Given the user on medsembly signup page
			When user enter jamit@mailinator.com as email in signup form
			And user enter spider@123 as password in signup form
			And user enter spider@123 as confirm password in signup form
			And user click on signup button for signup
			Then ensure that user should get error notification A user is already registered with this e-mail address.