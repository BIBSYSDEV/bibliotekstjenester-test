Feature: Innholdsinformasjon - tester

	@TEST_SMILE-1594 @TESTSET_SMILE-1623
	Scenario: Test av forsidebilde
		Given user sees the content description
		When ISBN and cover image exists
		Then user sees that the page contains cover image
	@TEST_SMILE-1595 @TESTSET_SMILE-1623
	Scenario: Test av kort beskrivelse
		Given user sees the content description
		When ISBN and short description exists
		Then user sees that the page contains short description
	@TEST_SMILE-1596 @TESTSET_SMILE-1623
	Scenario: Test av lang beskrivelse
		Given user sees the content description
		When ISBN and long description exists
		Then user sees that the page contains long description
