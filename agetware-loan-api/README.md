# Agetware Loan API

A simple Express + Sequelize + SQLite API for managing loans and payments.

## Setup

1. Install dependencies:
   ```bash
   npm install
   ```
2. Start the server:
   ```bash
   npm run dev
   ```
   The server runs at http://localhost:3000

## API Endpoints

### POST /lend
Create a new loan.
- **Body:** `{ customer_id, loan_amount, loan_period, rate_of_interest }`
- **Returns:** `{ loan_id, total_amount, monthly_emi }`

### POST /payment
Make a payment towards a loan.
- **Body:** `{ loan_id, amount, payment_type }`
- **Returns:** `{ message, remaining_amount }`

### GET /ledger/:loan_id
Get all payments and balance for a loan.
- **Returns:** `{ payments, balance_amount, monthly_emi, emi_left }`

### GET /account/:customer_id
Get all loans and payment summary for a customer.
- **Returns:** `[{ loan_id, principal, total_amount, interest, monthly_emi, paid, emi_left }]`

## Models
- **Loan**: loan_id, customer_id, principal, total_amount, interest_rate, loan_period_years, monthly_emi, status
- **Payment**: payment_id, loan_id, amount, payment_type, payment_date

---

**Note:**
- Database is SQLite and auto-creates on first run.
- All IDs are UUIDs. 