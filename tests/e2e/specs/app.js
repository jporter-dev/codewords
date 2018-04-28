// https://docs.cypress.io/api/introduction/api.html

describe('Codenames App', () => {
  it('Loads the homepage', () => {
    cy.visit('/')
    cy.hash().should('eq', '#/home')

  })
  it('Clicks the create button and displays the loading form', () => {
    cy.get('#create-btn').should('contain', 'Create').click()
    cy.contains('Use a custom wordbank')
    cy.contains('Mix Dictionaries')
    // cy.get('#create-btn').should('contain', 'Create').click()
  })

  // it('Creates a game and loads the Player view', () => {
  //   cy.get('#shuffle-btn').should('contain', 'Shuffle Words')
  // })

  // it('Switches to the Spymaster view', () => {})

  it('Loads the player view', () => {
    cy.visit('/#/12345/player')
    cy.hash().should('eq', '#/12345/player')
    cy.get('#shuffle-btn').should('contain', 'Shuffle Words')
  })
  it('Loads the spymaster view', () => {
    cy.visit('/#/12345/spymaster')
    cy.hash().should('eq', '#/12345/spymaster')
    cy.get('#spymaster-btn').should('contain', 'I understand. Make me a spymaster!')
  })

  it('Visits the homepage', () => {
    cy.visit('/')
    cy.hash().should('eq', '#/home')
    cy.get('#create-btn').should('contain', 'Create')
  })
})
