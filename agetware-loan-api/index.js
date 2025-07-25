const express = require('express');
const db = require('./models');
const { Loan, Payment } = db;

const app = express();
app.use(express.json());

// LEND endpoint
app.post('/lend', async (req, res) => {
  try {
    const { customer_id, loan_amount, loan_period, rate_of_interest } = req.body;
    const interest = (loan_amount * loan_period * rate_of_interest) / 100;
    const total_amount = loan_amount + interest;
    const monthly_emi = total_amount / (loan_period * 12);

    const loan = await Loan.create({
      customer_id,
      principal: loan_amount,
      total_amount,
      interest_rate: rate_of_interest,
      loan_period_years: loan_period,
      monthly_emi,
    });

    res.status(201).json({
      loan_id: loan.loan_id,
      total_amount,
      monthly_emi
    });
  } catch (error) {
    res.status(500).json({ error: 'Loan creation failed' });
  }
});

// PAYMENT endpoint
app.post('/payment', async (req, res) => {
  try {
    const { loan_id, amount, payment_type } = req.body;

    const loan = await Loan.findByPk(loan_id);
    if (!loan) return res.status(404).json({ error: 'Loan not found' });

    await Payment.create({ loan_id, amount, payment_type });

    loan.total_amount -= amount;
    await loan.save();

    res.json({ message: 'Payment successful', remaining_amount: loan.total_amount });
  } catch (error) {
    res.status(500).json({ error: 'Payment failed' });
  }
});

// LEDGER endpoint
app.get('/ledger/:loan_id', async (req, res) => {
  try {
    const { loan_id } = req.params;
    const loan = await Loan.findByPk(loan_id, { include: [Payment] });

    if (!loan) return res.status(404).json({ error: 'Loan not found' });

    const emi_left = Math.ceil(loan.total_amount / loan.monthly_emi);

    res.json({
      payments: loan.payments,
      balance_amount: loan.total_amount,
      monthly_emi: loan.monthly_emi,
      emi_left
    });
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch ledger' });
  }
});

// ACCOUNT endpoint
app.get('/account/:customer_id', async (req, res) => {
  try {
    const { customer_id } = req.params;
    const loans = await Loan.findAll({
      where: { customer_id },
      include: [Payment]
    });

    const overview = loans.map(loan => {
      const total_paid = loan.payments.reduce((sum, p) => sum + p.amount, 0);
      const emi_left = Math.ceil((loan.total_amount - total_paid) / loan.monthly_emi);

      return {
        loan_id: loan.loan_id,
        principal: loan.principal,
        total_amount: loan.principal + (loan.principal * loan.loan_period_years * loan.interest_rate) / 100,
        interest: (loan.principal * loan.loan_period_years * loan.interest_rate) / 100,
        monthly_emi: loan.monthly_emi,
        paid: total_paid,
        emi_left
      };
    });

    res.json(overview);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch account overview' });
  }
});

// Sync + Listen
db.sequelize.sync({ alter: true }).then(() => {
  app.listen(3000, () => {
    console.log('🚀 Server running at http://localhost:3000');
  });
});
