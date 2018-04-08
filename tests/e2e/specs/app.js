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
  it('Loads a bad game room', () => {
    cy.visit('/#/12345/player')
    cy.hash().should('eq', '#/12345/player')
    cy.get('.alert.error > div').should('contain', 'Unable to join room. Room does not exist.')
  })
})
