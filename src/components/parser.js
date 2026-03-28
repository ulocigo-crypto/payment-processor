const xml2js = require('xml2js');

function parsePaymentXml(xmlString) {
  return new Promise((resolve, reject) => {
    xml2js.parseString(xmlString, (err, result) => {
      if (err) {
        reject(err);
      } else {
        const payment = result.payment;
        const paymentMethod = payment.paymentMethod[0];
        const paymentAmount = payment.paymentAmount[0];
        const paymentCurrency = payment.paymentCurrency[0];
        const paymentDate = payment.paymentDate[0];

        const parsedPayment = {
          method: paymentMethod._,
          amount: parseFloat(paymentAmount._),
          currency: paymentCurrency._,
          date: new Date(paymentDate._),
        };

        resolve(parsedPayment);
      }
    });
  });
}

module.exports = parsePaymentXml;