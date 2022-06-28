import { Given, When, Then, And } from '@badeball/cypress-cucumber-preprocessor'

// Feature: Innholdsinformasjon - tester

	// #User wants to see the cover image for a document when the user sees the content description
	// @TEST_SMILE-1594 @TESTSET_SMILE-1623 @test
	// Scenario: User wants to see the cover image for a document
		Given ('user sees the content description', () =>{});
		When ('ISBN and cover image exists', () => {});
		Then ('user sees that the page contains cover image', () => {});

	// #User wants to see a short description for a document when the user sees the content description
	// @TEST_SMILE-1595 @TESTSET_SMILE-1623 @test
	// Scenario: User wants to see a short description for a document
	// 	Given user sees the content description
	// 	When ISBN and short description exists
	// 	Then user sees that the page contains short description

	// // #User wants to see a long description for a document when user sees the content description
	// // @TEST_SMILE-1596 @TESTSET_SMILE-1623 @test
	// // Scenario: User wants to see a long description for a document
	// 	Given user sees the content description
	// 	When ISBN and long description exists
	// 	Then user sees that the page contains long description

	// // #User wants to see a document with different forms of content descriptions when the user sees the content description
	// // @TEST_SMILE-1647 @TESTSET_SMILE-1623 @test
	// // Scenario: User wants to see a dokument with different forms of content descriptions
	// 	When ISBN, cover image, short descruption, long description and table of contents exists
	// 	Then user sees that the page contains cover image
	// 	And user sees that the page contains short description
	// 	And user sees that the page contains long description
	// 	And user sees that the page contains table of contents

	// // #User wants to see the table of contents for a document when the user sees the content description
	// // @TEST_SMILE-1646 @TESTSET_SMILE-1623 @test
	// // Scenario: User wants to see the table of contents for a document
	// 	Given user sees the content description
	// 	When ISBN and table of contents exists
	// 	Then user sees that the page contains table of contents

	// // #User wants to see if an audio file exists for a document when the user sees the content description
	// // @TEST_SMILE-1645 @TESTSET_SMILE-1623 @test
	// // Scenario: User wants to see if an audio file exists for a document
	// 	Given user sees the content description
	// 	When ISBN and an audio file exists
	// 	Then user sees that the page contains audio file