const { v4: uuidv4 } = require('uuid');

module.exports = (sequelize, DataTypes) => {
  const Loan = sequelize.define('Loan', {
    loan_id: {
      type: DataTypes.UUID,
      defaultValue: DataTypes.UUIDV4,
      primaryKey: true,
      unique: true,
    },
    customer_id: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    principal: DataTypes.FLOAT,
    total_amount: DataTypes.FLOAT,
    interest_rate: DataTypes.FLOAT,
    loan_period_years: DataTypes.INTEGER,
    monthly_emi: DataTypes.FLOAT,
    status: {
      type: DataTypes.STRING,
      defaultValue: 'ACTIVE',
    },
  });

  return Loan;
};
