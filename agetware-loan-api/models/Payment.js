const { v4: uuidv4 } = require('uuid');

module.exports = (sequelize, DataTypes) => {
  const Payment = sequelize.define('Payment', {
    payment_id: {
      type: DataTypes.UUID,
      defaultValue: DataTypes.UUIDV4,
      primaryKey: true,
      unique: true,
    },
    loan_id: {
      type: DataTypes.UUID,
      allowNull: false,
    },
    amount: DataTypes.FLOAT,
    payment_type: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    payment_date: {
      type: DataTypes.DATE,
      defaultValue: DataTypes.NOW,
    },
  });

  return Payment;
};
