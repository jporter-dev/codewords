// https://docs.cypress.io/api/introduction/api.html

describe('Codenames', () => {
  it('Loads the homepage', () => {
    cy.visit('/')
    cy.hash().should('eq', '#/home')
    cy.get('#create-btn').should('contain', 'Create')
  })
  it('Loads the create form', () => {
    cy.visit('/#/create')
    cy.hash().should('eq', '#/create')
    cy.get('#create-btn').should('contain', 'Create')
  })
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
})
