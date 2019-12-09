describe('Tests visiting the page to assert that no non-200 level responses are sent.', function() {
    it('Visits EleNa', function() {
        cy.visit('http://localhost:3000/');

        cy.contains('EleNa')
    })
});

describe('Tests visiting the page to assert that the Map component is visible.', function() {
    it('Tests Map component visibility.', function() {
        cy.visit('http://localhost:3000/');

        cy.get('.leaflet-container')
            .should('be.visible')
    })
});

describe('Tests visiting the page to assert that the Sidebar component is visible.', function() {
    it('Tests Sidebar component visibility.', function() {
        cy.visit('http://localhost:3000/');

        cy.get('.sidebar-container')
            .should('be.visible')
    })
});

describe('Asserts that the starting text box should hold input properly.', function() {
    it('Tests input to the starting point text box.', function() {
        cy.visit('http://localhost:3000/');

        cy.get('#start-input')
            .should('be.visible')
            .type('myAddress, MA')
            .should('have.value', 'myAddress, MA')
    })
});

describe('Asserts that the ending text box should hold input properly.', function() {
    it('Tests input to the end point text box.', function() {
        cy.visit('http://localhost:3000/');

        cy.get('#end-input')
            .should('be.visible')
            .type('myAddress, MA')
            .should('have.value', 'myAddress, MA')
    })
});
