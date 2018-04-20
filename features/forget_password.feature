Feature: user reset password by using forget password feature
		As a user i want to reset my password with valid data
		
Scenario: reset password to medsembly by valid user details
		  Given the user on medsembly reset password reset page
		  When user enter jamit@mailinator.com as email in password reset page
		  And user click on reset my password button 
		  Then ensure that after click on reset my password button user should be get message We have sent you an e-mail. Please contact us if you do not receive it within a few minutes.