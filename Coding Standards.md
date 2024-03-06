# Coding Standards

## Class and Function Naming:

Class names should follow PascalCase, e.g., PlayingCard, Deck, Table, StockWaste, Foundation.
Function names should be in camelCase, e,g., addCard, getTopCard.
Use clear and descriptive names for variables and functions to enhance code readability.

## Comments:

Use docstrings to provide documentation for classes and functions.
Add inline comments sparingly to explain complex or non-obvious logic.

## Constants:

Constants should be named in uppercase with underscores separating words, e.g., BREAK_STRING.

## String Formatting:

Use f-strings for string formatting where appropriate, as done with f"{self.name} {self.suit}".

## Error Handling:

Implement error handling where necessary. For example, check if the stock pile is empty before attempting to move a card to the waste pile.

## Whitespace and Indentation:

Use consistent indentation (4 spaces per level) to enhance code readability.
Ensure there are spaces around operators for improved clarity.

## User Interface:

Provide clear and concise instructions to the user, as seen in the printValidCommands function.
Consider adding more user prompts and feedback for a better interactive experience.

## Code Organization:

Group related functions and classes together.
Follow a logical order for function and method definitions within a class.

## Testing:

Implement comprehensive unit tests for critical functions and classes using the unittest module.

## Modularity:

Break down complex functions or methods into smaller, modular functions with a single responsibility.

## Consistency:

Be consistent in your coding style, naming conventions, and design patterns throughout the codebase.
