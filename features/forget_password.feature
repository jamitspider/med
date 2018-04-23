Feature: user reset password by using forget password feature
		As a user i want to reset my password with valid data
		
Scenario: reset password to medsembly by valid user details
		  Given the user on medsembly reset password reset page
		  When user enter jamit@mailinator.com as email in password reset page
		  And user click on reset my password button 
		  Then ensure that after click on reset my password button user should be get message We have sent you an e-mail. Please contact us if you do not receive it within a few minutes.
		  Given user go to mailinator.com to verify mail
		  When user open mail for password reset mail id
		  And user click on password reset link 
		  Then ensure that user should redirect to Change Password page for reset password
		  When user enter spider@123 as a new password on change password page
		  And user enter spider@123 as a confirm new password on change password page
		  When user click on chage password button to reset password
		  Then ensure that after click on change password button user get Your password is now changed. message on screen 
		  
Scenario: try to reset password to medsembly by wrong email id
		  Given the user on medsembly reset password reset page
		  When user enter xxx@mailinator.com as email in password reset page
		  And user click on reset my password button 
		  Then ensure that after click on reset my password button user should be get error message The e-mail address is not assigned to any user account
