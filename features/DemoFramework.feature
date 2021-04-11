Feature: Demo For EonNext Interview

  Scenario: Verify User can checkout items from Swaglabs
     Given  User opens Swaglabs portal
      When  User enters the Username
      And   User enters the Password
      Then  Navigate to Home page
      And   User has sorted the items by Price Low to High
      Then  User adds the Cheapest item to the basket
      And   User adds the second costliest item to the basket
      Then  User navigates to the basket
      And   User checks out the items


