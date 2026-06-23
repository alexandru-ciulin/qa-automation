# QA Automation Portfolio

This repository is a QA Automation learning project focused on building a scalable UI test automation framework using Playwright with Python and Pytest.

It demonstrates practical implementation of test automation principles, Page Object Model (POM), and real-world E2E test flows.

---

Technologies

- Python
- Pytest
- Playwright
- Git / GitHub

---

Covered topics

- Python fundamentals for test automation
- UI automation with Playwright
- Pytest framework (fixtures, assertions, parametrization)
- Page Object Model (POM) design pattern
- End-to-end test automation flows
- Negative testing strategies
- Test data parametrization
- Test suite structuring and modularization

---

Project structure

- pages/ → Page Object classes  
  (LoginPage, ProductsPage, CartPage, CheckoutPage)

- tests/ → Test cases grouped by feature  
  (products, cart, checkout, login flows)

- conftest.py → Shared Pytest fixtures

---

Test coverage

    Functional flows
    - Login functionality
    - Product listing validation
    - Product sorting validation (A → Z, Z → A, price low-to-high, price high-to-low)
    - Add / remove products from cart
    - Cart badge validation
    - Checkout process (full E2E flow)

    Checkout validation
    - Form validation (first name, last name, postal code)
    - Parametrized negative tests
    - Order completion verification

---

End-to-end scenario covered

Login → Products → Cart → Checkout → Order Completion

---

Status

Work in progress — actively improving framework design, test coverage, and best practices.

---

Future improvements

- API testing layer
- CI pipeline (GitHub Actions)
- Reporting (Allure)