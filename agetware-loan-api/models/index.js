const { Sequelize, DataTypes } = require('sequelize');
const path = require('path');

const sequelize = new Sequelize({
  dialect: 'sqlite',
  storage: path.join(__dirname, '../database.sqlite'),
});

const Loan = require('./Loan')(sequelize, DataTypes);
const Payment = require('./Payment')(sequelize, DataTypes);

// Associations
Loan.hasMany(Payment, { foreignKey: 'loan_id', onDelete: 'CASCADE' });
Payment.belongsTo(Loan, { foreignKey: 'loan_id' });

module.exports = {
  sequelize,
  Loan,
  Payment,
};
