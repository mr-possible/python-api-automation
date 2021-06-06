Feature: Verify if books are added and deleted using Library API

  @regression
  Scenario Outline: Verify AddBook functionality
    Given the Book Details which need to be added to the Library
    When we execute AddBook POST API with data :: <bookName> , <isbn>, <aisle> and <authorName>
    Then book is successfully added
    Examples:
      | bookName   | aisle | isbn    | authorName
      | rajni book | 3     | yui56j~ | murakami