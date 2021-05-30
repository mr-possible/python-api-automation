Feature: Verify if books are added and deleted using Library API
  Scenario: Verify AddBook functionality
    Given the Book Details which need to be added to the Library
    When we execute AddBook POST API
    Then book is successfully added